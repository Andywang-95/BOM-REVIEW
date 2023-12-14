from PyQt5 import QtWidgets
from controller import MainWindow_controller
from controller import SubWindow_controller
from controller import Setup_window

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    window = MainWindow_controller()
    subwindow = SubWindow_controller()
    setupwindow = Setup_window()
    window.show()
    window.ui.menuSetting.aboutToShow.connect(setupwindow.show)
    window.ui.custom_button.clicked.connect(subwindow.show)
    # 實時顯示設定內容在最上方欄位
    subwindow.ui.save_button.clicked.connect(window.preview_setting)
    
    sys.exit(app.exec_())
