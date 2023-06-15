
from tkinter import *
def c_far(*args):
    if len(celsius_entry.get())>0:
        c = celsius.get()
        farenheit.set(c*2)
    else:
        farenheit_entry.delete(0, END)
def far_c(*args):
    if len(farenheit_entry.get())>0:
        far = farenheit.get()
        celsius.set(far/2)
    else:
        celsius_entry.delete(0, END)
root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")
celsius = DoubleVar()
farenheit = DoubleVar()
celsius.set(0.0)
farenheit.set(0.0)
celsius_entry = Entry(textvariable=celsius)
celsius_entry.pack(padx=5, pady=5, anchor=NW)
farenheit_entry = Entry(textvariable=farenheit)
farenheit_entry.pack(padx=5, pady=5, anchor=NW)
celsius.trace_add("write", c_far)
farenheit.trace_add("write", far_c)
root.mainloop()


'''
1       text
textin formasi 3 cur elemek olur
wrap=word
wrap=char
wrap= none

2      scrollbarVertical = yuxaridan asagi surusdurmek ucun  command=editor.yview
       scrollbarHorizontal = sagdan sola surusdurmek ucun
       
3       insert = indexlere soz elave etmek
       
       
4       massagebox.showinfo("!",editor.get("1.0", "1.4"))      
       
       
5      delete       

6      replace


7 TRACE 
from tkinter import *

root = Tk()
root.title("METANIT.COM")
root.geometry("500x500")

# wrap=word
# wrap=char
editor = Text(wrap="none")
editor.place(width=200, height=200, x=200, y=200)

scrollbarVertical = Scrollbar(orient="vertical", command=editor.yview)
scrollbarVertical.place(x=400, y=200, height=200)
scrollbarHorizontal = Scrollbar(orient="horizontal", command=editor.xview)
scrollbarHorizontal.place(x=200, y=400, width=200)

editor["yscrollcommand"] = scrollbarVertical.set
editor["xscrollcommand"] = scrollbarHorizontal.set

root.mainloop()


from tkinter import *
from tkinter import messagebox
# Heljohnlo
# insert(3, "john")
# HeJohnewerwer
# HellJohnewerwr
# insert("2.4", "John")
def add_command():
    editor.insert("2.4", "John")
def get_command():
    messagebox.showinfo("!", editor.get("1.0", "2.4"))
def delete_command():
    editor.delete("1.2", "3.2")
def replace_command():
    editor.replace("1.0", "1.5", "Yes")
def undo():
    editor.edit_undo()
def redo():
    editor.edit_redo()
def clear():
    print("Check")
    editor.selection_clear()
# edit_undo
# edit_redo
root = Tk()
root.title("METANIT.COM")
root.geometry("500x500")
# wrap=word
# wrap=char
editor = Text(wrap="none", undo=True)
editor.place(width=200, height=200, x=200, y=200)
scrollbarVertical = Scrollbar(orient="vertical", command=editor.yview)
scrollbarVertical.place(x=400, y=200, height=200)
scrollbarHorizontal = Scrollbar(orient="horizontal", command=editor.xview)
scrollbarHorizontal.place(x=200, y=400, width=200)
button1 = Button(text="<-", command=undo)
button1.place(x=200, y=150, width=70, height=35)
button2 = Button(text="->", command=redo)
button2.place(x=300, y=150, width=70, height=35)
button3 = Button(text="Get", command=lambda: messagebox.showinfo("", editor.selection_get()))
button3.place(x=300, y=100, width=70, height=35)
button4 = Button(text="Clear", command=clear)
button4.place(x=200, y=100, width=70, height=35)
editor["yscrollcommand"] = scrollbarVertical.set
editor["xscrollcommand"] = scrollbarHorizontal.set
root.mainloop()
'''

















