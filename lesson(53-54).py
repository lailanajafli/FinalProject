# w - write
# a - append
# r - read

# b - binary

# w
# hello
# john
# -> john

# a
# hello
# john
# hellojohn


with open("hello.txt", "w") as somefile:
somefile.write("John\n")
somefile.write("James\n")
somefile.write("Emin\n")





# w - write
# a - append
# r - read

# b - binary

# w
# hello
# john
# -> john

# a
# hello
# john
# hellojohn


with open("hello.txt", "r") as somefile:
text = somefile.read()
print(text)




# w - write
# a - append
# r - read

# b - binary

# w
# hello
# john
# -> john

# a
# hello
# john
# hellojohn

# readlines() -> her bir setr listin elementi olur
# read() -> boyuk string
# readline() -> her defe cagiranda gelen setri oxuyur

with open("hello.txt", "r") as somefile:
text = somefile.readline()
print(text)
text = somefile.readline()
print(text)
text = somefile.readline()
print(text)
text = somefile.readline()
print(text)
text = somefile.readline()
print(text)




# .txt
# .dat

import pickle

list1 = [100, 20, 15]

# wb
# rb

# write -> pickle.dump
# read -> pickle.load

with open("hello.txt", "wb") as file:
pickle.dump(list1, file)

with open("hello.txt", "rb") as file:
result = pickle.load(file)
print(result)




# .txt
# .dat

import pickle

dict1 = {"name":"John", "surname": "Wick"}

# wb
# rb

# write -> pickle.dump
# read -> pickle.load

with open("people.dat", "wb") as file:
pickle.dump(dict1, file)

with open("people.dat", "rb") as file:
result = pickle.load(file)
print(result)
print(result["name"])




# .txt
# .dat

import pickle

class Person:
def __init__(self, name, surname):
self.name = name
self.surname = surname

def say_name(self):
print(f"My name is {self.name} {self.surname}")


# wb
# rb

# write -> pickle.dump
# read -> pickle.load

list1 = [Person("Asif", "Ivanov"), Person("James", "Bond"), Person("Harry", "Potter")]


with open("people", "wb") as file:
pickle.dump(list1, file)

with open("people", "rb") as file:
result = pickle.load(file)
for i in result:
i.say_name()






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