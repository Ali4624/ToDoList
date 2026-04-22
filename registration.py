import menu as m
import json
import os 
import manager
username = None
password = None
#Global variables
def validator(prompt): #Function that checks username and password for validation
    while True:
        data = input(prompt)
        if len(data) >= 8 and any(char.isdigit() for char in data):
            return data
        else:
            print("❌ Must be at least 8 characters and contain a digit. Try again please.\n")
            continue
    #Function always returns valid data
def save_user(file, username, password): #Function that saves all logins and passwords in a json file as a dictionary
    if os.path.exists(file):
        with open(file, 'r') as f:
            data = json.load(f)
    else:
        data = {}
    data[username] = password

    with open(file, 'w') as Ow:
        json.dump(data, Ow, indent = 4)
    #Function checks whether we already have users.json file or not
    #If we have, it loads data from it and saves as local dictionary
    #After overwrites the same file that dictionary with 1 new key:value pair
def register():
    global username, password
    username_prompt = "====================\nUsername should contain at least 8 symbols and a digit \nEnter your username:"
    password_prompt = "--------------------\nPassword should contain a digit and have at least 8 symbols<3\nEnter your password here:"
    username = validator(username_prompt)
    with open('users.json', 'r') as read:
        data = json.load(read)
        if username in data.keys():
            print("\nUsername already exists!\nPlease, try another one...\n")
            return 
    password = validator(password_prompt)

    #Working with data file where logins and passwords are saved
    save_user("users.json",username, password)
    print(f"\nHello, {username}")
    manager.main_menu(username)

           
