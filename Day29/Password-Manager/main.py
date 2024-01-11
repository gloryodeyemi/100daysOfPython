from tkinter import *
from tkinter import messagebox
import random

FONT_NAME = "Salsa"
LABEL_WIDTH = 15


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_list = [random.choice(letters) for _ in range(nr_letters)]
password_list += [random.choice(symbols) for _ in range(nr_symbols)]
password_list += [random.choice(numbers) for _ in range(nr_numbers)]

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # read password count from file
    try:
        with open("data-count.txt") as file:
            count = int(file.read())
    except:
        count = 0

    # get entries
    website = website_entry.get()
    email = email_entry.get()
    url = url_entry.get()
    password = password_entry.get()

    # validation
    if len(website) == 0 or len(url) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror(title="Missing details", message="Input field cannot be empty!")
    elif '@' not in email or '.com' not in email:
        messagebox.showerror(title="Invalid email", message="Email is not valid!")
    else:
        # save confirmation
        is_ok = messagebox.askokcancel(title=f"{website}", message=f"Confirm details:\nEmail/Username: {email}\n"
                                                                   f"Website URL: {url}\nPassword: {password}\n"
                                                                   f"Proceed to save?")

        if is_ok:
            # write password content to data file
            count += 1
            with open('data.txt', 'a') as password_file:
                content = (f"Entry {count}:\n---------\nWebsite: {website}\nEmail/Username: {email}\nWebsite URL: {url}"
                           f"\nPassword: {password}\n")
                password_file.write(content)

            # update the password count in the file
            with open("data-count.txt", 'w') as count_file:
                count_file.write(str(count))

            # clear entries
            website_entry.delete(0, 'end')
            url_entry.delete(0, 'end')
            password_entry.delete(0, 'end')


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
