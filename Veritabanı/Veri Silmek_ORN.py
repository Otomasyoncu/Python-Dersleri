import sys, pyodbc
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import *
uygulama = QtWidgets.QApplication(sys.argv)

pencere01 = QtWidgets.QWidget()
pencere01.setWindowTitle("Veri Düzenlemek")
pencere01.setGeometry(400, 50, 400, 400)
pencere01.setWindowIcon(QtGui.QIcon("logo.ico"))

etiket1 = QtWidgets.QLabel(pencere01)
etiket1.setText("Okul No")
etiket1.move(20, 33)
etiket1.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))

etiket2 = QtWidgets.QLabel(pencere01)
etiket2.setText("Okul No Girin ve SİL e Basınız")
etiket2.move(90, 120)
etiket2.setFont(QtGui.QFont("Times", 10, QtGui.QFont.ExtraBold))

ya1 = QtWidgets.QLineEdit(pencere01)
ya1.setText("")
ya1.setGeometry(100,30,120,25)
ya1.setEnabled(True)
ya1.setFont(QtGui.QFont("Times", 10))
ya1.setAlignment(Qt.AlignLeft)

def serkan():
    baglan = pyodbc.connect(
        r"Driver={Microsoft Access Driver (*.mdb)};"
        r"DBQ=database.tml;"
        r"PWD=12345;")
    islem = baglan.cursor()
    islem.execute(
        "delete from KULLANICILAR where OKUL_NO='"+ ya1.text() +"'"
    )
    baglan.commit()
    etiket2.setText("Silme İşlemi Tamamlandı.")

buton = QtWidgets.QPushButton(pencere01)
buton.setText("Sil")
buton.move(222, 29)
buton.setFixedSize(78, 27)
buton.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
buton.clicked.connect(serkan)

pencere01.show()
sys.exit(uygulama.exec_())