from tkinter import *
import pickle

class Food:
    def __init__(self, price):
        self.price = price
        self.count = 0
    def __str__(self):
        return str(self.count)
class Product:
    def __init__(self, price):
        self.price = price
        self.count = 0
    def __str__(self):
        return str(self.count)

class Masa:
    def __init__(self):
        self.orders = {"kabab": Food(20), "lahmacun": 0, "toyuq doner": 0, "xengel": 0, "merci": 0, "plov": 0, "dovga": 0, "kartof fri": 0, "pizza": 0, "pide": 0, "paytaxt": 0}

class Database:
    def __init__(self):
        self.tables = {"1": Masa(), "2": Masa(), "3": Masa(), "4": Masa(), "5": Masa(), "6": Masa(), "7": Masa(), "8": Masa()}
        self.products = {"zeytunyagi": Product(10.59), "merci": Product(3.75), "duyu": 0, "qatiq": 0, "duz": 0, "et": 0, "seker tozu": 0, "yumurta": 0, "mayonez": 0}
        self.prices = {"zeytunyagi": 10.59, "merci": 3.75, "duyu": 4.65, "qatiq": 3.4, "duz": 1.89, "et": 17, "seker tozu": 1.66, "yumurta": 20, "mayonez": 5.15}

database = Database()
def add_to_cart(label, product):
    database.products[product].count += 1
    label["text"] = database.products[product].count

def total_price(label, product, price):
    database.products[product] += 1
    label["text"] = database.prices[price]

def add_order(table, order, label):
    database.tables[table].orders[order].count += 1
    label["text"] = database.tables[table].orders[order].count

'''
def reset()
    database.products[product].delete(ANCHOR)
    database.products[product].get(0, END):
    for i in range(len(list(person_listbox.get(0, END)))):
        person.append(list(person_listbox.get(0, END)[i]))
'''
def open_plate(table_number):
    root_plate = Toplevel()
    root_plate.title("Plate")
    root_plate.geometry("1200x770+150+0")
    root_plate.resizable(False, False)

    plate11 = PhotoImage(file="Images/plate.png")
    plate1 = Label(root_plate, bg='peachpuff1', image=plate11)
    plate1.place(x=0, y=0)
    menu11 = PhotoImage(file="Images/menu.png")
    menu1 = Button(root_plate, bg='peachpuff1', activebackground='peachpuff1', image=menu11, command=lambda: open_menu(table_number))
    menu1.place(x=255, y=200)

    root_plate.mainloop()

def recipekab():
    root_recipe1 = Toplevel()
    root_recipe1.title("Kabab recipe")
    root_recipe1.geometry("1000x562+250+150")
    root_recipe1.resizable(False, False)

    recipeback1 = PhotoImage(file="Images/recipeback.png")
    recipeback = Label(root_recipe1, bg='peachpuff1', image=recipeback1)
    recipeback.place(x=0, y=0)
    kababrecipe = PhotoImage(file="Images/kabab.png")
    krecipe = Button(root_recipe1, text='Kabab Recipe', bg='grey18', activebackground='grey18', image=kababrecipe)
    krecipe.place(x=40, y=20)
    kababrepices = ['              Kabab:', ' Et',' Badimcan',' Pomidor',' Edviyyat',' Duz, Istiot',' Sogan']
    kabab_var = Variable(value=kababrepices)
    kabab_listbox = Listbox(root_recipe1, selectmode=DISABLED, listvariable=kabab_var, fg="grey", bg='grey18',highlightcolor="grey18",
    highlightbackground='grey18', font=20, highlightthickness=10, selectbackground="grey")
    kabab_listbox.place(width=360, height=350, x=40, y=150)

    root_recipe1.mainloop()


def recipelahmacun():
    root_recipe1 = Toplevel()
    root_recipe1.title("Lahmacun recipe")
    root_recipe1.geometry("1000x562+250+150")
    root_recipe1.resizable(False, False)

    recipeback1 = PhotoImage(file="Images/recipeback.png")
    recipeback = Label(root_recipe1, bg='peachpuff1', image=recipeback1)
    recipeback.place(x=0, y=0)
    lahmacunrecipe = PhotoImage(file="Images/lahmacun.png")
    lrecipe = Button(root_recipe1, text='Lahnacun Recipe', bg='grey18', activebackground='grey18', image=lahmacunrecipe)
    lrecipe.place(x=40, y=20)
    lahmacunrepices = ['              Lahmacun:', ' Et',' ',' Pomidor',' Edviyyat',' Duz, Istiot',' Sogan']
    lahmacun_var = Variable(value=lahmacunrepices)
    kabab_listbox = Listbox(root_recipe1, selectmode=DISABLED, listvariable=lahmacun_var, fg="grey", bg='grey18',highlightcolor="grey18",
    highlightbackground='grey18', font=20, highlightthickness=10, selectbackground="grey")
    kabab_listbox.place(width=360, height=350, x=40, y=150)

    root_recipe1.mainloop()


