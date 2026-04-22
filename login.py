import json
import manager
def Checker(username): #Function that reads file to check whether username and password exist or not 
    try:
        with open('users.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("\nInternal error!\nPlease try again later.\nSorry for inconvenience<3")
    if username in data.keys():
        password = input("\nEnter your password:")
        if data[username] == password:
            print(f"\nHello, {username}")
            manager.main_menu(username)
        else:
            print("Wrong username or password!\nPlease try again...")
    else:
        print("\nUsername not found!\nPlease try again...\n")
def logging_in():
    username = input('\nEnter your username:')
    Checker(username)
