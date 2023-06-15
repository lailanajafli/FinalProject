# Tapsiriq.


books = [{"Writer":"Xalid Huseyni", "Genre":"Roman", "release_date":"29.05.2003", "Nesriyyati":"Eli ve Nino","Sehife": 448}]

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
      new_book={}
      new_book["writer"] = input("Enter writer: ")
      new_book["genre"] = input("Enter genre: ")
      new_book["release_date"] = input("Enter release_date: ")
      new_book["nesriyyat"] = int(input("Enter nesriyyat: "))
      new_book["sehife"] = int(input("Enter sehife: "))
      books.append(new_book)

   elif option == '2':
      def delete_func(book, genre):
         if book["genre"] == genre:
            return book
      delete_book = "Roman"
      for i in list(filter(lambda x: delete_func(x, delete_book), books)):
         books.remove(i)
      print(books)

   elif option == '3':
      search = input("Axtarmaq istediyiniz melumati daxil edin:")
      for i in books:
         if search in i:
            print(i)
         else:
            print(" Siyahida bu adda melumat movcud deyil:")

   elif option == '4':
      option2 = input(" Deyisdirmek istediyiniz secimi daxil edin (1- buraxilis, 2 - page")

      if option2 == '1':
         writer = input("Enter writer:")
         new_release = int(input("Enter new release:"))
         for i in books:
            if i["writer"]==writer:
               i["release_date"] = new_release

      elif option2 == '2':
         writer = input("Enter writer:")
         new_page = int(input("Enter new page:"))
         for i in books:
            if i["writer"]==writer:
               i["page"] = new_page


   elif option == '5':
      break





















































































































