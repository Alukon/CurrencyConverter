# pip install pyqt5
# pip install pyqt5-tools
# pip install currencyconverter
# pyuic5.exe ui.ui -o ui.py -x
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow
from currency_converter import CurrencyConverter

class CurrencyConv(QtWidgets.QMainWindow):
    def __init__(self):
        super(CurrencyConv, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('Конвертер валют')
        self.setWindowIcon(QIcon('111.png'))

        self.ui.input_amount.setPlaceholderText('Из валюты:')
        self.ui.input_currency.setPlaceholderText('У меня есть:')
        self.ui.output_amount.setPlaceholderText('В валюту:')
        self.ui.output_currency.setPlaceholderText('Я получу:')
        self.ui.pushButton.clicked.connect(self.converter)

    def converter(self):
        c = CurrencyConverter()
        input_amount = self.ui.input_amount.text()
        output_amount = self.ui.output_amount.text()
        input_currency = int(self.ui.input_currency.text())

        output_currency = round(c.convert(input_currency, '%s' %(input_amount), '%s' % (output_amount)), 2)

        self.ui.output_amount.setText(str(output_amount))

app = QtWidgets.QApplication([])
application = CurrencyConv()
application.show()

sys.exit(app.exec_())



