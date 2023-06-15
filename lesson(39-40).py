'''
emekdaslar = [{"name":"1", "surname":"Memmedov", "position":"Direktor", "phone":"+994502223344","room": 201},{"name":"Vasif", "surname":"Memmedov", "position":"Programmer", "phone":"+994502223344","room": 201},{"name":"3", "surname":"Memmedov", "position":"Programmer", "phone":"+994502223344","room": 201},{"name":"4", "surname":"Memmedov", "position":"Programmer", "phone":"+994502223344","room": 201}]

menu = """
            Elave et =>      1
            Sil =>           2
            Tap =>           3
            Deyisdir =>      4
            Cixis =>         5
"""

while True:
   print(menu)
   option = input('Seçim daxil edin: ')
   if option == '1':
      yeni_emekdas={}
      yeni_emekdas["name"] = input("Enter name: ")
      yeni_emekdas["surname"] = input("Enter surname: ")
      emekdaslar.append(yeni_emekdas)

   elif option == '2':
      def silmek_func(emekdas, position):
         if emekdas["position"] == position:
            return emekdas
      delete_emekdas = "Programmer"
      for i in list(filter(lambda x: silmek_func(x, delete_emekdas), emekdaslar)):
         emekdaslar.remove(i)
      print(emekdaslar)

   # Axtaris
   elif option == '3':
      search = input("Axtarmaq istediyiniz melumati daxil edin:")
      for i in emekdaslar:
         if search in i:
            print(i)
         else:
            print(" Siyahida bu adda olke movcud deyil:")


# Edit  #Adnan axtaris -> deyismek lazimdi: phone, room
   elif option == '4':
      option2 = input(" Deyisdirmek istediyiniz secimi daxil edin (1- phone, 2 - room")

      if option2 == '1':
         name = input("Ad daxil edin:")
         new_phone = "0557555555"
         for i in emekdaslar:
            if i["name"]==name:
               i["phone"] = new_phone

      elif option2 == '2':
         name = input("Ad daxil edin:")
         new_room = "200"
         for i in emekdaslar:
            if i["name"]==name:
               i["room"] = new_room


   elif option == '5':
      break
'''


from tkinter import *
# math, random
from tkinter import messagebox

def func():
   messagebox.showinfo("Say Hello", "Hello World")
root = Tk()                                         # Tk() pencere yaradir
root.title("Program 1")                             # Pencerenin adi
root.iconbitmap(default="apple.ico")
root.geometry("600x250+300+300")                    # Pencerenin width x height
root.resizable(True, True)
root.minsize(300, 150)
root.maxsize(800, 400)
label = Label(text="Hello METANIT.COM", foreground="red", default="apple.ico") # Labelin yaradilmasi
label.pack()
# photo = PhotoImage(file = "apple.png")
btn = Button(text="Click me!", command=func, width=100, height=100)
btn.pack()
root.mainloop()    #Pəncərəni göstərmək və istifadəçi ilə qarşılıqlı əlaqə yaratmaq üçün pəncərədə mainloop() metodu adlanır






























# Add
# yeni_emekdas={}
# yeni_emekdas["name"] = input("Enter name: ")
# yeni_emekdas["surname"] = input("Enter surname: ")
# emekdaslar.append(yeni_emekdas)


# list1 = ["John", "James", "Bob"]
# list1.remove("James")
# print(list1)

































