from tkinter import *

FONT_NAME = "Salsa"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass


# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", font=(FONT_NAME, 12, "bold"))
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", font=(FONT_NAME, 12, "bold"))
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", font=(FONT_NAME, 12, "bold"))
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=37)
website_entry.grid(row=1, column=1, columnspan=2)

email_entry = Entry(width=37)
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=22)
password_entry.grid(row=3, column=1)

# Buttons
generate_button = Button(text="Generate Password", command=generate_password, width=11, font=(FONT_NAME, 12, "bold"))
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", command=generate_password, width=34, font=(FONT_NAME, 12, "bold"))
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
