import sys
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import *
from functools import partial

from mainwindow import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self,*args,**kwargs):
        super(Window,self).__init__(*args,**kwargs)

        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.openFile)
        self.pushButton_3.clicked.connect(self.openFile)

    def openFile(self):
        fileName1, filetype = QFileDialog.getOpenFileName(self,"选取文件","/Users/Kelisiya/Desktop","All Files (*);;Text Files (*.txt)")
        print(fileName1, filetype)
       
        img=cv2.imread(fileName1)                              #读取图像

        #cv2.imshow("result",img)

        #cv2.waitKey(0)
        
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)              #转换图像通道
        x = img.shape[1]                                        #获取图像大小
        y = img.shape[0]
        self.zoomscale=1                                        #图片放缩尺度
        frame = QImage(img, x, y, QImage.Format_RGB888)
        pix = QPixmap.fromImage(frame)
    
        self.item=QGraphicsPixmapItem(pix)                      #创建像素图元
        #self.item.setScale(self.zoomscale)
        self.scene=QGraphicsScene()                             #创建场景
        self.scene.addItem(self.item)
        self.graphicsView_2.setScene(self.scene)                #将场景添加至视图

        

        
       

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = Window()
    MainWindow.show()
    sys.exit(app.exec_())



