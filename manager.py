#Main manager of the console app to manage ToDo lists
from dotenv import load_dotenv
import mysql.connector 
import datetime as dt
import os 
load_dotenv(".config.env")
host: str = os.getenv("DB_HOST")
user: str = os.getenv("DB_USER")
password: str = os.getenv("DB_PASSWORD")
db_name: str = os.getenv("DB_NAME")
def delete_item(username):
    if os.path.exists(f"{username}.json"):
        data = print_all(username)
        while True:
            try:    
                choice = input("\nEnter the number of the plan you want to delete:")
                deleted_value = data.pop(choice)
                print(f"\n{deleted_value} is deleted from your list!!!\n")
                with open(f"{username}.json", 'w', encoding="utf8") as overwrite:
                    json.dump(data, overwrite, indent = 4, ensure_ascii=False)
                break
            except (ValueError, KeyError):
                print(f"\nInvalid input!\nPlease enter a number between 1 and {len(data.keys())}")
    else:
        print("\nError!\nYou have no active plans now...\nCreate one first please<3\n")
def print_all(username):
    if os.path.exists(f"{username}.json"):
        with open(f"{username}.json", "r", encoding="utf8") as read:
            data = json.load(read)
            counter = 1
            while counter <= len(data.keys()):
                print("="*10,f"\n{counter}.", end="")
                for element in data[str(counter)]:
                    print(f"{element}\n",'-'*10)
                counter += 1
        return data
    else:
        print("\nError!\nYou have no active plans now...\nCreate one first please<3\n")
def create_new(username):
    plan: str = input("\nEnter your plan here\n>>>")
    while True:
        if len(plan) > 50:
            print("\nThe length of the task description cannot be more than 50 symbols\nPlease make it shorter<3...")
            plan : str = input("\nEnter your plan here\n>>>")
        else:
            break  
    while True:
        due_time = input("Format: YYYY-mm-dd(e.g. 2025-01-15)\nEnter the due date:")
        try:
            dt.datetime.strptime(due_time, "%Y-%m-%d")
            break
        except ValueError:
            print("\nInvalid date. Please use YYYY-mm-dd (e.g. 2025-01-15)❤️")
    creation_time = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with mysql.connector.connect(host=host,user=user,password=password,database=db_name) as conn:
        with conn.cursor() as mycursor:
            mycursor.execute("INSERT INTO todos(username,task,creationTime,expectedCompletion) VALUES(%s,%s,%s,%s)", (username,plan,creation_time,due_time))
            conn.commit()
def status_change(username, status = "Created"):
    if os.path.exists(f"{username}.json"):
        data = print_all(username)
        counter = len(data.keys())+1
        while True:
            try:
                choice = input("Enter the number of the plan you want to change the status of:")
                if int(choice)>=counter:
                    print(f"\nInvalid input!\nYou have only {counter-1} active plans!!!")
                    continue
                print("\n1.InProcess\n2.Completed\n3.Frozen")
                slc = input("Enter a number from 1 to 3 below...\n>>>")
                if int(slc) == 1:
                    status = "InProcess"
                elif int(slc) == 2:
                    status = "Completed"
                elif int(slc) == 3:
                    status = "Frozen"
                else:
                    print("\nYou have entered a wrong input!\nPlease try again...")
                    continue
                data[choice][3] = status
                break
            except (ValueError,KeyError):
                print(f"\nInvalid input\nTry to enter an integer please...\nFrom 1 to {counter-1}<3")
                continue
        with open(f"{username}.json", 'w', encoding="utf8") as write:
            json.dump(data, write, indent=4, ensure_ascii=False)
    else:
        print("\nError!\nYou have no active plans now...\nCreate one first please<3\n")
def main_menu(username): 
    __username: str = username
    print("\n----------Welcome to ToDoList Manager!----------")
    while True:
        print("\n1.Create a new list!")
        print('2.Assign the status of the plan')
        print("3.Remove the list")
        print("4.Display all my plans")
        print("5.Profile")
        print("6.Log out...")
        choice: str = input("\nEnter a digit(1-5) please\nEnter your choice:")
        try:
            choice = int(choice) 
        except ValueError:
            print("Invalid input!\nPlease enter a digit from 1 to 5...")
            continue
        if choice == 1:
            create_new(__username)
        elif choice == 2:
            status_change(__username)
        elif choice == 3:
            delete_item(__username)
        elif choice == 4:
            print_all(__username)
        elif choice == 5:
            pass
        elif choice == 6:
            break
        else:
            print("\nYou have entered a wrong choice!\nPlease try again...")
            continue


