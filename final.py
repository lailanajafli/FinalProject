from tkinter import *
import pickle

class Food:
    def __init__(self, price):
        self.price = price
        self.count = 0
    def __str__(self):
        return str(self.count)
class Product:
    def __init__(self, price, warehouse):
        self.price = price
        #self.warehouse = warehouse
        self.count = 0
        self.warehouse = 0
    def __str__(self):
        return str(self.count)

class Masa:
    def __init__(self):
        self.orders = {"kabab": Food(20), "lahmacun": Food(3.20), "toyuq doner": Food(3.84), "xengel": Food(8.50), "merci": Food(3.20), "plov": Food(10),
                       "dovga": Food(4), "kartof fri": Food(4.50), "pizza": Food(8.40), "pide": Food(8.80), "paytaxt": Food(5), "mimoza": Food(5.50),
                       "su": Food(1.50), "cola": Food(1.98)}
        self.total_price = 0

class Database:
    def __init__(self):
        self.tables = {"1": Masa(), "2": Masa(), "3": Masa(), "4": Masa(), "5": Masa(), "6": Masa(), "7": Masa(), "8": Masa()}
        self.products = {"zeytunyagi": Product(10.59, 70), "merci": Product(3.75, 50), "qatiq": Product(3.4, 52), "duz": Product(1.89, 60), "sogan": Product(1.66, 20), "toyuq file": Product(5.15, 40),
                          "yumurta": Product(20, 150), "duyu": Product(4.65, 85), "corek": Product(1, 30), "pendir": Product(4.70, 112), "et": Product(17, 20), "mayonez": Product(5.15, 70), "kartof": Product(1.10, 30),
                         "badimcan": Product(2.29, 20), "pomidor": Product(1.79, 20), "kok": Product(1.09, 20), "goyerti": Product(3.10, 120), "xemir": Product(6.85, 20)}


database = Database()

total_shop = 0
totallabelshop = None
total_money = 10000
total_food_price = 0

def click_reset(totallabelshop, product_label_list):
    global total_shop
    total_shop = 0
    totallabelshop.config(text=str(total_shop))

    for label in product_label_list:
        label["text"] = "0"

    for key in database.products.keys():
        database.products[key].count = 0

def click_buy():
    global money, total_money
    total_money -= total_shop
    try:
        money.config(text=str(total_money))
    except:
        pass


def menu_reset(total_label, count_label_list, current_masa):
    global total_food_price
    total_label.config(text="0")
    total_food_price = 0

    for label in count_label_list:
        label["text"]  = "0"

    for key, value in current_masa.orders.items():
        current_masa.orders[key].count = 0


def buy_menu(current_masa):
    global money, total_money

    for key in current_masa.orders.keys():
        total_money += current_masa.orders[key].count * current_masa.orders[key].price


    try:
        money.config(text=str(total_money))
    except:
        pass

def add_to_cart(label, product, totallabelshop):
    global total_shop
    database.products[product].count += 1
    label["text"] = database.products[product].count
    total_product_price = 0

    for key in database.products.keys():
        total_product_price += database.products[key].count * database.products[key].price
    totallabelshop["text"] = str(total_product_price)
    total_shop = total_product_price

def total_price(total, label_total):
    global money,total_money
    label_total.config(text = str(total))


