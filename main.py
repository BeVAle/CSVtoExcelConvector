import os
import sys
from datetime import datetime

import pandas as pd
from PyQt6 import QtWidgets

import design


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self, filename=None, new_filename=None, csv_columns=None):
        super().__init__()
        self.setupUi(self)
        self.SelectFileButton.clicked.connect(self.browse_folder)
        self.ConvertorButton.clicked.connect(self.convert_file)
        self.OpenButton.clicked.connect(self.open_file)
        self.__filename = filename
        self.__new_filename = new_filename
        self.__csv_columns = csv_columns

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

    @property
    def csv_columns(self):
        return self.__csv_columns

    @csv_columns.setter
    def csv_columns(self, new):
        self.__csv_columns = new

    def browse_folder(self):
        file = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл")

        if file[0]:
            extension = os.path.splitext(file[0])
            if extension[1] != '.csv':
                self.lineEdit.setText('Неверный тип файла')
                return

            self.filename = file[0]
            self.lineEdit.setText(file[0])
            self.OpenButton.setVisible(False)

            file = pd.read_csv(self.filename)
            self.csv_columns = file.columns

            self.lineEditInformationOnConvertation.setText(", ".join(file.columns))
            self.labelInformationOnConvertation.setVisible(True)
            self.lineEditInformationOnConvertation.setVisible(True)

    def convert_file(self):
        self.lineEdit.setText("Конвертация")

        columnsFromLine = self.lineEditInformationOnConvertation.text().strip()
        columnsFromLinelList = list(filter(None, columnsFromLine.split(', ')))

        for element in columnsFromLinelList:
            if not element in self.csv_columns:
                self.lineEdit.setText('Нет такого ключа: ' + element)
                return

        read_file = pd.read_csv(self.filename, usecols=columnsFromLinelList)

        extension = os.path.splitext(self.filename)
        self.new_filename = extension[0] + '_' + str(datetime.now().strftime('%d%m%Y%H%M%S')) + '.xlsx'
        read_file.to_excel(self.new_filename, index=None, header=True)
        self.OpenButton.setVisible(True)
        self.lineEdit.setText("Конвертирование успешно")
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
