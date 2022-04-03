# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 16:13:25 2022

@author: Pro
"""
# SyntaxError:
# print ("Hello World!"     # SyntaxError: unexpected EOF while parsing
                            # EOF (End of function - funktsiya yakuni) xatoligi
# print("Hello World!   # SyntaxError: EOL while scanning string literal
                        #EOL (End of Line - qator yakuni) xatoligi
# IndentationError - JOY TASHLASHDA XATOLIK
# print ("Hello World!")

# print("O'ngacha sanaymiz")
# for n in range(10):
# print(n+1)                #IndentationError: expected an indented block

### Run time error

# TypeError
# son = input("Istalgan son kiriting: ") # noto'g'ri variant
# son = int(input("Istalgan son kiriting: ")) #to'g'ri variant
# print(f"{son} ning kvadrati {son**2} ga teng")

# NameError
# prit("Hello World!") #NameError: name 'prit' is not defined
# print ("Hello World!") #to'g'ri variant

# mevalar = ['olma','uzum','nok','anor','anjir']
# for meva in mvealar: #NameError: name 'mvealar' is not defined
#     print(meva)

# ValueError
# son = int(input("Istalgan son kiriting: ")) # noto'g'ri variant
# son = float(input("Istalgan son kiriting: ")) # to'g'ri variant
# if son>=0:
#    print("Musbat son")
# else:
#    print("Manfiy son")

# IndexError
# mevalar = ['olma','anor','uzum']
# print(mevalar[3]) # IndexError: list index out of range
# print(mevalar[2]) # to'g'ri variant

# ZeroDivisionError
# x, y = 60, 50
# z = 250/(x-y) #ZeroDivisionError: division by zero

# MANTIQIY XATOLAR
# radius = 5
# pi = 4.14 # xato 3.14 o'rniga 4.14 qilingan
# aylana_yuzi = pi*radius**2
# print(aylana_yuzi)

# son = float(input("Istalgan son kiriting: "))
# ildiz = son**1/2 # xato (1/2) qavs ichida bo'lishi kerak
# print(f"{son} ning ildizi {ildiz} ga teng")

# mevalar = ['olma','uzum','nok','anor','anjir']
# for meva in mevalar:
#     print(meva)
#    print("Dastur tugadi") # bu xato varian, chunki qayta-qayta chiqaradi
# print("Dastur tugadi") # bu to'g'ri variant, tugashida 1 ta chiqazadi


### AMALIYOT
# Kodlardagi xatolarni toping va to'g'rilang.
# Har bir dasturda bir nechta xatolar mavjud bo'lishi mumkin
# Xatolarni topish uchun dasturlarni bir necha marta, turli qiymatlar bilan bajarib ko'ring.

##01 xatolari
# son = float(input("Juft son kiriting: ")) # yakunda 1 ta )
# if son%2!=0:                              # == o'rniga !=
#     print("Bu son juft emas.")
# else:
#     print("Rahmat!")                      # yakunda ortiqcha )

##02 xatolari
# yosh = int(input("Yoshingiz nechida? "))    # int() qo'shildi
# if yosh<=4 or yosh>=60:
#     narh = 0
# elif yosh < 18:                             # : oxiriga qo'shildi
#     narh = 10000
# else:
#     narh = 20000
# print(f"Chipta {narh} so'm")                # o'ngga surilib qolgan ekan

##03 xatolari
# x = float(input("Birinchi sonni kiriting: ")) # ) oxiriga qo'shildi
# y = float(input("Ikkinchi sonni kiriting: ")) # ) oxiriga qo'shildi
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f"{x}<{y}")                         # f dan keyin ' o'rniga " qo'yildi
# else:                                         # : oxiriga qo'shildi
#     print(f"{x}>{y}")

#04 xatolari
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#               'kartoshka', 'olma', 'banan', 'uzum', 'qovun'] # ] oxiriga qo'shildi
# savat = []                                                    # shu qator qo'shildi

# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# if savat:
#     for mahsulot in savat:                                  # : oxiriga qo'shildi
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q")
# else: 
#     print("Savatingiz bo'sh")            

##05 xatolari
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
# savat = []
# for n in range(5):
#     savat.append(input(f'Savatga {n+1}-mahsulotni qo\'shing: ')) # o' o'rniga o\' qilindi
# 
# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)                 # mahslot o'rniga mahsulot yozildi
#     else:
#         mavjud_emas.append(mahsulot)
#
# if mavjud_emas:
#   print("Do'konimizda quyidagi mahsulotlar yo'q:")
# for mahsulot in mavjud_emas:
#   print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

##06 xatolari
# users = ['alisher1983', 'aziza', 'yasina', 'umar'] # , oxiriga qo'shildi

# login = input("Yangi login tanlang:" )             # ' o'rniga " oxiriga qo'shildi

# if login.lower() in users:                         # login o'rniga login.lower() qo'yildi
#     print('Login band, yangi login tanalng!') # tanalng o'rniga tanlang
# else:
#     print("Xush kelibsiz!")

















