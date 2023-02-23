#!/usr/bin/env python3
#
#  [Program]
#
#  Password Manager
#
#  [Author]
#
#  Drew, https://github.com/Ahendrix9624/
#
#  [License]
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#  See 'LICENSE' for more information.

from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

#Constants 
USERNAME = "Ahendrix9624"
EMAIL = "Ahendrix9624@gmail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password = password_entry.get()
    
    if len(password) == 0:
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        password_list = []

        password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
        password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
        password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

        password_list = password_letters + password_numbers + password_symbols
        random.shuffle(password_list)

        password = "".join(password_list)
        password_entry.insert(END, string=f"{password}")
        pyperclip.copy(password)
    else:
        password_entry.delete(0, END)
        generate_password()

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email_username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: { 
            "Email/Username": email_username,
            "Password": password
        
    }
        }
    
    # Input Validation 
    if len(website) == 0 or len(password) == 0 or len(email_username) == 0:
        messagebox.showinfo(title="No input!", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Email/Username: {email_username} "
                                f"\nPassword: {password} \nIs it ok to save?") 
        
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                #Updating old data with new data
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    #Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()

# ----------------------------  FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(message="No Database File Found")
    else:
        if website in data:
            email = data[website]["Email/Username"]
            password = data[website]["Password"]
            messagebox.showinfo(title="Creds", message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showerror(title="Error", message=f"No credentials saved for {website}")

# ---------------------------- UI SETUP ------------------------------- #
#Building the window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#Image to background
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username: ")
username_label.grid(column=0, row=2)

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

#Entries
website_entry = Entry(width=21)
website_entry.focus()
username_entry = Entry(width=39)
password_entry = Entry(width=21)

#Add some text in entries
password_entry.insert(END, string="")
username_entry.insert(END, string=EMAIL)

#Gets entry on screen
website_entry.grid(column=1, row=1)
username_entry.grid(column=1, row=2, columnspan=2)
password_entry.grid(column=1, row=3)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

search_button = Button(text="Search", command=find_password, width=13)
search_button.grid(column=2, row=1)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

#Keeps the program window running
window.mainloop()