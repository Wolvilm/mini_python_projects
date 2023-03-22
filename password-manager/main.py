from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        have_website = messagebox.showerror(title=website, message="Please enter a website and password")

    else:
        # is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nWebsite: {website}\n Email: {email}"
        #                                                       f"\nPassword: {password} \n Is it ok to save?")

        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# --------------------------------------- SEARCH PASSWORD ----------------------------------#

def find_password():
    website_to_search = website_entry.get()

    try:
        with open("data.json", 'r') as datafile:
            creds = json.load(datafile)

    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No Data file found")

    else:
        for website in creds:
            email = creds[website]["email"]
            password = creds[website]["password"]

            if website_to_search not in creds.keys():
                messagebox.showinfo(title="Oops", message="No details for the website exists")
                break

            elif website_to_search == website:
                messagebox.showinfo(title=f"Website:  {website}", message=f"Email:  {email}\n Password:  {password}")
                pyperclip.copy(password)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=300, pady=300)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# website entry
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)
website_entry = Entry(width=33)
website_entry.focus()
website_entry.grid(column=1, row=1)
search_button = Button(text="Search", command=find_password, width=14)
search_button.grid(column=2, row=1)

# email/username entry
email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)
email_entry = Entry(width=52)
email_entry.insert(0, "xyz@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

# Password entry
password_label = Label(text="Password: ")
password_label.grid(column=0, row=3, padx=20)
password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)
gen_password_button = Button(text="Generate Password", command=generate_password)
gen_password_button.grid(column=2, row=3)

# add button
add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
