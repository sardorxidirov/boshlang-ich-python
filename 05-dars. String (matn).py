# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 15:18:31 2022

@author: Pro
"""

#shahar = "Қўқон"
#viloyat = 'Фарғона'

#matn = 'Men yangi 📱 oldim'
#smayl = '😍'
#print(matn)
#print(smayl)

# STRING USTIDA AMALLAR

#ism = 'Ahmad'
#print("Mening ismim " + ism)

#ism = 'Ahad'
#familiya = 'Qayum'
#print(ism + familiya)
#print(ism +' ' + familiya)

# f-string

#ism = 'Ahad'
#familiya = 'Qayum'
#ism_sharif = f'{ism} {familiya}'
#print(ism_sharif)

#ism = "James"
#familiya = 'Bond'
#print(f"Salom, mening ismim {familiya}. {ism} {familiya}")

# Maxsus belgilar

#print('Hello World!')
#print('Hello \tWorld!')
#print('Hello \nWorld!')

# STRING METODLAR

# ism = 'james'
# familiya ='bond'
# ism_sharif = f"{ism} {familiya}"
# ism_sharif = ism_sharif.upper()
#print(ism_sharif.lower())
#print(ism_sharif.title())
#print(ism_sharif.capitalize())

# meva = "     olma     "
# print(meva)
# print("Men " + meva.lstrip() + " yaxshi ko'raman")
# print("Men " + meva.rstrip() + " yaxshi ko'raman")
# print("Men " + meva.strip() + " yaxshi ko'raman")
# print("Men " + meva + " yaxshi ko'raman")

# INPUT

# ism = input("Ismingiz nima?")
# print("Assalomu aleykum" + ism)

# ism = input("Ismingiz nima?\n>>>") #Foydalanuvchining ismini pastki qatordan yozishi
# print("Assalomu aleykum, " + ism.title())

# AMALIYOT 19.03.2022

#01 Quyidagi o'zgaruvchilarni yarating:
kocha = "Bog'bon"
mahalla = "Sog'bon"
tuman = "Bodomzor"
viloyat = "Samarqand"
# Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
# Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati
#print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + tuman + " tumani, " + viloyat + " viloyati")

#02 Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini foydalanuvchidan so'rang. 
    #Va avvalgi mashqni takrorlang.
#kocha = input("Ko'changizni nomi:\n>>>")
#mahalla = input("Mahallangizni nomi:\n>>>")
#tuman = input("Tumaningizni nomi:\n>>>")
#viloyat = input("Viloyatingizni nomi:\n>>>")
#print("Sizning manzilingiz " + kocha + " ko'chasi, " + mahalla + " mahallasi, " + tuman + " tumani, " + viloyat + " viloyati")

#03 Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing
    #bu masalaga #01 mashqdan o'zgaruvchi olindi
#print(kocha + " ko'chasi,\n" + mahalla + " mahallasi,\n" + tuman + " tumani,\n" + viloyat + " viloyati")

#04 Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang 
    #manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring.
    #bu masalaga #01 mashqdan o'zgaruvchi olindi
manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
print(manzil)
print(manzil.title())
print(manzil.upper())
print(manzil.lower())
print(manzil.capitalize())

















