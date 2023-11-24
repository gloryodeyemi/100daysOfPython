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
# my_label.pack(side="left")

button = Button(text="Click me", command=button_clicked)
button.place(x=0, y=0)  # precise positioning

# entry
my_input = Entry(width=10)
print(my_input.get())
my_input.grid(column=5, row=5)

window.mainloop()
