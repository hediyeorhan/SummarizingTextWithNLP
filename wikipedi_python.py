
from PyQt5 import QtCore, QtGui, QtWidgets
import bs4 as bs
import urllib.request
import re
import nltk
import heapq

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

class Ui_wikipedi(object):
    def ozetle(self):
        url = self.lineEdit.text()
        veri = urllib.request.urlopen(url)
        okunan_metin = veri.read()

        ayristirilan_metin = bs.BeautifulSoup(okunan_metin,'lxml')

        paragraflar = ayristirilan_metin.find_all('p')

        metin = ""

        for p in paragraflar:
            metin += p.text

        #print(metin) ## ozetlenecek metin 

        # Referans numaralarini kaldiriyoruz.
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


        # Burada en yuksek puana sahip ilk 8 cumleyi aliyoruz. Daha fazlasini da alabiliriz verecegimiz degere baglidir.
        ozet_cumleleri = heapq.nlargest(5, cumle_puanlari, key=cumle_puanlari.get)

        ozet = ' '.join(ozet_cumleleri)
        print("OZETLEME ALGORITMASI")
        #print(ozet)
        self.textBrowser.setText(ozet)
        f = open("ozetlenenMetinWikipedi.txt", "w")
        f.write(ozet)
        f.close()
    def setupUi(self, wikipedi):
        wikipedi.setObjectName("wikipedi")
        wikipedi.resize(642, 432)
        self.centralwidget = QtWidgets.QWidget(wikipedi)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.ozetle())
        self.pushButton.setGeometry(QtCore.QRect(540, 20, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 100, 621, 291))
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 60, 131, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.label_2.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 20, 391, 20))
        self.lineEdit.setObjectName("lineEdit")
        wikipedi.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(wikipedi)
        self.statusbar.setObjectName("statusbar")
        wikipedi.setStatusBar(self.statusbar)

        self.retranslateUi(wikipedi)
        QtCore.QMetaObject.connectSlotsByName(wikipedi)

    def retranslateUi(self, wikipedi):
        _translate = QtCore.QCoreApplication.translate
        wikipedi.setWindowTitle(_translate("wikipedi", "Wikipedia Verilerini Özetleme"))
        self.label.setText(_translate("wikipedi", "URL : "))
        self.pushButton.setText(_translate("wikipedi", "ÖZETLE"))
        self.label_2.setText(_translate("wikipedi", "ÖZET METİN"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_wikipedi()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())