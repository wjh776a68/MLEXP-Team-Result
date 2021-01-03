# coding: utf-8
from PIL import Image
from numpy import *
from pylab import *
import numpy as np
from PCV.geometry import homography, camera,sfm
from PCV.localdescriptors import sift
import importlib

camera = importlib.reload(camera)
homography = importlib.reload(homography)
sfm = importlib.reload(sfm)
sift = importlib.reload(sift)
 
# 提取特征，注意读取图片的顺序！
im1 = array(Image.open('D:/study/machine_learning/images/yosemite2.jpg'))
sift.process_image('D:/study/machine_learning/images/yosemite2.jpg', 'im1.sift')
 
im2 = array(Image.open('D:/study/machine_learning/images/yosemite1.jpg'))
sift.process_image('D:/study/machine_learning/images/yosemite1.jpg', 'im2.sift')
 
l1, d1 = sift.read_features_from_file('im1.sift')
l2, d2 = sift.read_features_from_file('im2.sift')
 
matches = sift.match_twosided(d1, d2)
 
ndx = matches.nonzero()[0]
x1 = homography.make_homog(l1[ndx, :2].T)#将点集转化为齐次坐标表示
ndx2 = [int(matches[i]) for i in ndx]
x2 = homography.make_homog(l2[ndx2, :2].T)#将点集转化为齐次坐标表示
 
d1n = d1[ndx]
d2n = d2[ndx2]
x1n = x1.copy()
x2n = x2.copy()
 
figure(figsize=(16,16))
sift.plot_matches(im1, im2, l1, l2, matches, True)#可视化
show()
 
def F_from_ransac(x1, x2, model, maxiter=5000, match_threshold=1e-6):
    """
    使用RANSAC从点对应中稳健估计基本矩阵F.
  （来自http://www.scipy.org/Cookbook/RANSAC的ransac.py）。
    input: x1, x2 (3*n arrays) points in hom. coordinates. """
 
    from PCV.tools import ransac
    data = np.vstack((x1, x2))
    d = 10 # 20 is the original
    # 计算F并返回inlier索引
    F, ransac_data = ransac.ransac(data.T, model,
                                   8, maxiter, match_threshold, d, return_all=True)
    return F, ransac_data['inliers']
 
 
# 通过RANSAC找到F.
model = sfm.RansacModel()
F, inliers = F_from_ransac(x1n, x2n, model, maxiter=5000, match_threshold=1e-3)
 
 
P1 = array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]])
P2 = sfm.compute_P_from_fundamental(F)#计算第二个相机矩阵
 
#print P2
print('F is')
print(F)
 
# triangulate inliers and remove points not in front of both cameras
X = sfm.triangulate(x1n[:, inliers], x2n[:, inliers], P1, P2)
 
# 绘制X的投影
cam1 = camera.Camera(P1)
cam2 = camera.Camera(P2)
x1p = cam1.project(X)
x2p = cam2.project(X)
 
figure(figsize=(16, 16))
imj = sift.appendimages(im1, im2)
imj = vstack((imj, imj))
imshow(imj)
 
cols1 = im1.shape[1]
rows1 = im1.shape[0]
for i in range(len(x1p[0])):
    if (0<= x1p[0][i]<cols1) and (0<= x2p[0][i]<cols1) and (0<=x1p[1][i]<rows1) and (0<=x2p[1][i]<rows1):
        plot([x1p[0][i], x2p[0][i]+cols1],[x1p[1][i], x2p[1][i]],'c')
axis('off')
show()
 
d1p = d1n[inliers]
d2p = d2n[inliers]
##读取特征
#im3 = array(Image.open('D:/test/test5/9.jpg'))
#sift.process_image('D:/test/test5/9.jpg', 'im3.sift')
#l3, d3 = sift.read_features_from_file('im3.sift')
#matches13 = sift.match_twosided(d1p, d3)
#ndx_13 = matches13.nonzero()[0]
#x1_13 = homography.make_homog(x1p[:, ndx_13])
#ndx2_13 = [int(matches13[i]) for i in ndx_13]
#x3_13 = homography.make_homog(l3[ndx2_13, :2].T)
#figure(figsize=(16, 16))
#imj = sift.appendimages(im1, im3)
#imj = vstack((imj, imj))
#imshow(imj)
 
#cols1 = im1.shape[1]
#rows1 = im1.shape[0]
#for i in range(len(x1_13[0])):
#    if (0<= x1_13[0][i]<cols1) and (0<= x3_13[0][i]<cols1) and (0<=x1_13[1][i]<rows1) and (0<=x3_13[1][i]<rows1):
#        plot([x1_13[0][i], x3_13[0][i]+cols1],[x1_13[1][i], x3_13[1][i]],'c')
#axis('off')
#show()
 
#P3 = sfm.compute_P(x3_13, X[:, ndx_13])#计算第三个相机的矩阵
 
##print P3
print('P1 is')
print(P1)
print('P2 is')
print(P2)
#print('P3 is')
#print(P3)
