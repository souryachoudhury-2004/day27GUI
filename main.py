from tkinter import *

window = Tk()
window.title("My first GUI program.")
window.minsize(width=500, height=300)

my_label = Label(text="This is a label.", font=("Arial", 24, "italic"))
my_label.pack(side="top")


def click():
    value = input.get()
    my_label.config(text=value)


button = Button(text="Click me!", command=click)
button.pack()

input = Entry(width=10)
input.pack()




window.mainloop()