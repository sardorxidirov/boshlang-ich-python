# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 09:38:52 2022

@author: Pro
"""

#mevalar = ["olma", "anjir", "shaftoli", "o'rik"] # mevalar ro'yxati (matnlar)
#narxlar = [12000, 18000, 10900, 22000, 25000, 36000, -25, 63.2] # narhlar ro'yxati (sonlar)
#sonlar = ['bir', 'ikki', 3, 4, 5] # narhlar ro'yxati (sonlar)
#ismlar = [] # bo'sh ro'yxat

# Yangi element qo'shish
# .append() metodi
# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
# mevalar.append("tarvuz") # mevalar ga tarvuz qo'shamiz
# print(mevalar)
# .append() metodi bo'sh ro'yxatni to'ldrisihda juda qulay usul. Odatda dastur boshida bo'sh ro'yxat yaratilib, dastur davomida ro'yxat foydalanuvchi tomonidan to'ldirib borilishi odatiy hol.

# cars = [] # bo'sh ro'yxat yaratamiz
# cars.append('Lacetti') # ro'yxatga Lacetti mashinasini qo'shamiz
# cars.append('Nexia 3') # ro'yxatga Nexia 3 mashinasini qo'shamiz
# cars.append('Cobalt')  # ro'yxatga Cobalt  mashinasini qo'shamiz
# print(cars)

# .insert() metodi
# Ro'yxatning istalgan joyiga yangi element qo'shish uchun .insert() metodidan foydalanamiz. .insert() metodi ichida yangi elementning indeksi va qiymati beriladi:
# cars = ['Lacetti', 'Nexia 3', 'Cobalt']
# cars.insert(0, 'Malibu') # 1-o'ringa yangi qiymat qo'shamiz
# print(cars)

# Elementni o'chirish
# Inedks yordamida olib tashlash uchun del operatoridan foydalanamiz:
# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
# del mevalar[1] # 2-element (anjir) ni o'chirib tashlaymiz
# print(mevalar)

# lement qiymati bo'yichi o'chirish uchun esa .remove(qiymat) metodidan foydalanamiz. Buning uchun qavs ichida o'chirib tashlash kerak bo'lgan qiymatni yozamiz
# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
# mevalar.remove('shaftoli') # Ro'yxatdan shaftolini o'chirdik
# print(mevalar)

# hayvonlar = ['it', 'mushuk', 'sigir', 'qo\'y', 'quyon', 'mushuk']
# hayvonlar.remove("mushuk") # Ro'yxatda 2 ta mushuk bor, ulardan birinchisi o'chadi
# print(hayvonlar)

# Elementni sug'urib olish
# Buning uchun Pythonda .pop(indeks) metodidan foydalanmiz.
# bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
# mahsulot = bozorlik.pop(3) # Ro'yxatdan banan ni sug'urib olamiz
# print("Men " + mahsulot + " sotib oldim")
# print("Olinmagan mahsulotlar: ", bozorlik)
# Agar .pop() metodida indeks berilmasa, ro'yxatdan o'xirgi qiymat sug'urib olinadi.

# AMALIYOT
#01 ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
#02 Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring:

# ismlar = ['Saidahmad', 'Orifjon', 'Nodir']
# xabar1 = "Salom " + ismlar[0] + ", do'stim ishlaring yaxshimi?"
# xabar2 = ismlar[1] + " do'stim yaxshimisiz?, futbolga boramizmi?"
# xabar3 = ismlar[2] + " uyga birga qaytamizmi?"

# print(xabar1)
# print(xabar2)
# print(xabar3)
# print(f"{ismlar[1]} va {ismlar[2]} bir birlarini yaxshi tanishadi")

#03 t_shaxslar va z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.
#04 Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring.

#sonlar = [25000, 11200, -8500, -36.5, 0.14, 5000]
#print(sonlar)
#sonlar.append(300)
#print(sonlar)
#sonlar.remove(-8500)
#print(sonlar)
#del sonlar[2]
#print(sonlar)
#sonlar.insert(2, 0.001)
#print(sonlar)
#sonlar2 = sonlar.pop(2)
#print(sonlar)

#05 t_shaxslar va z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.
#06 Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:

# t_shaxslar = ["Abu Bakr (r.a)", "Umar (r.a)", "Usmon (r.a)", "Ali (r.a)", "Imom Buxoriy", "Al-Xorazmiy", "Al-Beruniy", "Ibr Sino"]
# z_shaxslar = ["Abdulloh domla", "Abror Muxtor Aliy", "Shayx Muhammadsodiq Muhammadyusuf", "Putin", "Ilon Mask", "Anvar Narzullayev"]
# print("Men tarixiy shaxslardan " + t_shaxslar.pop(1) + " bilan,\nzamonaviy shaxslardan esa " + z_shaxslar.pop(0) + " bilan \nsuhbat qilishni istar edim")
# print(f"\nMen tarixiy shaxslardan {t_shaxslar.pop(1)} bilan,\n\zamonaviy shaxslardan esa {z_shaxslar.pop(0)} bilan\n\suhbat qilishni istar edim\n")

#07 friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
#08 Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang.

friends = []
friends.append('Saidahmad')
friends.append('Orifjon')
friends.append('Nodir')
friends.append('Sherzod')
friends.append('Xurshid')
friends.append('Jahongir')
# print(friends)
friends.remove('Sherzod')
# print(friends)
friends.insert(-1, 'Abdularif')
friends.insert(0, 'Muhammadali')
friends.insert(4, 'Toyloq')
print(friends)


#09 Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.

mehmonlar = []
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(3))
mehmonlar.append(friends.pop(-1))
print("\nKelgan mehmonlar: ", mehmonlar)















