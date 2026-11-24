from tkinter import *
from tkinter import messagebox
import pyperclip
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for symbol in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for num in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)
    print(password_list)
    password = "".join(password_list)

    entry_pass.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    website_name = entry_website.get()

    try:
        with open('data.json','r') as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(message="No Data File Found",title="Error")

    else:
        for website in data:
            if website.lower() == website_name.lower():
                email= data[website]['email']
                password = data[website]['password']
                messagebox.showinfo(message=f"Email : {email}\nPassword : {password}",title=website)
            else:
                messagebox.showinfo(message=f"No Details For {website} Exists")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def get_data():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_pass.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(message="Please fill all fields!")
    else:
        try:
            file = open("data.json","r")

        except FileNotFoundError:
            file = open('data.json','w')
            messagebox.showinfo(message="Created file data.json")
            json.dump(new_data, file, indent=4)

        else:
            #reading the json file
            data = json.load(file)
            #updating the data
            data.update(new_data)

            with open("data.json",mode="w") as file:
                #writing the data
                json.dump(data,file,indent=4)
                messagebox.showinfo(message="Success! Entry added.")
        finally:
            entry_website.delete(0, "end")
            entry_pass.delete(0, "end")
            file.close()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=20, pady=20)
window.title("Password Manager")

#canvas
canvas = Canvas(width=200,height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100 , 100, image=image)
canvas.grid(row=0,column=1)

#website label
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)

#Email Label
email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0)

#Password Label
pass_label = Label(text="Password:")
pass_label.grid(row=3,column=0)



#Entry for website
entry_website = Entry()
entry_website.grid(row=1,column=1,sticky="EW")

#Entry for email
entry_email = Entry(width=35)
entry_email.insert(0,"placeholder@mail.com")
entry_email.grid(row=2,column=1,columnspan=2,sticky="EW")

#Entry for password
entry_pass = Entry(width=21)
entry_pass.grid(row=3,column=1,sticky="EW")

#generate button
generate = Button(text="Generate Password",width=14,command=password_generator)
generate.grid(row=3,column=2,sticky="EW")

#Add button
add_button = Button(text="Add",command=get_data)
add_button.grid(row=4,column=1,columnspan=2,sticky="EW")

#Search button
search_button = Button(text="Search",command=find_password)
search_button.grid(row=1,column=2,sticky="EW")









window.mainloop()