def recipedoner():
    root_recipe1 = Toplevel()
    root_recipe1.title("Doner recipe")
    root_recipe1.geometry("1000x562+250+150")
    root_recipe1.resizable(False, False)

    recipeback1 = PhotoImage(file="Images/recipeback.png")
    recipeback = Label(root_recipe1, bg='peachpuff1', image=recipeback1)
    recipeback.place(x=0, y=0)
    donerrecipe = PhotoImage(file="Images/toyuqdoner.png")
    drecipe = Button(root_recipe1, text='Toyuq doner Recipe', bg='grey18', activebackground='grey18', image=donerrecipe)
    drecipe.place(x=40, y=20)
    doner_label = Label(root_recipe1, fg="grey", text='''
           Toyuq doner
    Et\nPomidor
    ''',bg='grey18',highlightcolor="grey18", font=20)
    doner_label.place(x=40, y=150)

    root_recipe1.mainloop()


def recipexengel():
    root_recipe1 = Toplevel()
    root_recipe1.title("Xengel recipe")
    root_recipe1.geometry("1000x562+250+150")
    root_recipe1.resizable(False, False)

    recipeback1 = PhotoImage(file="Images/recipeback.png")
    recipeback = Label(root_recipe1, bg='peachpuff1', image=recipeback1)
    recipeback.place(x=0, y=0)
    xengelrecipe = PhotoImage(file="Images/xengel.png")
    xrecipe = Button(root_recipe1, text='Xengel Recipe', bg='grey18', activebackground='grey18', image=xengelrecipe)
    xrecipe.place(x=40, y=20)
    xengel_label = Label(root_recipe1, fg="grey", text='''
           Xengel
    Et\nPomidor
    ''',bg='grey18',highlightcolor="grey18", font=20)
    xengel_label.place(x=40, y=150)

    root_recipe1.mainloop()


def recipemerci():
    root_recipe1 = Toplevel()
    root_recipe1.title("Merci recipe")
    root_recipe1.geometry("1000x562+250+150")
    root_recipe1.resizable(False, False)

    recipeback1 = PhotoImage(file="Images/recipeback.png")
    recipeback = Label(root_recipe1, bg='peachpuff1', image=recipeback1)
    recipeback.place(x=0, y=0)
    mercirecipe = PhotoImage(file="Images/mercisorbasi.png")
    mrecipe = Button(root_recipe1, text='Merci Recipe', bg='grey18', activebackground='grey18', image=mercirecipe)
    mrecipe.place(x=40, y=20)
    merci_label = Label(root_recipe1, fg="grey", text='''
           Merci
    Et\nPomidor
    ''',bg='grey18',highlightcolor="grey18", font=20)
    merci_label.place(x=40, y=150)

    root_recipe1.mainloop()


def recipeplov():
    root_recipe1 = Toplevel()
    root_recipe1.title("Plov recipe")
    root_recipe1.geometry("1000x562+250+150")
    root_recipe1.resizable(False, False)

    recipeback1 = PhotoImage(file="Images/recipeback.png")
    recipeback = Label(root_recipe1, bg='peachpuff1', image=recipeback1)
    recipeback.place(x=0, y=0)
    plovrecipe = PhotoImage(file="Images/plov.png")
    precipe = Button(root_recipe1, text='Plov Recipe', bg='grey18', activebackground='grey18', image=plovrecipe)
    precipe.place(x=40, y=20)
    plov_label = Label(root_recipe1, fg="grey", text='''
           Plov
    Et\nPomidor
    ''',bg='grey18',highlightcolor="grey18", font=20)
    plov_label.place(x=40, y=150)

    root_recipe1.mainloop()


def recipedovga():
    root_recipe1 = Toplevel()
    root_recipe1.title("Dovga recipe")
    root_recipe1.geometry("1000x562+250+150")
    root_recipe1.resizable(False, False)

    recipeback1 = PhotoImage(file="Images/recipeback.png")
    recipeback = Label(root_recipe1, bg='peachpuff1', image=recipeback1)
    recipeback.place(x=0, y=0)
    dovgarecipe = PhotoImage(file="Images/dovga.png")
    drecipe = Button(root_recipe1, text='Dovga Recipe', bg='grey18', activebackground='grey18', image=dovgarecipe)
    drecipe.place(x=40, y=20)
    dovga_label = Label(root_recipe1, fg="grey", text='''
           Dovga
    Et\nPomidor
    ''',bg='grey18',highlightcolor="grey18", font=20)
    dovga_label.place(x=40, y=150)

    root_recipe1.mainloop()


