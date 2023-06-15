# Tapsiriq.

countries = {"Azerbaycan":"Baki"}
menu = """
            Elave et =>      1
            Sil =>           2
            Deyisdir =>      3
            Tap =>           4
            Goster =>        5
            Cixis =>         6
"""

while True:
    print(menu)
    option = input('Seçim daxil edin: ')

    if option == '1':
       print()
       new_country = input("Enter the country: ")
       new_capital = input("Enter the capital: ")
       countries[new_country] = new_capital

    elif option == '2':
        print()
        delete = (input("Enter the country to delete: "))
        if delete in countries.keys():
            del countries[delete]
            print(countries)
            print(f'{delete} siyahidan silindi')
        else:
            print("Hemin olke movcud deyil")

    elif option == '3':
        print()
        del_country = input("Deyismek istediyinz olke adini daxil edin:")
        yeni_paytaxt = input('Yeni paytaxt adini daxil edin:')
        countries[del_country] = yeni_paytaxt
        print(countries)

    elif option == '4':
        print()
        search = input("Axtarmaq istediyiniz olkeni daxil edin:")
        for i in countries:
            if search in i:
                print(i)
            else:
                print(" Siyahida bu adda olke movcud deyil:")

    elif option == '5':
     print(countries)

    elif option == '6':
        break
    else:
        print('Zehmet olmasa (1-6) arasinda secim daxil edin:')

print(countries)




