import numpy as np
print("-"*25)
#a =np.arange(10) # 0 il 10 arasında a dizisi oluşturur.
a=[0,1,2,3,4,5,6,7,8,9]
print(a) # a dizisini yazdırır --> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[1]) # 1.indeksteki elemanı yazar --> 1
print(a[-1]) # dizinin sondan ilk elemanını yazar(0. indeks oluyor) -->  9
print(a[::-1]) # a dizisini tersten yazar --> [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(a[2:5]) # 2.indeksten 5.indekse kadar 5 dahil değil elemanları yazar --> [2, 3, 4]
print(a[2:]) # 2. indeksten başlayıp son eleman kadar elemanları yazar --> [2, 3, 4, 5, 6, 7, 8, 9]
print(a[1:6:2]) # 1 ile 6 arasında 2 şer aratak elamanları yazar --> [1, 3, 5]
print(a[::3]) #0 dan başlayıp son elemana kadar 3'er 3'er yazdırır --> [0, 3, 6, 9]
print(a[3:8]) # 3 ile 8 arasındaki  sayıları yazar [3,8) --> [3, 4, 5, 6, 7]
print(a[:4]) # 4'e a kadar olan sayilari yazar --> [0, 1, 2, 3]
print(a[::3]) #0 dan başlayı 3'er 3'er yazdırır --> [0, 3, 6, 9]
print(a[1:5:3]) # 1 5 indekseleri ARASINDA 3'er 3'er yazdır --> [1, 4]
print("a" , a[1:5:]) # 1 ve 5 indeksleri ARASINDA varsayılan olarak 1 artırır-->  [1, 2, 3, 4]
print("a" , a[1:5:1]) # 1 ve 5 indeksleri ARASINDA  1'er artarak --> [1, 2, 3, 4]
#a[3:8]=13  #3 ile 8 aralığındaki değerelie 13 yap anlamında --> otomatik oluşturulan dizide çalışıyor
a[8]=13
print(a)


print("-"*25)
