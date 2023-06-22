from tkinter import *
import pickle


class Database:
    def __init__(self):
        self.products = {"zeytunyagi": 0, "merci": 0, "duyu": 0, "qatiq": 0, "duz": 0, "et": 0, "sekertozu": 0}

database = Database()
def add_to_cart(label, product):
    database.products[product] += 1
    label["text"] = database.products[product]

def open_plate():
    root_plate = Toplevel()
    root_plate.title("Plate")
    root_plate.geometry("1200x770+150+0")
    root_plate.resizable(False, False)

    plate11 = PhotoImage(file="Images/plate.png")
    plate1 = Label(root_plate, bg='peachpuff1', image=plate11)
    plate1.place(x=0, y=0)
    menu11 = PhotoImage(file="Images/menu.png")
    menu1 = Button(root_plate, bg='peachpuff1', activebackground='peachpuff1', image=menu11, command=open_menu)
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



def open_menu():
    root_menu = Toplevel()
    root_menu.title("Menu")
    root_menu.geometry("1520x855")
    root_menu.resizable(False, False)

    menuback1 = PhotoImage(file="Images/menuback.png")
    menu = Label(root_menu, bg='peachpuff1', image=menuback1)
    menu.place(x=0, y=0)
    menuman1 = PhotoImage(file="Images/menuman.png")
    menuman = Label(root_menu, bg='grey18', image=menuman1)
    menuman.place(x=750, y=200)
    kabab1 = PhotoImage(file="Images/kabab.png")
    kabab = Button(root_menu, text='Kabab',bg='grey18', activebackground='grey18',image=kabab1)
    kabab.place(x=20, y=30)
    recipe11 = PhotoImage(file="Images/recipe.png")
    recipe1 = Button(root_menu,bg='peachpuff1', activebackground='peachpuff1', image=recipe11, command=recipekab)
    recipe1.place(x=215, y=57)
    lahmacun1 = PhotoImage(file="Images/lahmacun.png")
    lahmacun = Button(root_menu, text='Lahmacun', bg='grey18', activebackground='grey18', image=lahmacun1)
    lahmacun.place(x=20, y=164)
    recipe2 = Button(root_menu, bg='peachpuff1', activebackground='peachpuff1', image=recipe11, command=recipelahmacun)
    recipe2.place(x=215, y=189)
    toyuqdoner1 = PhotoImage(file="Images/toyuqdoner.png")
    toyuqdoner = Button(root_menu, text='Toyuq doner', bg='grey18', activebackground='grey18', image=toyuqdoner1)
    toyuqdoner.place(x=20, y=294)
    recipe3 = Button(root_menu, bg='peachpuff1', activebackground='peachpuff1', image=recipe11, command=recipedoner)
    recipe3.place(x=215, y=331)
    xengel1 = PhotoImage(file="Images/xengel.png")
    xengel = Button(root_menu, text='Xengel', bg='grey18', activebackground='grey18', image=xengel1)
    xengel.place(x=20, y=439)
    recipe4 = Button(root_menu, bg='peachpuff1', activebackground='peachpuff1', image=recipe11, command=recipexengel)
    recipe4.place(x=215, y=454)
    mercisorbasi1 = PhotoImage(file="Images/mercisorbasi.png")
    mercisorbasi = Button(root_menu, text='Merci sorbasi', bg='grey18', activebackground='grey18', image=mercisorbasi1)
    mercisorbasi.place(x=20, y=549)
    recipe5 = Button(root_menu, bg='peachpuff1', activebackground='peachpuff1', image=recipe11, command=recipemerci)
    recipe5.place(x=215, y=574)
    dovga1 = PhotoImage(file="Images/dovga.png")
    dovga = Button(root_menu, text='Dovga', bg='grey18', activebackground='grey18', image=dovga1)
    dovga.place(x=320, y=30)
    recipe6 = Button(root_menu, bg='peachpuff1', activebackground='peachpuff1', image=recipe11, command=recipedovga)
    recipe6.place(x=495, y=59)
    plovimage = PhotoImage(file="Images/plov.png")
    plov1 = Button(root_menu, text='Plov', bg='grey18', activebackground='grey18', image=plovimage)
    plov1.place(x=20, y=674)
    recipe7 = Button(root_menu, bg='peachpuff1', activebackground='peachpuff1', image=recipe11, command=recipeplov)
    recipe7.place(x=215, y=685)
    kartofri11 = PhotoImage(file="Images/kartofri.png")
    kartofri1 = Button(root_menu, bg='grey18', activebackground='grey18', image=kartofri11)
    kartofri1.place(x=320, y=166)
    recipe8 = Button(root_menu, bg='peachpuff1', activebackground='peachpuff1', image=recipe11, command=recipekartofri)
    recipe8.place(x=495, y=189)
    pizzaimage = PhotoImage(file="Images/pizza.png")
    pizza1 = Button(root_menu, bg='grey18', activebackground='grey18', image=pizzaimage)
    pizza1.place(x=320, y=288)
    recipe9 = Button(root_menu, bg='peachpuff1', activebackground='peachpuff1', image=recipe11, command=recipepizza)
    recipe9.place(x=495, y=310)
    totaltext = Label(root_menu, text='Total', font=13, bg='lightgrey')
    totaltext.place(x=1300, y=560, width=80)
    totallabel = Label(root_menu, text='', font=13, bg='lightgrey')
    totallabel.place(x=1300, y=600, width=80)
    buy = Button(root_menu, text='Buy', font=13, bg='green', activebackground='green')
    buy.place(x=1300, y=650, width=80)
    reset = Button(root_menu, text='Reset', font=13, bg='red', activebackground='red')
    reset.place(x=1300, y=700, width=80)

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
    merci1 = Button(root_shop, bg='lightgrey', activebackground='lightgrey', image=merciimage)
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
    duyu1 = Button(root_shop, bg='lightgrey', activebackground='lightgrey', image=duyuimage)
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
    qatiq1 = Button(root_shop, bg='lightgrey', activebackground='lightgrey', image=qatiqimage)
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
    duz1 = Button(root_shop, bg='lightgrey', activebackground='lightgrey', image=duzimage)
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
    et1 = Button(root_shop, bg='lightgrey', activebackground='lightgrey', image=etimage)
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
    sekertozu1 = Button(root_shop, bg='lightgrey', activebackground='lightgrey', image=sekertozu11)
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
    yumurta1 = Button(root_shop, bg='lightgrey', activebackground='lightgrey', image=yumurtaimage)
    yumurta1.place(x=490, y=140)
    yumurta_label = Label(root_shop, text='Yumurta', font=13, fg="black", bg='lightgrey')
    yumurta_label.place(x=860, y=425)
    yumurta_count = Label(root_shop, text=0, font=13, fg="black", bg='lightgrey')
    yumurta_count.place(x=1000, y=425)
    yumurta_price = Label(root_shop, text=20, font=13, fg="black")
    yumurta_price.place(x=530, y=237, height=15)
    yumurta_ceki = Label(root_shop, text='100 eded', font=13, fg="black", bg='lightgrey')
    yumurta_ceki.place(x=1060, y=428, height=22)
    totaltext = Label(root_shop, text='Total', font=13, bg='lightgrey')
    totaltext.place(x=1300, y=560, width=80)
    totallabel = Label(root_shop, text='', font=13, bg='lightgrey')
    totallabel.place(x=1300, y=600, width=80)
    buy = Button(root_shop, text='Buy', font=13 ,bg='green', activebackground='green')
    buy.place(x=1300, y=650, width=80)
    reset = Button(root_shop, text='Reset', font=13, bg='red', activebackground='red')
    reset.place(x=1300, y=700, width=80)


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
table2li_1 = Button(root, bg='peachpuff1', activebackground='peachpuff1',image= table2_1, command=open_plate)
table2li_1.place(x=750, y=170)
table2li_2 = Button(root, bg='peachpuff1', activebackground='peachpuff1',image= table2_2, command=open_plate)
table2li_2.place(x=1295, y=170)
table2li_3 = Button(root, bg='peachpuff1', activebackground='peachpuff1',image= table2_3, command=open_plate)
table2li_3.place(x=750, y=490)
table2li_4 = Button(root, bg='peachpuff1', activebackground='peachpuff1',image= table2_4, command=open_plate)
table2li_4.place(x=1295, y=490)
table4lu1 = Button(root, bg='peachpuff1', activebackground='peachpuff1',image= table4_1, command=open_plate)
table4lu1.place(x=750, y=330)
table4lu2 = Button(root, bg='peachpuff1', activebackground='peachpuff1',image= table4_2, command=open_plate)
table4lu2.place(x=1100, y=330)
table6li1 = Button(root, bg='peachpuff1', activebackground='peachpuff1',image= table6_1, command=open_plate)
table6li1.place(x=900, y=330)
table6li2 = Button(root, bg='peachpuff1', activebackground='peachpuff1',image= table6_2, command=open_plate)
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
