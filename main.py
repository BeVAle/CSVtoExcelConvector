import os
import sys

import pandas as pd
from PyQt6 import QtWidgets

import design


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self, filename=None, new_filename=None):
        super().__init__()
        self.setupUi(self)
        self.SelectFileButton.clicked.connect(self.browse_folder)
        self.ConvertorButton.clicked.connect(self.convert_file)
        self.OpenButton.clicked.connect(self.open_file)
        self.__filename = filename
        self.__new_filename = new_filename

    @property
    def filename(self):
        return self.__filename

    @filename.setter
    def filename(self, new):
        self.__filename = new

    @property
    def new_filename(self):
        return self.__new_filename

    @new_filename.setter
    def new_filename(self, new):
        self.__new_filename = new

    def browse_folder(self):
        file = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл")

        if file[0]:
            self.filename = file[0]
            self.lineEdit.setText(file[0])

    def convert_file(self):
        self.lineEdit.setText("Алесики")
        read_file = pd.read_csv(self.filename)
        self.new_filename = self.filename.replace('.csv', '.xlsx')
        read_file.to_excel(self.new_filename, index=None, header=True)
        self.OpenButton.setVisible(True)
        self.lineEdit.setText("Конвертированние успешно")
        return

    def open_file(self):
        os.system("start " + self.new_filename)
        return


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
