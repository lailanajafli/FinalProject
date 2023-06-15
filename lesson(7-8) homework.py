#Tapsiriq 1.
'''
try:
    secim = int(input('Heftenin gününün sira nömrəsini daxil edin (1-7) ' ))
    if secim == 1:
        print('Bazar ertesi')
    if secim == 2:
        print('Cersenbe axsami')
    if secim == 3:
        print('Cersenbe')
    if secim == 4:
        print('Cume axsami')
    if secim == 5:
        print('Cume')except
    elif secim == 6:
        print('Senbe')
    else:
        print('Bazar')
except Exception:
        print('Reqemlerden istifade edin.')

#Tapsiriq 2.

try:
    secim = int(input('Ayin adlarinin sira nomresini daxil edin:'))
    if secim == 1:
        print('Yanvar')
    elif secim == 2:
        print('Fevral')
    elif secim == 3:
        print('Mart')
    elif secim == 4:
        print('Aprel')
    elif secim == 5:
        print('May')
    elif secim == 6:
        print('Iyun')
    elif secim == 7:
        print('Iyul')
    elif secim == 8:
        print('Avqust')
    elif secim == 9:
        print('Sentyabr')
    elif secim == 10:
        print('Oktyabr')
    elif secim == 11:
        print('Noyabr')
    elif secim == 12:
        print('Dekabr')
    else:
        print('Dekabr')
 Exception:
    print('(1-12 arasi reqemlerden istifade edin:')

    #Tapsiriq 3.

num = int(input('Enter the number: '))
if num > 0:
    print('"Number is positive"')
elif num < 0:
    print('"Number is negative"')
else:
    print('"Number is equal to zero"')


#Tapsiriq 4.

num1 = int(input(' Enter the number: '))
num2 = int(input(' Enter the number: '))
if num1 > num2:
    print( f' {num2} {num1}-den kicikdir ')
elif num1 < num2:
    print( f' {num1} {num2}-den kicikdir ')
else:
    print( f' {num1} {num2}-e beraberdir ')
'''


start_number = int(input('Eded daxil edin: '))
end_number = int(input('Eded daxil edin: '))
while start_number < end_number:
    start_number += 1
    if start_number % 2 == 1:
        continue
    print(start_number)




