
def Menu():
    while True:
        print("\n— Welcome to the Menu! —")
        print("1. Buy")
        print("2. See Inventory")
        print("3. Leave")
        option = input("Select an option :D!!! :  ")

        if option == "1":
            #buy()               #buy!
        elif option == "2":
            #ShowInventory()  #fix
        elif option == "3":
            print("See u soon!!!")
            break
        else:
            print("Invalid option! Try again!")

if __name__ == "__main__":
    Menu()

