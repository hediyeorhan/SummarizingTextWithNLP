<h1> SummarizingTextWithNLP </h1>
<h2> 1.	PROJE KONUSU VE ÖZETİ </h2>

Günümüzde aradığımız birçok kaynak internette kolaylıkla bulunabilmektedir. Bu da bilgi fazlalığı ve çok fazla bilgi arasında kaybolmaya sebep olmaktadır. Bu nedenle metin özetleme uygulaması geliştirilmesine karar verilmiştir. 
Metin özetleme uygulamasında doğal dil işleme algoritmaları kullanılacaktır. Uygulama sayesinde bulunan kaynaklardaki çok uzun metinler özetlenebilecektir. Özetlenen metin içeriği okunarak aranan bilginin metin içerisine yer alıp almadığı kolaylıkla anlaşılabilecektir. İnternette literatür taraması ve kaynak taraması yapılırken hangi kaynakların incelenebileceğinin seçiminde kolaylık sağlayacaktır.
Metin özetleme çalışmalarının örnekleri birçok kaynakta mevcuttur. Bu yüzden projeye özgünlük kazandırmak adına özgün bir ara yüz tasarımı yapılacaktır. Uygulama ara yüz üzerinden girilen metnin özetini bize yine ara yüz aracılığı ile gösterecektir. Projenin geliştirilme süresine bağlı olarak imkân olursa uygulama, ara yüze belirli formatlarda dosya eklenebilmesi ve dosyaların özetinin çıkarılması şeklinde revize edilecektir.


<h2> 2. PROJENİN AMACI VE HEDEFİ </h2>

Projenin geliştirilmesindeki amaç insanların bir bilgiye ulaşmak için doğru kaynak ararken çok zaman harcamalarını engellemektir. Metin özetleme ile uzun metinler ve akademik çalışmaların kısa bir özeti elde edilecektir. Elde edilen özet incelenerek istenilen bilginin o çalışmada bulunup bulunmadığı anlaşılacaktır. Bu şekilde kaynak ve literatür taramasında harcanılan zamandan tasarruf edilecektir.  Projedeki temel amaç zamandan tasarruf etmektir.
Projenin bir diğer hedefi, kullanıcılara kullanışlı bir ara yüz sunmaktır. Ara yüz kullanımının basit olması kullanım kolaylığı sağlayacaktır.


<h2> 3.	PROJEDE KULLANILAN YAZILIMLAR </h2>

