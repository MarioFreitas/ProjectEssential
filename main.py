from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from gui.mainWindowGUI import Ui_MainWindow
import sys
import os
from gui.lib import *

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Main window of the application. Contains all global parameters of the GUI application.
    """

    def __init__(self, parent=None):
        """
        Initializes the main window and sets up the entire GUI application.
        :param parent: No parent
        :return: None
        """
        # Initiate parent class
        super(MainWindow, self).__init__(parent)

        # Setup GUI
        self.setupUi(self)
        self.setWindowIcon(QIcon('./img/icon.png'))
        self.setGeometry(100, 100, 800, 600)
        self.statusBar()
        self.change_qss('actionAqua')

    def change_qss(self, theme):
        themes = {'actionAqua': './gui/css/aqua/aqua.qss',
                  'actionBasicWhite': './gui/css/basicWhite/basicWhite.qss',
                  'actionBlueGlass': './gui/css/blueGlass/blueGlass.qss',
                  'actionDarcula': './gui/css/darcula/darcula.qss',
                  'actionDark': './gui/css/dark/darkstyle.qss',
                  'actionDarkBlue': './gui/css/darkBlue/style.qss',
                  'actionDarkBlueFreeCAD': './gui/css/darkBlue(FreeCAD)/stylesheet.qss',
                  'actionDarkGreen': './gui/css/darkGreen/darkGreen.qss',
                  'actionDarkGreenFreeCAD': './gui/css/darkGreen(FreeCAD)/stylesheet.qss',
                  'actionDarkOrange': './gui/css/darkOrange/darkOrange.qss',
                  'actionDarkOrangeFreeCAD': './gui/css/darkOrange(FreeCAD)/stylesheet.qss',
                  'actionLight': './gui/css/light/light.qss',
                  'actionLightBlueFreeCAD': './gui/css/lightBlue(FreeCAD)/stylesheet.qss',
                  'actionLightGreenFreeCAD': './gui/css/lightGreen(FreeCAD)/stylesheet.qss',
                  'actionLightOrangeFreeCAD': './gui/css/lightOrange(FreeCAD)/stylesheet.qss',
                  'actionMachinery': './gui/css/machinery/machinery.qss',
                  'actionMinimalist': './gui/css/minimalist/Minimalist.qss',
                  'actionNightMapping': './gui/css/nightMapping/style.qss',
                  'actionWombat': './gui/css/wombat/stylesheet.qss',
                  }
        # for i in themes.keys():
        #     eval('self.{}.setChecked(False)'.format(i))
        # eval('self.{}.setChecked(True)'.format(theme))

        qss = open_qss(themes[theme])
        app.setStyleSheet(qss)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = MainWindow()
    gui.show()
    sys.exit(app.exec_())