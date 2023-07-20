# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 15:10:08 2023

@author: USER
"""

# ad = "Asqar"
# fam = "janxojaev"
# ad_Fam =f"{ad} {fam}"
# print(ad_Fam)
# print(f" {ad}  {fam}")
# str1 = "Hello  World"
# print(str1)

# # string function
# print("upper function : "+ad_Fam.upper())
# print("lower function : "+ad_Fam.lower())
# print("capitalize function : "+ad_Fam.capitalize())
# print("title function : "+ad_Fam.title()) 

# meva = "    alma    "
# print("Men  "+meva+"  jaqsi koremen")
# print("Men  "+meva.lstrip()+"  jaqsi koremen")  # lstrip tekstti left jaqtan probelin kesedi
# print("Men  "+meva.rstrip()+"  jaqsi koremen")  # lstrip tekstti right jaqtan probelin kesedi
# print("Men  "+meva.strip()+"  jaqsi koremen")  # lstrip tekstti eki jaqtan probelin kesedi
# print("Men  "+meva+"  jaqsi koremen")
# meva = meva.strip()


# ad = input("Atiniz kim ? ")
# print("Sizin atiniz : "+ad.title())


# lists

# miywe = ['alma', 'almurt', 'shabdal']
# miywe.append("banan")  # apppend tek aqirina element qosadi
# miywe.insert(len(miywe)-7, "juzim")  # insert korsetilgen indeks boyinsha element qosadi
# pradukt = miywe.pop(2)   # pop listten elementti suwirip aladi
# miywe.remove("juzim")   # remove listten elementti manisi boyinsha oshirip taslaydi



# alindi = []
# bazarliq = ['makaron','alma','may','gurish']
# aldim = input(' bazardan men  adlim : ')
# alindi.append(bazarliq.remove(aldim)) 

# print('bazardan alingan onim : ',aldim)
# print('bazardan endi alaman : ',bazarliq)


# cars=['tesla', 'bmw','tayota','chevrolet','audi']

# print(sorted(cars, reverse=True))

# uzinliq funkciysai len()

# Range
# sanlar = list(range(0,11))  (0, 11) bolsa 0 den 10ga shekem aladi
# print(sanlar)
# print('jupsanlar : ', list(range(0,11,2)))
# print('jupsanlar : ', list(range(1,11,2)))


# MAX MIN SUM funkciyalari

# bahalar  = [150,125,135,100,241]
# print('en qimbat baha',max(bahalar))
# print('en arzan baha',min(bahalar))
# print('uluwna baha',sum(bahalar))


# Listti kesiw 

# cars=['tesla', 'bmw','tayota','chevrolet','audi']

# print(' 1-2-3 elementler : ',cars[1:4])  # 1-elementten baslap 4-elementke shekem shigaradi (4 kirmeydi)
# print('4-elementke shekembarligi  : ',cars[:4]) 
# print('1-den baslap hamme elementler : ',cars[1:])

# Listten kopiya aliw
# cars=['tesla', 'bmw','tayota','chevrolet','audi']
# my_cars=cars[:]   # kopiya aliw ushin : funkciyasinan paydalaniw kerek
# print(my_cars)


# TUPLE ozgermes constanta list esaplanadi

# cars=('tesla', 'bmw','tayota','chevrolet','audi')
# print(cars[2])
# # TUPLE -> List  # daslep listke aylandirirp sonra tuplege aytadan otkizemis
# cars=list(cars)
# cars.append('nexia')
# cars = tuple(cars)
# print(cars)


# Cikl operatori
# print('3 jaqin doslarin izdi kiritin :  ')
# dostlar = []
# for dost in range(3):
#     dostlar.append(input(f' {dost+1}-dostiniz atin jazin : '))
# print(dostlar)


#  Shart operatorlari if-else
#  misali ushin sanlardi salistiramiz
sanlar = [1,2,3,4,5,6,7,8,9,10]
for san  in sanlar :
    if san <=5 :
        print(san, '-bul san 5 ten kishi yamasa ten')
    else:
        print(san,'-bul san 5 ten aniq ulken')













