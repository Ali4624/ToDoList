#Main manager of the console app to manage ToDo lists
import datetime as dt
import os 
import json
def create_new(username,plan):
    due_time = input("Format: YYYY.mm.dd: 2025.01.15\nEnter the due date:")
    list = due_time.split(".")
    if os.path.exists(f"{username}.json"):
        with open(f"{username}.json", 'r', encoding='utf8') as files:
            data = json.load(files)
    else:
        data = {}
    data[plan] = [dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), due_time, "Created" ]    
    with open(f"{username}.json", 'w', encoding='utf8') as save:
            json.dump(data, save, indent = 4, ensure_ascii=False)
        
def main_menu(username): 
    __username = username
    print("\n----------Welcome to ToDoList Manager!----------\n")
    choice = None
    while True:
        print("1.Create a new list!")
        print('2.Mark list as completed.')
        print("3.Remove the list.")
        print("4.Log out...")
        choice = input("\nEnter a digit(1-4) please\nEnter your choice:")
        try: 
            if int(choice) == 1:
                plan = input("\nEnter you plans here\n>>>")
                create_new(username,plan)
            elif int(choice) == 2:
                pass
            elif int(choice) == 3:
                pass
            elif int(choice) == 4:
                break
            else:
                print("\nYou have entered a wrong choice!\nPlease try again...")
                continue
        except ValueError:
            print("Invalid input!\nPlease enter a digit from 1 to 4...")
            continue