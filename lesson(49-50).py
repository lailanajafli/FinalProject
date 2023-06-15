

# Tapsiriq 1.
class Animal:
    def __init__(self, name, cins, age):
        self.name = name
        self.cins = cins
        self.age = age

    def show_info(self):
        print(f"adi-{self.name}\ncinsi-{self.cins}\nyasi-{self.age}")

    def salam_ver(self):
        print("Miavv")

    def uyan(self):
        print("Uyannn")

    def yemek_ye(self):
        print("Ye")




# Tapsiriq 2.
class Qartal(Animal):
    def __init__(self, name, cins, age, qanad_uzunlugu, ucus_sureti):
        super().__init__(name, cins, age)
        self.qanad_uzunlugu = qanad_uzunlugu
        self.ucus_sureti = ucus_sureti

    def show_info(self):
        super().show_info()
        print(f"qanadinin uzunlugu{self.qanad_uzunlugu}\nucus sureti {self.ucus_sureti}-dir")

    def uch(self):
        print('uch')

    def ovla(self):
        print("ovla")

animal1 = Animal("pisik", "Burmilla", 5)
animal1.show_info()
animal1.salam_ver()
animal1.uyan()
animal1.yemek_ye()
qartal1 = Qartal('qartal', "Col qartali", 6, "50 sm", "150km")
qartal1.show_info()
qartal1.uch()
qartal1.ovla()



# OOP --> 1)encapsulation, 2)polymorphism 3)inheritance
#2)polymorphism --> yeeni eyni bir funksiya ferqli obyektlerde cavab qaytara biler
# 1) sehife 2 cur olur:  1. private, 2. public metodlardir
'''
sehifeni baglamaq (private) ucun, yeni deyisilmez elemek ucun

1)encapsulation da 2 cur olur: setter ve getter



# OOP - encapsulation, inheritance
# private public
class Transport:
    def __init__(self, ticket_price, start_point, end_point):
        self.ticket_price = ticket_price
        self.start_point = start_point
        self.end_point = end_point
        self.balans = 0
    def ticket_pass(self):
        self.balans += self.ticket_price
    def show_balance(self):
        print(self.balans)
    def show_info(self):
        print(f"Ticket price: {self.ticket_price}")
        print(f"Start: {self.start_point}")
        print(f"End: {self.end_point}")
        print(f"Balans: {self.balans}")

class Bus(Transport):
    def __init__(self, ticket_price, start_point, end_point, bus_number):
        super().__init__(ticket_price, start_point, end_point)
        self.bus_number = bus_number
    def signal(self):
        print("Beeep!")
    def show_info(self):
        super().show_info()
        print(f"Bus number: {self.bus_number}")

class Plane(Transport):
    def __init__(self, ticket_price, start_point, end_point, company):
        super().__init__(ticket_price, start_point, end_point)
        self.company = company
    def distribute_meals(self):
        print("All passengers got meals!")
    def show_info(self):
        print(f"Ticket price: {self.ticket_price}")
        print(f"Start: {self.start_point}")
        print(f"End: {self.end_point}")
        print(f"Balans: {self.balans}")
        print(f"Company: {self.company}")

class Taxi(Transport):
    def __init__(self, ticket_price, start_point, end_point, masin_nomresi):
        super().__init__(ticket_price, start_point, end_point)
        self.masin_nomresi = masin_nomresi
    def musteri_tap(self):
        print('Musteri axtariram...')
    def show_info(self):
        super().show_info()
        print(f"Masin nomresi: {self.masin_nomresi}")

bus1 = Bus(0.40, "Genclik Mall", "Qara Qarayev", "205")
bus1.ticket_pass()
bus1.ticket_pass()
bus1.ticket_pass()
bus1.ticket_pass()
bus1.ticket_pass()
bus1.show_balance()
bus1.signal()
bus1.show_info()
print("```````````")
plane1 = Plane(500, "Baku", "London", "AZAL")
plane1.ticket_pass()
plane1.ticket_pass()
plane1.ticket_pass()
plane1.show_balance()
plane1.distribute_meals()
plane1.show_info()