def recipekartofri():
    root_recipe1 = Toplevel()
    root_recipe1.title("Kartof fri recipe")
    root_recipe1.geometry("1000x562+250+150")
    root_recipe1.resizable(False, False)

    recipeback1 = PhotoImage(file="Images/recipeback.png")
    recipeback = Label(root_recipe1, bg='peachpuff1', image=recipeback1)
    recipeback.place(x=0, y=0)
    kartofrirecipe = PhotoImage(file="Images/kartofri.png")
    krecipe = Button(root_recipe1, text='Kartof fri Recipe', bg='grey18', activebackground='grey18', image=kartofrirecipe)
    krecipe.place(x=40, y=20)
    kartofri_label = Label(root_recipe1, fg="grey", text='''
           Plov
    Et\nPomidor
    ''',bg='grey18',highlightcolor="grey18", font=20)
    kartofri_label.place(x=40, y=150)

    root_recipe1.mainloop()


def recipepizza():
    root_recipe1 = Toplevel()
    root_recipe1.title("Pizza recipe")
    root_recipe1.geometry("1000x562+250+150")
    root_recipe1.resizable(False, False)

    recipeback1 = PhotoImage(file="Images/recipeback.png")
    recipeback = Label(root_recipe1, bg='peachpuff1', image=recipeback1)
    recipeback.place(x=0, y=0)
    pizzarecipe = PhotoImage(file="Images/pizza.png")
    precipe = Button(root_recipe1, text='Pizza Recipe', bg='grey18', activebackground='grey18', image=pizzarecipe)
    precipe.place(x=40, y=20)
    pizza_label = Label(root_recipe1, fg="grey", text='''
           Dovga
    Et\nPomidor
    ''',bg='grey18',highlightcolor="grey18", font=20)
    pizza_label.place(x=40, y=150)

    root_recipe1.mainloop()

def recipepide():
    root_recipe1 = Toplevel()
    root_recipe1.title("Pide recipe")
    root_recipe1.geometry("1000x562+250+150")
    root_recipe1.resizable(False, False)

    recipeback1 = PhotoImage(file="Images/recipeback.png")
    recipeback = Label(root_recipe1, bg='peachpuff1', image=recipeback1)
    recipeback.place(x=0, y=0)
    piderecipe1 = PhotoImage(file="Images/pide.png")
    piderecipe = Button(root_recipe1, text='Pide Recipe', bg='grey18', activebackground='grey18', image=piderecipe1)
    piderecipe.place(x=40, y=20)
    pide_label = Label(root_recipe1, fg="grey", text='''
           Dovga
    Et\nPomidor
    ''',bg='grey18',highlightcolor="grey18", font=20)
    pide_label.place(x=40, y=150)

    root_recipe1.mainloop()

def recipepaytaxt():
    root_recipe1 = Toplevel()
    root_recipe1.title("Paytaxt salati recipe")
    root_recipe1.geometry("1000x562+250+150")
    root_recipe1.resizable(False, False)

    recipeback1 = PhotoImage(file="Images/recipeback.png")
    recipeback = Label(root_recipe1, bg='peachpuff1', image=recipeback1)
    recipeback.place(x=0, y=0)
    payrecipe1 = PhotoImage(file="Images/paytaxt.png")
    paytaxtrecipe = Button(root_recipe1, text='Paytaxt Recipe', bg='grey18', activebackground='grey18', image=payrecipe1)
    paytaxtrecipe.place(x=40, y=20)
    paytaxt_label = Label(root_recipe1, fg="grey", text='''
           Dovga
    Et\nPomidor
    ''',bg='grey18',highlightcolor="grey18", font=20)
    paytaxt_label.place(x=40, y=150)

    root_recipe1.mainloop()

