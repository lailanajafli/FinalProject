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


'''
'''
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
'''


# StringVar() IntVar()
# textvariable

# Variable()
# listvariable




from tkinter import *
import pickle
person = []
def auto_save(wind):
    with open("saved data.dat", "wb") as data:
        pickle.dump(person, data)
    wind.destroy()
def save():
    with open("saved data.dat", "wb") as data:
        pickle.dump(person, data)


def add():
    name = name_entry.get()
    surname = surname_entry.get()
    age = age_entry.get()
    job = job_entry.get()
    new_person = [name, surname, age, job]
    person.append(new_person)
    person_var.set(person)
    name_entry.delete(0, END)
    surname_entry.delete(0, END)
    age_entry.delete(0, END)
    job_entry.delete(0, END)
    print(person)
def delete():
    global person
    print(person)
    person_listbox.delete(ANCHOR)
    person = []
    for i in range(len(list(person_listbox.get(0, END)))):
        person.append(list(person_listbox.get(0, END)[i]))
    print(person)
def edit():
    global person
    def save():
        index_data = person.index(data_person)
        person.remove(data_person)
        name = name_entry1.get()
        surname = surname_entry1.get()
        age = age_entry1.get()
        job = job_entry1.get()
        new_person = [name, surname, age, job]
        person.insert(index_data, new_person)
        person_var.set(person)
        print(person)
        root1.destroy()
    root1 = Toplevel(root)
    root1.title("EDIT")
    root1.geometry("400x400+400+400")
    data_person = [i for i in person_listbox.get(person_listbox.curselection())]
    name_entry1 = Entry(root1, width=35)
    name_entry1.grid(row=0, column=0, padx=10)
    name_entry1.insert(0, data_person[0])
    surname_entry1 = Entry(root1, width=35)
    surname_entry1.grid(row=1, column=0, padx=10)
    surname_entry1.insert(0, data_person[1])
    age_entry1 = Entry(root1, width=35)
    age_entry1.grid(row=2, column=0, padx=10)
    age_entry1.insert(0, data_person[2])
    job_entry1 = Entry(root1, width=35)
    job_entry1.grid(row=3, column=0, padx=10)
    job_entry1.insert(0, data_person[3])
    name_label1 = Label(root1, text="Name")
    name_label1.grid(row=0, column=1)
    surname_label1 = Label(root1, text="Surname")
    surname_label1.grid(row=1, column=1)
    age_label1 = Label(root1, text="Age")
    age_label1.grid(row=2, column=1)
    job_label1 = Label(root1, text="Job")
    job_label1.grid(row=3, column=1)
    save_bottun = Button(root1, text="Save", command=save, width=10)
    save_bottun.grid(row=4, column=1)
    root1.mainloop()

    with open("saved data.dat", "rb") as data:
        person = pickle.load(data)
root = Tk()
root.title("Personal data")
root.geometry("800x500+300+200")
root.protocol("WM_DELETE_WINDOW", lambda: auto_save(root))
person_var = Variable(value=person)
person_listbox = Listbox(selectmode=SINGLE, width=30, listvariable=person_var, fg="red", highlightcolor="green",
                         font=20, highlightthickness=10, selectbackground="blue", selectforeground="yellow")
person_listbox.grid(row=0, column=0, rowspan=4)
name_entry = Entry(width=35)
name_entry.grid(row=0, column=1, padx=10)
surname_entry = Entry(width=35)
surname_entry.grid(row=1, column=1, padx=10)
age_entry = Entry(width=35)
age_entry.grid(row=2, column=1, padx=10)
job_entry = Entry(width=35)
job_entry.grid(row=3, column=1, padx=10)
name_label = Label(text="Name")
name_label.grid(row=0, column=2)
surname_label = Label(text="Surname")
surname_label.grid(row=1, column=2)
age_label = Label(text="Age")
age_label.grid(row=2, column=2)
job_label = Label(text="Job")
job_label.grid(row=3, column=2)
add_button = Button(text="Add", command=add, width=10)
add_button.grid(row=4, column=1)
delete_button = Button(text="Delete", command=delete, width=10)
delete_button.grid(row=4, column=0)
edit_button = Button(text="Edit", width=10, command=edit)
edit_button.grid(row=5, column=0)
save_button = Button(text="Save", width=10, command=save)
save_button.grid(row=6, column=0)
root.mainloop()