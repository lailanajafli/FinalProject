from tkinter import *
root = Tk()
root.title("METANIT.COM")
root.geometry("1000x1500")



image1 = PhotoImage(file ="dxml55nt.png")
image2 = PhotoImage(file ="Images/Rec 2.png")

job5 = Label(master=root,bd=5, image=image1, font=1)
job5.place(x=0, y=0)
gg = Button(master=root,bd=5, image=image2, font=1)
gg.place(x=500, y=600)

# Position image

root.mainloop()