def open_menu(table_number):
    root_menu = Toplevel()
    root_menu.title("Menu")
    root_menu.geometry("1520x855")
    root_menu.resizable(False, False)
    current_masa = database.tables[table_number]

    menuback1 = PhotoImage(file="Images/menuback.png")
    menu = Label(root_menu, bg='peachpuff1', image=menuback1)
    menu.place(x=0, y=0)
    menuman1 = PhotoImage(file="Images/menuman.png")
    menuman = Label(root_menu, bg='grey18', image=menuman1)
    menuman.place(x=750, y=200)
    kabab1 = PhotoImage(file="Images/kabab.png")
    kabab = Button(root_menu, text='Kabab',bg='grey18', activebackground='grey18',image=kabab1, command=lambda: add_order(table_number,"kabab",count_kabab))
    kabab.place(x=20, y=30)
    recipe11 = PhotoImage(file="Images/recipe.png")
    kababprice = Label(root_menu, text='20 azn',bg='grey18', font=10)
    kababprice.place(x=215, y=40, height=37)
    recipe1 = Button(root_menu,bg='peachpuff1', activebackground='peachpuff1', image=recipe11, command=recipekab)
    recipe1.place(x=215, y=85)
    add_kabab = Label(root_menu, text='Kabab', fg='white', bg='grey18')
    add_kabab.place(x=857, y=470, width=200)
    count_kabab = Label(root_menu, text=0, fg='white', bg='grey18')
    count_kabab.place(x=1030, y=470)
    lahmacun1 = PhotoImage(file="Images/lahmacun.png")
    lahmacun = Button(root_menu, text='Lahmacun', bg='grey18', activebackground='grey18', image=lahmacun1, command=lambda: add_order(count_lahmacun,"lahmacun"))
    lahmacun.place(x=20, y=164)
    recipe2 = Button(root_menu, bg='peachpuff1', activebackground='peachpuff1', image=recipe11, command=recipelahmacun)
    recipe2.place(x=215, y=215)
    add_lahmacun = Label(root_menu, text='Lahmacun', fg='white', bg='grey18')
    add_lahmacun.place(x=857, y=487, width=200)
    count_lahmacun = Label(root_menu, text=0, fg='white', bg='grey18')
    count_lahmacun.place(x=1030, y=487)
    toyuqdoner1 = PhotoImage(file="Images/toyuqdoner.png")
    toyuqdoner = Button(root_menu, text='Toyuq doner', bg='grey18', activebackground='grey18', image=toyuqdoner1, command=lambda: add_order(count_doner,"toyuq doner"))
    toyuqdoner.place(x=20, y=294)
    recipe3 = Button(root_menu, bg='peachpuff1', activebackground='peachpuff1', image=recipe11, command=recipedoner)
    recipe3.place(x=215, y=357)
    add_doner = Label(root_menu, text='Toyuq doner', fg='white', bg='grey18')
    add_doner.place(x=857, y=504, width=200)
    count_doner = Label(root_menu, text=0, fg='white', bg='grey18')
    count_doner.place(x=1030, y=504)
    xengel1 = PhotoImage(file="Images/xengel.png")
    xengel = Button(root_menu, text='Xengel', bg='grey18', activebackground='grey18', image=xengel1, command=lambda: add_order(count_xengel,"xengel"))
    xengel.place(x=20, y=439)
    recipe4 = Button(root_menu, bg='peachpuff1', activebackground='peachpuff1', image=recipe11, command=recipexengel)
    recipe4.place(x=215, y=470)
    add_xengel = Label(root_menu, text='Xengel', fg='white', bg='grey18')
    add_xengel.place(x=857, y=521, width=200)
    count_xengel = Label(root_menu, text=0, fg='white', bg='grey18')
    count_xengel.place(x=1030, y=521)
    mercisorbasi1 = PhotoImage(file="Images/mercisorbasi.png")
    mercisorbasi = Button(root_menu, text='Merci sorbasi', bg='grey18', activebackground='grey18', image=mercisorbasi1, command=lambda: add_order(count_merci,"merci"))
    mercisorbasi.place(x=20, y=549)
    recipe5 = Button(root_menu, bg='peachpuff1', activebackground='peachpuff1', image=recipe11, command=recipemerci)
    recipe5.place(x=215, y=595)
    add_merci = Label(root_menu, text='Merci sorbasi', fg='white', bg='grey18')
    add_merci.place(x=857, y=538, width=200)
    count_merci = Label(root_menu, text=0, fg='white', bg='grey18')
    count_merci.place(x=1030, y=538)
    plovimage = PhotoImage(file="Images/plov.png")
    plov1 = Button(root_menu, text='Plov', bg='grey18', activebackground='grey18', image=plovimage, command=lambda: add_order(count_plov, "plov"))
    plov1.place(x=20, y=674)
    recipe7 = Button(root_menu, bg='peachpuff1', activebackground='peachpuff1', image=recipe11, command=recipeplov)
    recipe7.place(x=215, y=700)
    add_plov = Label(root_menu, text='Plov', fg='white', bg='grey18')
    add_plov.place(x=857, y=555, width=200)
    count_plov = Label(root_menu, text=0, fg='white', bg='grey18')
    count_plov.place(x=1030, y=555)
    dovga1 = PhotoImage(file="Images/dovga.png")
    dovga = Button(root_menu, text='Dovga', bg='grey18', activebackground='grey18', image=dovga1, command=lambda: add_order(count_dovga,"dovga"))
    dovga.place(x=320, y=30)
    recipe6 = Button(root_menu, bg='peachpuff1', activebackground='peachpuff1', image=recipe11, command=recipedovga)
    recipe6.place(x=495, y=90)
    add_dovga = Label(root_menu, text='Dovga', fg='white', bg='grey18')
    add_dovga.place(x=857, y=572, width=200)
    count_dovga = Label(root_menu, text=0, fg='white', bg='grey18')
    count_dovga.place(x=1030, y=572)
    kartofri11 = PhotoImage(file="Images/kartofri.png")
    kartofri1 = Button(root_menu, bg='grey18', activebackground='grey18', image=kartofri11, command=lambda: add_order(count_kartof,"kartof fri"))
    kartofri1.place(x=320, y=166)
    recipe8 = Button(root_menu, bg='peachpuff1', activebackground='peachpuff1', image=recipe11, command=recipekartofri)
    recipe8.place(x=495, y=210)
    add_kartofri = Label(root_menu, text='Kartof fri', fg='white', bg='grey18')
    add_kartofri.place(x=857, y=589, width=200)
    count_kartof = Label(root_menu, text=0, fg='white', bg='grey18')
    count_kartof.place(x=1030, y=589)
    pizzaimage = PhotoImage(file="Images/pizza.png")
    pizza1 = Button(root_menu, bg='grey18', activebackground='grey18', image=pizzaimage, command=lambda: add_order(count_pizza,"pizza"))
    pizza1.place(x=320, y=288)
    recipe9 = Button(root_menu, bg='peachpuff1', activebackground='peachpuff1', image=recipe11, command=recipepizza)
    recipe9.place(x=495, y=337)
    add_pizza = Label(root_menu, text='Pizza', fg='white', bg='grey18')
    add_pizza.place(x=857, y=606, width=200)
    count_pizza = Label(root_menu, text=0, fg='white', bg='grey18')
    count_pizza.place(x=1030, y=606)
    pideimage = PhotoImage(file="Images/pide.png")
    pide1 = Button(root_menu, bg='grey18', activebackground='grey18', image=pideimage, command=lambda: add_order(count_pide, "pide"))
    pide1.place(x=320, y=410)
    recipe9 = Button(root_menu, bg='peachpuff1', activebackground='peachpuff1', image=recipe11, command=recipepide)
    recipe9.place(x=495, y=453)
    add_pide = Label(root_menu, text='Pide', fg='white', bg='grey18')
    add_pide.place(x=857, y=623, width=200)
    count_pide = Label(root_menu, text=0, fg='white', bg='grey18')
    count_pide.place(x=1030, y=623)
    paytaxtimage = PhotoImage(file="Images/paytaxt.png")
    paytaxt1 = Button(root_menu, bg='grey18', activebackground='grey18', image=paytaxtimage, command=lambda: add_order(count_paytaxt, "paytaxt", totallabel, "paytaxt" ))
    paytaxt1.place(x=320, y=530)
    recipe9 = Button(root_menu, bg='peachpuff1', activebackground='peachpuff1', image=recipe11, command=recipepaytaxt)
    recipe9.place(x=495, y=570)
    add_paytaxt = Label(root_menu, text='Paytaxt', fg='white', bg='grey18')
    add_paytaxt.place(x=857, y=640, width=200)
    count_paytaxt = Label(root_menu, text=0, fg='white', bg='grey18')
    count_paytaxt.place(x=1030, y=640)
    totaltextmenu = Label(root_menu, text='Total', font=13, bg='lightgrey')
    totaltextmenu.place(x=1090, y=230, width=80)
    totallabelmenu = Label(root_menu, text='', font=13, bg='lightgrey')
    totallabelmenu.place(x=1090, y=270, width=80)
    buymenu = Button(root_menu, text='Buy', font=13, bg='green', activebackground='green')
    buymenu.place(x=920,y=680, width=80)
    resetmenu = Button(root_menu, text='Reset', font=13, bg='red', activebackground='red')
    resetmenu.place(x=765, y=230, width=80)

    count_kabab["text"] = current_masa.orders["kabab"]

    root_menu.mainloop()

