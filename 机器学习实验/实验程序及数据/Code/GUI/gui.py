'''
    Author: wjh776a68
    Date: 2021/01/03
    Function: Python-version Project GUI

'''

import cv2,sys
from PyQt5 import QtGui,QtWidgets,QtCore
import mainWin

def cvImgtoQtImg(cvImg): #定义opencv图像转PyQt图像的函数
    QtImgBuf = cv2.cvtColor(cvImg,  cv2.COLOR_BGR2BGRA)

    QtImg = QtGui.QImage(QtImgBuf.data, QtImgBuf.shape[1], QtImgBuf.shape[0], QtGui.QImage.Format_RGB32)
    
    return QtImg



class mainwin(QtWidgets.QMainWindow,mainWin.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bClose = False

        self.actionshowImg.triggered.connect(self.playVideoFile) #建立菜单点击的信号与方法playVideoFile连接

    def playVideoFile(self): #播放影片
##        cap = cv2.VideoCapture(r'f:\video\mydream.mp4') #打开影片
##        fps = 24
##        if not cap.isOpened():
##            print("Cannot open Video File")
##            exit()
##
##        while not self.bClose:
##            ret, frame = cap.read() #逐帧读取影片
##            if not ret:
##                if frame is None:
##                    print("The video has end.")
##                else:
##                    print("Read video error!")
##                break
##
##            QtImg = cvImgtoQtImg(frame)  #将帧数据转换为PyQt图像格式
##            self.ImgDisp.setPixmap(QtGui.QPixmap.fromImage(QtImg)) #在ImgDisp显示图像
##            size = QtImg.size() 
##            self.ImgDisp.resize(size)#根据帧大小调整标签大小
##            self.ImgDisp.show() #刷新界面
##            cv2.waitKey(int(1000/fps)) #休眠一会，确保每秒播放fps帧
##
##        # 完成所有操作后，释放捕获器
##        cap.release()


if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = mainwin()
    w.show()
    sys.exit(app.exec_())
