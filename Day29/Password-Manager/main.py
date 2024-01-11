from tkinter import *

FONT_NAME = "Salsa"
LABEL_WIDTH = 15
# data_count = 1
# with open("data-count.txt", 'w') as count_file:
#     count_file.write(str(data_count))


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    try:
        with open("data-count.txt") as file:
            count = int(file.read())
    except:
        count = 1

    with open('data.txt', 'a') as password_file:
        content = f"""Entry {count}:
---------
Website: {website_entry.get()}
Email/Username: {email_entry.get()}
Website URL: {url_entry.get()}
Password: {password_entry.get()}

"""
        password_file.write(content)
    count += 1

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
