import backend.manager as manager
from backend.database import get_connection
def validator(prompt): #Function that checks username and password for validation
    while True:
        data = input(prompt).strip()
        if len(data) >= 8 and any(char.isdigit() for char in data):
            return data
        else:
            print("❌ Must be at least 8 characters and contain a digit. Try again please.\n")
            continue
    #Function always returns valid data
def register(): #Function that saves username and password in database
    username_prompt: str = "====================\nUsername should contain at least 8 symbols and a digit \nEnter your username:"
    password_prompt: str = "--------------------\nPassword should contain a digit and have at least 8 symbols<3\nEnter your password here:"
    username: str = validator(username_prompt)
    while True:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT username FROM users WHERE username = %s",(username,))
                if cursor.fetchone() is not None:
                    print("Username already exists!!!\nPlease enter another username...")
                    username: str = validator(username_prompt)
                    continue
                passwrd: str = validator(password_prompt)
                cursor.execute("INSERT INTO users(username, password) VALUES(%s , %s)", (username, passwrd))
                conn.commit()
                break
    print(f"\nHello, {username}")
    manager.main_menu(username)
