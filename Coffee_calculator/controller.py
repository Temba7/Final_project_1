import random

from PyQt5.QtWidgets import *
from view_4 import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    """
    A class representing details about the coffee bill calculator
    """

    prices = {
        "Coffee Frappuccino": {"Tall": 2.95, "Grande": 3.65, "Venti": 4.15},                          #prices of the drinks 
        "Coffee Latte": {"Tall": 2.95, "Grande": 3.99, "Venti": 4.45},
        "Iced Coffee": {"Tall": 2.25, "Grande": 2.65, "Venti": 2.96}
    }

    order_price = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.submit())
        self.pushButton_2.clicked.connect(lambda: self.buy())

    def submit(self):
        """"
        Method to access the customer's want and size of their cup
        """

        want = self.comboBox.currentText()
        size = self.comboBox_2.currentText()
        self.order_price = self.prices[want][size]
                                                       
        self.order_summary.setText(f"{want}, {size}: ${self.order_price:.2f}")

    def buy(self):
        """"
        Method to access the customer's money.
        """
        try:

            total = float(self.get_money.text())

            amount = total - self.order_price

            if amount >= 0:
                self.final_receipt.setText(f"Change back  ({amount:.2f})")

            else:
                self.final_receipt.setText(f" Your $ {total} is not enough,you need {abs(amount):.2f} to buy something.")

        except ValueError:
            self.final_receipt.setText(f"Please insert the money!")     # in case thier money is not enough 



