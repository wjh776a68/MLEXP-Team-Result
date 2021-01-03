from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(625, 430)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ImgDisp = QtWidgets.QLabel(self.centralwidget)
        self.ImgDisp.setGeometry(QtCore.QRect(0, 0, 54, 12))
        self.ImgDisp.setObjectName("ImgDisp")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 625, 17))
        self.menubar.setObjectName("menubar")
        self.menushowImg = QtWidgets.QMenu(self.menubar)
        self.menushowImg.setObjectName("menushowImg")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionshowImg = QtWidgets.QAction(MainWindow)
        self.actionshowImg.setObjectName("actionshowImg")
        self.menushowImg.addAction(self.actionshowImg)
        self.menubar.addAction(self.menushowImg.menuAction())
        self.toolBar.addAction(self.actionshowImg)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ImgDisp.setText(_translate("MainWindow", "."))
        self.menushowImg.setTitle(_translate("MainWindow", "menu"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionshowImg.setText(_translate("MainWindow", "showImg"))
