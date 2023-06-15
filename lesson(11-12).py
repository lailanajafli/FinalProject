#Mesele 1
# Pul qabı meselesi: İstifadeçinin pul qabısı var.
# O, buradan müeyyen bir mebleğ götürmek isteyir.
# Eger kifayet geder mebleğ varsa, istifadeçiye verilsin.
# Yoxdursa, müvafiq mesaj çap olunsun. Pul qabındakı qalıq da çap olunsun.
# Deyişenler: wallet, request

wallet = 100
request = float(input('Mebleğ daxil edin: '))
if request <= wallet:
    print(f'İstediyiniz mebleğ: {request}')
    wallet = wallet - request   # wallet -=1
    print(f'Qalan mebleğ: {wallet}')
else:
    print('Pul qabında kifayet qeder vesait yoxdur')


#Mesele2: Yuxarıdaki mesele pul qabında vesait qalmayana geder davam etsin.
wallet = 100
while True:
    request = float(input('Mebleğ daxil edin: '))
    if request <= wallet:
        print(f'İstediyiniz mebleğ: {request}')
        wallet = wallet - request   # wallet -= 1
        print(f'Qalan mebleğ: {wallet}')
        if wallet == 0:
            print('Vesait qalmadı. Proqramdan çıxış')
            break
    else:
        print('Pul qabında kifayet qeder vesait yoxdur')

#Mesele3. Bir adam 1-ci mertebeden 5-ci mertebeye qalxmalıdır.
# Mertebeler arasındakı pille sayı 20-dir. Her 70 pilleden sonra adam
# istirahet edir, enerji toplayır ve qalxmağa davam edir.
# Bu meselenin proqramını yazın.
# Lazım olacaq elementler: floor, steps_count, energy = 70, dövr operatoru.
floor = 1
steps_count = 0
energy = 70
while floor <= 5:
    print(f'I am on the {floor} floor')
    while steps_count != 20:
        steps_count += 1
        energy -= 1
        if energy == 0:
            print('I need some energy')
            energy = 70
    floor = floor + 1
    steps_count = 0
print('Done!')


#Mesele4
#While-dan istifade etmekle valyuta mübadilesi,
# kalkulyator, mili kilometre çeviren proqramları sonsuz dövre salın.
project_menu = """
            Valyuta =>      1
            Kalkulyator =>  2
            Mile to km =>   3
            Çıxış =>        0


valyuta_menu = """
            AZN to USD =>  1
            AZN to EUR =>  2
            AZN to RUB =>  3
            Çıxış =>       0

while True:
    print(project_menu)
    choice = input('Seçim daxil edin: ')
    if choice == '1':
        pass
    elif choice == '2':
        num1 = float(input('1-ci ededi daxil edin:'))
        num2 = float(input('2-ci ededi daxil edin:'))
        while True:
            op = input('Emeliyyat daxil edin: (+, -, *, /): ')
            if op == '+' or op == '-' or op == '*' or op == '/':
                break
        if op == '+':
            print(f'{num1} + {num2}=', num1 + num2)
        elif op == '-':
            print(f'{num1} - {num2}=', num1 - num2)
        elif op == '*':
            print(f'{num1} * {num2}=', num1 * num2)
        else:
            print(f'{num1} / {num2}=', num1 / num2)
    elif choice == '3':
        wile = float(input('Mil daxil edin: '))     #km = mile * 1.609
        print(f'{mile} mil = {mile * 1.609} km')
    elif choice == '0':
        print('Proqramdan cixis...')
    else:
        print('Secim dogru deyil! ')

        project_menu = """
                    Valyuta =>      1
                    Kalkulyator =>  2
                    Mile to km =>   3
                    Çıxış =>        0


        valyuta_menu = """
        AZN
        to
        USD = > 1
        AZN
        to
        EUR = > 2
        AZN
        to
        RUB = > 3
        Çıxış = > 0

    while True:
        print(project_menu)
        choice = input('Seçim daxil edin: ')
        if choice == '1':
            azn_balans = float(input('Mebleğ daxil edin: '))
            print(valyuta_menu)
            while True:
                valyuta = input('Valyuta seçimi daxil edin: ')
                if valyuta == '1':
                    print(f'{azn_balans} AZN = {azn_balans / 1.7} USD')
                elif valyuta == '2':
                    print(f'{azn_balans} AZN = {azn_balans / 1.9} EUR')
                elif valyuta == '3':
                    print(f'{azn_balans} AZN = {azn_balans / 0.026} RUB')
                elif valyuta == '0':
                    print('Valyuta proqramından çıxış...')
                    break
                else:
                    print('Valyuta seçimini dwzgwn daxil edin!)
                    elif choice == '2':
                    num1 = float(input('1-ci ededi daxil edin: '))
                    num2 = float(input('2-ci ededi daxil edin: '))
            while True:
                op = input('Emeliyyat daxil edin (+, -, *, /): ')
                if op == '+' or op == '-' or op == '*' or op == '/':
                    break
            if op == '+':
                print(f'{num1} + {num2} = ', num1 + num2)
            elif op == '-':
                print(f'{num1} - {num2} = ', num1 - num2)
            elif op == '*':
                print(f'{num1} * {num2} = ', num1 * num2)
            else:
                print(f'{num1} / {num2} = ', num1 / num2)
        elif choice == '3':
            mile = float(input('Mil daxil edin: '))  # km = mile * 1.609
            print(f'{mile} mil = {mile * 1.609} km')
        elif choice == '0':
            print('Proqramdan çıxış...')
            break
        else:
            print('Seçim doğru deyil!')

