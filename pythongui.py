#This is what my password manager looks like now. I did fix the insults so all of that works now. 
#I also bound the buttons to the enter key, so instead of using the mouse to submit information, you can
#just hit enter
#I added a timer feature to it at well, so that when you type in the wrong password, it will show an insult,
#Stay there for 10 seconds, and then end the program. But right now, the first time you enter the wring password,
#it opens a new window of the program. I have no idea why it's doing that and I have yet to fix it. 
#I also haven't started working on cleaning up my code yet. I'm planning on doing it using classes. But the thing is,
#I know what classes are and how to make one, but I have never made my OWN class before, so I'm doing some research
#on that first.

import tkinter  as tk 
from tkinter import *
from tkinter import ttk
import random
import multiprocessing
import time
#import customtkinter

#customtkinter.set_default_color_theme('blue')

one = ['artless', 'bawdy', 'beslubbering', 'bootless', 'churlish', 'cockered', 'clouted', 'craven', 'currish', 'dankish', 'dissembling', 
    'droning','errant', 'fawning', 'fobbing' 'froward', 'frothy', 'gleeking', 'goatish', 'gorbellied', 'impertinent', 'infectious', 
    'jarring', 'loggerheaded', 'lumpish', 'mammering', 'mangled', 'mewling', 'paunchy', 'pribbling', 'puking', 'puny', 'quailing', 'rank', 
    'reeky', 'roguish', 'ruttish', 'saucy' 'spleeny', 'spongy', 'surly', 'tottering', 'unmuzzled', 'vain', 'venomed', 'villainous', 'warped',
    'wayward', 'weedy', 'yeasty']

two = ['base-court', 'bat-fowling', 'beef-witted', 'beetle-headed', 'boil-brained', 'clapper-clawed', 'clapper-clawed', 'clay-brained',
    'common-kissing','crook-pated', 'dismal-dreaming', 'dizzy-eyed', 'doghearted', 'dread-bolted','earth-vexing', 'elf-skinned', 
    'fat-kidneyed', 'fen-sucked', 'flap-mouthed', 'fly-bitten', 'folly-fallen', 'fool-born', 'full-gorged',
    'guts-griping', 'half-faced', 'hasty-witted', 'hedge-born', 'hell-hated', 'idle-headed', 'ill-breeding', 'ill-nurtured', 
    'knotty-pated', 'milk-livered', 'motley-minded', 'onion-eyed', 'plume-plucked', 'pottle-deep', 'pox-marked', 'reeling-ripe', 
    'ough-hewn', 'rude-growing', 'rump-fed', 'shard-borne', 'sheep-biting', 'spur-galled', 'swag-bellied', 'tardy-gaited', 'tickle-brained',
    'urchin-snouted', 'weather-bitten' ]

three = ['apple-john', 'baggage', 'barnacle', 'bladder', 'boar-pig', 'bugbear', 'bum-bailey', 'canker-blossom', 'clack-dish', 'clotpole',
    'oxcomb', 'codpiece', 'death-token', 'dewberry', 'flap-dragon', 'flax-wench', 'flirt-gill', 'foot-licker', 'fustilarian', 'giglet',
    'gudgeon', 'haggard', 'harpy', 'hedge-pig', 'horn-beast', 'hugger-mugger', 'jolthead', 'lewdster', 'lout', 'maggot-pie', 'malt-worm',
    'mammet', 'measle', 'minnow', 'miscreant', 'moldwarp', 'mumble-news', 'nut-hook', 'pigeon-egg', 'pignut', 'puttock', 'pumpion', 
    'ratsbane', 'scut', 'skainsmate', 'strumpet', 'varlet', 'vassal', 'whey-face', 'wagtail']

words = '\nThou ' + random.choice(one) + " " + random.choice(two) + " " + random.choice(three) + '!!!! How dare thee snoop and try to access my passwords?!!!'

def get_input(string):
    string = string.get()
    return string

def remove(strs):
    ns=""
    for i in strs:
        if(not i.isspace()):
            ns+=i
    return ns   

def encrypt(strs):           
    string = ""                         
    for letter in strs:                          
        value = ord(letter) + 13    
        letter = chr(value)              
        string += letter       
    final_message = string
    final_message = str(final_message)
    return final_message

def decrypt(strs):            
    string = ""
    final_message = ""
    strs = remove(strs)                        
    for letter in strs:                          
        value = ord(letter) - 13    
        letter = chr(value)              
        string += letter       
    final_message = (string)
    final_message = str(final_message)
    return final_message

def adding(tab1):
    #my_tabs.add(tab1) # adding tab
    l1 = tk.Label(tab1, text="Account Name:")
    l1.grid(row=1, column=0)
    l1.grid_rowconfigure(1, weight = 1)
    l1.grid_columnconfigure(0, weight = 1)
    account_name = tk.Label(tab1)
    account_name.grid(row=1, column=1)
    account_name.grid_rowconfigure(1, weight = 1)
    account_name.grid_columnconfigure(1, weight = 1)
    l2 = tk.Label(tab1, text="Username:")
    l2.grid(row=3, column=0)
    l2.grid_rowconfigure(3, weight = 1)
    l2.grid_columnconfigure(0, weight = 1)
    username = tk.Label(tab1)
    username.grid(row=3, column=1)
    username.grid_rowconfigure(3, weight = 1)
    username.grid_columnconfigure(1, weight = 1)
    l3 = tk.Label(tab1, text="Password:")
    l3.grid(row=5, column=0)
    l3.grid_rowconfigure(5, weight = 1)
    l3.grid_columnconfigure(0, weight = 1)
    password = tk.Label(tab1)
    password.grid(row=5, column=1)
    password.grid_rowconfigure(5, weight = 1)
    password.grid_columnconfigure(1, weight = 1)
    account_name = str(account_name.get)
    username = encrypt(get_input(username))
    password = encrypt(get_input(password))

    # def write():
    #     with open("passwords.txt", "a") as f:
    #         f.write("Account Name: " + str(account_name) + "\n" + "Username: " + str(username) + "\n" + "Password: " + str(password) + "\n"+"\n")
    #         my_tabs.add(tab2, text ='View') # adding tab
    #         my_tabs.pack(expand = 1, fill ="both")

    #     turn_in = Button(tab1, text="Submit", command=write)
    #     turn_in.grid(row=4, column=4)
    #     my_w.bind('<Return>',lambda event:write())

