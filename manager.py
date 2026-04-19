#Main manager of the console app to manage ToDo lists
import datetime as dt
import os 
import json
counter = 1
def create_new(username,plan):
    global counter
    due_time = input("Format: YYYY.mm.dd: 2025.01.15\nEnter the due date:")
    if os.path.exists(f"{username}.json"):
        with open(f"{username}.json", 'r', encoding='utf8') as files:
            data = json.load(files)
    else:
        data = {}
    data[counter] = [plan,dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), due_time, "Created" ]    
    with open(f"{username}.json", 'w', encoding='utf8') as save:
            json.dump(data, save, indent = 4, ensure_ascii=False)
    counter += 1
        
def status_change(username, status = "Completed"):
    if os.path.exists(f"{username}.json"):
        with open(f"{username}.json", "r", encoding="utf8") as read:
            data = json.load(read)
            counter = 1
            while counter <= len(data.keys()):
                print("="*10,f"\n{counter}.", end="")
                for element in data[str(counter)]:
                    print(f"{element}\n",'-'*10)
                counter += 1
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
    choice = None
    while True:
        print("1.Create a new list!")
        print('2.Assign the status of the plan')
        print("3.Remove the list.")
        print("4.Log out...")
        choice = input("\nEnter a digit(1-4) please\nEnter your choice:")
        try: 
            if int(choice) == 1:
                plan = input("\nEnter you plans here\n>>>")
                create_new(__username,plan)
            elif int(choice) == 2:
                status_change(__username)
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