def add_order(table, order, label, label_total):
    database.tables[table].orders[order].count += 1
    label["text"] = database.tables[table].orders[order].count

    total = 0
    for key, value in database.tables[table].orders.items():
        total += database.tables[table].orders[key].count * database.tables[table].orders[key].price

    total_price(total, label_total)


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
    krecipe = Label(root_recipe1, text='Kabab Recipe', bg='grey18', image=kababrecipe)
    krecipe.place(x=40, y=20)
    kababname = Label(root_recipe1, text='Kabab:', font=13, fg="white", bg='grey18')
    kababname.place(x=100, y=155)
    kabab_product = Label(root_recipe1, text='Et\nPomidor\nBadimcan\nDuz', font=13, fg="white", bg='grey18')
    kabab_product.place(x=40, y=200, width=185, height=120)

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
    lrecipe = Label(root_recipe1, text='Lahnacun Recipe', bg='grey18', activebackground='grey18', image=lahmacunrecipe)
    lrecipe.place(x=40, y=20)
    lahmacunname = Label(root_recipe1, text='Lahmacun:', font=13, fg="white", bg='grey18')
    lahmacunname.place(x=80, y=155)
    lahmacun_product = Label(root_recipe1, text='Et\nXemir\Pomidor\nGoyerti\nDuz', font=13, fg="white", bg='grey18')
    lahmacun_product.place(x=40, y=210, width=185, height=120)

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
    drecipe = Label(root_recipe1, text='Toyuq doner Recipe', bg='grey18', activebackground='grey18', image=donerrecipe)
    drecipe.place(x=40, y=20)
    donername = Label(root_recipe1, text='Toyuq doner:', font=13, fg="white", bg='grey18')
    donername.place(x=70, y=160)
    doner_product = Label(root_recipe1, text='Corek\nEt\nMayonez\nToyuq file\nPomidor\nGoyerti\nDuz', font=13, fg="white", bg='grey18')
    doner_product.place(x=40, y=210, width=185, height=170)

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
    xrecipe = Label(root_recipe1, text='Xengel Recipe', bg='grey18', activebackground='grey18', image=xengelrecipe)
    xrecipe.place(x=40, y=35)
    xengelname = Label(root_recipe1, text='Xengel:', font=13, fg="white", bg='grey18')
    xengelname.place(x=90, y=145)
    doner_product = Label(root_recipe1, text='Xemir\nEt\nDuz\nQatiq', font=13, fg="white", bg='grey18')
    doner_product.place(x=40, y=210, width=185, height=120)

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
    mrecipe = Label(root_recipe1, text='Merci Recipe', bg='grey18', activebackground='grey18', image=mercirecipe)
    mrecipe.place(x=40, y=30)
    merciname = Label(root_recipe1, text='Merci sorbasi:', font=13, fg="white", bg='grey18')
    merciname.place(x=65, y=155)
    merci_product = Label(root_recipe1, text='Merci\nKok\nPomidor\nZeytun yagi\nCorek\nDuz', font=13, fg="white", bg='grey18')
    merci_product.place(x=40, y=210, width=185, height=150)

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
    precipe = Label(root_recipe1, text='Plov Recipe', bg='grey18', activebackground='grey18', image=plovrecipe)
    precipe.place(x=40, y=33)
    plovname = Label(root_recipe1, text='PLov:', font=13, fg="white", bg='grey18')
    plovname.place(x=100, y=140)
    plov_product = Label(root_recipe1, text='Duyu\nToyuq\nYumurta\nQatiq\nDuz', font=13, fg="white", bg='grey18')
    plov_product.place(x=40, y=210, width=185, height=140)

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
    drecipe = Label(root_recipe1, text='Dovga Recipe', bg='grey18', activebackground='grey18', image=dovgarecipe)
    drecipe.place(x=40, y=20)
    dovganame = Label(root_recipe1, text='Dovga:', font=13, fg="white", bg='grey18')
    dovganame.place(x=80, y=152)
    dovga_product = Label(root_recipe1, text='Qatiq\nGoyerti\nYumurta\nDuyu\nDuz', font=13, fg="white", bg='grey18')
    dovga_product.place(x=40, y=210, width=185, height=125)

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
    krecipe = Label(root_recipe1, text='Kartof fri Recipe', bg='grey18', activebackground='grey18', image=kartofrirecipe)
    krecipe.place(x=40, y=20)
    kartofname = Label(root_recipe1, text='Kartof fri:', font=13, fg="white", bg='grey18')
    kartofname.place(x=80, y=152)
    kartofri_product = Label(root_recipe1, text='Kartof\nZeytun yagi\nDuz', font=13, fg="white", bg='grey18')
    kartofri_product.place(x=40, y=210, width=185, height=120)

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
    precipe = Label(root_recipe1, text='Pizza Recipe', bg='grey18', activebackground='grey18', image=pizzarecipe)
    precipe.place(x=40, y=20)
    pizzaname = Label(root_recipe1, text='Pizza:', font=13, fg="white", bg='grey18')
    pizzaname.place(x=95, y=152)
    pizza_product = Label(root_recipe1, text='Xemir\nToyuq file\nPomidor\nDuz\nPendir', font=13, fg="white", bg='grey18')
    pizza_product.place(x=40, y=210, width=185, height=130)

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
    piderecipe = Label(root_recipe1, text='Pide Recipe', bg='grey18', activebackground='grey18', image=piderecipe1)
    piderecipe.place(x=40, y=20)
    pidename = Label(root_recipe1, text='Pide:', font=13, fg="white", bg='grey18')
    pidename.place(x=95, y=152)
    pizza_product = Label(root_recipe1, text='Xemir\nEt\nPomidor\nDuz\nPendir\nYumurta', font=13, fg="white",bg='grey18')
    pizza_product.place(x=40, y=210, width=185, height=130)

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
    paytaxtrecipe = Label(root_recipe1, text='Paytaxt Recipe', bg='grey18', activebackground='grey18', image=payrecipe1)
    paytaxtrecipe.place(x=40, y=30)
    paytaxtname = Label(root_recipe1, text='Paytaxt salati:', font=13, fg="white", bg='grey18')
    paytaxtname.place(x=53, y=150)
    paytaxt_product = Label(root_recipe1, text='Toyuq\nEt\nPomidor\nDuz\nPendir\nYumurta', font=13, fg="white", bg='grey18')
    paytaxt_product.place(x=40, y=210, width=185, height=130)

    root_recipe1.mainloop()

