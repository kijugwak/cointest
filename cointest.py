import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pybithumb
import time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(800, 150, 120, 180)
        self.setWindowTitle("PyQt")
        self.setWindowIcon(QIcon("icon.png"))

        btn = QPushButton("ETC", self)
        btn.move(10, 10)
        btn.clicked.connect(self.btn_clicked1)
        df = pybithumb.get_ohlcv("ETC")
        ma5 = df['close'].rolling(window=5).mean()
        last_ma5 = ma5[-2]

        price = pybithumb.get_current_price("ETC")

        if price > last_ma5:
            print("ETC 상승장")
        else:
            print("ETC 하락장")
        
        btn = QPushButton("MBL", self)
        btn.move(10, 50)
        btn.clicked.connect(self.btn_clicked2)
        df = pybithumb.get_ohlcv("MBL")
        ma5 = df['close'].rolling(window=5).mean()
        last_ma5 = ma5[-2]

        price = pybithumb.get_current_price("MBL")

        if price > last_ma5:
            print("MBL 상승장")
        else:
            print("MBL 하락장")

        btn = QPushButton("XRP", self)
        btn.move(10, 90)
        btn.clicked.connect(self.btn_clicked3)
        df = pybithumb.get_ohlcv("XRP")
        ma5 = df['close'].rolling(window=5).mean()
        last_ma5 = ma5[-2]

        price = pybithumb.get_current_price("XRP")

        if price > last_ma5:
            print("XRP 상승장")
        else:
            print("XRP 하락장")

        btn = QPushButton("CHZ", self)
        btn.move(10, 130)
        btn.clicked.connect(self.btn_clicked4)
        df = pybithumb.get_ohlcv("CHZ")
        ma5 = df['close'].rolling(window=5).mean()
        last_ma5 = ma5[-2]

        price = pybithumb.get_current_price("CHZ")

        if price > last_ma5:
            print("CHZ 상승장")
        else:
            print("XRP 하락장")
    class MyApp(QWidget):
        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):

            btn = QPushButton('Quit', self)

            btn.move(50,50)
            btn.resize(btn.sizeHint())

            btn.clicked.connect(QCoreApplication.instance().quit)
            
            self.setWindowTitle('Quit Test')
            self.setGeometry(300, 300, 300, 200)
            self.show()


    def btn_clicked1(self):
        price = pybithumb.get_current_price("BTC")
        print(price)
        time.sleep(0.5)

    def btn_clicked2(self):
        price = pybithumb.get_current_price("MBL")
        print(price)
        time.sleep(0.5)

    def btn_clicked3(self):
        price = pybithumb.get_current_price("XRP")
        print(price)
        time.sleep(0.5)

    def btn_clicked4(self):
        price = pybithumb.get_current_price("CHZ")
        print(price)
        time.sleep(0.5)


                    
app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
ex = MyApp()
sys.exit(app.exec_())
