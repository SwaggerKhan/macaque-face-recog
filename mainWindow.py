# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import main


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(654, 470)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 40, 321, 361))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.gridLayoutWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.uploadButton = QtWidgets.QPushButton(self.frame)
        self.uploadButton.setGeometry(QtCore.QRect(10, 300, 301, 32))
        self.uploadButton.setObjectName("uploadButton")
        self.uploadButton.clicked.connect(self.uploader)
        self.imageBox = QtWidgets.QGraphicsView(self.frame)
        self.imageBox.setGeometry(QtCore.QRect(10, 10, 291, 231))
        self.imageBox.setObjectName("imageBox")
        self.imgLabel = QtWidgets.QLabel(self.frame)
        self.imgLabel.setGeometry(QtCore.QRect(39, 35, 231, 171))
        self.imgLabel.setText("")
        self.imgLabel.setObjectName("imgLabel")
        self.gridLayout.addWidget(self.frame, 0, 0, 2, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(370, 40, 251, 361))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.listView = QtWidgets.QListView(self.frame_2)
        self.listView.setGeometry(QtCore.QRect(10, 10, 231, 231))
        self.listView.setMinimumSize(QtCore.QSize(231, 231))
        self.listView.setMaximumSize(QtCore.QSize(231, 231))
        self.listView.setObjectName("listView")
        self.foundLabel = QtWidgets.QLabel(self.frame_2)
        self.foundLabel.setGeometry(QtCore.QRect(30, 30, 191, 171))
        self.foundLabel.setText("")
        self.foundLabel.setObjectName("foundLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 654, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction()) 
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def uploader(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self.imageBox, 'Open File',"","Images (*.png *.jpg *.jpeg *.bmp *.gif)")
        #newImage = main_new.ImageRec(fileName)
        pixmap = QtGui.QPixmap(fileName)
        #pixmap = pixmap.scaled(261, 351, QtCore.Qt.KeepAspectRatio)
        self.imgLabel.setPixmap(pixmap)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "U.R.M.I.S"))
        self.uploadButton.setText(_translate("MainWindow", "Upload Image"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