def open_budget():
    root_budget = Toplevel()
    root_budget.title("Budget")
    root_budget.geometry("1300x867+100+0")
    root_budget.resizable(False, False)

    budget1 = PhotoImage(file="Images/Budget.png")
    budget = Label(root_budget, bg='peachpuff1', image=budget1)
    budget.place(x=0, y=0)
    tittle1 = Label(root_budget,bg='dodgerblue4', text='Money in the budget', font=13, width=30, height=2)
    tittle1.place(x=40, y=40)
    tittle1 = Button(root_budget, bg='dodgerblue4',activebackground='dodgerblue4', text='10000', font=13)
    tittle1.place(x=400, y=46)
    root_budget.mainloop()

def warehouse():
    root_ware = Toplevel()
    root_ware.title("Warehouse")
    root_ware.geometry("1530x884+0+0")
    root_ware.resizable(False, False)

    warehouseback = PhotoImage(file="Images/warehouse.png")
    warehouse1 = Label(root_ware,bg='grey2', image=warehouseback)
    warehouse1.place(x=0, y=0)
    zeytunoilimage = PhotoImage(file="Images/zeytunyagi.png")
    zeytunoil1 = Label(root_ware, bg='lightgrey', activebackground='lightgrey', image=zeytunoilimage)
    zeytunoil1.place(x=55, y=120)
    zetuncount = Label(root_ware, text=120,font=10,bg='peachpuff1')
    zetuncount.place(x=90, y=210, height=20)
    merciimage = PhotoImage(file="Images/merci.png")
    merci1 = Label(root_ware, bg='lightgrey', activebackground='lightgrey', image=merciimage)
    merci1.place(x=183, y=120)
    mercicount = Label(root_ware, text=100, font=10, bg='peachpuff1')
    mercicount.place(x=197, y=210, height=20)
    duyuimage = PhotoImage(file="Images/duyu.png")
    duyu1 = Label(root_ware, bg='lightgrey', activebackground='lightgrey', image=duyuimage)
    duyu1.place(x=260, y=120)
    duyucount = Label(root_ware, text=85, font=10, bg='peachpuff1')
    duyucount.place(x=285, y=210, height=20)
    qatiqimage = PhotoImage(file="Images/qatiq.png")
    qatiq1 = Label(root_ware, bg='lightgrey', activebackground='lightgrey', image=qatiqimage)
    qatiq1.place(x=350, y=120)
    duzimage = PhotoImage(file="Images/duz.png")
    duz1 = Label(root_ware, bg='lightgrey', activebackground='lightgrey', image=duzimage)
    duz1.place(x=418, y=120)
    sekertozu11 = PhotoImage(file="Images/sekertozu.png")
    sekertozu1 = Label(root_ware, bg='lightgrey', activebackground='lightgrey', image=sekertozu11)
    sekertozu1.place(x=488, y=120)
    yumurtaimage = PhotoImage(file="Images/yumurta.png")
    yumurta1 = Label(root_ware, bg='lightgrey', activebackground='lightgrey', image=yumurtaimage)
    yumurta1.place(x=55, y=285)

    root_ware.mainloop()