def recipemimoza():
    root_recipe1 = Toplevel()
    root_recipe1.title("Mimoza salati recipe")
    root_recipe1.geometry("1000x562+250+150")
    root_recipe1.resizable(False, False)

    recipeback1 = PhotoImage(file="Images/recipeback.png")
    recipeback = Label(root_recipe1, bg='peachpuff1', image=recipeback1)
    recipeback.place(x=0, y=0)
    mirecipe1 = PhotoImage(file="Images/mimoza.png")
    mimozarecipe = Label(root_recipe1, text='Mimoza Recipe', bg='grey18', image=mirecipe1)
    mimozarecipe.place(x=40, y=30)
    mimozaname = Label(root_recipe1, text='Mimoza salati:', font=13, fg="white", bg='grey18')
    mimozaname.place(x=50, y=163)
    mimoza_product = Label(root_recipe1, text='Toyuq\nEt\nPomidor\nDuz\nPendir\nYumurta', font=13, fg="white", bg='grey18')
    mimoza_product.place(x=40, y=210, width=185, height=130)

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
    kabab = Button(root_menu, text='Kabab',bg='grey18', activebackground='grey18',image=kabab1, command=lambda: add_order(table_number,"kabab",count_kabab, totallabelmenu))
    kabab.place(x=20, y=30)
    recipe11 = PhotoImage(file="Images/recipe.png")
    kababprice = Label(root_menu, text='20 azn',bg='grey20', font=10)
    kababprice.place(x=215, y=40, height=37)
    recipe1 = Button(root_menu,bg='peachpuff1', activebackground='peachpuff1', image=recipe11, command=recipekab)
    recipe1.place(x=215, y=85)
    add_kabab = Label(root_menu, text='Kabab', fg='white', bg='grey18')
    add_kabab.place(x=857, y=470, width=200)
    count_kabab = Label(root_menu, text=0, fg='white', bg='grey18')
    count_kabab.place(x=1030, y=470)
    lahmacun1 = PhotoImage(file="Images/lahmacun.png")
    lahmacun = Button(root_menu, text='Lahmacun', bg='grey18', activebackground='grey18', image=lahmacun1, command=lambda: add_order(table_number,"lahmacun",count_lahmacun, totallabelmenu))
    lahmacun.place(x=20, y=164)
    lahmacunprice = Label(root_menu, text='3.20 azn', bg='grey20', font=10)
    lahmacunprice.place(x=215, y=170, height=37)
    recipe2 = Button(root_menu, bg='peachpuff1', activebackground='peachpuff1', image=recipe11, command=recipelahmacun)
    recipe2.place(x=215, y=215)
    add_lahmacun = Label(root_menu, text='Lahmacun', fg='white', bg='grey18')
    add_lahmacun.place(x=857, y=487, width=200)
    count_lahmacun = Label(root_menu, text=0, fg='white', bg='grey18')
    count_lahmacun.place(x=1030, y=487)
    toyuqdoner1 = PhotoImage(file="Images/toyuqdoner.png")
    toyuqdoner = Button(root_menu, text='Toyuq doner', bg='grey18', activebackground='grey18', image=toyuqdoner1, command=lambda: add_order(table_number,"toyuq doner",count_doner, totallabelmenu))
    toyuqdoner.place(x=20, y=294)
    donerprice = Label(root_menu, text='3.84 azn', bg='grey20', font=10)
    donerprice.place(x=215, y=310, height=37)
    recipe3 = Button(root_menu, bg='peachpuff1', activebackground='peachpuff1', image=recipe11, command=recipedoner)
    recipe3.place(x=215, y=357)
    add_doner = Label(root_menu, text='Toyuq doner', fg='white', bg='grey18')
    add_doner.place(x=857, y=504, width=200)
    count_doner = Label(root_menu, text=0, fg='white', bg='grey18')
    count_doner.place(x=1030, y=504)
    xengel1 = PhotoImage(file="Images/xengel.png")
    xengel = Button(root_menu, text='Xengel', bg='grey18', activebackground='grey18', image=xengel1, command=lambda: add_order(table_number,"xengel",count_xengel, totallabelmenu))
    xengel.place(x=20, y=439)
    xengelprice = Label(root_menu, text='8.50 azn', bg='grey20', font=10)
    xengelprice.place(x=215, y=438, height=37)
    recipe4 = Button(root_menu, bg='peachpuff1', activebackground='peachpuff1', image=recipe11, command=recipexengel)
    recipe4.place(x=215, y=480, height=50)
    add_xengel = Label(root_menu, text='Xengel', fg='white', bg='grey18')
    add_xengel.place(x=857, y=521, width=200)
    count_xengel = Label(root_menu, text=0, fg='white', bg='grey18')
    count_xengel.place(x=1030, y=521)
    mercisorbasi1 = PhotoImage(file="Images/mercisorbasi.png")
    mercisorbasi = Button(root_menu, text='Merci sorbasi', bg='grey18', activebackground='grey18', image=mercisorbasi1, command=lambda: add_order(table_number,"merci",count_merci, totallabelmenu))
    mercisorbasi.place(x=20, y=549)
    merciprice = Label(root_menu, text='3.20 azn', bg='grey20', font=10)
    merciprice.place(x=215, y=555, height=37)
    recipe5 = Button(root_menu, bg='peachpuff1', activebackground='peachpuff1', image=recipe11, command=recipemerci)
    recipe5.place(x=215, y=598)
    add_merci = Label(root_menu, text='Merci sorbasi', fg='white', bg='grey18')
    add_merci.place(x=857, y=538, width=200)
    count_merci = Label(root_menu, text=0, fg='white', bg='grey18')
    count_merci.place(x=1030, y=538)
    plovimage = PhotoImage(file="Images/plov.png")
    plov1 = Button(root_menu, text='Plov', bg='grey18', activebackground='grey18', image=plovimage, command=lambda: add_order(table_number,"plov",count_plov, totallabelmenu))
    plov1.place(x=20, y=674)
    plovprice = Label(root_menu, text='10 azn', bg='grey20', font=10)
    plovprice.place(x=215, y=670, height=37)
    recipe6 = Button(root_menu, bg='peachpuff1', activebackground='peachpuff1', image=recipe11, command=recipeplov)
    recipe6.place(x=215, y=715, height=50)
    add_plov = Label(root_menu, text='Plov', fg='white', bg='grey18')
    add_plov.place(x=857, y=555, width=200)
    count_plov = Label(root_menu, text=0, fg='white', bg='grey18')
    count_plov.place(x=1030, y=555)
    dovga1 = PhotoImage(file="Images/dovga.png")
    dovga = Button(root_menu, text='Dovga', bg='grey18', activebackground='grey18', image=dovga1, command=lambda: add_order(table_number,"dovga",count_dovga, totallabelmenu))
    dovga.place(x=320, y=30)
    dovgaprice = Label(root_menu, text='4 azn', bg='grey20', font=10)
    dovgaprice.place(x=495, y=40, height=37)
    recipe7 = Button(root_menu, bg='peachpuff1', activebackground='peachpuff1', image=recipe11, command=recipedovga)
    recipe7.place(x=495, y=90)
    add_dovga = Label(root_menu, text='Dovga', fg='white', bg='grey18')
    add_dovga.place(x=857, y=572, width=200)
    count_dovga = Label(root_menu, text=0, fg='white', bg='grey18')
    count_dovga.place(x=1030, y=572)
    kartofri11 = PhotoImage(file="Images/kartofri.png")
    kartofri1 = Button(root_menu, bg='grey18', activebackground='grey18', image=kartofri11, command=lambda: add_order(table_number,"kartof fri",count_kartof, totallabelmenu))
    kartofri1.place(x=320, y=166)
    kartofprice = Label(root_menu, text='4.50 azn', bg='grey20', font=10)
    kartofprice.place(x=495, y=168, height=37)
    recipe8 = Button(root_menu, bg='peachpuff1', activebackground='peachpuff1', image=recipe11, command=recipekartofri)
    recipe8.place(x=495, y=215, height=51)
    add_kartofri = Label(root_menu, text='Kartof fri', fg='white', bg='grey18')
    add_kartofri.place(x=857, y=589, width=200)
    count_kartof = Label(root_menu, text=0, fg='white', bg='grey18')
    count_kartof.place(x=1030, y=589)
    pizzaimage = PhotoImage(file="Images/pizza.png")
    pizza1 = Button(root_menu, bg='grey18', activebackground='grey18', image=pizzaimage, command=lambda: add_order(table_number,"pizza",count_pizza, totallabelmenu))
    pizza1.place(x=320, y=288)
    pizzaprice = Label(root_menu, text='8.40 azn', bg='grey20', font=10)
    pizzaprice.place(x=495, y=288, height=37)
    recipe9 = Button(root_menu, bg='peachpuff1', activebackground='peachpuff1', image=recipe11, command=recipepizza)
    recipe9.place(x=495, y=337)
    add_pizza = Label(root_menu, text='Pizza', fg='white', bg='grey18')
    add_pizza.place(x=857, y=606, width=200)
    count_pizza = Label(root_menu, text=0, fg='white', bg='grey18')
    count_pizza.place(x=1030, y=606)
    pideimage = PhotoImage(file="Images/pide.png")
    pide1 = Button(root_menu, bg='grey18', activebackground='grey18', image=pideimage, command=lambda: add_order(table_number,"pide",count_pide, totallabelmenu))
    pide1.place(x=320, y=410)
    pideprice = Label(root_menu, text='8.80 azn', bg='grey20', font=10)
    pideprice.place(x=495, y=410, height=37)
    recipe10 = Button(root_menu, bg='peachpuff1', activebackground='peachpuff1', image=recipe11, command=recipepide)
    recipe10.place(x=495, y=458, height=52)
    add_pide = Label(root_menu, text='Pide', fg='white', bg='grey18')
    add_pide.place(x=857, y=623, width=200)
    count_pide = Label(root_menu, text=0, fg='white', bg='grey18')
    count_pide.place(x=1030, y=623)
    paytaxtimage = PhotoImage(file="Images/paytaxt.png")
    paytaxt1 = Button(root_menu, bg='grey18', activebackground='grey18', image=paytaxtimage, command=lambda: add_order(table_number,"paytaxt",count_paytaxt, totallabelmenu))
    paytaxt1.place(x=320, y=530)
    paytaxtprice = Label(root_menu, text='5 azn', bg='grey20', font=10)
    paytaxtprice.place(x=495, y=530, height=37)
    recipee11 = Button(root_menu, bg='peachpuff1', activebackground='peachpuff1', image=recipe11, command=recipepaytaxt)
    recipee11.place(x=495, y=576, height=52)
    add_paytaxt = Label(root_menu, text='Paytaxt', fg='white', bg='grey18')
    add_paytaxt.place(x=857, y=640, width=200)
    count_paytaxt = Label(root_menu, text=0, fg='white', bg='grey18')
    count_paytaxt.place(x=1030, y=640)
    mimozaimage = PhotoImage(file="Images/mimoza.png")
    mimoza1 = Button(root_menu, bg='grey18', activebackground='grey18', image=mimozaimage, command=lambda: add_order(table_number, "mimoza", count_mimoza, totallabelmenu))
    mimoza1.place(x=320, y=645)
    mimozaprice = Label(root_menu, text='5.50 azn', bg='grey20', font=10)
    mimozaprice.place(x=495, y=655, height=37)
    recipe12 = Button(root_menu, bg='peachpuff1', activebackground='peachpuff1', image=recipe11, command=recipemimoza)
    recipe12.place(x=495, y=702, height=52)
    add_mimoza = Label(root_menu, text='Mimoza', fg='white', bg='grey18')
    add_mimoza.place(x=857, y=657, width=200)
    count_mimoza = Label(root_menu, text=0, fg='white', bg='grey18')
    count_mimoza.place(x=1030, y=657)
    suimage = PhotoImage(file="Images/su.png")
    su1 = Button(root_menu, bg='grey18', activebackground='grey18', image=suimage, command=lambda: add_order(table_number, "su", count_su, totallabelmenu))
    su1.place(x=650, y=10)
    suprice = Label(root_menu, text='1.50 azn', bg='grey20', font=10)
    suprice.place(x=720, y=80, height=37)
    add_su = Label(root_menu, text='Su', fg='white', bg='grey18')
    add_su.place(x=857, y=674, width=200)
    count_su = Label(root_menu, text=0, fg='white', bg='grey18')
    count_su.place(x=1030, y=674)
    colaimage = PhotoImage(file="Images/cola.png")
    cola1 = Button(root_menu, bg='grey18', activebackground='grey18', image=colaimage, command=lambda: add_order(table_number, "cola", count_cola, totallabelmenu))
    cola1.place(x=840, y=10)
    colaprice = Label(root_menu, text='1.98 azn', bg='grey20', font=10)
    colaprice.place(x=910, y=80, height=37)
    add_cola = Label(root_menu, text='Cola', fg='white', bg='grey18')
    add_cola.place(x=857, y=691, width=200)
    count_cola = Label(root_menu, text=0, fg='white', bg='grey18')
    count_cola.place(x=1030, y=691)
    totaltextmenu = Label(root_menu, text='Total', font=13, bg='lightgrey')
    totaltextmenu.place(x=1090, y=230, width=80)
    totallabelmenu = Label(root_menu, text='', font=13, bg='lightgrey')
    totallabelmenu.place(x=1090, y=270, width=80)
    buymenu = Button(root_menu, text='Buy', font=13, bg='green', activebackground='green', command= lambda : buy_menu(current_masa))
    buymenu.place(x=920,y=715, width=75, height=30)
    resetmenu = Button(root_menu, text='Reset', font=13, bg='red', activebackground='red', command= lambda : menu_reset(totallabelmenu, count_label_list, current_masa))
    resetmenu.place(x=765, y=230, width=80)

    count_kabab["text"] = current_masa.orders["kabab"]
    count_lahmacun["text"] = current_masa.orders["lahmacun"]
    count_doner["text"] = current_masa.orders["toyuq doner"]
    count_xengel["text"] = current_masa.orders["xengel"]
    count_merci["text"] = current_masa.orders["merci"]
    count_plov["text"] = current_masa.orders["plov"]
    count_dovga["text"] = current_masa.orders["dovga"]
    count_merci["text"] = current_masa.orders["merci"]
    count_kartof["text"] = current_masa.orders["kartof fri"]
    count_pizza["text"] = current_masa.orders["pizza"]
    count_pide["text"] = current_masa.orders["pide"]
    count_paytaxt["text"] = current_masa.orders["paytaxt"]
    count_mimoza["text"] = current_masa.orders["mimoza"]
    count_su["text"] = current_masa.orders["su"]
    count_cola["text"] = current_masa.orders["cola"]

    count_label_list = [
        count_kabab,
        count_lahmacun,
        count_doner,
        count_xengel,
        count_merci,
        count_plov,
        count_dovga,
        count_merci,
        count_kartof,
        count_pizza,
        count_pide,
        count_paytaxt,
        count_mimoza,
        count_su,
        count_cola
    ]

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
    money = Label(root_budget, bg='dodgerblue4',activebackground='dodgerblue4', text=str(total_money), font=13)
    money.place(x=400, y=50)
    root_budget.mainloop()

