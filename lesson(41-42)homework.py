
# Tapsiriq 1.
'''
from tkinter import *

root = Tk()
root.tittle = 'Thermometer'
root.geometry('1000x400')

def c_to_f():
    C = float(celsius_entry1.get())
    F = C * 9/5 + 32
    fahrenheit_entry.delete(0, END)
    fahrenheit_entry.insert(0, str(F))


def f_to_c():
    F = float(fahrenheit_entry2.get())
    C = 5/9 * (F-32)
    celsius_entry2.delete(0, END)
    celsius_entry2.insert(0, str(round(C, 2)))


celsius1 = Label(text = "Celsius", fg="black", width = 10, font=25)
celsius1.place(x = 40, y = 36)

celsius2 = Label(text = "Celsius", fg="black", width = 10, font=25)
celsius2.place(x = 490, y = 167)

celsius_entry1 = Entry(width = 26, font=15)
celsius_entry1.place(x = 50, y = 70)

celsius_entry2 = Entry(width = 26, font=15)
celsius_entry2.place(x = 490, y = 200)

to = Label(text = "to", fg="black", width = 10, font=25)
to.place(x = 350, y = 70)

to2 = Label(text = "to", fg="black", width = 10, font=25)
to2.place(x = 350, y = 200)

fahrenheit1 = Label(text = "Fahrenheit", fg="black", width = 10, font=25)
fahrenheit1.place(x = 500, y = 36)

fahrenheit2 = Label(text = "Fahrenheit", fg="black", width = 10, font=25)
fahrenheit2.place(x = 50, y = 167)

fahrenheit_entry = Entry(width = 26, font=15)
fahrenheit_entry.place(x = 490, y = 70)

fahrenheit_entry2 = Entry(width = 26, font=15)
fahrenheit_entry2.place(x = 50, y = 200)

click1 = Button(text="Convert", font=15, fg="white", bg="black", command = c_to_f)
click1.place(width=150, x=800, y=67)

click2 = Button(text="Convert", font=15, fg="white", bg="black", command = f_to_c)
click2.place(width=150, x=800, y=197)
root.mainloop()
'''

'''
# Tapsiriq 2.
from tkinter import *

import random
root = Tk()
root.tittle = 'Texmiin oyunu'
root.geometry('1000x400')


def control():
    global luck
    global number2
    if number1.get().isdigit():
        s1 = int(number1.get())
        luck = luck + 1
        if s1 > number2:
            yazi2.configure(text = 'Asagi')
        elif s1 < number2:
            yazi2.configure(text= 'Yuxari')
        else:
            yazi2.configure(text='{} defe de texmin etdiniz'.format(luck))
            number2 = random.randint(1, 100)
            luck = 0
    number1.selection_range(0, END)

yazi = Label(text = "Eded daxil edin: ", fg="black", width = 25, font=30)
yazi.place(x = 15, y = 20)

number1 = Entry(width = 15, font=20)
number1.place(x = 70, y = 50)
number1.focus()

kontrol = Button(text="Kontrol", font= 14, fg="white", width=10, bg="black", command= control)
kontrol.place( x=90, y=80)

yazi2 = Label(text = " ", fg="black", width = 25, font=25)
yazi2.place(x = 0, y = 120)

number2 = random.randint(1,100)
luck = 0

root.mainloop()
'''

# Tapsiriq 3.

from tkinter import *
root = Tk()
root.tittle = 'Texmiin oyunu'
root.geometry('1000x400')
current_question = 0
duzgun = IntVar()
sehv = IntVar()
duzgun.set(0)
sehv.set(0)
def load_question():
    sual["text"] = questions[current_question]["Sual"]
    varA["text"] = questions[current_question]["A"]
    varB["text"] = questions[current_question]["B"]
    varC["text"] = questions[current_question]["C"]
    varD["text"] = questions[current_question]["D"]

def cavabi_yoxla(variant):
    global current_question
    if variant == questions[current_question]["Correct"]:
        duzgun.set(duzgun.get()+1)
    else:
        sehv.set(sehv.get()+1)
    current_question += 1
    load_question()

questions = [{"Sual":"En uzun cay hansidir?", "A":"Amazon cayi", "B":"Araz cayi", "C":"Kur cayi", "D":"Nil cayi", "Correct": "A"},
             {"Sual":"En hundur dag hansidi?", "A":"Kavkaz", "B":"Everest", "C":"Altay", "D":"Alp", "Correct": "B"},
             {"Sual":"5+5", "A":"10", "B":"7", "C":"3", "D":"2", "Correct": "A"}]

sual = Label(text = "", fg="black", width = 25, font=25)
sual.place(x = 3, y = 30)
varA = Button(text="", font=15, fg="black", bg="pink", command= lambda : cavabi_yoxla("A"))
varA.place(width=200, x=37, y=65)
varB = Button(text="", font=15, fg="black", bg="pink", command= lambda : cavabi_yoxla("B"))
varB.place(width=200, x=37, y=115)
varC = Button(text="", font=15, fg="black", bg="pink", command= lambda : cavabi_yoxla("C"))
varC.place(width=200, x=37, y=165)
varD = Button(text="", font=15, fg="black", bg="pink", command= lambda : cavabi_yoxla("D"))
varD.place(width=200, x=37, y=215)
false_entry = Label(textvariable=sehv,width = 10, font=15)
false_entry.place(x = 490, y = 300)
true_entry = Label(textvariable=duzgun, width = 10, font=15)
true_entry.place(x = 330, y = 300)
false = Label(text = "False", fg="red", width = 25, font=25)
false.place(x = 410, y = 270)
true = Label(text = "True", fg="green",font=25)
true.place(x = 360, y = 270)
load_question()
root.mainloop()



