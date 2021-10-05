from typing import Any
from PySide2.QtUiTools import loadUiType

class UiLoader(object):
    def __init__(self, path: str):
        self.path = path


    def load(self, module: str) -> Any:
        module_file = module + ".ui"
        module_path = self.path + module + "_ui"
        class_name = "Ui_" + module

        ui_class, qt_class = loadUiType(module_file)
