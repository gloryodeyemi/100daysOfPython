from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

FONT_NAME = "Salsa"
LABEL_WIDTH = 15


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)  # copy password to clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # get entries
    website = website_entry.get()
    email = email_entry.get()
    url = url_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "url": url,
            "password": password,
        }
    }

    # validation
    if len(website) == 0 or len(url) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror(title="Missing details", message="Input field cannot be empty!")
    elif '@' not in email or '.com' not in email:
        messagebox.showerror(title="Invalid email", message="Email is not valid!")
    else:
        try:
            with open('data.json', 'r') as password_file:
                data = json.load(password_file)  # read old data
                data.update(new_data)  # update with new data
        except FileNotFoundError:
            with open('data.json', 'w') as password_file:
                json.dump(new_data, password_file, indent=4)  # create json file and write to file
        else:
            with open('data.json', 'w') as password_file:
                json.dump(data, password_file, indent=4)  # write updated data to file

        # clear entries
        website_entry.delete(0, END)
        url_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", anchor="e", justify=RIGHT, font=(FONT_NAME, 12, "bold"), width=LABEL_WIDTH)
website_label.config(padx=10, pady=0)
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", anchor="e", justify=RIGHT, font=(FONT_NAME, 12, "bold"), width=LABEL_WIDTH)
email_label.config(padx=10, pady=0)
email_label.grid(row=2, column=0)

url_label = Label(text="Website URL:", anchor="e", justify=RIGHT, font=(FONT_NAME, 12, "bold"), width=LABEL_WIDTH)
url_label.config(padx=10, pady=0)
url_label.grid(row=3, column=0)

password_label = Label(text="Password:", anchor="e", justify=RIGHT, font=(FONT_NAME, 12, "bold"), width=LABEL_WIDTH)
password_label.config(padx=10, pady=0)
password_label.grid(row=4, column=0)

# Entries
website_entry = Entry(width=37)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=37)
email_entry.insert(0, 'test123@gmail.com')
email_entry.grid(row=2, column=1, columnspan=2)

url_entry = Entry(width=37)
url_entry.grid(row=3, column=1, columnspan=2)

password_entry = Entry(width=22)
password_entry.grid(row=4, column=1)

# Buttons
generate_button = Button(text="Generate Password", command=generate_password, width=11, font=(FONT_NAME, 12, "bold"))
generate_button.grid(row=4, column=2)

add_button = Button(text="Add", command=save, width=34, font=(FONT_NAME, 12, "bold"))
add_button.grid(row=5, column=1, columnspan=2)

window.mainloop()
