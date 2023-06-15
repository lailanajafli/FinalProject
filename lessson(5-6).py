# Serti ifadeler ve metntiqi konstruksiyalar.
'''
print("1 == 1 :", 1 == 1)
print("1 == 2 :", 1 == 2)
print("1 != 1 :", 1 != 1)
print("1 != 2 :", 1 != 2)
print("1 > 1 :", 1 > 1)
print("1 > 2 :", 1 > 2)
print("2 > 1 :", 2 > 1)
print("1 < 1 :", 1 < 1)
print("1 >= 1:", 1 >= 1)
print("1 >= 2:", 1 >= 2)
print("2 >= 1:", 2 >= 1)
print("1 <= 1:", 1 <= 1)
print("1 <= 2:", 1 <= 2)
print("2 <= 1:", 2 <= 1)

#
print(bool(""))                    #False
print(bool(0.0))                   #False
print(bool(None))                  #False
print(bool("IT STEP ACADEMY"))     #True
print(bool(1))                     #True
'''
'''
#Mentiqi operatorlar

competent = True
responsible = False
print(competent and responsible) # and butun sertler true olduqda true qaytarir
print(competent or responsible) 


time = int(input('Saati daxil edin: ')) % 24
ticket = True
money = True
luggage = False
print((money or ticket) and not luggage and time > 6)


#if sert konstruksiyasi
car_speed = int(input('Süret daxil edin: '))
if car_speed > 100:
print('Mashın yüksek süretle hereket edir')
print('if bloku bitdi')

# 1-den cox sertin verilmesi ve intervalin verilmesi
car_speed = 100
if (car_speed > 50 and car_speed < 150):
    print('Maşının süreti 50 ile 150 arasındadır')

# Icra bloku anlayisi
if 1 > 4:
    print("bu setir blokun daxilindedir")
    print("bu setir blokun daxilindedir")
    print("bu setir de blokun daxilindedir")
    print("bu setir blokun sonuncu setridir")
print("bu setir blokun daxilinde deyil")

# if ... elif ... else konstruksiyası
car_speed = 102
if car_speed >= 100:
print('Maşın yüksek süretle hereket edir')
elif car_speed >= 70 and car_speed < 100:
print('Maşın orta süretle hereket edir')
else:
print('Maşın aşağı süretle hereket edir')


eded = int(input('Ededi daxil edin: '))
if eded % 2 == 0:
    print(f'{eded} ededi cut ededdir ')
else:
    print(f'{eded} ededi tek ededdir ')


 #Tapsiriq 2.
 #Ededin 7-ye bolunub- bolunmemesi
eded = int(input('Ededi daxil edin: '))
if eded % 7 == 0
    print(f'{eded} ededi 7-ye bolunendir ')
    print(f'{eded} ededi 7-ye bolunmur ')


#Ededlerden minimum olanin tapilmasi
#Tapsiriq 4.
eded1 = int(input('Ededi daxil edin: ')) #56
eded2 = int(input('Ededi daxil edin: ')) #83
if eded1 > eded2
    print(f'{eded1} {eded2}-den böyükdür')
    elif eded1 < eded2:
    print(f'{eded1} {eded2}-den kiçikdir')
    else:
    print(f'{eded1} ve {eded2} beraberdir')
    


# Tapşırıq 5
eded1 = int(input('1-ci ededi daxil edin: '))
eded2 = int(input('2-ci ededi daxil edin: '))
sechim = int(input('Emeliyyat nömresini daxil edin (1-4): '))
if sechim == 1:
cem = eded1 + eded2
print(f'{eded1} + {eded2} = {cem}')
elif sechim == 2:
ferq = abs(eded1 - eded2) # abs() funksiyası riyaziyyatdakı modul demekdir
print(f'{eded1} - {eded2} = {ferq}')
elif sechim == 3:
ededi_orta = (eded1 + eded2)/2
print(f'Ededi orta = {ededi_orta}')
elif sechim == 4:
hasil = eded1 * eded2
print(f'{eded1} * {eded2} = {hasil}')
else:
print('1 ile 4 arasında eded daxil edin')
'''

