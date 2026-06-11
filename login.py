import mysql.connector as msl
import manager

def Checker(username): #Function that reads file to check whether username and password exist or not 
    with msl.connect(host=manager.host, user = manager.user, password = manager.password, database = manager.db_name) as conn:
        with conn.cursor() as mycursor:
            mycursor.execute('SELECT username FROM users WHERE username = %s', (username,))
            try:
                if username in mycursor.fetchone():
                    passwrd: str  = input("\nEnter your password:")
                    mycursor.execute('SELECT password FROM users WHERE username = %s', (username,))
                    if passwrd  in mycursor.fetchone():
                        print(f"\nHello, {username}")
                        manager.main_menu(username)
                    else:
                        print("\nWrong password, please try again...")
            except TypeError:
                print("Wrong username or password!\nPlease try again...")
def logging_in():
    username: str = input('\nEnter your username:')
    Checker(username)