def open_shop():
    root_shop = Toplevel()
    root_shop.title("Shop")
    root_shop.geometry("1500x938+0+0")
    root_shop.resizable(False, False)

    shopback1 = PhotoImage(file="Images/shop.png")
    shopback = Label(root_shop, image=shopback1)
    shopback.place(x=0, y=0)
    shop_shelf1 = PhotoImage(file="Images/shop shelf.png")
    shop_shelf = Label(root_shop, bg='lightgrey', image=shop_shelf1)
    shop_shelf.place(x=210, y=0)
    shop_mirror1 = PhotoImage(file="Images/shelfmirror.png")
    shop_mirror = Label(root_shop, bg='lightgrey', image=shop_mirror1)
    shop_mirror.place(x=775, y=0)
    zeytunoilimage = PhotoImage(file="Images/zeytunyagi.png")
    zeytunoil1 = Button(root_shop,bg='lightgrey', activebackground='lightgrey', image=zeytunoilimage, command=lambda: add_to_cart(zeytun_count,"zeytunyagi"))
    zeytunoil1.place(x=270, y=25)
    zeytun_label = Label(root_shop, text='Zeytun yagi', font=13,fg="black", bg='lightgrey')
    zeytun_label.place(x=860, y=215)
    zeytun_count = Label(root_shop, text=0, font=13, fg="black", bg='lightgrey')
    zeytun_count.place(x=1000, y=215)
    zeytun_price = Label(root_shop, text=10.59, font=13, fg="black")
    zeytun_price.place(x=300, y=117, height=15)
    zeytun_ceki = Label(root_shop, text='1 l', font=13, fg="black", bg='lightgrey')
    zeytun_ceki.place(x=1060, y=222, height=15)
    merciimage = PhotoImage(file="Images/merci.png")
    merci1 = Button(root_shop, bg='lightgrey', activebackground='lightgrey', image=merciimage, command=lambda: add_to_cart(merci_count,"merci"))
    merci1.place(x=397, y=25)
    merci_label = Label(root_shop, text='Merci', font=13, fg="black", bg='lightgrey')
    merci_label.place(x=860, y=245)
    merci_count = Label(root_shop, text=0, font=13, fg="black", bg='lightgrey')
    merci_count.place(x=1000, y=245)
    merci_price = Label(root_shop, text=3.75, font=13, fg="black")
    merci_price.place(x=408, y=117, height=15)
    merci_ceki = Label(root_shop, text='800 qr', font=13, fg="black", bg='lightgrey')
    merci_ceki.place(x=1060, y=247, height=22)
    duyuimage = PhotoImage(file="Images/duyu.png")
    duyu1 = Button(root_shop, bg='lightgrey', activebackground='lightgrey', image=duyuimage, command=lambda: add_to_cart(duyu_count,"duyu"))
    duyu1.place(x=470, y=25)
    duyu_label = Label(root_shop, text='Duyu', font=13, fg="black", bg='lightgrey')
    duyu_label.place(x=860, y=275)
    duyu_count = Label(root_shop, text=0, font=13, fg="black", bg='lightgrey')
    duyu_count.place(x=1000, y=275)
    duyu_price = Label(root_shop, text=4.65, font=13, fg="black")
    duyu_price.place(x=485, y=117, height=15)
    duyu_ceki = Label(root_shop, text='1 kq', font=13, fg="black", bg='lightgrey')
    duyu_ceki.place(x=1060, y=278, height=22)
    qatiqimage = PhotoImage(file="Images/qatiq.png")
    qatiq1 = Button(root_shop, bg='lightgrey', activebackground='lightgrey', image=qatiqimage, command=lambda: add_to_cart(qatiq_count,"qatiq"))
    qatiq1.place(x=560, y=25)
    qatiq_label = Label(root_shop, text='Qatiq', font=13, fg="black", bg='lightgrey')
    qatiq_label.place(x=860, y=305)
    qatiq_count = Label(root_shop, text=0, font=13, fg="black", bg='lightgrey')
    qatiq_count.place(x=1000, y=305)
    qatiq_price = Label(root_shop, text=3.40, font=13, fg="black")
    qatiq_price.place(x=572, y=117, height=15)
    qatiq_ceki = Label(root_shop, text='870 qr', font=13, fg="black", bg='lightgrey')
    qatiq_ceki.place(x=1060, y=308, height=22)
    duzimage = PhotoImage(file="Images/duz.png")
    duz1 = Button(root_shop, bg='lightgrey', activebackground='lightgrey', image=duzimage, command=lambda: add_to_cart(duz_count,"duz"))
    duz1.place(x=630, y=25)
    duz_label = Label(root_shop, text='Duz', font=13, fg="black", bg='lightgrey')
    duz_label.place(x=860, y=335)
    duz_count = Label(root_shop, text=0, font=13, fg="black", bg='lightgrey')
    duz_count.place(x=1000, y=335)
    duz_price = Label(root_shop, text=1.89, font=13, fg="black")
    duz_price.place(x=637, y=117, height=15)
    duz_ceki = Label(root_shop, text='3 kq', font=13, fg="black", bg='lightgrey')
    duz_ceki.place(x=1060, y=338, height=22)
    etimage = PhotoImage(file="Images/et.png")
    et1 = Button(root_shop, bg='lightgrey', activebackground='lightgrey', image=etimage, command=lambda: add_to_cart(et_count,"et"))
    et1.place(x=273, y=140)
    et_label = Label(root_shop, text='Et', font=13, fg="black", bg='lightgrey')
    et_label.place(x=860, y=365)
    et_price = Label(root_shop, text=17, font=13, fg="black")
    et_price.place(x=320, y=237, height=15)
    et_count = Label(root_shop, text=0, font=13, fg="black", bg='lightgrey')
    et_count.place(x=1000, y=365)
    et_ceki = Label(root_shop, text='1 kq', font=13, fg="black", bg='lightgrey')
    et_ceki.place(x=1060, y=368, height=22)
    sekertozu11 = PhotoImage(file="Images/sekertozu.png")
    sekertozu1 = Button(root_shop, bg='lightgrey', activebackground='lightgrey', image=sekertozu11, command=lambda: add_to_cart(seker_count,"seker tozu"))
    sekertozu1.place(x=415, y=140)
    seker_label = Label(root_shop, text='Seker tozu', font=13, fg="black", bg='lightgrey')
    seker_label.place(x=860, y=395)
    seker_count = Label(root_shop, text=0, font=13, fg="black", bg='lightgrey')
    seker_count.place(x=1000, y=395)
    seker_price = Label(root_shop, text=1.66, font=13, fg="black")
    seker_price.place(x=422, y=237, height=15)
    seker_ceki = Label(root_shop, text='700 qr', font=13, fg="black", bg='lightgrey')
    seker_ceki.place(x=1060, y=399, height=22)
    yumurtaimage = PhotoImage(file="Images/yumurta.png")
    yumurta1 = Button(root_shop, bg='lightgrey', activebackground='lightgrey', image=yumurtaimage, command=lambda: add_to_cart(yumurta_count,"yumurta"))
    yumurta1.place(x=490, y=140)
    yumurta_label = Label(root_shop, text='Yumurta', font=13, fg="black", bg='lightgrey')
    yumurta_label.place(x=860, y=425)
    yumurta_count = Label(root_shop, text=0, font=13, fg="black", bg='lightgrey')
    yumurta_count.place(x=1000, y=425)
    yumurta_price = Label(root_shop, text=20, font=13, fg="black")
    yumurta_price.place(x=530, y=237, height=15)
    yumurta_ceki = Label(root_shop, text='100 eded', font=13, fg="black", bg='lightgrey')
    yumurta_ceki.place(x=1060, y=428, height=22)
    mayonezimage = PhotoImage(file="Images/mayonez.png")
    mayonez1 = Button(root_shop, bg='lightgrey', activebackground='lightgrey', image=mayonezimage, command=lambda: add_to_cart(mayonez_count, "mayonez"))
    mayonez1.place(x=620, y=140)
    mayonez_label = Label(root_shop, text='Mayonez', font=13, fg="black", bg='lightgrey')
    mayonez_label.place(x=860, y=455)
    mayonez_count = Label(root_shop, text=0, font=13, fg="black", bg='lightgrey')
    mayonez_count.place(x=1000, y=455)
    mayonez_price = Label(root_shop, text=5.15, font=13, fg="black")
    mayonez_price.place(x=630, y=237, height=15)
    mayonez_ceki = Label(root_shop, text='800 qr', font=13, fg="black", bg='lightgrey')
    mayonez_ceki.place(x=1060, y=458, height=22)
    totaltextshop = Label(root_shop, text='Total', font=13, bg='lightgrey')
    totaltextshop.place(x=1300, y=560, width=80)
    totallabelshop = Label(root_shop, text='', font=13, bg='lightgrey')
    totallabelshop.place(x=1300, y=600, width=80)
    buyshop = Button(root_shop, text='Buy', font=13 ,bg='green', activebackground='green')
    buyshop.place(x=1300, y=650, width=80)
    resetshop = Button(root_shop, text='Reset', font=13, bg='red', activebackground='red')
    resetshop.place(x=1300, y=700, width=80)

    root_shop.mainloop()