Algoritmanın geliştirilme aşamasında Python programlama dili kullanılacaktır. Python, nesne yönelimli, yorumlamalı, birimsel, etkileşimli ve yüksek seviyeli bir programlama dilidir. Python programlama dili ile algoritmayı kodlamak için Visual Studio Code ortamı kullanılacaktır. Visual Studio Code, içerisinde birçok eklentiyi barındıran, çapraz platformlarda çalışabilen ve birçok programlama dili (C, C#, Java, Python, PHP ve Go) desteği olan tam özellikli bir kod editörüdür. Visual Studio Code, hata ayıklama, gömülü Git kontrolü, sözdizimi vurgulama, akıllı kod tamamlama, snippet’ler ve kodu yeniden yapılandırma desteği içerir. Uygulamada kullanılacak ara yüz için pyqt5 kullanılacaktır. Pyqt, bir Python eklentisi olarak uygulanan platformalar arası GUI araç seti Qt’nin bir Python bağlantısıdır. 
      

<h2> PROJENİN YAPIM AŞAMALARI VE SONUÇ </h2>

Proje geliştirilirken öncelikle bir veri setinin gerekli olup olmadığı araştırılmıştır. Yapılan araştırmalar sonucunda veri setine gerek duyulmadığı anlaşılmıştır. Projede kullanılacak ara yüz için pyqt5 [3] kütüphanesi kurulumu gerçekleştirilmiştir. Kurulum aşaması ve kullanılan komut Şekil 1’de görülmektedir.

![image](https://user-images.githubusercontent.com/59260491/207919743-8a381bad-71e3-4230-b456-38e0c25ff37c.png)

Şekil 1: Pyqt5 kurulumu

Pyqt5 kurulumu gerçekleştirildikten sonra metin üzerinde işlemler yapılmasını sağlayan ntlk [4] kütüphanesi kurulumu ve internet üzerinden veri çekerken kullanılacak beautifulsoup [5] kütüphanesi kurulumu gerçekleştirilmiştir. Gerekli kurulumlar gerçekleştirildikten sonra ilk olarak metin özetleme fonksiyonu üzerinde çalışılmıştır. Sonrasında ara yüz oluşturulmuştur ve özetleme fonksiyonu ile ara yüz birleştirilmiştir. 
Projede metin özetleme kısmında iki seçenek bulunmaktadır. Wikipedia sitesinde istenilen konuda bir metin üzerinde özetleme gerçekleştirilebilmektedir. Özetlenmesi istenilen konunun url adresi belirtilerek buradan çekilen konu ile ilgili metin özetleme algoritmasına verilerek özetlenecektir.  Şekil 2’de verilerin çekilmesi ve özetlenecek metin formatına getirilmesi görülmektedir.

![image](https://user-images.githubusercontent.com/59260491/207919826-641c625e-8130-43ca-bc20-a7cbe348f1d7.png)

Şekil 2: Verilerin çekilmesi ve istenilen formata getirilmesi

Veriler çekildikten sonra wikipedia metinlerinde bulunan referans numaraları kaldırılmıştır. Metindeki cümleler ayrıştırılmıştır ve bir liste yapısında tutulmuştur. Sonrasında kelimelerin tekrar sayılarını bulmak için metinlerde bulunan noktalama işaretleri kaldırılmıştır. Şekil 3’te bu işlemlerin sırası ile yapıldığı görülmektedir.

![image](https://user-images.githubusercontent.com/59260491/207919912-61ddc7e2-5411-49b0-a8d2-56b1ab2e9812.png)

Şekil 3: Veri ön işleme adımları
										
Noktalama işaretlerinin kaldırıldığı ve sadece kelimelerden oluşan metin üzerinden kelimelerin tekrar etme sayıları bir sözlük yapısında tutulmuştur. En çok tekrar eden kelimenin tekrar sayısı elde edilmiştir. Bu maksimum tekrar sayısı tüm kelimelerin tekrar sayılarına tek tek bölünerek ağırlıklı sıklık değeri elde edilmiştir. Sonrasında bu değerler cümle puanlamaları yapmak için kullanılacaktır. Yapılan işlemlere ait kod blokları Şekil 4’te görülmektedir.

![image](https://user-images.githubusercontent.com/59260491/207919987-defd2354-5a2d-4b2e-947c-877f49275a87.png)
 
Şekil 4: Kullanılacak değerlerin elde edilmesi

Elde edilen metindeki cümleler ayrılıp bir cümle listesinde tutulmuştur. Cümlelerin bulunduğu liste for döngüsü ile gezilerek her bir cümle tek tek ele alınmıştır sonrasında bu cümlelerdeki kelimeler yine for döngüsü ile ayrıştırılmıştır. Sonrasında cümlelerde bulunan kelimeler oluşturulan kelime tekrarı sözlüğünde bulunuyorsa bu cümlelerin puanı hesaplanmıştır. Cümlelerdeki kelimeler boşluklara göre ayrılmıştır ve bu kelimeler kelime tekrarlarının bulunduğu sözlük yapısında mevcut ise buradaki frekans değerleri eklenmiştir mevcut değil ise başlangıç olarak 1 değeri atanmıştır. Şekil 5’te yapılan cümle puanlarının hesaplanması görülmektedir.

![image](https://user-images.githubusercontent.com/59260491/207920073-c53c77f1-7a98-4d27-b5d6-c319f00baf65.png)

Şekil 5: Cümle puanlarının hesaplanması
	
Hesaplanan cümle puanlarından en yüksek puana sahip n adet cümle alınarak özetleme işlemi bitiriliyor. Kaç adet cümle alınacağı isteğe göre belirlenebilir.  Şekil 6’da en yüksek puana sahip ilk 7 cümlenin alındığı görülmektedir. Daha sonra bu cümleler birleştirilerek bir özet metin oluşturulmuştur.

![image](https://user-images.githubusercontent.com/59260491/207920153-bff8b536-dcfb-41ae-862a-894e1d517b76.png)
 
Şekil 6: Özetlenen cümlelerin birleştirilmesi ve özet metnin oluşturulması

Özetlenen metin kayıt altına alınması ve tutulması için bir txt dosyasına yazdırılmıştır. Şekil 7’de bu işlem görülmektedir.

![image](https://user-images.githubusercontent.com/59260491/207920205-b9d2cb59-a329-4a9d-9b08-a96452f71e3f.png) 

Şekil 7: Özetlenen metnin txt formatında kayıt edilmesi


Metin özetleme algoritmaları bittikten sonra ara yüz tasarımına geçilmiştir. Ara yüz tasarımın Qt Designer kullanılmıştır. Şekil 8’de ara yüz uygulamalarının oluşturulma aşaması görülmektedir. Qt Designer kullanılarak oluşturulan ara yüz dosyası, python dosyası haline çevrilerek metin özetleme fonksiyonları dâhil edilmiştir. Şekil 9’da .ui uzantılı tasarım dosyasının python dosyasına dönüşümü görülmektedir.

![image](https://user-images.githubusercontent.com/59260491/207920296-1eee9204-bad1-4f53-8304-33fd0b3baf70.png)
 
Şekil 8: Ara yüz oluşturulma aşaması

![image](https://user-images.githubusercontent.com/59260491/207920349-f8df010d-911d-4a72-a83a-35b82eb7802f.png)
 
Şekil 9: .ui dosyasının .py dosyasına dönüşümü


Kullanıcı hangi tür metin özetlemek istediğini seçim ekranı aracılığıyla seçebilmektedir. Bu seçimlere göre kullanıcının hizmetine iki ayrı pencere açılmaktadır.

![image](https://user-images.githubusercontent.com/59260491/207920386-a1d5af31-3ff7-4367-9580-b29217325888.png)

Şekil 10: Seçim ekranı


Kullanıcı wikipedia seçeneğini seçtiğinde url girilmesi gereken bir kısım gelmektedir. Girilen url adresindeki metnin özetlenmiş hali özet metin kutusunda görülecektir. Wikipedia için geliştirilen ara yüz ve kullanımı Şekil 11’de görülmektedir.

![image](https://user-images.githubusercontent.com/59260491/207920435-be6de91f-5b1b-464b-828f-657da5b29bb5.png)
 
Şekil 11: Wikipedia için geliştirilen ara yüz ve kullanımı


Kullanıcının istediği herhangi bir metni girmesi ve bu metnin özetlenmesi için bir de metin ara yüzü oluşturulmuştur. Şekil 12’de kullanıcıdan alınan metin özetlenmiştir.

![image](https://user-images.githubusercontent.com/59260491/207920496-42c12022-590e-45e2-a3c5-854c2fd727bc.png)
 
Şekil 12: Kullanıcıdan alınan metnin özetlenmesi

Ara yüz üzerindeki wikipedia ve kullanıcı metinlerinin özetlenmiş hallerinin kayıt edilmesi ve kaybolmaması için özetler txt formatında tutulmuştur. Şekil 13’ de görülmektedir.

![image](https://user-images.githubusercontent.com/59260491/207920549-adc12814-b9ce-49df-aa5d-288de74e8a6c.png)
 
Şekil 13: Özet metinlerin txt formatında tutulması


<h2> KAYNAKLAR </h2>

[1]	Metin Özetleme Algoritmaları. Available: https://mgminsights.com/2021/05/09/nlpde-metin-ozetleme-algoritmalari/

[2]	Text Summarization. Available: https://www.projectpro.io/article/text-summarization-python-nlp/546

[3]	PyQT5. Available: https://pypi.org/project/PyQt5/

[4]	NLTK Library. Available: https://www.nltk.org/

[5]	Beatiful Soup Library. Available: https://pypi.org/project/beautifulsoup4/








 
