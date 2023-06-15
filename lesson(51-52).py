'''

statik sahe, statik metod
import math

class Fiqur:
    def saheni_tap(self):
    pass

class Square:
    def __init__(self, a):
    self.a = a

    def saheni_tap(self):
    return self.a*self.a

class Circle:
    def __init__(self, r):
    self.r = r

    def saheni_tap(self):
    return math.pi*self.r**2


circle1 = Circle(4)
print(circle1.saheni_tap())

square1 = Square(4)
print(square1.saheni_tap())



class School:
def __init__(self, students, number):
self.students = students
self.nomre = number

#magic method
 def __str__(self):
return f"School #{self.nomre} has {self.students} students"

 def show_school_number(self):
print(f"School number #{self.nomre}")



school1 = School(100, 20)
a = str(school1)
print(a)



class School:
def __init__(self, students, number):
self.students = students
self.nomre = number

def show_students(self, *students):
for student in students:
print(student)


school1 = School(100, 20)
school1.show_students("Emil", "Eyyub", "John")




class Game:
total_count = 0
 info = "Bu Game klass bize oyun ucun obyektlari yaratmaga komek edir!"
 games = []

def __init__(self, name, multiplayer):
Game.games.append(name)
self.name = name
self.multiplayer = multiplayer
self.count = 0

 def play(self):
Game.total_count += 1
 self.count += 1
 print("You play the game!")

def show_count(self):
print(f"Bugun {self.count} defe {self.name} oynayibsan!")

@staticmethod
 def show_games():
print(f"Sizin oyunlar: {Game.games}")


mario_game = Game('Mario', False)
need_for_speed = Game("Need for Speed", True)

mario_game.play()
need_for_speed.play()
need_for_speed.play()
mario_game.play()
need_for_speed.play()

need_for_speed.show_count()
mario_game.show_count()

print(Game.total_count)
print(Game.info)
Game.show_games()




from tkinter import *

def show():
new_list = [i for j, i in enumerate(languages_var.get()) if j not in languages_listbox.curselection()]
languages_var.set(new_list)



root = Tk()
root.title("METANIT.COM")
root.geometry("500x500")

languages = ["JavaScript", "C#", "Java","JavaScript", "C#", "Java","JavaScript", "C#", "Java"]
languages_var = Variable(value=languages)

languages_listbox = Listbox(selectmode= MULTIPLE,listvariable=languages_var, fg="red", highlightcolor="green", font=20, highlightthickness=10, selectbackground="blue",selectforeground="yellow")
languages_listbox.place(width=200, height=300, x=20)

button1 = Button(text="Click", command=show)
button1.place(x=250)



# languages2 = ["C", "C++"]
# languages_var.set(languages2)

# print(languages_var.get())

# print(languages_listbox.insert(0, "AAAAAAAA"))


# current selection - indi secdiyimiz

root.mainloop()



# StringVar() IntVar()
# textvariable

# Variable()
# listvariable
'''



from tkinter import *

import pickle
def add():
    my_ad = ad1.get()
    my_soyad = soyad1.get()
    my_age = age1.get()
    my_job = job1.get()
    my_person = Person(my_ad, my_soyad, my_age, my_job)
    people.append(my_person)
    people_var.set(people)

    print("~~~~~~~~~~~")
    print(people)
    for i in people:
        print(i)
    print("~~~~~~~~~~~")
def delete():
    people.pop(languages_listbox.curselection()[0]) # (0)
    people_var.set(people)


def save():
    with open('file1.txt', 'wb') as file:
        pickle.dump(people, file)
    print("+++++++++")
    print(people)
    for i in people:
        print(i)
    print("+++++++++")

class Person:
    def __init__(self, name, surname, age, job):
        self.name = name
        self.surname = surname
        self.age = age
        self.job = job
    def __str__(self):
        return f'{self.name} {self.surname} {self.age} {self.job}'
'''
dict1 = {"name":"John", "surname": "Wick"}
with open("people.dat", "wb") as file:
    pickle.dump( file)

with open("people.dat", "rb") as file:
    result = pickle.load(file)
print(result)
print(result["name"])
'''
root = Tk()
root.title("METANIT.COM")
root.geometry("1000x500")


people = []

try:
    file = open("file1.txt", "rb")
    try:
        people = pickle.load(file)
    except Exception:
        print("Melumat goture bilmedim")
    finally:
        file.close()
except Exception:
    print("File yoxdu!")



people_var = Variable(value=people)
languages_listbox = Listbox(selectmode= SINGLE,listvariable=people_var, fg="red", highlightcolor="green", font=20, highlightthickness=10, selectbackground="blue",selectforeground="yellow")
languages_listbox.place(width=400, height=300, x=20)
ad1 = Entry(master=root, bg="pink", fg='black', font=25)
ad1.place(x=500, y=20)
soyad1 = Entry(master=root, bg="pink", fg='black', font=25)
soyad1.place(x=500, y=60)
age1 = Entry(master=root, bg="pink", fg='black', font=25)
age1.place(x=500, y=100)
job1 = Entry(master=root, bg="pink", fg='black', font=25)
job1.place(x=500, y=140)
ad2 = Label(master=root, text='Name', bg="pink", fg='black', font=10)
ad2.place(x=750, y=20)
soyad2 = Label(master=root, text='Surname', bg="pink", fg='black', font=10)
soyad2.place(x=750, y=60)
age2 = Label(master=root, text='Age', bg="pink", fg='black', font=10)
age2.place(x=750, y=100)
job2 = Label(master=root, text='Job', bg="pink", fg='black', font=10)
job2.place(x=750, y=140)
delete = Button(master=root, text="Delete", bg='red', fg='black', font=13, command=delete)
delete.place(x=30, y=310, width=80, height=40)
add = Button(master=root, text="Add", bg='red', fg='black', font=13, command=add)
add.place(x=500, y=200, width=80, height=40)
save = Button(master=root, text="Save", bg='red', fg='black', font=13, command= save)
save.place(x=600, y=200, width=80, height=40)
Age = Button(master=root, text="Calculate Age", bg='red', fg='black', font=13)
Age.place(x=600, y=450, width=150, height=40)
label1 = Label(master=root, text="Calculate Age", bg='red', fg='black', font=13)
label1.place(x=600, y=450, width=150, height=40)


root.mainloop()