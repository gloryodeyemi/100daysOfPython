from tkinter import *


# button function
def button_clicked():
    print("I got clicked.")
    my_label["text"] = my_input.get()


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label["text"] = "New Text"
my_label.config(text="Another Text")
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)

# button
button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

# new button
button2 = Button(text="New button", command=button_clicked)
button2.grid(column=2, row=0)

# entry
my_input = Entry(width=10)
print(my_input.get())
my_input.grid(column=3, row=2)

window.mainloop()
