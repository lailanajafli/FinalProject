from tkinter import *
import re
from tkinter import ttk
text = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
when an unknown printer took a galley of type and scrambled it to make a type
specimen book. It has survived not only five centuries, but also the leap into
electronic typesetting, remaining essentially unchanged. It was popularised in
the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,
and more recently with desktop publishing software like Aldus PageMaker including
versions of Lorem Ipsum."""
def windowEdit():
    def undo():
        edit_text.edit_undo()
    def redo():
        edit_text.edit_redo()
    def save():
        global text
        text = edit_text.get("1.0", "end")
        text1.delete("1.0", "end")
        text1.insert("1.0", text)
    def on_modified(event):
        counter1["text"] = len(edit_text.get("1.0", END))-1
        counter2["text"] = len(re.findall('\w+', edit_text.get("1.0", END)))
    global text
    window = Toplevel()
    window.title("Edit TEXT")
    window.geometry("1200x750")
    edit_text = Text(master=window, undo=True, font=13)
    edit_text.place(height=230, x=280, y=200)
    edit_text.bind("<KeyRelease>", on_modified)
    edit_text.insert('1.0', text)
    button_redo = Button(master=window, text="Redo", bg='indianred3', fg='black', font=13, command=redo)
    button_redo.place(x=600, y=450, width=90, height=50)
    button_undo = Button(master=window, text="Undo", bg='hotpink4', fg='black', font=13, command=undo)
    button_undo.place(x=700, y=450, width=90, height=50)
    button_save = Button(master=window, text="Save", bg='hotpink', fg='black', font=13, command=save)
    button_save.place(x=800, y=450, width=90, height=50)
    sym_counter = Label(master=window, text="Symbol counter:", bg="cadetblue1", fg="black", font=25)
    sym_counter.place(x=250, y=600)
    word_counter = Label(master=window, text="Word counter:", bg="cadetblue1", fg="black", font=25)
    word_counter.place(x=250, y=650)
    counter1 = Label(master=window, fg="black", font=25)
    counter1.place(x=430, y=600)
    counter2 = Label(master=window, fg="black", font=25)
    counter2.place(x=430, y=650)
    window.grab_set()

root = Tk()
root.title("TEXT")
root.geometry("1200x750")
text1 = Text(master=root, fg="black", font=25)
text1.place(x=250, y=200, height=230)
text1.insert("1.0", text)
text1.bind("<Key>", lambda e: "break")
button_edit = Button(master=root, text="Edit", bg='pink', fg='black', font=13, command= windowEdit)
button_edit.place(x=630, y=450, width=90, height=50)
root.mainloop()