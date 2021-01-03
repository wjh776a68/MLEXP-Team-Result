'''
    Author: wjh776a68
    Date: 2021/01/03
    Function: Python-version Test Dymanic Video Stitch

'''



import cv2
import main
from Stitcher import Stitcher
from matplotlib import pyplot as plt





device1_url=input("请输入设备1的IP地址")#admin:admin@172.28.25.10:8081
device2_url=input("请输入设备2的IP地址")#admin:admin@172.28.24.25:8081

#device1_url="http://admin:admin@172.20.10.5:8081"
#device2_url="http://admin:admin@172.20.10.4:8081"

#url1 = "http://admin:admin@172.28.25.10:8081"
#url2 = "http://admin:admin@172.28.25.10:8081"
# 程序是执行状态，但是没有打开摄像头
# url = "http://admin:123456@192.168.3.16:8081"
# 正确打开摄像头

#url = "rtsp://admin:admin@192.168.3.16:8554/live"
# 直接返回错误：[rtsp @ 000001ee2b0824c0] method DESCRIBE failed: 401 Unauthorized

# url = "rtsp://admin:123456@192.168.3.16:8554/live"
# [rtsp @ 0000019250a424c0] method DESCRIBE failed: 404 Stream Not Found  手机的摄像头会被打开，然后程序报错

print('start')
device1_cap = cv2.VideoCapture(device1_url)#读取视频流
device2_cap = cv2.VideoCapture(device2_url)#读取视频流

while(device1_cap.isOpened() or device2_cap.isOpened()):
    print('success')
    if(device1_cap.isOpened()):
        device1_ret, device1_frame = device1_cap.read()
        cv2.imshow('frame1',device1_frame)
    if(device2_cap.isOpened()):
        device2_ret, device2_frame = device2_cap.read()
        cv2.imshow('frame2',device2_frame)

    if(device1_cap.isOpened() and device2_cap.isOpened()):
    # 把图像拼接成全景图
        stitcher = Stitcher()
        (result, vis) = stitcher.stitch([device1_frame, device2_frame], showMatches=True)
        print("panomanic mode")
        cv2.imshow("Result", result)
   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


print('end')
device1_cap.release()
device2_cap.release()

cv2.destroyAllWindows()
