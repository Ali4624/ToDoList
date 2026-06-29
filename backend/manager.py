#Main manager of the console app to manage ToDo lists
from datetime import datetime
from backend.database import get_connection
def delete_item(username,/)->str:
    while True:
        ids_list: list = print_all(username)
        id : int = input("Enter the ID of the task you want to delete(e.g 100):")
        try:
            id = int(id)
            if id in ids_list:
                break
            else:
                print("Wrong input,No task with such id...\nPlease try again")
                continue
        except  ValueError:
            print("Enter an integer values please!")      
    with get_connection() as conn:
        with conn.cursor() as my_cursor:
            my_cursor.execute("SELECT task FROM todos WHERE taskId = %s", (id,))
            task_description: tuple[str] = my_cursor.fetchone()
            my_cursor.execute("DELETE FROM todos WHERE taskId = %s", (id,))
            conn.commit()
    return task_description
def print_all(username,/)->list:
    with get_connection() as conn:
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
def create_new(username,/):
    plan: str = input("\nEnter your plan here\n>>>")
    while True:
        if len(plan) > 50:
            print("\nThe length of the task description cannot be more than 50 symbols\nPlease make it shorter<3...")
            plan : str = input("\nEnter your plan here\n>>>")
        else:
            break  
    while True:
        due_time = input("Format: YYYY-mm-dd(e.g. 2025-01-15)\nEnter the due date:").strip()
        try:
            datetime.strptime(due_time, "%Y-%m-%d")
            break
        except ValueError:
            print("\nInvalid date. Please use YYYY-mm-dd (e.g. 2025-01-15)❤️")
    creation_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with get_connection() as conn:
        with conn.cursor() as mycursor:
            mycursor.execute("INSERT INTO todos(username,task,creationTime,expectedCompletion) VALUES(%s,%s,%s,%s)", (username,plan,creation_time,due_time))
            conn.commit()
def status_change(username,/):
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
    with get_connection() as conn:
        with conn.cursor() as my_cursor:
            match status:
                case 1:
                    my_cursor.execute("UPDATE todos SET status ='CANCELLED' WHERE taskId = %s", (id,))
                case 2:
                    my_cursor.execute("UPDATE todos SET status ='COMPLETED' WHERE taskId = %s", (id,))
                case _:
                    print("Something went wrong...\nTry again later please\nSorry for inconvenience<3")
            conn.commit()
def profile(username,/):
    name: str = input("Enter your full name please(e.g John White):").strip()
    while True:
        gender: int = input("What gender are you?\n1.Male\n2.Female\nEnter here(e.g 1 or 2)\n>>>").strip()
        birthday: str = input("Enter the date of your birthday\nIn the format YYYY-mm-dd(e.g 2008-06-30)\n>>>").strip()
        try:
            gender = int(gender)
            datetime.strptime(birthday, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid input!\nPlease try again...")
    with get_connection() as conn:
        with conn.cursor() as my_cursor:
            my_cursor.execute("UPDATE users SET name = %s, sex = %s, bday = %s WHERE username = %s",(name,gender,birthday,username))
            conn.commit()
def main_menu(username): 
    print("\n----------Welcome to ToDoList Manager!----------")
    while True:
        print("\n1.Create a new list!")
        print('2.Assign the status of the plan')
        print("3.Remove the list")
        print("4.Display all my plans")
        print("5.Profile")
        print("6.Log out...")
        choice: str = input("\nEnter a digit(1-6) please\nEnter your choice:")
        try:
            choice = int(choice) 
        except ValueError:
            print("Invalid input!\nPlease enter a digit from 1 to 6...")
            continue
        if choice == 1:
            create_new(username)
        elif choice == 2:
            status_change(username)
        elif choice == 3:
            delete_item(username)
        elif choice == 4:
            print_all(username)
        elif choice == 5:
            profile(username)
        elif choice == 6:
            break
        else:
            print("\nYou have entered a wrong choice!\nPlease try again...")
            continue


