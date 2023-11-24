from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="Another Text")


# button
def button_clicked():
    my_label["text"] = my_input.get()
    # print("I got clicked.")


button = Button(text="Click me", command=button_clicked)
button.pack()

# entry
my_input = Entry()
my_input.pack()
# print(my_input.get())

window.mainloop()
