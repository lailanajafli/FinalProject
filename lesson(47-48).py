class BankAccount:
    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def depozit(self, yatirilan_mebleg):
        print(f"{self.owner} {self.account_number}  nomreli hesabiniza {yatirilan_mebleg} yatirildi")
        self.balance += yatirilan_mebleg

    def withdraw(self, cekilen_mebleg):
        print(f"{self.owner} {self.account_number}  nomreli hesabiniza {cekilen_mebleg} cixarildi")
        self.balance -= cekilen_mebleg

    def get_balance(self):
        print({self.balance})


    def get_info(self):
        print(f"{self.owner} {self.account_number}  nomreli hesabinizdaa {self.balance} qaldi")

bank1 = BankAccount("11111", "Leyla", 100000)
bank1.get_balance()
bank1.depozit(50000)
bank1.get_info()




class Car:
def __init__(self, reng, model):
self.reng = reng
self.model = model

def signal(self, signal_gucu):
print(f"{self.model} {self.reng} Beeeep!!!! {signal_gucu}")
print(f"{self.model} {self.reng} Beeeep!!!! {signal_gucu}")
print(f"{self.model} {self.reng} Beeeep!!!! {signal_gucu}")
print(f"{self.model} {self.reng} Beeeep!!!! {signal_gucu}")
print(f"{self.model} {self.reng} Beeeep!!!! {signal_gucu}")


def baqaji_ac(self):
print(f"{self.model} {self.reng} Baqaj acildi!")

car1 = Car(model="Mercedes", reng="qirmizi")
car2 = Car(model="Opel", reng="blue")
car3 = Car("pink", "Toyota")

car2.signal("150%")
print(car2.reng)















































'''
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
'''

# OOP --> 1)encapsulation, 2)polymorphism, 3)inheritance

# 1) sehife 2 cur olur:  1. private, 2. public
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
'''
