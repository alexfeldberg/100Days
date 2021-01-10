from tkinter import *

CONVERSION_RATE = 1.609


def calculate():
    miles = float(usr_input.get())
    km = miles * CONVERSION_RATE
    km_num.config(text=km)
    pass


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)
anchor_labor = Label()
anchor_labor.grid(column=0, row=0)

# Entry
usr_input = Entry(width=5)
usr_input.grid(column=1, row=0)

# Label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

km_num = Label(text="   0")
km_num.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Button
my_button = Button(text="Calculate", command=calculate)
my_button.grid(column=1, row=2)

window.mainloop()
