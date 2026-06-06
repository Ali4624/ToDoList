import mysql.connector 
import manager
def validator(prompt): #Function that checks username and password for validation
    while True:
        data = input(prompt)
        if len(data) >= 8 and any(char.isdigit() for char in data):
            return data
        else:
            print("❌ Must be at least 8 characters and contain a digit. Try again please.\n")
            continue
    #Function always returns valid data
def register(): #Function that saves username and password in database
    username_prompt = "====================\nUsername should contain at least 8 symbols and a digit \nEnter your username:"
    password_prompt = "--------------------\nPassword should contain a digit and have at least 8 symbols<3\nEnter your password here:"
    username = validator(username_prompt)
    with mysql.connector.connect(host=manager.host, user=manager.user, password=manager.password, database=manager.db_name) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT username FROM users")
            usernames = cursor.fetchall()
            if username in usernames:
                print("Username already exists!!!\nPlease enter another username...")
                username = validator(username_prompt) 
            passwrd = validator(password_prompt)
            cursor.execute("INSERT INTO users(username, password) VALUES(%s , %s)", (username, passwrd))
            conn.commit()
    print(f"\nHello, {username}")
    manager.main_menu(username)