def warehouse():
    root_ware = Toplevel()
    root_ware.title("Warehouse")
    root_ware.geometry("1530x1020+0+0")
    root_ware.resizable(False, False)

    warehouseback = PhotoImage(file="Images/warehouse.png")
    warehouse1 = Label(root_ware,bg='grey2', image=warehouseback)
    warehouse1.place(x=0, y=0)
    warehouseshelf1 = PhotoImage(file="Images/warehouseshelf.png")
    warehouseshelf = Label(root_ware, bg='silver', image=warehouseshelf1)
    warehouseshelf.place(x=350, y=100)
    zeytunoilimage = PhotoImage(file="Images/zeytunyagi.png")
    zeytunoil1 = Label(root_ware, bg='silver',image=zeytunoilimage)
    zeytunoil1.place(x=420, y=200)
    zetuncount = Label(root_ware, text=70,font=10,bg='peachpuff1')
    zetuncount.place(x=459, y=285, height=20)
    merciimage = PhotoImage(file="Images/merci.png")
    merci1 = Label(root_ware, bg='silver',image=merciimage)
    merci1.place(x=543, y=200)
    mercicount = Label(root_ware, text=50, font=10, bg='peachpuff1')
    mercicount.place(x=554, y=285, height=20)
    qatiqimage = PhotoImage(file="Images/qatiq.png")
    qatiq1 = Label(root_ware, bg='silver', image=qatiqimage)
    qatiq1.place(x=765, y=200)
    qatiqcount = Label(root_ware, text=52, font=10, bg='peachpuff1')
    qatiqcount.place(x=780, y=285, height=20)
    duzimage = PhotoImage(file="Images/duz.png")
    duz1 = Label(root_ware, bg='silver', image=duzimage)
    duz1.place(x=832, y=200)
    duzcount = Label(root_ware, text=60, font=10, bg='peachpuff1')
    duzcount.place(x=842, y=285, height=20)
    soganimage = PhotoImage(file="Images/sogan.png")
    sogan1 = Label(root_ware, bg='silver', image=soganimage)
    sogan1.place(x=420, y=541)
    sogancount = Label(root_ware, text=20, font=10, bg='peachpuff1')
    sogancount.place(x=433, y=647, height=20)
    fileimage = PhotoImage(file="Images/toyuq file.png")
    file1 = Label(root_ware, bg='silver', image=fileimage)
    file1.place(x=970, y=205)
    filecount = Label(root_ware, text=40, font=10, bg='peachpuff1')
    filecount.place(x=990, y=285, height=20)
    yumurtaimage = PhotoImage(file="Images/yumurta.png")
    yumurta1 = Label(root_ware, bg='silver', image=yumurtaimage)
    yumurta1.place(x=425, y=375)
    yumurtacount = Label(root_ware, text=150, font=10, bg='peachpuff1')
    yumurtacount.place(x=465, y=466, height=20)
    duyuimage = PhotoImage(file="Images/duyu.png")
    duyu1 = Label(root_ware, bg='silver', image=duyuimage)
    duyu1.place(x=660, y=375)
    duyucount = Label(root_ware, text=85, font=10, bg='peachpuff1')
    duyucount.place(x=683, y=466, height=20)
    corekimage = PhotoImage(file="Images/corek.png")
    corek1 = Label(root_ware, bg='silver', image=corekimage)
    corek1.place(x=550, y=375)
    corekcount = Label(root_ware, text=30, font=10, bg='peachpuff1')
    corekcount.place(x=585, y=466, height=20)
    pendirimage = PhotoImage(file="Images/pendir.png")
    pendir1 = Label(root_ware, bg='silver', image=pendirimage)
    pendir1.place(x=612, y=205)
    pendircount = Label(root_ware, text=112, font=10, bg='peachpuff1')
    pendircount.place(x=650, y=285, height=20)
    etimage = PhotoImage(file="Images/et.png")
    et1 = Label(root_ware, bg='silver', image=etimage)
    et1.place(x=785, y=377)
    etcount = Label(root_ware, text=20, font=10, bg='peachpuff1')
    etcount.place(x=835, y=467, height=20)
    mayonezimage = PhotoImage(file="Images/mayonez.png")
    mayonez1 = Label(root_ware, bg='silver', image=mayonezimage)
    mayonez1.place(x=900, y=202)
    mayonezcount = Label(root_ware, text=70, font=10, bg='peachpuff1')
    mayonezcount.place(x=910, y=285, height=20)
    kartofimage = PhotoImage(file="Images/kartof.png")
    kartof1 = Label(root_ware, bg='silver', image=kartofimage)
    kartof1.place(x=617, y=543)
    kartofcount = Label(root_ware, text=30, font=10, bg='peachpuff1')
    kartofcount.place(x=650, y=647, height=20)
    badimcanimage = PhotoImage(file="Images/badimcan.png")
    badimcan1 = Label(root_ware, bg='silver', image=badimcanimage)
    badimcan1.place(x=500, y=541)
    badimcancount = Label(root_ware, text=20, font=10, bg='peachpuff1')
    badimcancount.place(x=530, y=647, height=20)
    pomidorimage = PhotoImage(file="Images/pomidor.png")
    pomidor1 = Label(root_ware, bg='silver', image=pomidorimage)
    pomidor1.place(x=780, y=541)
    pomidorcount = Label(root_ware, text=20, font=10, bg='peachpuff1')
    pomidorcount.place(x=815, y=647, height=20)
    kokimage = PhotoImage(file="Images/kok.png")
    kok1 = Label(root_ware, bg='silver', image=kokimage)
    kok1.place(x=930, y=541)
    kokcount = Label(root_ware, text=20, font=10, bg='peachpuff1')
    kokcount.place(x=970, y=647, height=20)
    goyertiimage = PhotoImage(file="Images/goyerti.png")
    goyerti1 = Label(root_ware, bg='silver', image=goyertiimage)
    goyerti1.place(x=935, y=380)
    goyerticount = Label(root_ware, text=120, font=10, bg='peachpuff1')
    goyerticount.place(x=977, y=467, height=20)

    root_ware.mainloop()

