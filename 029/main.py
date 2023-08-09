from tkinter import *
from random import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pw_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    pw_list = password_letters + password_symbols + password_numbers
    shuffle(pw_list)

    password = "".join(pw_list)
    pw_entry.delete(0, END)
    pw_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = web_entry.get()
    name = name_entry.get()
    pw = pw_entry.get()

    if web == "" or name == "" or pw == "":
        messagebox.showinfo(title="Error", message="You can't save with empty field.")

    else:
        is_ok = messagebox.askokcancel(title="Notice", message=f"These are the details entered: \nEmail: {name}\nPassword: {pw}\nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as f:
                f.write(f"{web}  |  {name}  |  {pw}\n")
            web_entry.delete(0, END)
            pw_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)
name_label = Label(text="Email/Username:")
name_label.grid(column=0, row=2)
pw_label = Label(text="Password:")
pw_label.grid(column=0, row=3)

# Entries
web_entry = Entry(width=40)
web_entry.grid(column=1, row=1, columnspan=2)
web_entry.focus()
name_entry = Entry(width=40)
name_entry.grid(column=1, row=2, columnspan=2)
name_entry.insert(0, "shinwoo@gmail.com")
pw_entry = Entry(width=24)
pw_entry.grid(column=1, row=3)

# Buttons
pw_button = Button(text="Generate Password", width=15, command=pw_generator)
pw_button.grid(column=2, row=3)
add_button = Button(text="Add", width=40, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