root = Tk()
root.title("My Restaurant")
root.geometry("1528x780+0+0")
root.resizable(False, False)

backphotowin1 = PhotoImage(file="Images/stock-photo-texture-beige-color-paper-background.png")
table2_1 = PhotoImage(file="Images/Rec 2.png")
table2_2 = PhotoImage(file="Images/Rec 2.png")
table2_3 = PhotoImage(file="Images/Rec 2.png")
table2_4 = PhotoImage(file="Images/Rec 2.png")
table4_1 = PhotoImage(file="Images/Round 4.png")
table4_2 = PhotoImage(file="Images/Round 4.png")
table6_1 = PhotoImage(file="Images/Rec 6.png")
table6_2 = PhotoImage(file="Images/Rec 6.png")
kenar11 = PhotoImage(file="Images/635e9e0327dcbc383d0eb2b6-artiflr-6-ft-artificial-peony-garland - Köçür.png")
kenar22 = PhotoImage(file="Images/635e9e0327dcbc383d0eb2b6-artiflr-6-ft-artificial-peony-garland.png")
kenar33 = PhotoImage(file="Images/635e9e0327dcbc383d0eb2b6-artiflr-6-ft-artificial-peony-garland.png")
kenar44 = PhotoImage(file="Images/635e9e0327dcbc383d0eb2b6-artiflr-6-ft-artificial-peony-garland - Köçür.png")
plant11 = PhotoImage(file="Images/169-1691852_organic-quality-takes-time.png")
plant22 = PhotoImage(file="Images/169-1691852_organic-quality-takes-time.png")
kassa1 = PhotoImage(file="Images/Picsart_23-06-15_22-47-04-631.png")
warehouseimg = PhotoImage(file="Images/Picsart_23-06-15_23-01-47-610.png")
shop1 = PhotoImage(file="Images/Picsart_23-06-15_23-17-52-508.png")


