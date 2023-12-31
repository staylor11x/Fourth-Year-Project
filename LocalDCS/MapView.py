# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MapView.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(818, 608)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 836, 626))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(818, 608))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Heading = QtWidgets.QLabel(self.frame)
        self.Heading.setGeometry(QtCore.QRect(0, -20, 761, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.Heading.setFont(font)
        self.Heading.setObjectName("Heading")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(310, 390, 160, 104))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_C_P2 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_C_P2.setEnabled(False)
        self.label_C_P2.setMaximumSize(QtCore.QSize(30, 30))
        self.label_C_P2.setText("")
        self.label_C_P2.setPixmap(QtGui.QPixmap("Graphics/YellowWarningjpg-removebg-preview.png"))
        self.label_C_P2.setScaledContents(True)
        self.label_C_P2.setObjectName("label_C_P2")
        self.gridLayout_3.addWidget(self.label_C_P2, 1, 0, 1, 1)
        self.label_C_P1 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_C_P1.setEnabled(False)
        self.label_C_P1.setMaximumSize(QtCore.QSize(30, 30))
        self.label_C_P1.setText("")
        self.label_C_P1.setPixmap(QtGui.QPixmap("Graphics/YellowWarning-removebg-preview.png"))
        self.label_C_P1.setScaledContents(True)
        self.label_C_P1.setObjectName("label_C_P1")
        self.gridLayout_3.addWidget(self.label_C_P1, 2, 0, 1, 1)
        self.label_C_P3 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_C_P3.setEnabled(False)
        self.label_C_P3.setMaximumSize(QtCore.QSize(30, 30))
        self.label_C_P3.setText("")
        self.label_C_P3.setPixmap(QtGui.QPixmap("Graphics/RedWarning-removebg-preview.png"))
        self.label_C_P3.setScaledContents(True)
        self.label_C_P3.setObjectName("label_C_P3")
        self.gridLayout_3.addWidget(self.label_C_P3, 0, 0, 1, 1)
        self.label_C1_P3 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_C1_P3.setText("")
        self.label_C1_P3.setObjectName("label_C1_P3")
        self.gridLayout_3.addWidget(self.label_C1_P3, 0, 1, 1, 1)
        self.label_C1_P2 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_C1_P2.setText("")
        self.label_C1_P2.setObjectName("label_C1_P2")
        self.gridLayout_3.addWidget(self.label_C1_P2, 1, 1, 1, 1)
        self.label_C1_P1 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_C1_P1.setText("")
        self.label_C1_P1.setObjectName("label_C1_P1")
        self.gridLayout_3.addWidget(self.label_C1_P1, 2, 1, 1, 1)
        self.pushButton_AreaC = QtWidgets.QPushButton(self.frame)
        self.pushButton_AreaC.setGeometry(QtCore.QRect(10, 350, 521, 171))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(241, 228, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 228, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 228, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 228, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 228, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 228, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 228, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 228, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 228, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButton_AreaC.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_AreaC.setFont(font)
        self.pushButton_AreaC.setAutoFillBackground(False)
        self.pushButton_AreaC.setStyleSheet("background-color: #F1E4FF ")
        self.pushButton_AreaC.setFlat(False)
        self.pushButton_AreaC.setObjectName("pushButton_AreaC")
        self.pushButton_AreaB = QtWidgets.QPushButton(self.frame)
        self.pushButton_AreaB.setGeometry(QtCore.QRect(390, 130, 331, 211))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 253, 222))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 253, 222))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 253, 222))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 253, 222))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 253, 222))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 253, 222))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 253, 222))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 253, 222))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 253, 222))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButton_AreaB.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_AreaB.setFont(font)
        self.pushButton_AreaB.setAutoFillBackground(False)
        self.pushButton_AreaB.setStyleSheet("background-color: #FFFDDE")
        self.pushButton_AreaB.setFlat(False)
        self.pushButton_AreaB.setObjectName("pushButton_AreaB")
        self.pushButton_AreaA = QtWidgets.QPushButton(self.frame)
        self.pushButton_AreaA.setGeometry(QtCore.QRect(10, 130, 331, 211))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(222, 255, 233))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 255, 233))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 255, 233))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 255, 233))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 255, 233))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 255, 233))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 255, 233))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 255, 233))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 255, 233))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButton_AreaA.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_AreaA.setFont(font)
        self.pushButton_AreaA.setAutoFillBackground(False)
        self.pushButton_AreaA.setStyleSheet("background-color: #DEFFE9 ")
        self.pushButton_AreaA.setFlat(False)
        self.pushButton_AreaA.setObjectName("pushButton_AreaA")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(0, 40, 751, 80))
        self.groupBox.setObjectName("groupBox")
        self.back_button = QtWidgets.QPushButton(self.groupBox)
        self.back_button.setGeometry(QtCore.QRect(10, 20, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.back_button.setFont(font)
        self.back_button.setObjectName("back_button")
        self.MainMenu_button = QtWidgets.QPushButton(self.groupBox)
        self.MainMenu_button.setGeometry(QtCore.QRect(110, 20, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.MainMenu_button.setFont(font)
        self.MainMenu_button.setObjectName("MainMenu_button")
        self.ListView_button = QtWidgets.QPushButton(self.groupBox)
        self.ListView_button.setGeometry(QtCore.QRect(210, 20, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ListView_button.setFont(font)
        self.ListView_button.setObjectName("ListView_button")
        self.Refresh_button = QtWidgets.QPushButton(self.groupBox)
        self.Refresh_button.setGeometry(QtCore.QRect(310, 20, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Refresh_button.setFont(font)
        self.Refresh_button.setObjectName("Refresh_button")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(590, 190, 121, 104))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_B_P2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_B_P2.setEnabled(False)
        self.label_B_P2.setMaximumSize(QtCore.QSize(30, 30))
        self.label_B_P2.setText("")
        self.label_B_P2.setPixmap(QtGui.QPixmap("Graphics/YellowWarningjpg-removebg-preview.png"))
        self.label_B_P2.setScaledContents(True)
        self.label_B_P2.setObjectName("label_B_P2")
        self.gridLayout_2.addWidget(self.label_B_P2, 1, 0, 1, 1)
        self.label_B_P1 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_B_P1.setEnabled(False)
        self.label_B_P1.setMaximumSize(QtCore.QSize(30, 30))
        self.label_B_P1.setText("")
        self.label_B_P1.setPixmap(QtGui.QPixmap("Graphics/YellowWarning-removebg-preview.png"))
        self.label_B_P1.setScaledContents(True)
        self.label_B_P1.setObjectName("label_B_P1")
        self.gridLayout_2.addWidget(self.label_B_P1, 2, 0, 1, 1)
        self.label_B_P3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_B_P3.setEnabled(False)
        self.label_B_P3.setMaximumSize(QtCore.QSize(30, 30))
        self.label_B_P3.setText("")
        self.label_B_P3.setPixmap(QtGui.QPixmap("Graphics/RedWarning-removebg-preview.png"))
        self.label_B_P3.setScaledContents(True)
        self.label_B_P3.setObjectName("label_B_P3")
        self.gridLayout_2.addWidget(self.label_B_P3, 0, 0, 1, 1)
        self.label_B1_P3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_B1_P3.setText("")
        self.label_B1_P3.setObjectName("label_B1_P3")
        self.gridLayout_2.addWidget(self.label_B1_P3, 0, 1, 1, 1)
        self.label_B1_P2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_B1_P2.setText("")
        self.label_B1_P2.setObjectName("label_B1_P2")
        self.gridLayout_2.addWidget(self.label_B1_P2, 1, 1, 1, 1)
        self.label_B1_P1 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_B1_P1.setText("")
        self.label_B1_P1.setObjectName("label_B1_P1")
        self.gridLayout_2.addWidget(self.label_B1_P1, 2, 1, 1, 1)
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(210, 190, 121, 104))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_A1_P3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_A1_P3.setText("")
        self.label_A1_P3.setObjectName("label_A1_P3")
        self.gridLayout.addWidget(self.label_A1_P3, 0, 1, 1, 1)
        self.label_A_P2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_A_P2.setEnabled(False)
        self.label_A_P2.setMaximumSize(QtCore.QSize(30, 30))
        self.label_A_P2.setText("")
        self.label_A_P2.setPixmap(QtGui.QPixmap("Graphics/YellowWarningjpg-removebg-preview.png"))
        self.label_A_P2.setScaledContents(True)
        self.label_A_P2.setObjectName("label_A_P2")
        self.gridLayout.addWidget(self.label_A_P2, 1, 0, 1, 1)
        self.label_A_P1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_A_P1.setEnabled(False)
        self.label_A_P1.setMaximumSize(QtCore.QSize(30, 30))
        self.label_A_P1.setText("")
        self.label_A_P1.setPixmap(QtGui.QPixmap("Graphics/YellowWarning-removebg-preview.png"))
        self.label_A_P1.setScaledContents(True)
        self.label_A_P1.setObjectName("label_A_P1")
        self.gridLayout.addWidget(self.label_A_P1, 2, 0, 1, 1)
        self.label_A1_P2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_A1_P2.setText("")
        self.label_A1_P2.setObjectName("label_A1_P2")
        self.gridLayout.addWidget(self.label_A1_P2, 1, 1, 1, 1)
        self.label_A1_P1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_A1_P1.setText("")
        self.label_A1_P1.setObjectName("label_A1_P1")
        self.gridLayout.addWidget(self.label_A1_P1, 2, 1, 1, 1)
        self.label_A_P3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_A_P3.setEnabled(False)
        self.label_A_P3.setMaximumSize(QtCore.QSize(30, 30))
        self.label_A_P3.setText("")
        self.label_A_P3.setPixmap(QtGui.QPixmap("Graphics/RedWarning-removebg-preview.png"))
        self.label_A_P3.setScaledContents(True)
        self.label_A_P3.setObjectName("label_A_P3")
        self.gridLayout.addWidget(self.label_A_P3, 0, 0, 1, 1)
        self.pushButton_AreaC.raise_()
        self.Heading.raise_()
        self.gridLayoutWidget_3.raise_()
        self.pushButton_AreaB.raise_()
        self.pushButton_AreaA.raise_()
        self.groupBox.raise_()
        self.gridLayoutWidget_2.raise_()
        self.gridLayoutWidget.raise_()
        self.verticalLayout_2.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 818, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Heading.setText(_translate("MainWindow", "Facility Map View"))
        self.pushButton_AreaC.setText(_translate("MainWindow", "Area C"))
        self.pushButton_AreaB.setText(_translate("MainWindow", "Area B"))
        self.pushButton_AreaA.setText(_translate("MainWindow", "Area A"))
        self.groupBox.setTitle(_translate("MainWindow", "ToolBar"))
        self.back_button.setText(_translate("MainWindow", "Back"))
        self.MainMenu_button.setText(_translate("MainWindow", "Main Menu"))
        self.ListView_button.setText(_translate("MainWindow", "List View"))
        self.Refresh_button.setText(_translate("MainWindow", "Refresh"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