def commands():

    def view():

        def refresh():
            text.delete(1.0,'end')
            with open("passwords.txt", "r", encoding="utf-8") as f:
                for line in f.readlines():
                    length = len(line)
                    print(length)
                    if length > 1:
                        one = line.partition(":")[0]
                        two = decrypt(line.partition(":")[-1])
                        #text = tk.Label(root, text=one + ": " + two)
                        #text.pack()
                        text.insert(END, one + ": " + two + '\n')

                    if length == 1: 
                        #text2 = tk.Label(root, text="\n")
                        #text2.pack()
                        text.insert(END, "\n")

        button = tk.Button(tab2, text = "Refresh", command=refresh)
        button.pack()

        scroll_bar = tk.Scrollbar(tab2)
  
        scroll_bar.pack( side = RIGHT, fill = Y )


        with open("passwords.txt", "r", encoding="utf-8") as f:
            text = tk.Listbox(tab2, yscrollcommand = scroll_bar.set )
            for line in f.readlines():
                    length = len(line)
                    print(length)
                    if length > 1:
                        one = line.partition(":")[0]
                        two = decrypt(line.partition(":")[-1])
                        #text = tk.Label(root, text=one + ": " + two)
                        #text.pack()
                        text.insert(END, one + ": " + two + '\n')

                    if length == 1: 
                        #text2 = tk.Label(root, text="\n")
                        #text2.pack()
                        text.insert(END, "\n")

        text.pack(fill=BOTH, expand=True)
        scroll_bar.configure( command = text.yview )

    insulted = tk.Label(tab0, text = " ")
    insulted.grid(row=5, column=0)

    def stop():
        p.start()
        # Wait 10 seconds for foo
        time.sleep(50)

        # Terminate foo
        p.terminate()
        exit()

    if get_input(m_password) != "hello":
        insulted.config(text = words)
        p = multiprocessing.Process(name="Foo", args=(10,))
        if __name__ == "__main__":
            stop()
    elif get_input(m_password) == "hello":
        if insulted.winfo_exists() == 1:
            insulted.destroy()
    tab1 = my_tabs.add('Add') # adding tab
    l1 = tk.Label(tab1, text="Account Name:")
    l1.grid(row = 1, column = 0)
    account_name = tk.Entry(tab1, placeholder_text='Account Name')
    account_name.grid(row = 1, column = 2)
    l2 = tk.Label(tab1, text="Username:")
    l2.grid(row = 2, column = 0)
    username = tk.Entry(tab1, placeholder_text='Username')
    username.grid(row = 2, column = 2)
    l3 = tk.Label(tab1, text="Password:")
    l3.grid(row = 3, column = 0)
    password = tk.Entry(tab1, placeholder_text='Password')
    password.grid(row = 3, column = 2)
    tab2 = my_tabs.add('View') # adding tab
    my_tabs.pack(expand = 1, fill ="both")
    info = tk.Label(tab2, text=view())
    info.pack()

    def write():
        account_name_input = encrypt(get_input(account_name))
        username_input = encrypt(get_input(username))
        password_input = encrypt(get_input(password))
        with open("passwords.txt", "a", encoding="utf-8") as f:
            f.write("Account Name: " + account_name_input + "\n" + "Username: " + username_input + "\n" + "Password: " + password_input + "\n"+"\n")

        account_name.delete(0, END)
        username.delete(0, END)
        password.delete(0, END)

    turn_in = tk.Button(tab1, text="Submit", command=write)
    turn_in.grid(row=4, column=4)
    my_w.bind('<Return>',lambda event:write())



my_w = tk.Tk()
my_w.geometry("400x200")
my_w.title('Password Manager')
my_tabs = ttk.Notebook(my_w) # declaring 

tab0 = my_tabs.add('Master Password')
# tab1 = my_tabs.add('Add')
# test = tk.Label(tab1, text='hello')
# test.pack()
# tab2 = my_tabs.add('View')

#my_tabs.add(tab0) # adding tab
my_tabs.pack(expand = 1, fill ="both")
instructions = tk.Label(tab0, text = "Please enter your master password below:")
instructions.grid(row=2,column=0)
m_password = tk.Entry(tab0, placeholder_text='Master Password')
m_password.grid(row=3, column=0)
submit = tk.Button(tab0, text = "Submit", command=commands)
submit.grid(row=4, column=0)
my_w.bind('<Return>',lambda event:commands())

# def my_msg(*args):
#     t_nos=str(my_tabs.index(my_tabs.select()))
#     l4.config(text='tab No: '+ t_nos)
	
#my_tabs.bind('<<NotebookTabChanged>>') 

# l4=tk.Label(my_w,text='message here')
# l4.pack(side=LEFT)

my_w.mainloop()  # Keep the window open