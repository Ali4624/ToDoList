import json
username = None
password = None
def Checker(username): #Function that reads file to check whether username and password exist or not 
    global password
    try:
        with open('users.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("\nInternal error!\nPlease try again later.\nSorry for inconvenience<3")
    if username in data.keys():
        password = input("\nEnter your password:")
        if data[username] == password:
            print("\nYaaay, you have logged in successfully!")
    else:
        print("\nUsername not found!\nPlease try again...\n")
def logging_in():
    global username
    username = input('\nEnter your username:')
    Checker(username)
