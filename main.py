from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range( random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0,END)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website_text = website_entry.get()
    email_text = email_entry.get()
    password_text = password_entry.get()

    if len(website_text) == 0 or len(password_text) == 0:
        messagebox.showerror(title="ERROR",message="El website o la contraseña estan vacios")
    else:
        is_ok = messagebox.askokcancel(title=website_text,
                               message=f"estos son tus datos:\nEmail: {email_text}\n"
                                       f"Password: {password_text} ")
        if is_ok:
            with open("cuentas.txt", "a") as data_file:
                data_file.write(f"{website_text} | {email_text} |{password_text}\n")
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

#canvas

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

#label

website = Label(text="Website:")
website.grid(row=1, column=0,sticky="e")

email= Label(text="Email/Username:")
email.grid(row=2, column=0,sticky="e")

password = Label(text="Password:")
password.grid(row=3, column=0,sticky="e")

#entry

website_entry = Entry(width=51)
website_entry.grid(column=1, row=1, columnspan=2,sticky="w",padx=5)
website_entry.focus()


email_entry = Entry(width=51)
email_entry.grid(column=1, row=2, columnspan=2,sticky="w",padx=5)
email_entry.insert(0,"@gmail.com")

password_entry = Entry(width=30)
password_entry.grid(column=1, row=3,sticky="w",padx=5)

#button

generate_pass = Button(text="Generate Password",command=generate_password)
generate_pass.grid(column= 2, row=3)

add_button = Button(text="Add",width=43,command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
