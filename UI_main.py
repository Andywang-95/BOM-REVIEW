# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(827, 666)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/andy.wang.GC/Downloads/你的段落文字__2_-removebg-preview.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.path_label = QtWidgets.QLabel(self.widget_2)
        self.path_label.setMinimumSize(QtCore.QSize(90, 30))
        self.path_label.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(8)
        self.path_label.setFont(font)
        self.path_label.setStyleSheet("border-width : 1px ;\n"
"border-style : solid;\n"
"border-color : black\n"
"")
        self.path_label.setObjectName("path_label")
        self.horizontalLayout_8.addWidget(self.path_label)
        self.database_path = QtWidgets.QTextBrowser(self.widget_2)
        self.database_path.setMinimumSize(QtCore.QSize(0, 26))
        self.database_path.setMaximumSize(QtCore.QSize(16777215, 26))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(9)
        self.database_path.setFont(font)
        self.database_path.setObjectName("database_path")
        self.horizontalLayout_8.addWidget(self.database_path)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pn_label = QtWidgets.QLabel(self.widget_2)
        self.pn_label.setMinimumSize(QtCore.QSize(90, 30))
        self.pn_label.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(8)
        self.pn_label.setFont(font)
        self.pn_label.setStyleSheet("border-width : 1px ;\n"
"border-style : solid;\n"
"border-color : black\n"
"")
        self.pn_label.setObjectName("pn_label")
        self.horizontalLayout_5.addWidget(self.pn_label)
        self.pn_text = QtWidgets.QTextBrowser(self.widget_2)
        self.pn_text.setMinimumSize(QtCore.QSize(0, 26))
        self.pn_text.setMaximumSize(QtCore.QSize(50, 26))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.pn_text.setFont(font)
        self.pn_text.setObjectName("pn_text")
        self.horizontalLayout_5.addWidget(self.pn_text)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_9.setStretch(0, 4)
        self.horizontalLayout_9.setStretch(1, 1)
        self.gridLayout.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.widget_2, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("QTabBar::tab{\n"
"width: 120px; \n"
"height:30px;\n"
"font:20px \'Arial\';\n"
"}")
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bomlabel_1 = QtWidgets.QLabel(self.tab)
        self.bomlabel_1.setMaximumSize(QtCore.QSize(100, 40))
        self.bomlabel_1.setStyleSheet("font:15px \'Arial\'")
        self.bomlabel_1.setObjectName("bomlabel_1")
        self.horizontalLayout.addWidget(self.bomlabel_1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.bompath_text_1 = QtWidgets.QTextBrowser(self.widget)
        self.bompath_text_1.setMinimumSize(QtCore.QSize(0, 30))
        self.bompath_text_1.setMaximumSize(QtCore.QSize(16777215, 40))
        self.bompath_text_1.setObjectName("bompath_text_1")
        self.horizontalLayout_3.addWidget(self.bompath_text_1)
        self.bompath_tool_1 = QtWidgets.QToolButton(self.widget)
        self.bompath_tool_1.setMinimumSize(QtCore.QSize(40, 30))
        self.bompath_tool_1.setMaximumSize(QtCore.QSize(40, 30))
        self.bompath_tool_1.setObjectName("bompath_tool_1")
        self.horizontalLayout_3.addWidget(self.bompath_tool_1)
        self.verticalLayout.addWidget(self.widget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget1 = QtWidgets.QWidget(self.tab)
        self.widget1.setMinimumSize(QtCore.QSize(700, 45))
        self.widget1.setMaximumSize(QtCore.QSize(100000, 45))
        self.widget1.setStyleSheet("")
        self.widget1.setObjectName("widget1")
        self.add_label = QtWidgets.QLabel(self.widget1)
        self.add_label.setGeometry(QtCore.QRect(9, 11, 100, 20))
        self.add_label.setMinimumSize(QtCore.QSize(100, 20))
        self.add_label.setMaximumSize(QtCore.QSize(100, 20))
        self.add_label.setStyleSheet("font:13px \'Arial\'")
        self.add_label.setObjectName("add_label")
        self.y_radio = QtWidgets.QRadioButton(self.widget1)
        self.y_radio.setGeometry(QtCore.QRect(115, 11, 129, 20))
        self.y_radio.setMinimumSize(QtCore.QSize(35, 15))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.y_radio.setFont(font)
        self.y_radio.setStyleSheet("font:13px \'Arial\'")
        self.y_radio.setChecked(True)
        self.y_radio.setObjectName("y_radio")
        self.r_radio = QtWidgets.QRadioButton(self.widget1)
        self.r_radio.setGeometry(QtCore.QRect(250, 11, 60, 20))
        self.r_radio.setMinimumSize(QtCore.QSize(35, 15))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.r_radio.setFont(font)
        self.r_radio.setMouseTracking(True)
        self.r_radio.setStyleSheet("font:13px \'Arial\'")
        self.r_radio.setChecked(False)
        self.r_radio.setObjectName("r_radio")
        self.n_radio = QtWidgets.QRadioButton(self.widget1)
        self.n_radio.setGeometry(QtCore.QRect(316, 11, 79, 20))
        self.n_radio.setMinimumSize(QtCore.QSize(35, 15))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.n_radio.setFont(font)
        self.n_radio.setStyleSheet("font:13px \'Arial\'")
        self.n_radio.setObjectName("n_radio")
        self.custom_radio = QtWidgets.QRadioButton(self.widget1)
        self.custom_radio.setGeometry(QtCore.QRect(401, 11, 252, 20))
        self.custom_radio.setMinimumSize(QtCore.QSize(35, 15))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.custom_radio.setFont(font)
        self.custom_radio.setStyleSheet("font:13px \'Arial\'")
        self.custom_radio.setObjectName("custom_radio")
        self.custom_button = QtWidgets.QToolButton(self.widget1)
        self.custom_button.setEnabled(False)
        self.custom_button.setGeometry(QtCore.QRect(659, 9, 30, 25))
        self.custom_button.setMinimumSize(QtCore.QSize(30, 25))
        self.custom_button.setObjectName("custom_button")
        self.horizontalLayout_2.addWidget(self.widget1)
        spacerItem1 = QtWidgets.QSpacerItem(37, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.review_button = QtWidgets.QPushButton(self.tab)
        self.review_button.setMinimumSize(QtCore.QSize(90, 30))
        self.review_button.setMaximumSize(QtCore.QSize(90, 30))
        self.review_button.setStyleSheet("font:13px \'Arial\'")
        self.review_button.setObjectName("review_button")
        self.horizontalLayout_4.addWidget(self.review_button)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.display_1 = QtWidgets.QTextBrowser(self.tab)
        self.display_1.setObjectName("display_1")
        self.verticalLayout.addWidget(self.display_1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.bomlabel_2 = QtWidgets.QLabel(self.tab_2)
        self.bomlabel_2.setMaximumSize(QtCore.QSize(100, 40))
        self.bomlabel_2.setStyleSheet("font:15px \'Arial\'")
        self.bomlabel_2.setObjectName("bomlabel_2")
        self.horizontalLayout_6.addWidget(self.bomlabel_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.bompath_text_2 = QtWidgets.QTextBrowser(self.tab_2)
        self.bompath_text_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.bompath_text_2.setObjectName("bompath_text_2")
        self.horizontalLayout_7.addWidget(self.bompath_text_2)
        self.bompath_tool_2 = QtWidgets.QToolButton(self.tab_2)
        self.bompath_tool_2.setMinimumSize(QtCore.QSize(40, 30))
        self.bompath_tool_2.setMaximumSize(QtCore.QSize(40, 30))
        self.bompath_tool_2.setObjectName("bompath_tool_2")
        self.horizontalLayout_7.addWidget(self.bompath_tool_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.import_button = QtWidgets.QPushButton(self.tab_2)
        self.import_button.setMinimumSize(QtCore.QSize(90, 30))
        self.import_button.setMaximumSize(QtCore.QSize(90, 30))
        self.import_button.setStyleSheet("font:13px \'Arial\'")
        self.import_button.setObjectName("import_button")
        self.horizontalLayout_10.addWidget(self.import_button)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.display_2 = QtWidgets.QTextBrowser(self.tab_2)
        self.display_2.setObjectName("display_2")
        self.verticalLayout_2.addWidget(self.display_2)
        self.verticalLayout_2.setStretch(3, 10)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setMinimumSize(QtCore.QSize(0, 0))
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.update_button = QtWidgets.QPushButton(self.tab_3)
        self.update_button.setMinimumSize(QtCore.QSize(90, 30))
        self.update_button.setMaximumSize(QtCore.QSize(90, 30))
        self.update_button.setStyleSheet("font:13px \'Arial\'")
        self.update_button.setObjectName("update_button")
        self.horizontalLayout_11.addWidget(self.update_button)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.display_3 = QtWidgets.QTextBrowser(self.tab_3)
        self.display_3.setObjectName("display_3")
        self.verticalLayout_3.addWidget(self.display_3)
        self.gridLayout_4.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 827, 21))
        self.menubar.setObjectName("menubar")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuSetting.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CE BOM Review"))
        self.path_label.setText(_translate("MainWindow", "Database Path:"))
        self.pn_label.setText(_translate("MainWindow", "P/N Location:"))
        self.bomlabel_1.setText(_translate("MainWindow", "BOM File Path:"))
        self.bompath_tool_1.setText(_translate("MainWindow", "..."))
        self.add_label.setText(_translate("MainWindow", "是否區分主替料"))
        self.y_radio.setText(_translate("MainWindow", "BOM_TipTop_PTC"))
        self.r_radio.setText(_translate("MainWindow", "Result"))
        self.n_radio.setText(_translate("MainWindow", "系統BOM"))
        self.custom_radio.setText(_translate("MainWindow", "自定義(請至 選項→設定 中修改PN位置)"))
        self.custom_button.setText(_translate("MainWindow", "..."))
        self.review_button.setText(_translate("MainWindow", "Start Review"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Review"))
        self.bomlabel_2.setText(_translate("MainWindow", "BOM File Path:"))
        self.bompath_tool_2.setText(_translate("MainWindow", "..."))
        self.import_button.setText(_translate("MainWindow", "Start Import"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Import"))
        self.update_button.setText(_translate("MainWindow", "Start Update"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Update"))
        self.menuSetting.setTitle(_translate("MainWindow", "設定流程"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
