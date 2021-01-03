import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
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

        png=QtGui.QPixmap(fileName1)
        graphicsView_2.setPixmap(png)
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = Window()
    MainWindow.show()
    sys.exit(app.exec_())



