import time as t
import registration as reg
def Menu(): #Menu function that prints the main menu on console
    while True:
        print("==========\n1. Login\n==========\n2. Registration\n==========\n3. Exit\n==========")
        choice = input("\nEnter your choice:")
        try:
            if int(choice)==3:
                cycles = 3
                print("Exitting")
                while cycles >0:
                    for i in range(1,4):
                        print('.'*i+" "*(3-i), end = '\r', flush = True)
                        t.sleep(0.7)
                    cycles-=1
                break
            elif int(choice)==2:
                reg.login()
            elif int(choice)==1:
                pass
        except ValueError:
            print("\nEnter an integer value please!")