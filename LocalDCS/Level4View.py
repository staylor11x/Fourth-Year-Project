# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Level4View.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(490, 401)
        self.L_WarningSymbol = QtWidgets.QLabel(Form)
        self.L_WarningSymbol.setGeometry(QtCore.QRect(20, 20, 91, 81))
        self.L_WarningSymbol.setText("")
        self.L_WarningSymbol.setPixmap(QtGui.QPixmap("Graphics/GreyWarning-modified.png"))
        self.L_WarningSymbol.setScaledContents(True)
        self.L_WarningSymbol.setObjectName("L_WarningSymbol")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(140, 20, 261, 121))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.L_AlarmStatus = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.L_AlarmStatus.setFont(font)
        self.L_AlarmStatus.setObjectName("L_AlarmStatus")
        self.gridLayout.addWidget(self.L_AlarmStatus, 1, 0, 1, 1)
        self.L_Pri = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.L_Pri.setFont(font)
        self.L_Pri.setObjectName("L_Pri")
        self.gridLayout.addWidget(self.L_Pri, 2, 0, 1, 1)
        self.L_Time = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.L_Time.setFont(font)
        self.L_Time.setObjectName("L_Time")
        self.gridLayout.addWidget(self.L_Time, 3, 0, 1, 1)
        self.L_TagNo_data = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.L_TagNo_data.setFont(font)
        self.L_TagNo_data.setObjectName("L_TagNo_data")
        self.gridLayout.addWidget(self.L_TagNo_data, 0, 1, 1, 1)
        self.L_Pri_data = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.L_Pri_data.setFont(font)
        self.L_Pri_data.setObjectName("L_Pri_data")
        self.gridLayout.addWidget(self.L_Pri_data, 2, 1, 1, 1)
        self.L_Time_data = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.L_Time_data.setFont(font)
        self.L_Time_data.setObjectName("L_Time_data")
        self.gridLayout.addWidget(self.L_Time_data, 3, 1, 1, 1)
        self.L_AlarmStatus_data = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.L_AlarmStatus_data.setFont(font)
        self.L_AlarmStatus_data.setObjectName("L_AlarmStatus_data")
        self.gridLayout.addWidget(self.L_AlarmStatus_data, 1, 1, 1, 1)
        self.L_TagNo = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.L_TagNo.setFont(font)
        self.L_TagNo.setObjectName("L_TagNo")
        self.gridLayout.addWidget(self.L_TagNo, 0, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 180, 471, 141))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 0, 2, 1, 1)
        self.TB_Actions = QtWidgets.QTextBrowser(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.TB_Actions.setFont(font)
        self.TB_Actions.setObjectName("TB_Actions")
        self.gridLayout_2.addWidget(self.TB_Actions, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)
        self.TB_Causes = QtWidgets.QTextBrowser(self.gridLayoutWidget_2)
        self.TB_Causes.setObjectName("TB_Causes")
        self.gridLayout_2.addWidget(self.TB_Causes, 1, 1, 1, 1)
        self.TB_Conseq = QtWidgets.QTextBrowser(self.gridLayoutWidget_2)
        self.TB_Conseq.setObjectName("TB_Conseq")
        self.gridLayout_2.addWidget(self.TB_Conseq, 1, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 1, 1, 1)
        self.PB_Resolved = QtWidgets.QPushButton(Form)
        self.PB_Resolved.setEnabled(False)
        self.PB_Resolved.setGeometry(QtCore.QRect(10, 340, 151, 41))
        self.PB_Resolved.setStyleSheet("background-color:rgb(202, 255, 207)")
        self.PB_Resolved.setObjectName("PB_Resolved")
        self.PB_Silence = QtWidgets.QPushButton(Form)
        self.PB_Silence.setEnabled(False)
        self.PB_Silence.setGeometry(QtCore.QRect(170, 340, 151, 41))
        self.PB_Silence.setStyleSheet("background-color:rgb(253, 255, 196)")
        self.PB_Silence.setObjectName("PB_Silence")
        self.PB_Freeze = QtWidgets.QPushButton(Form)
        self.PB_Freeze.setEnabled(False)
        self.PB_Freeze.setGeometry(QtCore.QRect(330, 340, 141, 41))
        self.PB_Freeze.setStyleSheet("background-color:rgb(255, 211, 207)")
        self.PB_Freeze.setObjectName("PB_Freeze")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.L_AlarmStatus.setText(_translate("Form", "Alarm Status:"))
        self.L_Pri.setText(_translate("Form", "Priority:"))
        self.L_Time.setText(_translate("Form", "Time:"))
        self.L_TagNo_data.setText(_translate("Form", "n/a"))
        self.L_Pri_data.setText(_translate("Form", "n/a"))
        self.L_Time_data.setText(_translate("Form", "n/a"))
        self.L_AlarmStatus_data.setText(_translate("Form", "n/a"))
        self.L_TagNo.setText(_translate("Form", "Tag No:"))
        self.label_12.setText(_translate("Form", "Consequences"))
        self.TB_Actions.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Queue empty</span></p></body></html>"))
        self.label_10.setText(_translate("Form", "Actions:"))
        self.TB_Causes.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">N/A</span></p></body></html>"))
        self.TB_Conseq.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">N/A</span></p></body></html>"))
        self.label_11.setText(_translate("Form", "Causes"))
        self.PB_Resolved.setText(_translate("Form", "Resolved"))
        self.PB_Silence.setText(_translate("Form", "Silence"))
        self.PB_Freeze.setText(_translate("Form", "Freeze/shutdown"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
