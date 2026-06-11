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
def print_all(username)->list:
    with mysql.connector.connect(host=host,user=user,password=password,database=db_name) as conn:
        with conn.cursor() as my_cursor:
            my_cursor.execute("SELECT taskId, task, creationTime, expectedCompletion, status FROM todos WHERE username = %s", (username,))
            output = my_cursor.fetchall()
            id_nums = []
            for row in output:
                id,task,cr_time,exp_time,status = row
                print("==============================================")
                print(f"ID:{id}\nTask description:{task}\nCreation time:{cr_time}\nDue time:{exp_time}\nStatus:{status}")
                id_nums.append(id)
    return id_nums
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
def status_change(username):
    prompt: str = "1.Cancelled\n2.Completed\nEnter the status to be changed(1 or 2):"
    while True:
        ids_list: list = print_all(username)
        id : int = input("Enter the ID of the task you want to edit(e.g 100):")
        status: int = input(prompt)
        try:
            id = int(id)
            status = int(status)
            if id in ids_list and (status == 1 or status == 2):
                break
            else:
                print("Something went wrong...\nPlease try again")
                continue
        except  ValueError:
            print("Enter an integer values please!")      
    with mysql.connector.connect(host=host, user=user,password=password,database=db_name) as conn:
        with conn.cursor() as my_cursor:
            match status:
                case 1:
                    my_cursor.execute("UPDATE todos SET status ='CANCELLED' WHERE taskId = %s", (id,))
                case 2:
                    my_cursor.execute("UPDATE todos SET status ='COMPLETED' WHERE taskId = %s", (id,))
                case _:
                    print("Something went wrong...\nTry again later please\nSorry for inconvenience<3")
            conn.commit()
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


