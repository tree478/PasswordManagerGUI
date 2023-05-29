import tkinter as tk
from tkinter import *
from tkinter import ttk
from typing import Optional, Tuple, Union
import customtkinter as ctk
from cryptography.fernet import Fernet
import json 

class PasswordManager(ctk.CTk):

    def __init__(self):
    
        super().__init__()

        self.key = self.load_key()
        self.fer = Fernet(self.key)

        self.title("Password Manager")
        self.geometry("1200x600")
        self.configure(width=1200, height=600)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1) 

        self.interface = ctk.CTkFrame(self, width=1200, height=600)
        self.interface.grid(row=0, column=0, sticky='nsew')

        self.entry_frame = ctk.CTkFrame(self, width=1200, height=600)
        self.entry_frame.grid(row=0, column=0, sticky='nsew')

        self.entry_frame.grid_rowconfigure(0, weight=1)
        self.entry_frame.grid_rowconfigure(4, weight=1)
        self.entry_frame.grid_columnconfigure(0, weight=1)
        self.entry_frame.grid_columnconfigure(2, weight=1)

        self.instructions = ctk.CTkLabel(self.entry_frame, text = "Please enter your master password:")
        self.instructions.grid(row=0, column=0, sticky='NEWS')

        self.password_entry = ctk.CTkEntry(self.entry_frame, placeholder_text="Master Password", width=20)
        self.password_entry.grid(row=1, column=0, sticky='NEWS')

        self.verify_button = ctk.CTkButton(self.entry_frame, text="Submit", command=self.check_password, width=2, height=8)
        self.verify_button.grid(row=2, column=0, sticky='NEWS')

        self.sidebar_frame = ctk.CTkFrame(self.interface, width=300, height=600)
        self.sidebar_frame.pack(side='left', fill='y')

        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.sidebar_frame.grid_columnconfigure(10, weight=1)

        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Password Manager", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_button_1 = ctk.CTkButton(self.sidebar_frame, text='View Passwords', command=self.change_to_view_passwords)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

        self.sidebar_button_2 = ctk.CTkButton(self.sidebar_frame, text='Add Password', command=self.change_to_add_password)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

        self.sidebar_button_3 = ctk.CTkButton(self.sidebar_frame)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

        self.mainpage = ctk.CTkFrame(self.interface, width=1000, height=600)
        self.mainpage.pack(side='left', fill='both')
        
        self.welcome_label = ctk.CTkLabel(self.mainpage, text='Welcome! Please choose an option from the sidebar menu!')
        self.welcome_label.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.show_frame(self.entry_frame)

    def show_frame(self, frame):
        frame.tkraise()
    
    def get_input(self, string):
        string = string.get()
        return string

    def check_password(self):
        password = self.password_entry.get()
        if password == 'hello':
            self.interface.tkraise()
        else:
           self.destroy()

    def load_key(self):
        self.file = open("key.key", "rb")
        self.key = self.file.read()
        self.file.close()
        return self.key
    
    def write_dict(self, dict):
        with open("data.py", "a") as file:
            #json.dump(dict, file)
            file.write(json.dumps(dict) + '\n')

    def read_list(self):
        with open('data.py', 'rb') as file:
            n_list = json.load(file)
            return n_list

    def store_input(self): #when you press submit on the add passwords frame, this function runs, it stores the user input in data.py

        self.info = {}

        self.account_name_input = str(self.fer.encrypt(self.account_name_entry.get().encode()))
        print(self.account_name_entry.get())
        print("this was printed")
        self.info['account_name'] = self.account_name_input
        self.username_input = str(self.fer.encrypt(b'self.username_entry.get()'))
        self.info['username'] = self.username_input
        self.password_input = str(self.fer.encrypt(b'self.password_entry.get()'))
        self.info['password'] = self.password_input
        self.notes_input = str(self.fer.encrypt(b'self.notes_entry.get()'))
        self.info['notes'] = self.notes_input

        self.write_dict(self.info)

    def change_to_add_password(self): #this changes the frame to the add passwords form

        for self.widget in self.mainpage.winfo_children():
            self.widget.destroy()

        self.add_password_instructions = ctk.CTkLabel(self.mainpage, text="Please enter the account information:")
        self.add_password_instructions.grid(row=1, column=1, sticky='news', padx=20, pady=20)

        self.account_name_label = ctk.CTkLabel(self.mainpage, text="Account Name:")
        self.account_name_label.grid(row=2, column=1, sticky='news', padx=20, pady=20)

        self.account_name_entry = ctk.CTkEntry(self.mainpage, placeholder_text="Account Name")
        self.account_name_entry.grid(row=2, column=2, sticky='news', pady=20)

        self.username_label = ctk.CTkLabel(self.mainpage, text="Username:")
        self.username_label.grid(row=3, column=1, sticky='news', padx=20, pady=20)

        self.username_entry = ctk.CTkEntry(self.mainpage, placeholder_text="Username")
        self.username_entry.grid(row=3, column=2, sticky='news', pady=20)

        self.password_label = ctk.CTkLabel(self.mainpage, text="Password:")
        self.password_label.grid(row=4, column=1, sticky='news', padx=20, pady=20)

        self.password_entry = ctk.CTkEntry(self.mainpage, placeholder_text="Password")
        self.password_entry.grid(row=4, column=2, sticky='news', pady=20)

        self.notes_label = ctk.CTkLabel(self.mainpage, text="Notes:")
        self.notes_label.grid(row=5, column=1, sticky='news', padx=20, pady=20)

        self.notes_entry = ctk.CTkEntry(self.mainpage, placeholder_text="Notes", height=50)
        self.notes_entry.grid(row=5, column=2, sticky='news', pady=20)

        self.submit_info = ctk.CTkButton(self.mainpage, text="Submit", command=self.store_input)
        self.submit_info.grid(row=6, column=2, padx=20, pady=20)

        self.mainpage.configure(width=1000, height=600)
        self.mainpage.grid_propagate(False)

    def change_to_view_passwords(self): #the fucntion to let you view passwords, runs when you press the 'view passwords button'
        for self.widget in self.mainpage.winfo_children():
            self.widget.destroy()

        with open("data.py", "rb") as file:
            for line in file.readlines():
                line = json.loads(line)
                for value in line.values():
                    print("the decrypted account name:", str(self.fer.decrypt(bytes(value[2:-1], 'utf-8'))))

if __name__ == '__main__':
    app = PasswordManager()
    app.mainloop()






