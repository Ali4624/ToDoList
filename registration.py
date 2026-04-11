def Validator(username):
    if len(username) < 8:
        return False
    else:
        return True
def login():
    while True:
        print('\n----------\nWelcome to ToDoList Manager!\n----------')
        user_name = input("Enter your username(min 8 symbols):")
        if Validator(user_name):
            password = input("Enter your password:")
            with open('Logins.txt', 'a') as L:
                L.write(f"{user_name}\t-\t{password}\n")
            print("You have registered successfully!")
            break
        else:
            continue             
