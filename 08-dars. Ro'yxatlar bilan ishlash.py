# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 15:36:23 2022

@author: Pro
"""

# RO'YXATNI TARTIBLASH
cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# cars.sort()
# print(cars)

# Katta va kichik harf
# cars = ['Bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# cars.sort()
# print(cars)

# Teskari tartib
# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# cars.sort(reverse=True)
# print(cars)

### sorted() funktsiyasi 3 asl ro'yxat ichidagi elementlarning ketma-ketligini buzmagan holda ro'yxatni tartiblash
# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# print("sorted () qaytargan ro'yxat: ", sorted(cars))
# print("Asl ro'yxat o'zgarmas qoldi:", cars)

### Ro'yxatni ortidan boshlab chiqarish asl o'zgarmagan holda
# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# print(sorted(cars, reverse=True))

###Ro'yxatni teskarisiga almashtirib qo'yish
# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# cars.reverse()
# print(cars)

### Sonlar bilan amallar
# sonlar = [12, 98, 34, 65, 34, 76, 11, -7.2, -5]
# sonlar.sort()
# print(sonlar)
# print(sorted(sonlar, reverse=True))

### RO'YXATNING UZUNLIGINI BILISH
# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# print(len(cars))

### ma'lum oraliqdagi sonlar ketma-ketligini yaratish
# sonlar = list(range(0,11))
# print("Sonlar: ", sonlar)
### qadamni berish uchun
# toq_sonlar = list(range(1,20,2))
# juft_sonlar = list(range(0,20,2))
# sanash = list(range(0,101,10)) # 1 dan 100 gacha 10 qadamdan sanamoqchi bo'lsak
# print("Juft sonlar: ", juft_sonlar)
# print("Toq sonlar: ", toq_sonlar)
# print("10 qadamdan sanasak: ", sanash)

### Maksimum va minimumini topish
# narxlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
# arzon = min(narxlar)
# qimmat = max(narxlar)
# jami = sum(narxlar)
# print("Eng arzon narx ", arzon, ". Eng qimmati ", qimmat, ". Jami: ", jami)

### RO'YXATNI KESISH
# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# my_cars = cars[0:3]
# print(my_cars)

# Ro'yxat boshidan 4-gacha kesadi (0,1,2,3)
# print(cars[:4])
# 2-elementdan boshlab ro'yxat oxirigacha kesib oladi
# print(cars[2:])

### RO'YXATDAN NUSXA OLISH
# sonlar = [1, 2, 3, 4, 5] # sonlar degan ro'yxat yaratamiz
# sonlar2 =  sonlar[:] # sonlar2 degan ro'yxatni sonlar ga tenglaymiz
# sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
# sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz
# print("Bu sonlar ro'yxati:", sonlar)
# print("Bu sonlar2 ro'yxati:", sonlar2)

# toys = ('bus','car','bear','dino','snake','lizard')
# print(toys[0])
# print(toys[-1])
# print(toys[2:5])
### TUPLES - O'ZGARMAS RO'YXAT

#      AMALIYOT

#01 O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
#02 Ro'yxatning uzunligini konsolga chiqaring
# MO_davlatlari = ["O'zbekiston", "Turkmaniston", "Qozog'iston", "Tojikiston", "Qirg'iziston"]
# print(len(MO_davlatlari))
# print(sorted(MO_davlatlari))
# print(sorted(MO_davlatlari, reverse=True))
# print(MO_davlatlari)
#print(MO_davlatlari.reverse(2))
# MO_davlatlari.sort()
# print(MO_davlatlari)
# MO_davlatlari.sort(reverse=True)
# print(MO_davlatlari)

#08 -----120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
# juft_sonlar = list(range(120, 1201, 2))
# print(juft_sonlar)
# print(f"Elementlar soni: {len(juft_sonlar)} ta")
# print(f"Juft sonlar yig'indisi - {sum(juft_sonlar)} ga teng")
# print(f"max - min = {max(juft_sonlar) - min(juft_sonlar)} ga teng")
# boshi = juft_sonlar[:20]
# ortasi = juft_sonlar[280:300]
# oxiri = juft_sonlar[-20:]
# print(boshi)
# print(ortasi)
# print(oxiri)

#013 taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar = ['manti', 'osh', 'xonim', 'norin', 'somsa']
nonushta = taomlar[:]
nonushta.remove('manti')
nonushta.remove('xonim')
nonushta.remove('norin')
print(nonushta)
nonushta.append('choy')
nonushta.append('xolva')
print(f"\nTaomlar ro'yxati {taomlar} dan iborat,")
print(f"\nErtalabki nonushta {nonushta}.")
nonushta = tuple(nonushta)
# nonushta[0] = 'qaymoq va non' #o'zgarmas ro'yxatga o'zgargani uchun ishlamaydi









