'''
from tkinter import *
name = 'leyla'
password = '123'
def login():
    if name==entryName.get() and password==entryPassword.get():
       btn1["fg"] = "pink"
    else:
       label2["fg"] = "red"
root = Tk()
root.title = "STEP IT"
root.geometry("900x600+200+100")
btn1 = Button(root, text="Login", command=login, font=20, fg="red", bg="white")
btn1.place(x=370, y=350)
label1 = Label(text="Name", font=15, fg="black", bg="white")
label1.place(x=255, y=216)
label2 = Label(text="Password", font=15, fg="black", bg="white")
label2.place(x=255, y=286)
entryName = Entry(bg="white", fg="black", font=20, )
entryName.place(width=300,x=250, y=250)
entryPassword = Entry(bg="white", fg="black", font=20, show="*")
entryPassword.place(width=300,x=250, y=320)
labelResult = Label(text="", font=20)
labelResult.place(x=370, y=420)
root.mainloop()
'''


from tkinter import *

root = Tk()
root.title = "STEP IT"
root.geometry("900x600+200+100")

def add():
    topla = int(yuxari_sol.get()) + int(yuxari_sag.get())
    cavab['text'] = topla

def cix():
    sum1 = int(yuxari_sol.get()) - int(yuxari_sag.get())
    cavab['text'] = sum1

def vur():
    sum2 = int(yuxari_sol.get()) * int(yuxari_sag.get())
    cavab['text'] = sum2

def bol():
    sum3 = int(yuxari_sol.get()) / int(yuxari_sag.get())
    cavab['text'] = sum3

yuxari_sol = Entry(bg="white", fg="black", font=15, )
yuxari_sol.place(width=250,x=600, y=100)

yuxari_sag = Entry(bg="white", fg="black", font=15, )
yuxari_sag.place(width=250,x=92, y=100)

topla = Button(text="+", font=15, fg="white", bg="brown", command=add)
topla.place(width=200, x=350, y=200)

cix = Button(text="-", font=15, fg="white", bg="brown", command=cix)
cix.place(width=200, x=350, y=250)

vur = Button(text="*", font=15, fg="white", bg="brown", command=vur)
vur.place(width=200, x=350, y=300)

bol = Button(text="/", font=15, fg="white", bg="brown", command=bol)
bol.place(width=200, x=350, y=350)

cavab = Label(text="Cavab", font=15, fg="black", bg="pink")
cavab.place(width=200, x=580, y=440)
root.mainloop()


























'''
from tkinter import *
from tkinter import messagebox
def hello():
   label1["text"] = entry1.get()
   label1["fg"] = "white"
   label1["bg"] = "black"
root = Tk()
root.title = "STEP IT"
root.geometry("900x600+200+100")
# foreground
# background
# SIDE - TOP, BOTTOM, LEFT, RIGHT
# fill - BOTH, X, Y, NONE
btn1 = Button(root, text="Click", command=hello, underline=3, font=20, fg="red", bg="blue", borderwidth=1)
# btn1.pack(padx=20, pady=50, ipadx=20, ipady=20, expand=True, fill=NONE, anchor="se")
# btn1.place(width=500, height=500, x=100, y=100)
btn1.place(x=100, y=200)
# Pencere 500 -> relx=0.5 = 250
# relwitdh = 0.5 -> pencere = 500 -> Button = 250
label1 = Label(text="Hello", font=15, fg="green", bg="red")
label1.place(x=100, y=100)
entry1 = Entry(bg="red", fg="white", font=20, show="*")
entry1.place(width=300,x=100, y=150)
root.mainloop()
































































































































from tkinter import *

root = Tk()
root.title("HELLO LEYLA")
root.iconbitmap(default="OIP.ico")
root.geometry('200x300')
root.resizable(True, True)

root.minsize(200,150)
root.maxsize(4700,800)

root.mainloop()


from tkinter import *

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")

btn = Button(text="Hello")
btn.pack()


def print_info(widget, depth=0):
    widget_class = widget.winfo_class()                           #               |
    widget_width = widget.winfo_width()       #click i bele cik elemek ucun   ____|
    widget_height = widget.winfo_height()
    widget_x = widget.winfo_x()
    widget_y = widget.winfo_y()
    print("   " * depth + f"{widget_class} width={widget_width} height={widget_height}  x={widget_x} y={widget_y}")
    for child in widget.winfo_children():
        print_info(child, depth + 1)


root.update()  # обновляем информацию о виджетах

print_info(root)

root.mainloop()

Düymə:   düymə
Label:   Mətn etiketi
Giriş:   Tək sətirli mətn qutusu
Teqlər:   Çox sətirli mətn qutusu
Checkbutton:   checkbox
Radiobutton:   Switch və ya radio düyməsi
Çərçivə:   Vidjetləri qruplara təşkil edən çərçivə
Siyahı qutusu:   siyahı
Kombobox:   açılan siyahı
Menyu:   Menyu üzvü
Scrollbar:   Scrollbar
Treeview:   Ağac və masa öğeleri yaratmaq üçün imkan verir
Tərəzi:   Mətn etiketi
Spinbox:   elementlər vasitəsilə hərəkət etmək üçün oxları olan dəyərlərin siyahısı
Progressbar:   Mətn etiketi
Canvas:   Mətn etiketi
Qeyd dəftəri:   Tab çubuğu
'''



































