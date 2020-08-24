from PySide2.QtCore import QCoreApplication
from PySide2.QtWidgets import QMainWindow, QLabel

from ..ui.MainWindow_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    """Main Window."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        hello = QCoreApplication.translate("MainWindow", "Hello, click the logo for informations about Qt")
        clickQt = QLabel(self)
        clickQt.setWordWrap(True)
        clickQt.setText(hello)
        self.ui.verticalLayout.insertWidget(0, clickQt)
