from tkinter import *
from tkinter import messagebox
import random
import pyperclip

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
    
    # Input Validation 
    if len(website) == 0 or len(password) == 0 or len(email_username) == 0:
        messagebox.showinfo(title="No input!", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Email/Username: {email_username} "
                                f"\nPassword: {password} \nIs it ok to save?") 
        
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email_username} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()

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
website_entry = Entry(width=35)
website_entry.focus()
username_entry = Entry(width=35)
password_entry = Entry(width=18)

#Add some text in entries
password_entry.insert(END, string="")
username_entry.insert(END, string=EMAIL)

#Gets entry on screen
website_entry.grid(column=1, row=1, columnspan=2)
username_entry.grid(column=1, row=2, columnspan=2)
password_entry.grid(column=1, row=3)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=32, command=save)
add_button.grid(column=1, row=4, columnspan=2)

#Keeps the program window running
window.mainloop()