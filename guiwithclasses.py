# I have recreated this program using classes and methods. It doesn't work yet, I am having trouble with variable scope. 
# I made some variables in my methods global, but when I try to access them in a different class, it keeps showing
# me an error saying that the variable is not defined. I have yet to figure out why that is, I googled it a bunch, 
# but didn't find anything useful. But I think my code looks a lot neater now(even though it doesn't work yet!)

import tkinter  as tk
from tkinter import *
from tkinter import ttk
import random
import multiprocessing
import time
from ShakespearanInsults import words

class data:
    def __init__(self):
        pass

    def get_input(self):
        string = string.get()
        return string

    def remove(self):
        ns=""
        for i in self:
            if(not i.isspace()):
                ns+=i
        return ns

    def encrypt(self):
        string = ""
        for letter in self:
            value = ord(letter) + 13
            letter = chr(value)
            string += letter
        final_message = string
        final_message = str(final_message)
        return final_message

    def decrypt(self):
        string = ""
        final_message = ""
        self = data.remove(self)
        for letter in self:
            value = ord(letter) - 13
            letter = chr(value)
            string += letter
        final_message = (string)
        final_message = str(final_message)
        return final_message
    def print(self):
        self = data.encrypt(self)
        print(self)

class unlock:
    def __init__(self):
        pass

    def add(self, my_tabs, tab1):

        my_tabs.add(tab1, text ='Add') # adding tab

        l1 = Label(tab1, text="Account Name:")
        l1.grid(row=1, column=0)
        l1.grid_rowconfigure(1, weight = 1)
        l1.grid_columnconfigure(0, weight = 1)

        account_name = Entry(tab1)
        account_name.grid(row=1, column=1)
        account_name.grid_rowconfigure(1, weight = 1)
        account_name.grid_columnconfigure(1, weight = 1)

        l2 = Label(tab1, text="Username:")
        l2.grid(row=3, column=0)
        l2.grid_rowconfigure(3, weight = 1)
        l2.grid_columnconfigure(0, weight = 1)

        username = Entry(tab1)
        username.grid(row=3, column=1)
        username.grid_rowconfigure(3, weight = 1)
        username.grid_columnconfigure(1, weight = 1)

        l3 = Label(tab1, text="Password:")
        l3.grid(row=5, column=0)
        l3.grid_rowconfigure(5, weight = 1)
        l3.grid_columnconfigure(0, weight = 1)

        password = Entry(tab1)
        password.grid(row=5, column=1)
        password.grid_rowconfigure(5, weight = 1)
        password.grid_columnconfigure(1, weight = 1)

        account_name = str(account_name.get)
        username = data.encrypt(data.get_input(username))
        password = data.encrypt(data.get_input(password))

    def write(self, account_name, username, password, tab1, my_w):
        account_name_input = data.encrypt(data.get_input(account_name))
        username_input = data.encrypt(data.get_input(username))
        password_input = data.encrypt(data.get_input(password))
        with open("passwords.txt", "a", encoding="utf-8") as f:
            f.write("Account Name: " + account_name_input + "\n" + "Username: " + username_input + "\n" + "Password: " + password_input + "\n"+"\n")

        account_name.delete(0, END)
        username.delete(0, END)
        password.delete(0, END)

        turn_in = Button(tab1, text="Submit", command=unlock.write)
        turn_in.grid(row=4, column=4)
        my_w.bind('<Return>',lambda event:unlock.write)

    def view(self, tab2):

        global scroll_bar
        scroll_bar = Scrollbar(tab2)
        scroll_bar.pack( side = RIGHT, fill = Y )

        with open("passwords.txt", "r", encoding="utf-8") as f:
            global text
            text = Listbox(tab2, yscrollcommand = scroll_bar.set )
            for line in f.readlines():
                length = len(line)
                if length > 1:
                    one = line.partition(":")[0]
                    two = data.decrypt(line.partition(":")[-1])
                    #text = tk.Label(root, text=one + ": " + two)
                    #text.pack()
                    text.insert(END, one + ": " + two)

                if length == 1:
                    #text2 = tk.Label(root, text="\n")
                    #text2.pack()
                    text.insert(END, "\n")

        button = tk.Button(tab2, text = "Refresh", command=unlock.refresh)
        button.pack()

    def refresh(self):
        text.delete(0,'end')
        with open("passwords.txt", "r", encoding="utf-8") as f:
            for line in f.readlines():
                length = len(line)
                if length > 1:
                    one = line.partition(":")[0]
                    two = data.decrypt(line.partition(":")[-1])
                    #text = tk.Label(root, text=one + ": " + two)
                    #text.pack()
                    text.insert(END, one + ": " + two)

                if length == 1:
                    #text2 = tk.Label(root, text="\n")
                    #text2.pack()
                    text.insert(END, "\n")

class window:
    def __init__(self):
        pass

    def first_tab(my_w, my_tabs, tab0):
        my_tabs.add(tab0, text ='Master Password') # adding tab
        my_tabs.pack(expand = 1, fill ="both")
        instructions = tk.Label(tab0, text = "Please enter your master password below:")
        instructions.grid(row=2,column=0)
        m_password = Entry(tab0, width=20)
        m_password.grid(row=3, column=0)
        submit = tk.Button(tab0, text = "Submit", command=lambda:[unlock.add, unlock.view])
        submit.grid(row=4, column=0)
        my_w.bind('<Return>',lambda event:unlock.add, unlock.view)

my_w = tk.Tk()
my_w.geometry("400x200")

my_tabs = ttk.Notebook(my_w, padding=10)
tab0 = ttk.Frame(my_tabs)
tab1 = ttk.Frame(my_tabs)
tab2 = ttk.Frame(my_tabs)

if __name__ == '__main__':
    #PasswordManager = window()
    instance = window.first_tab(my_w, my_tabs, tab0)
    my_w.mainloop()
    while True:

        if instance == "hello":
            unlock.add(my_tabs, tab1)
            unlock.view(tab2)
        elif instance != "hello":
            pass

