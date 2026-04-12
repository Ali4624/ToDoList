import menu as m
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
def login():
    global username, password
    username_prompt = "Username should contain at least 8 symbols and a digit \nEnter your username:"
    password_prompt = "Password should contain a digit and have at least 8 symbols<3\nEnter your password here:"

    print('\n----------\nWelcome to ToDoList Manager!\n----------')
    
    username = validator(username_prompt)
    password = validator(password_prompt)

    #Working with data file where logins and passwords are saved
    with open('Logins.txt', 'a') as L:
        L.write(f"{username}\t-\t{password}\n")
    print("You have registered successfully!")   
           
