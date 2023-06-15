'''
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
'''



from tkinter import *
from tkinter import ttk
root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")
for c in range(3): root.columnconfigure(index=c, weight=1)
for r in range(3): root.rowconfigure(index=r, weight=1)
button1 = Button(text="Hello", bg="blue", padx = 15, pady = 15)
button1.grid(row=2, column=1, sticky="nsew")
button2 = Button(text="Hello", bg="blue")
button2.grid(row=2, column=2,sticky="nsew")
label1 = Label(text="John")
label1.grid(row=1, column=0)
label1 = Label(text="James")
label1.grid(row=0, column=2)
root.mainloop()







