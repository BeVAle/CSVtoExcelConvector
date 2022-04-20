import sys

import pandas as pd
from PyQt6 import QtWidgets

import design


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self, filename=None):
        super().__init__()
        self.setupUi(self)
        self.SelectFileButton.clicked.connect(self.browse_folder)
        self.ConvertorButton.clicked.connect(self.convert_file)
        self.__filename = filename

    @property
    def filename(self):
        return self.__filename

    @filename.setter
    def filename(self, new):
        self.__filename = new

    def browse_folder(self):
        file = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл")

        if file[0]:
            self.filename = file[0]
            self.lineEdit.setText(file[0])

    def convert_file(self):
        self.lineEdit.setText("Алесики")
        read_file = pd.read_csv('csvFile.csv')
        read_file.to_excel('testExcel.xlsx', index=None, header=True)
        handle = open(self.filename, "r")
        return


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
