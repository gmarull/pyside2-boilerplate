from PySide2.QtWidgets import QMainWindow

from ..ui.MainWindow_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """Main Window."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
