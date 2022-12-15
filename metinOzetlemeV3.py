import bs4 as bs
import urllib.request
import re
import nltk
import heapq

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

## wikipedi sitesinden ozetlenecek konu ile ilgili metni cekiyoruz.
veri = urllib.request.urlopen('https://en.wikipedia.org/wiki/Natural_language_processing')
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

# Hangi kelimenin agirlikli olarak tekrarlandigini bulmak icin noktalama isaretlerini de kaldiriyoruz.
sadece_kelime_metni = re.sub('[^a-zA-Z]', ' ', metin )
sadece_kelime_metni = re.sub(r'\s+', ' ', sadece_kelime_metni)

# ingilizcedeki durdurma kelimelerini aliyoruz.
durdurma_kelimeleri = nltk.corpus.stopwords.words('english')



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
# Cumlelerdeki kelimelere erisiyoruz. Kelimeler kelime tekrarlari yapisinda bulunuyor mu bakiyoruz.
cumle_puanlari = {}
for cumle_kelimeleri in cumle_listesi:
    for kelime in nltk.word_tokenize(cumle_kelimeleri.lower()):
        if kelime in kelime_tekrarlari.keys():
            if len(cumle_kelimeleri.split(' ')) < 30: ## 30 kelimeden az olan cumleler icin hesapliyoruz. Cok uzun olmamasi icin
                if cumle_kelimeleri in cumle_puanlari.keys(): # Cumleler anahtar deger olarak aliniyor. Cumledeki ilk kelimenin frekansi atanir.
                    cumle_puanlari[cumle_kelimeleri] += kelime_tekrarlari[kelime]
                else:
                    cumle_puanlari[cumle_kelimeleri] = kelime_tekrarlari[kelime]


# Burada en yuksek puana sahip ilk 7 cumleyi aliyoruz. Daha fazlasini da alabiliriz verecegimiz degere baglidir.
ozet_cumleleri = heapq.nlargest(7, cumle_puanlari, key=cumle_puanlari.get)

ozet = ' '.join(ozet_cumleleri)
print("OZETLEME ALGORITMASI")
print(ozet)

f = open("ozetlenenMetin.txt", "w")
f.write(ozet)
f.close()