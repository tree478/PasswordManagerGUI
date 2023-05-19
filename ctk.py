import tkinter as tk
from tkinter import *
from tkinter import ttk
from typing import Optional, Tuple, Union
import customtkinter as ctk


class PasswordManager(ctk.CTk):

    def __init__(self):
    
        super().__init__()

        self.title("Password Manager")
        self.geometry("1200x600")
        self.configure(width=1200, height=600)

        self.grid_rowconfigure(0, weight=1) # this needed to be added
        self.grid_columnconfigure(0, weight=1) # as did this

        #self.grid_columnconfigure(1, weight=1)
        #self.grid_columnconfigure((2, 3), weight=0)
        #self.grid_rowconfigure((0, 1, 2), weight=1)

        self.interface = ctk.CTkFrame(self, width=1200, height=600)
        print(self.winfo_width(), self.winfo_height())
        self.interface.grid(row=0, column=0, sticky='nsew')
        #self.interface.pack()

        self.entry_frame = ctk.CTkFrame(self, width=1200, height=600)
        self.entry_frame.grid(row=0, column=0, sticky='nsew')
        #self.entry_frame.pack()

        self.entry_frame.grid_rowconfigure(0, weight=1)
        self.entry_frame.grid_rowconfigure(4, weight=1)
        self.entry_frame.grid_columnconfigure(0, weight=1)
        self.entry_frame.grid_columnconfigure(2, weight=1)

        self.instructions = ctk.CTkLabel(self.entry_frame, text = "Please enter your master password:")
        #self.instructions.pack(side='left', padx=500)
        self.instructions.grid(row=0, column=0, sticky='NEWS')



        self.password_entry = ctk.CTkEntry(self.entry_frame, placeholder_text="Master Password", width=20)
        #self.password_entry.pack(side='top')
        self.password_entry.grid(row=1, column=0, sticky='NEWS')

        self.verify_button = ctk.CTkButton(self.entry_frame, text="Submit", command=self.check_password, width=2, height=8)
        #self.verify_button.pack()
        self.verify_button.grid(row=2, column=0, sticky='NEWS')

        password_frame = AddPassword()

        self.sidebar_frame = ctk.CTkFrame(self.interface, width=300, height=600)
        #self.sidebar_frame.grid(row=0, column=0, columnspan=4, sticky="nsew")
        self.sidebar_frame.pack(side='left', fill='y')
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.sidebar_frame.grid_columnconfigure(10, weight=1)
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Password Manager", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = ctk.CTkButton(self.sidebar_frame, text='View Passwords')
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = ctk.CTkButton(self.sidebar_frame, text='Add Password', command=self.show_frame(password_frame))
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = ctk.CTkButton(self.sidebar_frame)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

        self.welcome_screen = ctk.CTkFrame(self.interface, width=1000, height=600)
        self.welcome_screen.pack(side='left', fill='both')
        self.welcome_label = ctk.CTkLabel(self.welcome_screen, text='Welcome! Please choose an option from the sidebar menu!')
        self.welcome_label.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.show_frame(self.entry_frame)

    def show_frame(self, frame):
        frame.tkraise()

    def check_password(self):
        password = self.password_entry.get()
        if password == 'hello':
            self.interface.tkraise()
        else:
           self.destroy()

class AddPassword(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.grid_rowconfigure(0, weight=1) # this needed to be added
        self.grid_columnconfigure(0, weight=1) # as did this

        self.add_password_frame = ctk.CTkFrame(self, width=1000, height=600)
        self.add_password_frame.pack(side='right', fill='both')

        self.test_label = ctk.CTkLabel(self.add_password_frame, text='this works?')
        self.test_label.pack()





if __name__ == '__main__':
    app = PasswordManager()
    app.mainloop()


# class PasswordManager(tk.Tk):
#     def build(self):

#         ctk.set_appearance_mode("Dark")
#         #self.geometry('1000x600')

#         self.menu_bar = ctk.CTkFrame(self)
#         self.menu_bar.grid(row=0, column=0)

#         self.add_password_button = ctk.CTkButton(self.menu_bar, text="Add a new account", command=PasswordManager.build_frame1(self))
#         self.add_password_button.grid(row=0, column=0)

#         self.view_accounts_button = ctk.CTkButton(self.menu_bar, text="View existing accounts")
#         self.view_accounts_button.grid(row=1, column=0)

#         self.make_a_new_password_button = ctk.CTkButton(self.menu_bar, text="Password Generator")
#         self.make_a_new_password_button.grid(row=2, column=0)

#     def __init__(self):
#         tk.Tk.__init__(self)
#         self.title("Password Manager")
#         self.build()
#         #self.build_frame1()

#     def build_frame1(self):
#         self.frame = ctk.CTkFrame(self)
#         self.frame.grid(row=2, column=2)

#         self.label = ctk.CTkLabel(self.frame, text="A label")
#         self.label.grid(row=3, column=3)
        
#     def show_frame(self):
#         self.frame.ctkraise()

# class AddPassword():
#     pass

# app = PasswordManager()
# app.mainloop()






