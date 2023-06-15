
str1 = 'Hello world!'
print(str1[0])
print(str1[1])
print(str1[8])

print(str1[12])   #IndexError -> out of range
        012345
str1 = 'Hello'

print(str1[-1])
print(str1[-2])
print(str1[-3])

#Multiline string elani

multiline_str = '''
        lorem ipsum dolor sit amet, consectetur adipiscing
        elit. cras sed scelerisque enim, eu laoreet magna.
'''
print(multiline_str)

#string daxilinde escape sequence-lara muraciet

print(multiline_str[0])

multiline_str = '''\n
        lorem ipsum dolor sit amet, consectetur adipiscing
        elit. cras sed scelerisque enim, eu laoreet magna.
'''
#Setrin uzunlugunun tapilmasi -- len()

print(len(multiline_str))


#Setirler ile is
str1 = 'python'
str2 = 'Bootcamp'
str3 = str1 + str2
print(str3)

#String ile int
str1 = 'Python'
#str3 = str1 +5  -> TypeError: can only concatenate str with str.
print(str3)

#String ile int --> vurma aparmaq olar. Kopyalama emeliyyati icra olunar.
str1 = 'Python'
str3 = str1 +10
print(str3)


# String slicing -> setirlerin indekslere gore parcalanmasi
str1 = 'Python bootcamp 2023'
print(str[3:10])   #  ->  3-den 10-a qeder setir elementlerini getirir
print(str[:10])    #  ->  en basdan 10-a qeder setir elementlerini getirir
print(str[3:])     #  ->  3-den en sona qeder setir elementlerini getirir.
print(str[:])      #  ->  en basdan en son qeder setir elementlerini getirir.
print(str[0:len(str1):2])     #  ->  en basdan en son qeder 2 elementden bir setir elementlerini getirir.

#String slicing sintaksisinde sonuncu limiti oldugundan yuksesk vermek olar.
#Hec bir xeta bas vermeyecek ve netice dogru olacaq.
str1 = 'Python bootcamp 2023'
print(str[3:55])
#Arxada isleyen kod:
'''
for i in range(3, 55):
    print(str[i])
    if i == len(str) -1:
        break
'''
#Setrin tersine cevrilmesi. reverse string
str1 = 'Python bootcamp 2023'
print(str1[::-1])

#Mesele. Istifadeci eded daxil edir. Ve bu ededin polindrom olub- olmadigini yoxlayan
# proqram yazin. Polindrom eded her iki terefden oxusu eyni olan ededdir.

number = int(input('Eded daxil edin: '))           #1-ci yol
if number == number[::-1]:
    print(f'{number} polindromdur')
else:
    print(f'{number} polindrom deyil')

f'''
number = int(input('Eded daxil edin: '))           #2-ci yol
print(bool(number == number [::-1]))
'''

#metodlar. Metod ile funksiyalarin ferqi
# Funksiyalar -> alt proqramlardir, hansi ki,
# mueyyen emeliyyatlari yerine yetirir ve bize bir cavab qaytarir.
# Prosedur anlayisi -> alt proqramlardir, hansilar ki, mueyyen emeliyyatlari yerine yetirir,
# lakin cavab qaytarmir.
# Metodlar -> funksiya ve ya prosedurlardir ki, hansilar ki, mueyyen sininfe (class) ve ya
# sinfin numayendesine (instance of a class) aid olur.
# metodlarin cagirilmasin sintaksisi
objectname.methodname(args)

#Daxili metodlar. Xarici metodlar
#Kitabxanalar -> basqa proqramcilar terefinden yazilmis ve
#funksionalligina gore qruplasdirilmis metodlar toplusudur

import random #random adli kitabxanani layihemize import etmis oluruq.
#random kitabxanasi tesadufi deyerler kitabxanasidir

print(random.random())  0 ile 1 arasinda deyer qaytarir
print(random.randint(-90, 100)) # verilmis diapazondaki integer deyerler qaytarir
print(random.uniform(-90, 100)) # verilmis diapazondaki kesr deyerler qaytarir
print(random.choice('Hello World')) # verilmis setirdeki tesadufi simvolu qaytarir

#Mesele. Tesadufi 10 eded random simvoldan ibaret sifre yaradilmasi proqramini yazin.

uppercase = 'ASDFVGBHNJM'
lowercase = 'asdcfghbvvfg'
digits = '1234567890'
simvollar = '!@#$%^&*'

full_string = uppercase + lowercase + digits + symbols

password = ''
for i in range(10):
    password += random.choice(full_string)  #password = password +random.choice(full_string
print(password)
'''
#String methods
str_name = 'lorem ipsum dolor sit amet, consectetur adipiscing elit. 
            lorem cras sed scelerisque enim, eu laoreet magna.'
print(str_name.capitalize())     # -> Setri boyuk herfden basladir.
print(str_name.tittle())     # -> Setrdeki sozlerin her birini boyuk herfden basladir
print(str_name.upper())    # -> butun herfleri boyuk edir
print(str_name.lower())    # -> butun herfleri kicik edir

#Setrin daxilinde axtaris 

print(str_name.find('ghgfh'))    # -> axtarilan elementin indeksini qaytarir
#element yoxdursa -1 qaytarir
print(str_name.replace('lorem', 'dolor'))   # -> elementleri evez edir.

str_name = 'lorem ipsum dolor sit amet, consectetur adipiscing elit.
           lorem cras sed scelerisque enim, eu laoreet magna.'
print(str_name.replace('dolor', 'Python', 3))  # -> ilk 3-nu evez edir


# Qeyd. String-in metodlari hemin string-in kopyalari uzerinde isleyir.
#Orginal string mezmunu deyismir.

str_name = 'lorem ipsum dolor sit amet, consectetur adipiscing elit. 
            lorem cras sed scelerisque enim, eu laoreet magna.'
print(str_name.count('dolor'))
print(str_name.count('s'))

# String Check Metods  -> Metoda ve string mezmununa gore True ve ya False qaytarirlar.
str_name = 'lorem ipsum dolor sit amet, consectetur adipiscing elit. 
            lorem cras sed scelerisque enim, eu laoreet magna.'
print(str_name.isupper(''))
print(str_name.islower(''))
print(str_name.isalpha(''))
print(str_name.isnumeric(''))
print(str_name.isalnum(''))
isspace   # boslugu tapmaq ucun
print(str_name.isascii(''))
print(str_name.startswith('Lorem'))
print(str_name.endswith('.png'))
cmmcmcdmoeml;fsd



