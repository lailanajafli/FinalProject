
from tkinter import *
root = Tk()
root.title("My Restaurant")
root.geometry("1573x899")



def open_plate():
    root2 = Tk()
    root2.title("Plate")
    root2.geometry("1200x770")
    plate11 = PhotoImage(file="Picsart_23-06-15_23-51-38-798.png")
    plate1 = Label(root2, bg='peachpuff1', image=plate11)
    plate1.place(x=150, y=400)



backphotowin1 = PhotoImage(file="stock-photo-texture-beige-color-paper-background.png")
table2_1 = PhotoImage(file="Rec 2.png")
table2_2 = PhotoImage(file="Rec 2.png")
table2_3 = PhotoImage(file="Rec 2.png")
table2_4 = PhotoImage(file="Rec 2.png")
table4_1 = PhotoImage(file="Round 4.png")
table4_2 = PhotoImage(file="Round 4.png")
table6_1 = PhotoImage(file="Rec 6.png")
table6_2 = PhotoImage(file="Rec 6.png")
kenar11 = PhotoImage(file="635e9e0327dcbc383d0eb2b6-artiflr-6-ft-artificial-peony-garland - Köçür.png")
kenar22 = PhotoImage(file="635e9e0327dcbc383d0eb2b6-artiflr-6-ft-artificial-peony-garland.png")
kenar33 = PhotoImage(file="635e9e0327dcbc383d0eb2b6-artiflr-6-ft-artificial-peony-garland.png")
kenar44 = PhotoImage(file="635e9e0327dcbc383d0eb2b6-artiflr-6-ft-artificial-peony-garland - Köçür.png")
plant11 = PhotoImage(file="169-1691852_organic-quality-takes-time.png")
plant22 = PhotoImage(file="169-1691852_organic-quality-takes-time.png")
kassa1 = PhotoImage(file="Picsart_23-06-15_22-47-04-631.png")
warehouse1 = PhotoImage(file="Picsart_23-06-15_23-01-47-610.png")
shop1 = PhotoImage(file="Picsart_23-06-15_23-17-52-508.png")


back1 = Label(root,image= backphotowin1)
back1.place(x=0, y=0)
table2li_1 = Button(root, bg='peachpuff1', activebackground='peachpuff1',image= table2_1, command=open_plate)
table2li_1.place(x=750, y=170)
table2li_2 = Button(root, bg='peachpuff1', activebackground='peachpuff1',image= table2_2)
table2li_2.place(x=1295, y=170)
table2li_3 = Button(root, bg='peachpuff1', activebackground='peachpuff1',image= table2_3)
table2li_3.place(x=750, y=490)
table2li_4 = Button(root, bg='peachpuff1', activebackground='peachpuff1',image= table2_4)
table2li_4.place(x=1295, y=490)
table4lu1 = Button(root, bg='peachpuff1', activebackground='peachpuff1',image= table4_1)
table4lu1.place(x=750, y=330)
table4lu2 = Button(root, bg='peachpuff1', activebackground='peachpuff1',image= table4_2)
table4lu2.place(x=1100, y=330)
table6li1 = Button(root, bg='peachpuff1', activebackground='peachpuff1',image= table6_1)
table6li1.place(x=900, y=330)
table6li2 = Button(root, bg='peachpuff1', activebackground='peachpuff1',image= table6_2)
table6li2.place(x=1250, y=330)
kassa = Button(root, bg='peachpuff1', activebackground='peachpuff1',image= kassa1)
kassa.place(x=20, y=20)
warehouse = Button(root, bg='peachpuff1', activebackground='peachpuff1',image= warehouse1)
warehouse.place(x=20, y=560)
shop = Button(root, bg='peachpuff1', activebackground='peachpuff1',image= shop1)
shop.place(x=20, y=350)
kenar1 = Label(root,image= kenar11)
kenar1.place(x=1455, y=0)
kenar2 = Label(root,image= kenar22)
kenar2.place(x=630, y=0)
kenar3 = Label(root,image= kenar33)
kenar3.place(x=630, y=715)
kenar4 = Label(root,image= kenar44)
kenar4.place(x=630, y=180)
plant1 = Label(root,bg= 'peachpuff1', image= plant11)
plant1.place(x=1000, y=150)
plant1 = Label(root,bg= 'peachpuff1', image= plant22)
plant1.place(x=1000, y=500)









root.mainloop()
