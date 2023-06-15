from tkinter import *
root = Tk()
root.title("METANIT.COM")
root.geometry("260x300")


def delete():
   ekran.delete(0, END)
   hesab.delete(0, END)

def click(num):
   ekran.insert(END, num)

def equal ():
   cav = ekran.get()
   hesab.delete(0, END)
   hesab.insert(0, eval(cav))



for i in range(8):
   root.columnconfigure(i, weight=1)
for i in range(9):
   root.rowconfigure(i, weight=1)

button1 = Button(text="1", bg="black",fg="white", font= 14, command= lambda: click('1'))
button1.grid(row=2, column=0, columnspan=5, ipadx = 55,  ipady=50)
button2 = Button(text="2", bg="black",fg="white", font= 14, command= lambda: click('2'))
button2.grid(row=2, column=1, columnspan=5, ipadx = 55, ipady=50)
button3 = Button(text="3",bg="black",fg="white", font= 14, command= lambda: click('3'))
button3.grid(row=2, column=2, columnspan=5, ipadx = 55, ipady=50)
button_add = Button(text="+",bg="grey",fg="white", font= 14,  command= lambda: click('+'))
button_add.grid(row=2, column=3, columnspan=5, ipadx = 55, ipady=50)

button4 = Button(text="4", bg="black",fg="white", font= 14, command= lambda: click('4'))
button4.grid(row=3, column=0, columnspan=5,  ipadx = 55, ipady=50)
button5 = Button(text="5", bg="black",fg="white", font= 14, command= lambda: click('5'))
button5.grid(row=3, column=1, columnspan=5, ipadx = 55, ipady=50)
button6 = Button(text="6", bg="black",fg="white", font= 14, command= lambda: click('6'))
button6.grid(row=3, column=2, columnspan=5, ipadx = 55, ipady=50)
button_cix = Button(text="-",bg="grey",fg="white", font= 14,  command= lambda: click('-'))
button_cix.grid(row=3, column=3, columnspan=5, ipadx = 55, ipady=50)

button7 = Button(text="7",bg="black",fg="white", font= 14, command= lambda: click('7'))
button7.grid(row=4, column=0,columnspan=5,ipadx = 55, ipady=50)
button8 = Button(text="8",bg="black",fg="white", font= 14, command= lambda: click('8'))
button8.grid(row=4, column=1, columnspan=5, ipadx = 55, ipady=50)
button9 = Button(text="9", bg="black",fg="white", font= 14, command= lambda: click('9'))
button9.grid(row=4, column=2, columnspan=5, ipadx = 55, ipady=50)
button_multi = Button(text="*",bg="grey",fg="white", font= 14,  command= lambda: click('*'))
button_multi.grid(row=4, column=3, columnspan=5, ipadx = 55, ipady=50)

button_C = Button(text="C", bg="grey",fg="white", font= 14, command= delete)
button_C.grid(row=5, column=0, columnspan=5, ipadx = 55, ipady=50)
button0 = Button(text="0", bg="black",fg="white", font= 14, command= lambda: click('0'))
button0.grid(row=5, column=1, columnspan=5, ipadx = 55, ipady=50)
button_equal = Button(text="=", bg="red",fg="white", font= 14, command= equal)
button_equal.grid(row=5, column=2, columnspan=5, ipadx = 55, ipady=50)
button_divid = Button(text="/", bg="grey",fg="white", font= 14,  command= lambda: click('/'))
button_divid.grid(row=5, column=3, columnspan=5, ipadx = 55, ipady=50)

ekran = Entry(bg="grey",fg="white", font= 14)
ekran.grid(row=1, column=2,columnspan=2, ipadx = 37, ipady=55)
hesab = Entry(bg="grey",fg="white", font= 14)
hesab.grid(row=1, column=3, columnspan=4, ipadx = 37, ipady=55)

root.mainloop()