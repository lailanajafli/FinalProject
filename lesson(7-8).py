# try except sintaksis nümune
'''
try:
amount = int(input('Enter the amount of product: '))
product_type = input('Enter the type of product: ')
parts_number = int(input('Enter the number of parts: '))
parts = amount / parts_number
    print(f'{parts_number}')
    print(f'{parts}')m
except ValueError:
    print('The amount should be integer')
except ZeroDivisionError:
    print('0-a bölmek olmaz')
else: # else heç bir except işlemedikde işleyir
    print('Everything worked properly.')
finally: # her zaman işleyir
    print('The problem has solved.')


# raise Exception
try:
    time = int(input('Saati daxil edin: '))
    deqiqe = int(input(' Deqiqeni daxil edin'))
    if time > 23 or time < 0 or deqiqe > 59 or deqiqe < 0:
        raise Exception
    else:
        print(f'Saat: {saat}:{deqiqe}-dir')
except Exception:
    print('Zamani duzgun daxil edin.')


#Tapsiriq 2.
try:
    time = int(input('Saati daxil edin: '))
    if time > 0 and time < 6:
        print('Good Night')
    elif time > 6 and time < 13:
         print('Good Morning')

except Exception:
    print('Zamani duzgun daxil edin.')


#Tapsiriq
num = int(input('5 reqemli eded daxil edin'))
        raise Exception
    else:
        print(f'Saat: {saat}:{deqiqe}-dir')
except Exception:
    print('Zamani duzgun daxil edin.')


console_price = int(input(" Qiymet daxil edin: "))
amount = int(input'Sayini daxil edin: ')
sale = int(input('Endirim faizini daxil edin: '))
choice = int()
'''

#Tapsiriq 1.
try:
    secim = int(input('Heftenin gununun sira nomresini daxil edin (1-7) '))
if secim = 1:
    print('Bazar ertesi')
    print('Cersenbe axsami')
except Exception:
    print('Zehmet olmasa (1-7) arasinda bir eded daxil edin: ')
finally:
    print('Bazar')
