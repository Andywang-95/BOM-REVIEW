# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_sub.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SubWindow(object):
    def setupUi(self, SettingWindow):
        SettingWindow.setObjectName("SettingWindow")
        SettingWindow.resize(560, 288)
        self.centralwidget = QtWidgets.QWidget(SettingWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.group1 = QtWidgets.QGroupBox(self.centralwidget)
        self.group1.setMinimumSize(QtCore.QSize(0, 90))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.group1.setFont(font)
        self.group1.setStyleSheet("")
        self.group1.setObjectName("group1")
        self.gridLayout = QtWidgets.QGridLayout(self.group1)
        self.gridLayout.setObjectName("gridLayout")
        self.path_text = QtWidgets.QTextBrowser(self.group1)
        self.path_text.setEnabled(False)
        self.path_text.setMinimumSize(QtCore.QSize(0, 30))
        self.path_text.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.path_text.setStyleSheet("")
        self.path_text.setObjectName("path_text")
        self.gridLayout.addWidget(self.path_text, 0, 0, 1, 1)
        self.path_check = QtWidgets.QCheckBox(self.group1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.path_check.setFont(font)
        self.path_check.setShortcut("")
        self.path_check.setCheckable(True)
        self.path_check.setObjectName("path_check")
        self.gridLayout.addWidget(self.path_check, 0, 1, 1, 1)
        self.path_tool = QtWidgets.QToolButton(self.group1)
        self.path_tool.setEnabled(False)
        self.path_tool.setMinimumSize(QtCore.QSize(30, 22))
        self.path_tool.setMaximumSize(QtCore.QSize(30, 22))
        self.path_tool.setObjectName("path_tool")
        self.gridLayout.addWidget(self.path_tool, 0, 2, 1, 1)
        self.gridLayout_3.addWidget(self.group1, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pn_label = QtWidgets.QLabel(self.groupBox_2)
        self.pn_label.setMinimumSize(QtCore.QSize(130, 20))
        self.pn_label.setMaximumSize(QtCore.QSize(150, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pn_label.setFont(font)
        self.pn_label.setStyleSheet("QLabel {\n"
"qproperty-alignment: AlignRight;\n"
"}")
        self.pn_label.setObjectName("pn_label")
        self.horizontalLayout_3.addWidget(self.pn_label)
        self.pn_text = QtWidgets.QTextEdit(self.groupBox_2)
        self.pn_text.setEnabled(False)
        self.pn_text.setMinimumSize(QtCore.QSize(0, 0))
        self.pn_text.setMaximumSize(QtCore.QSize(50, 25))
        self.pn_text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pn_text.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pn_text.setReadOnly(False)
        self.pn_text.setObjectName("pn_text")
        self.horizontalLayout_3.addWidget(self.pn_text)
        self.pn_check = QtWidgets.QCheckBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pn_check.setFont(font)
        self.pn_check.setShortcut("")
        self.pn_check.setCheckable(True)
        self.pn_check.setObjectName("pn_check")
        self.horizontalLayout_3.addWidget(self.pn_check)
        spacerItem = QtWidgets.QSpacerItem(225, 15, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.firstcol_label = QtWidgets.QLabel(self.groupBox_2)
        self.firstcol_label.setMinimumSize(QtCore.QSize(130, 20))
        self.firstcol_label.setMaximumSize(QtCore.QSize(150, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.firstcol_label.setFont(font)
        self.firstcol_label.setStyleSheet("QLabel {\n"
"qproperty-alignment: AlignRight;\n"
"}")
        self.firstcol_label.setObjectName("firstcol_label")
        self.horizontalLayout_2.addWidget(self.firstcol_label)
        self.firstcol_text = QtWidgets.QTextEdit(self.groupBox_2)
        self.firstcol_text.setEnabled(False)
        self.firstcol_text.setMinimumSize(QtCore.QSize(0, 0))
        self.firstcol_text.setMaximumSize(QtCore.QSize(50, 25))
        self.firstcol_text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.firstcol_text.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.firstcol_text.setReadOnly(False)
        self.firstcol_text.setObjectName("firstcol_text")
        self.horizontalLayout_2.addWidget(self.firstcol_text)
        self.firstcol_check = QtWidgets.QCheckBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.firstcol_check.setFont(font)
        self.firstcol_check.setShortcut("")
        self.firstcol_check.setCheckable(True)
        self.firstcol_check.setObjectName("firstcol_check")
        self.horizontalLayout_2.addWidget(self.firstcol_check)
        spacerItem1 = QtWidgets.QSpacerItem(225, 15, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setMinimumSize(QtCore.QSize(0, 25))
        self.save_button.setObjectName("save_button")
        self.horizontalLayout.addWidget(self.save_button)
        self.close_button = QtWidgets.QPushButton(self.centralwidget)
        self.close_button.setMinimumSize(QtCore.QSize(0, 25))
        self.close_button.setObjectName("close_button")
        self.horizontalLayout.addWidget(self.close_button)
        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        SettingWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SettingWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 560, 21))
        self.menubar.setObjectName("menubar")
        SettingWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SettingWindow)
        self.statusbar.setObjectName("statusbar")
        SettingWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SettingWindow)
        QtCore.QMetaObject.connectSlotsByName(SettingWindow)

    def retranslateUi(self, SettingWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingWindow.setWindowTitle(_translate("SettingWindow", "設定"))
        self.group1.setTitle(_translate("SettingWindow", "Database 資料夾位置"))
        self.path_text.setHtml(_translate("SettingWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.path_check.setText(_translate("SettingWindow", "自定義"))
        self.path_tool.setText(_translate("SettingWindow", "..."))
        self.groupBox_2.setTitle(_translate("SettingWindow", "BOM設定"))
        self.pn_label.setText(_translate("SettingWindow", "Part Number 列名"))
        self.pn_text.setHtml(_translate("SettingWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pn_check.setText(_translate("SettingWindow", "自定義"))
        self.firstcol_label.setText(_translate("SettingWindow", "起始行"))
        self.firstcol_text.setHtml(_translate("SettingWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.firstcol_check.setText(_translate("SettingWindow", "自定義"))
        self.save_button.setText(_translate("SettingWindow", "Save"))
        self.close_button.setText(_translate("SettingWindow", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SettingWindow = QtWidgets.QMainWindow()
    ui = Ui_SubWindow()
    ui.setupUi(SettingWindow)
    SettingWindow.show()
    sys.exit(app.exec_())
