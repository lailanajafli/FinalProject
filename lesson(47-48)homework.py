
# Tapsiriq 1.
class Counter:
    def __init__(self, count):
        self.count = 0

    def increment(self, num):
        self.count += num

    def decrement(self, num):
       self.count -= num

    def get_count(self):
        print(f"{self.count}")

saygac1 = Counter(0)
saygac1.increment(45)
saygac1.decrement(26)
saygac1.get_count()


# Tapsiriq 2.
class Book:
    def __init__(self, title, author, year, janr):
        self.title = title
        self.author = author
        self.year = year
        self.janr = janr

    def get_info(self):
        print(f" Kitabin adi - {self.title}, muellifi - {self.author}, nesr ili ise {self.year}-dir")
        
    def get_info(self):
        print(f" Kitabin adi - {self.title}, muellifi - {self.author}, nesr ili, {self.year}, janri ise {self.janr} - dir")


book = Book("Cerpeleng Ucuran", "Xalid Huseyni", 2003, 'Roman')
book.get_info()


# Tapsiriq 3.
class Student:
    def __init__(self, name, age, grade, group):
        self.name = name
        self.age = age
        self.grade = grade
        self.group = group

    def get_info(self):
        print(f" Adi-{self.name}\n yasi-{self.age}\n sinifi-{self.grade}")

    def get_info(self):
        print(f" Adi-{self.name}\n Yasi-{self.age}\n Sinifi-{self.grade}\n Secmek istediyi qrup-{self.group}")


student1 = Student('Sofiya', 15, 9, '3-cu qrup')
student1.get_info()









