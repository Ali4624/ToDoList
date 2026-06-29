import backend.manager as manager
from backend.database import get_connection

def Checker(username): #Function that reads file to check whether username and password exist or not
    with get_connection() as conn:
        with conn.cursor() as mycursor:
            mycursor.execute('SELECT username FROM users WHERE username = %s', (username,))
            try:
                if mycursor.fetchone() is not None:
                    passwrd: str  = input("\nEnter your password:")
                    mycursor.execute('SELECT password FROM users WHERE username = %s', (username,))
                    row: tuple[str] = mycursor.fetchone()
                    if passwrd == row[0]:
                        print(f"\nHello, {username}")
                        manager.main_menu(username)
                    else:
                        print("\nWrong password, please try again...")
            except TypeError:
                print("Wrong username or password!\nPlease try again...")
def logging_in():
    username: str = input('\nEnter your username:').strip()
    Checker(username)