back1 = Label(root,image= backphotowin1)
back1.place(x=0, y=0)
table2li_1 = Button(root, bg='peachpuff1', activebackground='peachpuff1',image= table2_1, command=lambda: open_plate("1"))
table2li_1.place(x=750, y=170)
table2li_2 = Button(root, bg='peachpuff1', activebackground='peachpuff1',image= table2_2, command=lambda: open_plate("2"))
table2li_2.place(x=1295, y=170)
table2li_3 = Button(root, bg='peachpuff1', activebackground='peachpuff1',image= table2_3, command=lambda: open_plate("3"))
table2li_3.place(x=750, y=490)
table2li_4 = Button(root, bg='peachpuff1', activebackground='peachpuff1',image= table2_4, command=lambda: open_plate("4"))
table2li_4.place(x=1295, y=490)
table4lu1 = Button(root, bg='peachpuff1', activebackground='peachpuff1',image= table4_1, command=lambda: open_plate("5"))
table4lu1.place(x=750, y=330)
table4lu2 = Button(root, bg='peachpuff1', activebackground='peachpuff1',image= table4_2, command=lambda: open_plate("6"))
table4lu2.place(x=1100, y=330)
table6li1 = Button(root, bg='peachpuff1', activebackground='peachpuff1',image= table6_1, command=lambda: open_plate("7"))
table6li1.place(x=900, y=330)
table6li2 = Button(root, bg='peachpuff1', activebackground='peachpuff1',image= table6_2, command=lambda: open_plate("8"))
table6li2.place(x=1250, y=330)
kassa = Button(root, bg='peachpuff1', activebackground='peachpuff1',image= kassa1, command= open_budget)
kassa.place(x=20, y=20)
warehouse = Button(root, bg='peachpuff1', activebackground='peachpuff1',image= warehouseimg, command= warehouse)
warehouse.place(x=20, y=560)
shop = Button(root, bg='peachpuff1', activebackground='peachpuff1',image= shop1, command=open_shop)
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
