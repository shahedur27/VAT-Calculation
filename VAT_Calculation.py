from PyQt5 import QtWidgets
import sys
from vat_gui import Ui_MainWindow

class my_app(QtWidgets.QMainWindow):
    def __init__(self):
        super(my_app, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.calculate)

    def calculate(self):
        net = round((float(self.ui.lineEdit.text()) * 100) / (float(self.ui.lineEdit_2.text()) + 100), 2)
        vat = round((float(self.ui.lineEdit_2.text()) * net) / 100, 2)
        vap = round(float(self.ui.lineEdit_2.text()), 2)
        gross = round(float(self.ui.lineEdit.text()), 2)

        self.ui.net_result.setText(str(net))
        self.ui.vat_result.setText(str(vat))
        self.ui.vat_presult.setText(str(vap) + "%")
        self.ui.gross_result.setText(str(gross))




def app():
    app = QtWidgets.QApplication(sys.argv)
    win = my_app()
    win.show()
    sys.exit(app.exec_())

app()