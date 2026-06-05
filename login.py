import mysql.connector as msl
import manager
def Checker(username): #Function that reads file to check whether username and password exist or not 
    with msl.connect(host='localhost', user = 'root', password = 'Awesome004', database = 'todolist') as conn:
        with conn.cursor() as mycursor:
            mycursor.execute("SELECT username, password FROM users")
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
