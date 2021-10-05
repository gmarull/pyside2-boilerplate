from PySide2.QtCore import QCoreApplication
from PySide2.QtWidgets import QMainWindow, QLabel

from app._ui.MainWindow_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    """Main Window."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        hello = self.__tr("Hello, click the logo for informations about Qt")
        clickQt = QLabel(self)
        # clickQt.setWordWrap(True)
        clickQt.setText(hello)
        self.ui.verticalLayout.insertWidget(0, clickQt)
        # self.adjustSize()


    # Needed for https://bugreports.qt.io/browse/PYSIDE-131
    def __tr(self, txt, disambiguation=None, n=-1):
        return QCoreApplication.translate("MainWindow", txt, disambiguation, n)
