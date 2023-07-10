from tkinter import *

def converter():

    miles = mile_input.get()
    try:
        miles = float(miles)
        kilometres = 1.60934*miles
        kilometres = str(round(kilometres, 2))
        output.config(text=f"Distance in kilometres: {kilometres} km")
    except ValueError:
        output.config(text="Please enter a valid numeric value!")

screen = Tk()
screen.title("Mile to Kilometre Converter")
screen.minsize(width=500, height=300)

label = Label(text="Enter distance in miles: ", font=("Gabriola", 22, "bold"))
label.pack()

mile_input = Entry(width=20)
mile_input.pack(pady=15)

mile_label = Label(text="miles", font=("Gabriola", 18, "bold"))
mile_label.place(x=330, y=62)

convert_button = Button(text="Calculate", font=("Times New Roman", 15, "bold"), command=converter, height=1, width=10)
convert_button.pack()

output = Label(font=("Gabriola", 20, "bold"))
output.pack()


screen.mainloop()