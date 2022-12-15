from PyQt5 import QtCore, QtGui, QtWidgets
import bs4 as bs
import urllib.request
import re
import nltk
import heapq

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

class Ui_metin(object):
    def ozetle(self):
        metin = self.plainTextEdit.toPlainText()
        metin = re.sub(r'\[[0-9]*\]', ' ', metin)
        metin = re.sub(r'\s+', ' ', metin)

        print(metin)

        # metni cumlelere ayiriyoruz.
        cumle_listesi = nltk.sent_tokenize(metin)

        # ingilizcedeki durdurma kelimelerini aliyoruz.
        durdurma_kelimeleri = nltk.corpus.stopwords.words('english')

        # Hangi kelimenin agirlikli olarak tekrarlandigini bulmak icin noktalama isaretlerini de kaldiriyoruz.
        sadece_kelime_metni = re.sub('[^a-zA-Z]', ' ', metin )
        sadece_kelime_metni = re.sub(r'\s+', ' ', sadece_kelime_metni)

        # burada kelimelerin tekrar sayilarini tutuyoruz.
        kelime_tekrarlari = {}
        # ilk olarak ingilizcedeki durdurma kelimeleri mi bakiyoruz.
        # eger oyleyse kelime sozlukte varsa +1 eklenir, yoksa 1 olarak baslatilir.
        for kelime in nltk.word_tokenize(sadece_kelime_metni):
            if kelime not in durdurma_kelimeleri:
                if kelime in kelime_tekrarlari.keys():
                    kelime_tekrarlari[kelime] += 1
                else:
                    kelime_tekrarlari[kelime] = 1

        # en cok tekrar eden agirlikli kelimeyi aliyoruz.
        max_tekrarlanan_kelime = max(kelime_tekrarlari.values())

        # Son olarak, agirlikli sikligi bulmak için, asagida gosterildigi gibi, tüm sozcuklerin gecis sayisini en cok gecen 
        # sozcugun sikligina bolebiliriz.
        for kelime in kelime_tekrarlari.keys():
            kelime_tekrarlari[kelime] = (kelime_tekrarlari[kelime]/max_tekrarlanan_kelime)

        # Bu kisimda her cumleye ait bir puan hesapliyoruz.
        # Metinden ayirdigimiz cumleler uzerinde for ile geziniyoruz.
        # Cumlelerdeki kelimelere erisiyoruz. Kelimeler word_frequencies yapisinda bulunuyor mu bakiyoruz.
        cumle_puanlari = {}
        for cumle_kelimeleri in cumle_listesi:
            for kelime in nltk.word_tokenize(cumle_kelimeleri.lower()):
                if kelime in kelime_tekrarlari.keys():
                    if len(cumle_kelimeleri.split(' ')) < 30: ## 30 kelimeden az olan cumleler icin hesapliyoruz. Cok uzun olmamasi icin
                        if cumle_kelimeleri in cumle_puanlari.keys(): # Cumleler anahtar deger olarak aliniyor. Cumledeki ilk kelimenin frekansi atanir.
                            cumle_puanlari[cumle_kelimeleri] += kelime_tekrarlari[kelime]
                        else:
                            cumle_puanlari[cumle_kelimeleri] = kelime_tekrarlari[kelime]


        # Burada en yuksek puana sahip ilk 10 cumleyi aliyoruz. Daha fazlasini da alabiliriz verecegimiz degere baglidir.
        ozet_cumleleri = heapq.nlargest(7, cumle_puanlari, key=cumle_puanlari.get)

        ozet = ' '.join(ozet_cumleleri)
        print("OZETLEME ALGORITMASI")
        print(ozet)
        self.textBrowser_2.setText(ozet)
        f = open("ozetlenenMetin.txt", "w")
        f.write(ozet)
        f.close()

        
    def setupUi(self, metin):
        metin.setObjectName("metin")
        metin.resize(697, 584)
        self.centralwidget = QtWidgets.QWidget(metin)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 89, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 400, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(200, 290, 481, 251))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.ozetle())
        self.pushButton.setGeometry(QtCore.QRect(40, 250, 101, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.pushButton.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(200, 10, 481, 251))
        self.plainTextEdit.setObjectName("plainTextEdit")
        metin.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(metin)
        self.statusbar.setObjectName("statusbar")
        metin.setStatusBar(self.statusbar)

        self.retranslateUi(metin)
        QtCore.QMetaObject.connectSlotsByName(metin)

    def retranslateUi(self, metin):
        _translate = QtCore.QCoreApplication.translate
        metin.setWindowTitle(_translate("metin", "MainWindow"))
        self.label.setText(_translate("metin", "ÖZETLENECEK METİN"))
        self.label_2.setText(_translate("metin", "ÖZETLENEN METİN"))
        self.pushButton.setText(_translate("metin", "ÖZETLE"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_metin()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())