#Main manager of the console app to manage ToDo lists
import datetime as dt
import os 
import json
counter = NotImplemented
def delete_item(username):
    if os.path.exists(f"{username}.json"):
        data = print_all(username)
        while True:
            try:    
                choice = input("\nEnter the number of the plan you want to delete:")
                deleted_value = data.pop(int(choice))
                print(f"\n{deleted_value} is deleted from your list!!!\n")
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
    global counter 
    plan = input("\nEnter you plan here\n>>>")
    due_time = input("Format: YYYY.mm.dd: 2025.01.15\nEnter the due date:")
    if os.path.exists(f"{username}.json"):
        with open(f"{username}.json", 'r', encoding='utf8') as files:
            data = json.load(files)
            counter = len(data.keys())+1
    else:
        data = {}
        counter = 1 
    data[counter] = [plan,dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), due_time, "Created" ]    
    with open(f"{username}.json", 'w', encoding='utf8') as save:
            json.dump(data, save, indent = 4, ensure_ascii=False)
    counter += 1
        
def status_change(username, status = "Created"):
    if os.path.exists(f"{username}.json"):
        data = print_all(username)
        while True:
            try:
                choice = input("Enter the number of the plan you want to change the status of:")
                data[choice][3] = status
                break
            except (ValueError,KeyError):
                print(f"\nInvalid input\nTry to enter an integer please...\nFrom 1 to {counter}<3")
        with open(f"{username}.json", 'w', encoding="utf8") as write:
            json.dump(data, write, indent=4, ensure_ascii=False)
    else:
        print("\nError!\nYou have no active plans now...\nCreate one first please<3\n")
def main_menu(username): 
    __username = username
    print("\n----------Welcome to ToDoList Manager!----------\n")
    while True:
        print("1.Create a new list!")
        print('2.Assign the status of the plan')
        print("3.Remove the list")
        print("4.Display all my plans")
        print("5.Log out...")
        choice = input("\nEnter a digit(1-5) please\nEnter your choice:")
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
            break
        else:
            print("\nYou have entered a wrong choice!\nPlease try again...")
            continue