def open_shop():
    global totallabelshop
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
    zeytunoil1 = Button(root_shop,bg='lightgrey', activebackground='lightgrey', image=zeytunoilimage, command=lambda: add_to_cart(zeytun_count,"zeytunyagi", totallabelshop))
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
    merci1 = Button(root_shop, bg='lightgrey', activebackground='lightgrey', image=merciimage, command=lambda: add_to_cart(merci_count,"merci", totallabelshop))
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
    duyu1 = Button(root_shop, bg='lightgrey', activebackground='lightgrey', image=duyuimage, command=lambda: add_to_cart(duyu_count,"duyu", totallabelshop))
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
    qatiq1 = Button(root_shop, bg='lightgrey', activebackground='lightgrey', image=qatiqimage, command=lambda: add_to_cart(qatiq_count,"qatiq", totallabelshop))
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
    duz1 = Button(root_shop, bg='lightgrey', activebackground='lightgrey', image=duzimage, command=lambda: add_to_cart(duz_count,"duz", totallabelshop))
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
    et1 = Button(root_shop, bg='lightgrey', activebackground='lightgrey', image=etimage, command=lambda: add_to_cart(et_count,"et", totallabelshop))
    et1.place(x=273, y=140)
    et_label = Label(root_shop, text='Et', font=13, fg="black", bg='lightgrey')
    et_label.place(x=860, y=365)
    et_price = Label(root_shop, text=17, font=13, fg="black")
    et_price.place(x=320, y=237, height=15)
    et_count = Label(root_shop, text=0, font=13, fg="black", bg='lightgrey')
    et_count.place(x=1000, y=365)
    et_ceki = Label(root_shop, text='1 kq', font=13, fg="black", bg='lightgrey')
    et_ceki.place(x=1060, y=368, height=22)
    sogan11 = PhotoImage(file="Images/sogan.png")
    sogan1 = Button(root_shop, bg='lightgrey', activebackground='lightgrey', image=sogan11, command=lambda: add_to_cart(sogan_count,"sogan", totallabelshop))
    sogan1.place(x=415, y=140)
    sogan_label = Label(root_shop, text='Sogan', font=13, fg="black", bg='lightgrey')
    sogan_label.place(x=860, y=395)
    sogan_count = Label(root_shop, text=0, font=13, fg="black", bg='lightgrey')
    sogan_count.place(x=1000, y=395)
    sogan_price = Label(root_shop, text=1.66, font=13, fg="black")
    sogan_price.place(x=422, y=237, height=15)
    sogan_ceki = Label(root_shop, text='1 kq', font=13, fg="black", bg='lightgrey')
    sogan_ceki.place(x=1060, y=399, height=22)
    yumurtaimage = PhotoImage(file="Images/yumurta.png")
    yumurta1 = Button(root_shop, bg='lightgrey', activebackground='lightgrey', image=yumurtaimage, command=lambda: add_to_cart(yumurta_count,"yumurta", totallabelshop))
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
    mayonez1 = Button(root_shop, bg='lightgrey', activebackground='lightgrey', image=mayonezimage, command=lambda: add_to_cart(mayonez_count, "mayonez", totallabelshop))
    mayonez1.place(x=620, y=140)
    mayonez_label = Label(root_shop, text='Mayonez', font=13, fg="black", bg='lightgrey')
    mayonez_label.place(x=860, y=455)
    mayonez_count = Label(root_shop, text=0, font=13, fg="black", bg='lightgrey')
    mayonez_count.place(x=1000, y=455)
    mayonez_price = Label(root_shop, text=5.15, font=13, fg="black")
    mayonez_price.place(x=630, y=237, height=15)
    mayonez_ceki = Label(root_shop, text='800 qr', font=13, fg="black", bg='lightgrey')
    mayonez_ceki.place(x=1060, y=458, height=22)
    kartofimage = PhotoImage(file="Images/kartof.png")
    kartof1 = Button(root_shop, bg='lightgrey', activebackground='lightgrey', image=kartofimage, command=lambda: add_to_cart(kartof_count, "kartof", totallabelshop))
    kartof1.place(x=300, y=264)
    kartof_label = Label(root_shop, text='Kartof', font=13, fg="black", bg='lightgrey')
    kartof_label.place(x=860, y=485)
    kartof_count = Label(root_shop, text=0, font=13, fg="black", bg='lightgrey')
    kartof_count.place(x=1000, y=485)
    kartof_price = Label(root_shop, text=1.10, font=13, fg="black")
    kartof_price.place(x=335, y=357, height=15)
    kartof_ceki = Label(root_shop, text='1 kq', font=13, fg="black", bg='lightgrey')
    kartof_ceki.place(x=1060, y=488, height=22)
    fileimage = PhotoImage(file="Images/toyuq file.png")
    file1 = Button(root_shop, bg='lightgrey', activebackground='lightgrey', image=fileimage, command=lambda: add_to_cart(file_count, "toyuq file", totallabelshop))
    file1.place(x=415, y=264)
    file_label = Label(root_shop, text='Toyuq filesi', font=13, fg="black", bg='lightgrey')
    file_label.place(x=860, y=515)
    file_count = Label(root_shop, text=0, font=13, fg="black", bg='lightgrey')
    file_count.place(x=1000, y=515)
    file_price = Label(root_shop, text=5.15, font=13, fg="black")
    file_price.place(x=432, y=357, height=15)
    file_ceki = Label(root_shop, text='800 qr', font=13, fg="black", bg='lightgrey')
    file_ceki.place(x=1060, y=518, height=22)
    pomidorimage = PhotoImage(file="Images/pomidor.png")
    pomidor1 = Button(root_shop, bg='lightgrey', activebackground='lightgrey', image=pomidorimage, command=lambda: add_to_cart(pomidor_count, "pomidor", totallabelshop))
    pomidor1.place(x=508, y=264)
    pomidor_label = Label(root_shop, text='Pomidor', font=13, fg="black", bg='lightgrey')
    pomidor_label.place(x=860, y=545)
    pomidor_count = Label(root_shop, text=0, font=13, fg="black", bg='lightgrey')
    pomidor_count.place(x=1000, y=545)
    pomidor_price = Label(root_shop, text=1.79, font=13, fg="black")
    pomidor_price.place(x=545, y=357, height=15)
    pomidor_ceki = Label(root_shop, text='1 kq', font=13, fg="black", bg='lightgrey')
    pomidor_ceki.place(x=1060, y=548, height=22)
    kokimage = PhotoImage(file="Images/kok.png")
    kok1 = Button(root_shop, bg='lightgrey', activebackground='lightgrey', image=kokimage, command=lambda: add_to_cart(kok_count, "kok", totallabelshop))
    kok1.place(x=270, y=387)
    kok_label = Label(root_shop, text='Kok', font=13, fg="black", bg='lightgrey')
    kok_label.place(x=860, y=575)
    kok_count = Label(root_shop, text=0, font=13, fg="black", bg='lightgrey')
    kok_count.place(x=1000, y=575)
    kok_price = Label(root_shop, text=1.09, font=13, fg="black")
    kok_price.place(x=305, y=480, height=15)
    kok_ceki = Label(root_shop, text='1 kq', font=13, fg="black", bg='lightgrey')
    kok_ceki.place(x=1060, y=578, height=22)
    badimcanimage = PhotoImage(file="Images/badimcan.png")
    badimcan1 = Button(root_shop, bg='lightgrey', activebackground='lightgrey', image=badimcanimage, command=lambda: add_to_cart(badimcan_count, "badimcan", totallabelshop))
    badimcan1.place(x=400, y=387)
    badimcan_label = Label(root_shop, text='Badimcan', font=13, fg="black", bg='lightgrey')
    badimcan_label.place(x=860, y=605)
    badimcan_count = Label(root_shop, text=0, font=13, fg="black", bg='lightgrey')
    badimcan_count.place(x=1000, y=605)
    badimcan_price = Label(root_shop, text=2.29, font=13, fg="black")
    badimcan_price.place(x=430, y=480, height=15)
    badimcan_ceki = Label(root_shop, text='1 kq', font=13, fg="black", bg='lightgrey')
    badimcan_ceki.place(x=1060, y=608, height=22)
    goyertiimage = PhotoImage(file="Images/goyerti.png")
    goyerti1 = Button(root_shop, bg='lightgrey', activebackground='lightgrey', image=goyertiimage, command=lambda: add_to_cart(goyerti_count, "goyerti", totallabelshop))
    goyerti1.place(x=515, y=387)
    goyerti_label = Label(root_shop, text='Goyerti', font=13, fg="black", bg='lightgrey')
    goyerti_label.place(x=860, y=635)
    goyerti_count = Label(root_shop, text=0, font=13, fg="black", bg='lightgrey')
    goyerti_count.place(x=1000, y=635)
    goyerti_price = Label(root_shop, text=3.10, font=13, fg="black")
    goyerti_price.place(x=555, y=480, height=15)
    goyerti_ceki = Label(root_shop, text='10 eded', font=13, fg="black", bg='lightgrey')
    goyerti_ceki.place(x=1060, y=638, height=22)
    pendirimage = PhotoImage(file="Images/pendir.png")
    pendir1 = Button(root_shop, bg='lightgrey', activebackground='lightgrey', image=pendirimage, command=lambda: add_to_cart(pendir_count, "pendir", totallabelshop))
    pendir1.place(x=280, y=512)
    pendir_label = Label(root_shop, text='Pendir', font=13, fg="black", bg='lightgrey')
    pendir_label.place(x=860, y=662)
    pendir_count = Label(root_shop, text=0, font=13, fg="black", bg='lightgrey')
    pendir_count.place(x=1000, y=662)
    pendir_price = Label(root_shop, text=4.70, font=13, fg="black")
    pendir_price.place(x=320, y=604, height=15)
    pendir_ceki = Label(root_shop, text='250 qr', font=13, fg="black", bg='lightgrey')
    pendir_ceki.place(x=1060, y=665, height=22)
    corekimage = PhotoImage(file="Images/corek.png")
    corek1 = Button(root_shop, bg='lightgrey', activebackground='lightgrey', image=corekimage, command=lambda: add_to_cart(corek_count, "corek", totallabelshop))
    corek1.place(x=415, y=512)
    corek_label = Label(root_shop, text='Corek', font=13, fg="black", bg='lightgrey')
    corek_label.place(x=860, y=688)
    corek_count = Label(root_shop, text=0, font=13, fg="black", bg='lightgrey')
    corek_count.place(x=1000, y=688)
    corek_price = Label(root_shop, text=1, font=13, fg="black")
    corek_price.place(x=465, y=604, height=15)
    corek_ceki = Label(root_shop, text='1 eded', font=13, fg="black", bg='lightgrey')
    corek_ceki.place(x=1060, y=691, height=22)
    xemirimage = PhotoImage(file="Images/xemir.png")
    xemir1 = Button(root_shop, bg='lightgrey', activebackground='lightgrey', image=xemirimage, command=lambda: add_to_cart(xemir_count, "xemir", totallabelshop))
    xemir1.place(x=550, y=512)
    xemir_label = Label(root_shop, text='Xemir', font=13, fg="black", bg='lightgrey')
    xemir_label.place(x=860, y=715)
    xemir_count = Label(root_shop, text=0, font=13, fg="black", bg='lightgrey')
    xemir_count.place(x=1000, y=715)
    xemir_price = Label(root_shop, text=6.85, font=13, fg="black")
    xemir_price.place(x=590, y=604, height=15)
    xemir_ceki = Label(root_shop, text='1 kq', font=13, fg="black", bg='lightgrey')
    xemir_ceki.place(x=1060, y=718, height=22)
    totaltextshop = Label(root_shop, text='Total', font=13, bg='lightgrey')
    totaltextshop.place(x=1300, y=560, width=80)
    totallabelshop = Label(root_shop, text='', font=13, bg='lightgrey')
    totallabelshop.place(x=1300, y=600, width=80)
    buyshop = Button(root_shop, text='Buy', font=13 ,bg='green', activebackground='green', command = click_buy)
    buyshop.place(x=1300, y=650, width=80)
    product_count_list = [
        zeytun_count,
        merci_count,
        duyu_count,
        qatiq_count,
        duz_count,
        et_count,
        sogan_count,
        yumurta_count,
        mayonez_count,
        kartof_count,
        file_count,
        pomidor_count,
        kok_count,
        badimcan_count,
        goyerti_count,
        pendir_count,
        corek_count,
        xemir_count
    ]
    resetshop = Button(root_shop, text='Reset', font=13, bg='red', activebackground='red', command = lambda : click_reset(totallabelshop, product_count_list))
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
