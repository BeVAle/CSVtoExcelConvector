import sys
from PyQt6 import QtWidgets

import design
import os

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self.SelectFileButton.clicked.connect(self.browse_folder)

    def browse_folder(self):
        directory = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл")

        if directory[0]:
            self.lineEdit.setText(directory[0])


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()  
    window.show()
    app.exec()


if __name__ == '__main__':
    main()