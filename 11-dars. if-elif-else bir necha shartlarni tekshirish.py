# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 13:53:18 2022

@author: Pro
"""

# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4:
#    print('Sizga kirish bepul.')
# elif yosh<=12:
#    print('Sizga kirish 5000 so\'m')
# elif yosh<18:
#    print('SIzga kirish 8000 so\'m')
# else:
#    print('Sizga kirish 10000 so\'m')

### ko'p dasturchilar buning o'rniga quyidagicha bajaradi
    
# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4:
#     narx = 0
# elif yosh<=12:
#     narx =5000
# elif yosh<18:
#     narx = 8000
# else:
#     narx = 10000

# print(f"Sizga kirish {narx} so'm")

# kun = input("Bugun nima kun?>>>")
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print('Bugun dam olish kuni.')
# else:
#     print('Bugun ish kuni.')

# kun = input("Bugun nima kun?")
# harorat = float(input("Havo harorati qanday?"))
# if kun.lower()=='yakshanba' and harorat>=30:
#    print("Cho'milgani ketdik!")
# elif kun.lower()=='yakshanba' and harorat<30:
#    print("Uyda dam olamiz!")

# kun = input("Bugun nima kun?")
# harorat = float(input("Havo harorati qanday?"))
# if (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat>=30:
#    print("Cho'milgani ketdik!")
#e lif (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat<30:
#    print("Uyda dam olamiz!")

# narh = 15000 # mijoz 15000 so'mga taom oldi.
# choy = True # mijoz choy ham oldi
# salat = True # mijoz salat olmadi

# if choy and salat: # agar mijoz choy ham salat ham olgan bo'lsa
#     narh = narh + 10000 # narhga 10000 so'm qo'shamiz
# elif choy or salat: # agar choy yoki salat olgan bo'lsa
#    narh = narh + 5000 # narhga 5000 so'm qo'shamiz

# print(f"Jami {narh} so'm") # yakuniy narhni chiqaramiz

# narh = 15000 # mijoz 15 so'mga ovqat oldi
# choy = True
# salat = False
# non = True
# kompot = True
# assorti = False
#Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
# if choy:   # agar choy olsa
#     print("Mijoz choy oldi.")
#     narh = narh + 3000
# if salat:  # agar salat olsa
#     print("Mijoz salat oldi.")
#     narh = narh + 5000
# if non:    # agar non olsa
#     print("Mijoz non oldi.")
#     narh = narh + 2000
# if kompot: # agar kompot olsa
#     print("Mijoz kompot oldi.")
#     narh = narh + 5000
# if assorti: # agar assorti olsa
#     print("Mijoz assorti oldi.")
#     narh = narh + 15000
    
# print(f"Jami {narh} so'm")


# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# 'manti' in menu # menu da manti bormi?


# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# ovqat = input('Nima ovqat yeysiz?>>>')
# if ovqat.lower() in menu:
#     print('Buyurtma qabul qilindi.')
# else:
#    print('Afsuski bizda bunday ovqat yo\'q')


# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# 'manti' not in menu # menu da manti yo'qmi?

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# 'osh' not in menu # menu da osh yo'qmi?


# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# ovqat = input('Nima ovqat yeysiz?>>>')
# if ovqat.lower() not in menu:
#    print('Afsuski bizda bunday ovqat yo\'q')
# else:
#    print('Buyurtma qabul qilindi.')


# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ["osh","somsa","manti", "shashlik"]

# for taom in buyurtmalar:
#    if taom in menu:
#        print(f"Menuda {taom} bor")
#    else:
#       print(f"Kechirasiz, menuda {taom} yo'q")

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ["osh","somsa","manti", "shashlik"]

# if buyurtmalar: # ro'yxatda biror element bo'lsa bu ifoda TRUE qaytaradi
#    for taom in buyurtmalar:
#        if taom in menu:
#            print(f"Menuda {taom} bor")
#        else:
#            print(f"Kechirasiz, menuda {taom} yo'q")
# else: # agar ro'yxat bo'sh bo'lsa
#    print("Savatchangiz bo'sh!")


#### AMALIYOT

#01 Foydalanuvchidan juft son kiritishni so'rang. 
    # Agar foydalanuvchi juft son kiritsa "Rahmat!", 
    # agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
# son = float(input("Iltimos, juft son kiriting:_"))
# if son%2:
#     print("Bu son juft emas.")
# else:
#    print("Rahmat!")
    
#02 Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
    # Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
    # Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
    # Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
# yosh = int(input("Yoshingiz nechida?_"))
# if yosh<=4 or yosh>60:
#     print("Sizga kirish bepul!")    
# elif yosh<18:
#     print("Kirish 10000 so'm")
# else:
#     print("Sizga kirish 20000 so'm")

#2-variant
# yosh = int(input("Yoshingiz nechida?_"))
# if yosh<=4 or yosh>60:
#     narx = 0
# elif yosh<18:
#     narx = 10000
# else:
#     narx = 20000
# print(f"Kirish {narx} so'm")

#03 Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring 
    # va ularning teng yoki katta/kichikligi haqida xabarni chiqaring
# a = float(input("1-sonni kiriting: "))
# b = float(input("2-sonni kiriting: "))
# if a>b:
#     print(f"{a} > {b}")
# elif a == b:
#     print(f"{a} = {b}")
# else:
#    print(f"{a} < {b}")
    

#04 mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. 
    # Yangi, savat degan bo'sh ro'yxat yarating 
    # va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. 
    # Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring 
    # va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" 
    # aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
# mahsulotlar = ['sut', "saryog'", 'tuz', 'shakar', "yog'", 'non', 'bumaga', 'xolva', 'shokolad', 'qurt']
# savat = []

# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni kiriting: "))
    
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"Do'konimizda {mahsulot} bor")
#     else:
#         print(f"Do'konimizda {mahsulot} yo'q")


#05 Yuqoridagi dasturni quyidagicha o'zgartiring: 
    # foydalanuvchidan 5 ta mahsulot kiritishni so'rang. 
    # Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yangi, bor_mahsulotlar degan ro'yxatga,
    # do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.
    # Agar mavjud_emas ro'yxati bo'sh bo'lsa, 
    # "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni,
    # aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.
    
# mahsulotlar = ['sut', "saryog'", 'tuz', 'shakar', "yog'", 'non', 'bumaga', 'xolva', 'shokolad', 'qurt']
# savat = []

# for n in range(5):
#    savat.append(input(f"Savatga {n+1}-mahsulotni kiriting: "))

# bor_mahsulotlar = []
# mavjud_emas = []    
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
         
# if mavjud_emas:
#    print("Do'konimizda quyidagi mahsulotlar yo'q: ")
#    for mahsulot in mavjud_emas:
#        print(mahsulot)
#    else:
#        print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

       
#06 foydalanuvchilar degan ro'yxat tuzing,
    # va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni so'rang 
    # va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. 
    # Agar ro'yxatda bunday login mavjud bo'lsa, 
    # "Login band, yangi login tanlang!" 
    # aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.

# users = ['abdulatif', 'muhammadali', 'zafar', 'bexruz', 'shukur']
# login = input("Yangi login tanlang: ")
# if login.lower() in users:
#     print("Login band, yangi login tanlang!")
# else:
#    users.append(login.lower())   # bu qismini o'zim qo'shdim, hali takomillashtirish kerak
#    print(f"Xush kelibsiz, {login.title()}")


#07 Foydalanuvchidan biror butun son kiritishni so'rang. 
    # Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.

# son = int(input("Istalgan butun son kiriting: "))

# for n in range(2, 11):
#    if not (son%n):
#       print(f"{son} soni {n} ga qoldiqsiz bo'linadi")






















