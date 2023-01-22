from tkinter import *
import pyperclip
from random import choice, randint, shuffle
from tkinter import messagebox
class PasswordGenerator():
    def __init__(self,window):


        #------------------- UI DESIGN -----------------------------------
        self.window = window
        window.title('password manager')
        window.config(padx=50, pady=50)

        self.canvas = Canvas(height=200, width=200)
        self.logo_img = PhotoImage(file="logo.png")
        self.canvas.create_image(100, 100, image=self.logo_img)
        self.canvas.grid(row=0, column=1)        


        # Website label
        self.website_label = Label(window,text="Website:")
        self.website_label.grid(row=1,column=0)
    
        # Website Input
        self.website_input = Entry(window,width=20)
        self.website_input.grid(row=1,column=1)

        # Email label
        self.Email_label = Label(window,text="Email/Username:")
        self.Email_label.grid(row=2,column=0)
        
        # Email Input
        self.Email_input = Entry(window,width=20)
        self.Email_input.grid(row=2,column=1)

        # Password label
        self.Password_label = Label(window,text="Password:")
        self.Password_label.grid(row=3,column=0)

        # Password Input
        self.Password_input = Entry(window,width=10)
        self.Password_input.grid(row=3,column=1)

        # password button
        self.Password_button = Button(window,text="Generate Password",command=self.generate_password)
        self.Password_button.grid(row=3,column=2)        


        # Add button
        self.add_buttn = Button(window,text="Add",command=self.save)
        self.add_buttn.grid(row=4,column=2)
        #------------------- Functions -----------------------------------
    def generate_password(self):
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        password_letters = [choice(self.letters) for _ in range(randint(8, 10))]
        password_symbols = [choice(self.symbols) for _ in range(randint(2, 4))]
        password_numbers = [choice(self.numbers) for _ in range(randint(2, 4))]

        self.password_list = password_letters + password_symbols + password_numbers
        shuffle(self.password_list)

        self.password = "".join(self.password_list)
        self.Password_input.insert(0, self.password)
        pyperclip.copy(self.password)

    def save(self):
            self.website = self.website_input.get()
            self.email = self.Email_input.get()
            self.password = self.Password_input.get()

            if len(self.website) == 0 or len(self.password) == 0:
                messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
            else:
                is_ok = messagebox.askokcancel(title=self.website, message=f"These are the details entered: \nEmail: {self.email} "f"\nPassword: {self.password} \nIs it ok to save?")
                if is_ok:
                    with open("data.txt", "a") as data_file:
                        data_file.write(f"{self.website} | {self.email} | {self.password}\n")
                        self.website_input.delete(0, END)
                        self.Password_input.delete(0, END)



mywin = Tk()
Pswgen = PasswordGenerator(mywin)
mywin.mainloop()
