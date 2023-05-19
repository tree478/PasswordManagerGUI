#This is a password manager. When you run it, it first ask you for a master password. If you type in the right one(hello), it will give you three options:
#Add = this will then ask you for an account name, username, and password. It will then encrypt them and then write them in a text file, so that if anyone 
#opens the text file, they won't be able to figure out what your passwords are. 
#View = this will decrypt the encrypted passwords in the text file and print them. 
#Quit = this just breaks the program
#If you enter the wrong master password, it will insult you, Shakespearen style! 
#I also want to create a GUI for this, which is what I am going to work on next. 

import random

def remove(strs):
    ns=""
    for i in strs:
        if(not i.isspace()):
            ns+=i
    return ns   

def encrypt(strs):           
    output = ""                         
    for letter in strs:                          
        value = ord(letter) + 13    
        letter = chr(value)              
        output += letter       
    final_message = output
    final_message = str(final_message)
    return final_message

    

def decrypt(strs):            
    output = ""
    final_message = ""
    strs = remove(strs)                        
    for letter in strs:                          
        value = ord(letter) - 13    
        letter = chr(value)              
        output += letter       
    final_message = (output)
    final_message = str(final_message)
    return final_message

def add():
    account = encrypt(input("Account name:"))
    username = encrypt(input("Username:"))
    password = encrypt(input("Password:"))
    with open("passwords.txt", "a") as f:
        f.write("Account Name: " + account + "\n" + "Username: " + username + "\n" + "Password: " +   password + "\n"+"\n")

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            length = len(line)
            if length > 1:
                one = line.partition(":")[0]
                two = decrypt(line.partition(":")[-1])
                print(one + ": " + two)
            if length == 1: 
                print("\n")

def insult():

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


    insult = print('\nThou', random.choice(one), random.choice(two), random.choice(three),'!!!! How dare thee snoop and try to access my passwords?!!!')
    return insult

master_password = input("What is the master password?")


if master_password == "hello":
    while True:
        mode = input("Would you like to add a password, view your passwords, or quit?(add/view/quit)?")
        if mode == "add":
            add()
        if mode == "view":
            view()
        if mode == "quit":
            break
else:
    insult()