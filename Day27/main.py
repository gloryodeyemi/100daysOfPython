from tkinter import *


# button
def button_clicked():
    print("I got clicked.")
    my_label["text"] = my_input.get()


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label["text"] = "New Text"
my_label.config(text="Another Text")
my_label.pack()

button = Button(text="Click me", command=button_clicked)
button.pack()

# entry
my_input = Entry(width=10)
print(my_input.get())
my_input.pack()

window.mainloop()
