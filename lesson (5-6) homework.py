#Tapsiriq 1.

num1 = int(input('1-ci ededi daxil edin: '))
num2 = int(input('2-ci ededi daxil edin: '))
num3 = int(input('3-cu ededi daxil edin: '))
secim = int(input('Emeliyyatin nomresini daxil edin (1-2) '))
if secim == 1:
    cem = num1 + num2 + num3
    print(f'{num1} + {num2} + {num3} = {cem} ')
elif secim == 2:
    hasil = num1 * num2 * num3
    print(f'{num1} * {num2} * {num3} = {hasil} ')
else:
    print(' 1 ve ya 2 seciminden birini daxil edin ')


#Tapsiriq 2.

num1 = int(input('1-ci ededi daxil edin: '))  #24
num2 = int(input('2-ci ededi daxil edin: '))  #20
num3 = int(input('3-cu ededi daxil edin: '))  #19
secim = int(input('Emeliyyatin nomresini daxil edin (1-3) '))
if secim == 1:
    print('Ededlerin en böyüyünü secek: ')
    if num1 > num2 > num3:
        print(f'En boyuk eded {num1}-dir ')
elif secim == 2:
        print('Ededlerin en kiciyini secek: ')
        print(f'Ededlerin en kiciyi {num3}-dur')
else:
    print('Ededlerin ededi ortasini tapaq: ')
    print((num1 + num2 + num3) / 3)


#Tapsiriq 3.

number = int(input('Metrle ixtiyari bir uzunluq daxil edin: '))
secim = int(input('Emeliyyatin nomresini daxil edin (1-2) '))
if secim == 1:
    km = (number / 1000)
    print(f'Metri kilometre cevirdikde {km} alinir ')
elif secim == 2:
    sm = (number * 100)
    print(f'Metri santimetre cevirdikde {sm} alinir')



#Tapsiriq 1.
day =
