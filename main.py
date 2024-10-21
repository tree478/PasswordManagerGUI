import tkinter as tk
from tkinter import *
from tkinter import ttk
from typing import Optional, Tuple, Union
import customtkinter as ctk
from cryptography.fernet import Fernet
import json
import webbrowser

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
        #hello

        self.entry_frame = ctk.CTkFrame(self, width=1200, height=600)
        self.entry_frame.grid(row=0, column=0, sticky='nsew')

        self.instructions = ctk.CTkLabel(self.entry_frame, text = "Please enter your master password:")
        self.instructions.grid(row=0, column=0, sticky='NEWS', padx=500, pady=(250,10))

        self.password_entry = ctk.CTkEntry(self.entry_frame, placeholder_text="Master Password")
        self.password_entry.grid(row=1, column=0, sticky='NEWS', padx=500, pady=(0,10))

        self.verify_button = ctk.CTkButton(self.entry_frame, text="Submit", command=self.check_password, height=12)
        self.verify_button.grid(row=2, column=0, sticky='NEWS', padx=500, pady=(0,250))

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

        self.mainpage = ctk.CTkFrame(self.interface, width=1000, height=600)
        self.mainpage.pack(side='left', fill='both')
        
        self.welcome_label = ctk.CTkLabel(self.mainpage, text='Welcome! Please choose an option from the sidebar menu!')
        self.welcome_label.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.show_frame(self.entry_frame)

        self.dict_of_buttons = {}

        self.bind('<Return>', lambda event: self.check_password())

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
            json.dump(dict,file)

    def read_list(self):
        with open('data.py', 'rb') as file:
            n_list = json.load(file)
            return n_list
        
    def open_link(self, link):
        print(link)
        chrome = webbrowser.Chrome(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
        chrome.open(link)

    def store_input(self): #when you press submit on the add passwords frame, this function runs, it stores the user input in data.py
        self.info = {}

        self.account_name_input = str(self.fer.encrypt(self.account_name_entry.get().encode()))
        self.info['account_name'] = self.account_name_input
        self.username_input = str(self.fer.encrypt(self.username_entry.get().encode()))
        self.info['username'] = self.username_input
        self.password_input = str(self.fer.encrypt(self.password_entry.get().encode()))
        self.info['password'] = self.password_input
        self.notes_input = str(self.fer.encrypt(self.notes_entry.get().encode()))
        self.info['notes'] = self.notes_input
        self.link_input = str(self.fer.encrypt(self.link_entry.get().encode()))
        self.info['link'] = self.link_input

        self.write_dict(self.info)

        self.account_name_entry.delete(0, END)
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.link_entry.delete(0, END)
        self.notes_entry.delete(0, END)

    def show_account(self, account, number):

        with open("data.py", "r") as f:
            list_of_accounts = []
            lines = f.readlines()
            for line in lines:
                line = json.loads(line)
                value = line['account_name']
                list_of_accounts.append(str(self.fer.decrypt(bytes(value[2:-1], 'utf-8'))))
            
        data = json.loads(lines[number-1])

        for self.widget in self.mainpage.winfo_children():
            self.widget.destroy()

        self.account_name_frame = ctk.CTkFrame(self.mainpage, width=600, height=40)
        self.account_name_frame.grid(row=0, column=0, padx=200, pady=5)

        self.account_name = ctk.CTkLabel(self.account_name_frame, text="Account Name: " + str(self.fer.decrypt(bytes(data['account_name'][2:-1], 'utf-8')))[2:-1])
        self.account_name.grid(row=0, column=0, padx=30, pady=10)

        self.username_frame = ctk.CTkFrame(self.mainpage, width=600, height=40)
        self.username_frame.grid(row=1, column=0, padx=200, pady=5)

        self.username = ctk.CTkLabel(self.username_frame, text="Username: " + str(self.fer.decrypt(bytes(data['username'][2:-1], 'utf-8')))[2:-1])
        self.username.grid(row=0, column=0, padx=30, pady=10)

        self.password_frame = ctk.CTkFrame(self.mainpage, width=600, height=40)
        self.password_frame.grid(row=2, column=0, padx=200, pady=5)

        self.password = ctk.CTkLabel(self.password_frame, text="Password: " + str(self.fer.decrypt(bytes(data['password'][2:-1], 'utf-8')))[2:-1])
        self.password.grid(row=0, column=0, padx=30, pady=10)

        self.link_frame = ctk.CTkFrame(self.mainpage, width=600, height=40)
        self.link_frame.grid(row=4, column=0, padx=200, pady=5)

        self.link = ctk.CTkButton(self.link_frame, text="Link: " + str(self.fer.decrypt(bytes(data['link'][2:-1], 'utf-8')))[2:-1], command= lambda: self.open_link(str(self.fer.decrypt(bytes(data['link'][2:-1], 'utf-8')))[2:-1]))
        self.link.grid(row=0, column=0, padx=30, pady=10)

        self.notes_frame = ctk.CTkFrame(self.mainpage, width=600, height=40)
        self.notes_frame.grid(row=3, column=0, padx=200, pady=5)

        self.notes = ctk.CTkLabel(self.notes_frame, text="Notes: " + str(self.fer.decrypt(bytes(data['notes'][2:-1], 'utf-8')))[2:-1])
        self.notes.grid(row=0, column=0, padx=30, pady=10)

        self.mainpage.configure(width=1000, height=600)
        self.account_name_frame.configure(width=600, height=40)
        self.username_frame.configure(width=600, height=40)
        self.password_frame.configure(width=600, height=40)
        self.link_frame.configure(width=600, height=40)
        self.notes_frame.configure(width=600, height=40)


    def change_to_add_password(self): #this changes the frame to the add passwords form

        for self.widget in self.mainpage.winfo_children():
            self.widget.destroy()

        self.add_password_instructions_frame = ctk.CTkFrame(self.mainpage, width=1000, height=100)
        self.add_password_instructions_frame.pack(side='top')

        self.add_password_instructions = ctk.CTkLabel(self.add_password_instructions_frame, text="Please enter the account information:")
        self.add_password_instructions.grid(row=1, column=1, sticky='news', padx=400, pady=20)

        self.add_info_frame = ctk.CTkFrame(self.mainpage, width=1000, height=500)
        self.add_info_frame.pack(side='top')

        self.account_name_label = ctk.CTkLabel(self.add_info_frame, text="Account Name:")
        self.account_name_label.grid(row=2, column=1, sticky='news', padx=(350,20), pady=20)

        self.account_name_entry = ctk.CTkEntry(self.add_info_frame, placeholder_text="Account Name")
        self.account_name_entry.grid(row=2, column=2, sticky='news', pady=20)

        self.username_label = ctk.CTkLabel(self.add_info_frame, text="Username:")
        self.username_label.grid(row=3, column=1, sticky='news', padx=(350,20), pady=20)

        self.username_entry = ctk.CTkEntry(self.add_info_frame, placeholder_text="Username")
        self.username_entry.grid(row=3, column=2, sticky='news', pady=20)

        self.password_label = ctk.CTkLabel(self.add_info_frame, text="Password:")
        self.password_label.grid(row=4, column=1, sticky='news', padx=(350,20), pady=20)

        self.password_entry = ctk.CTkEntry(self.add_info_frame, placeholder_text="Password")
        self.password_entry.grid(row=4, column=2, sticky='news', pady=20)

        self.link_label = ctk.CTkLabel(self.add_info_frame, text="Link:")
        self.link_label.grid(row=5, column=1, sticky='news', padx=(350,20), pady=20)

        self.link_entry = ctk.CTkEntry(self.add_info_frame, placeholder_text="Link")
        self.link_entry.grid(row=5, column=2, sticky='news', pady=20)

        self.notes_label = ctk.CTkLabel(self.add_info_frame, text="Notes:")
        self.notes_label.grid(row=6, column=1, sticky='news', padx=(350,20), pady=20)

        self.notes_entry = ctk.CTkEntry(self.add_info_frame, placeholder_text="Notes", height=50)
        self.notes_entry.grid(row=6, column=2, sticky='news', pady=20)

        self.submit_info = ctk.CTkButton(self.add_info_frame, text="Submit", command=self.store_input)
        self.submit_info.grid(row=7, column=2, padx=20, pady=20)

        self.add_password_instructions_frame.configure(width=1000, height=100)
        self.add_password_instructions_frame.grid_propagate(False)

        self.add_info_frame.configure(width=1000, height=500)
        self.add_info_frame.grid_propagate(False)

        self.bind('<Return>', lambda event: self.store_input())

        self.mainpage.configure(width=1000, height=600)
        self.mainpage.grid_propagate(False)

    def create_button(self, account, number):
        account_button = ctk.CTkButton(self.mainpage, text=account[2:-1], width=980, height=30, command=lambda: self.show_account(account, number))
        self.dict_of_buttons[(account, number)] = account_button
        return account_button


    def change_to_view_passwords(self): #the fucntion to let you view passwords, runs when you press the 'view passwords button'
        for self.widget in self.mainpage.winfo_children():
            self.widget.destroy()

        with open("data.py", "rb") as file:
            line_no = 1
            list_of_accounts = []
            for line in file.readlines():
                line = json.loads(line)
                value = line['account_name']
                list_of_accounts.append(str(self.fer.decrypt(bytes(value[2:-1], 'utf-8'))))
            
            row_=0
            self.number = 1
            for self.account in list_of_accounts:
                self.create_button(self.account, self.number).grid(row=row_, column=0, padx=10, pady=15)
                row_ += 1
                self.number += 1
            self.mainpage.configure(width=1000, height=600)
            self.mainpage.grid_propagate(False)
                
            line_no += 1

if __name__ == '__main__':
    app = PasswordManager()
    app.mainloop()






