#Main manager of the console app to manage ToDo lists
import datetime as dt
def create_new(username,plan):
    with open(f"{username}.txt", 'a') as files:
        due_date = input("\nEnter the data in Year-Month-Day format...\nEnter the due date of this task:")
        creation_time = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        files.write(f"{plan}\t-\t{creation_time}\n========================\nThe due date is {due_date}\n---------------------------------")
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