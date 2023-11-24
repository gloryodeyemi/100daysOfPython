from tkinter import *


# convert miles to km
def convert():
    miles = miles_input.get()
    km = round(int(miles) * 1.60934, 2)
    km_value_label.config(text=km)


# window configuration
converter_window = Tk()
converter_window.title("Mile to Km Converter")
converter_window.minsize(width=300, height=100)
converter_window.config(padx=50, pady=20)

# miles entry configuration
miles_input = Entry(width=10)
miles_input.insert(END, string="0")
miles_input.grid(column=1, row=0)

# miles label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# equal label
equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

# km value label
km_value_label = Label(text="0")
km_value_label.grid(column=1, row=1)

# km label
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# calculate button
calc_button = Button(text="Calculate", command=convert)
calc_button.grid(column=1, row=2)

converter_window.mainloop()
