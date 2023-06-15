# Tapsiriq 1.
#1
class Mehsul:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_info(self):
        print(f" Mehsulun adi-{self.name}\nQiymeti-{self.price}")

    def endirim(self):
        print(f"Mehsul 40 % endirimdedir. Endirimli qiymeti ise {self.price - 28} azn-dir")


#2
class Elektronika(Mehsul):
    def __init__(self, name, price, brend, garanti_muddeti):
        super().__init__(name, price)
        self.brend = brend
        self.garanti_muddeti = garanti_muddeti

    def show_model(self):
        print(f'Mehsulun brendi {self.brend}')


#3
class Phone(Elektronika):
    def __init__(self, name, price, brend, garanti_muddeti, isleme_sistemi, kamera_mexfilik):
        super().__init__(name, price, brend, garanti_muddeti)
        self.isleme_sistemi = isleme_sistemi
        self.kamera_mexfilik = kamera_mexfilik

    def zeng_et(self):
        print('Zeng et')


#4
class Akilli_saat(Elektronika):
    def __init__(self, name, price, brend, garanti_muddeti, ekran_olcusu, batarya_omru):
        super().__init__(name, price, brend, garanti_muddeti)
        self.ekran_olcusu = ekran_olcusu
        self.batarya_omru = batarya_omru

    def bildiris_goster(self):
        print('Bir mesajiniz var!')



mehsul1 = Mehsul('koynek', 70)
mehsul1.show_info()
mehsul1.endirim()

print()
elektronika = Elektronika('utu', 100, 'bosh', '3 il')
elektronika.show_model()
print()

phone = Phone('Samsung', 800, 'Samsung A53', ' 2 il', 'Android', 'camera')
phone.zeng_et()
print()

akilli_saat = Akilli_saat('Watch', 619, 'Apple Watch SE', '2 il', 44, '18 saat')
akilli_saat.bildiris_goster()
print()

# Tapsiriq 2.
#1
class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def show_info(self):
        print(f'Adi {self.name}, soyadi {self.surname}, yasi {self.age}')

    def qarsilama_et(self):
        print(f'Salam {self.name}')


#2.
import datetime

class Isci(Person):
    def __init__(self, name, surname, age, vezife, maas):
        super().__init__(name, surname, age)
        self.vezife = vezife
        self.maas = maas

    def ishe_basla(self):
       print(f'{self.name} {datetime.date.today()} tarixinde ise baslamisdir')

    def maas_artir(self):
        print(f'Iscinin artirilmis maasi {self.maas + 200}-dur')


#3

class Menecer(Isci):
    def __init__(self, name, surname, age, vezife, maas, departament, bonus):
        super().__init__(name, surname, age, vezife, maas)
        self.departament = departament
        self.bonus = bonus

    def ishcileri_yonet(self):
        print('Iscileri yonetmek ucun onlarla mutemadi olaraq gorusler teskil et.')

    def bonus_teyin_et(self):
        print('Gordukleri isde mueyyen muveffeqiyyeti elde etmis iscilerin maasina + 150 azn bonus elave olunacaq')


person = Person('Sofiya', 'Osmanova', 25)
person.show_info()
person.qarsilama_et()
print()

isci = Isci('Alisa', 'Imanova', 24, 'Muhasib', 700)
isci.ishe_basla()
isci.maas_artir()
print()

menecer = Menecer('Lala', 'Ceferova', 27, 'Mutexessis', 750, 'Maliyye', '+150 azn')
menecer.ishcileri_yonet()
menecer.bonus_teyin_et()
print()
