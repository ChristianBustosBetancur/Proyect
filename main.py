import time
import os

class Client:
    def __init__(self,name,id,phone):
        self.Name = name
        self.Id = id
        self.Phone = phone

    def __str__(self):
        return f"{self.Name} (ID: {self.Id}, Phone: {self.Phone})"
Clients = {} #Dict of all clients



class Product:
    def __init__(self, name, quantity, price):
        self.Name = name
        self.Quantity = quantity
        self.Price = price

Products = {
    #Instantiation of Products
    'Water': Product('Water', 10, 3000),
    'Apple': Product('Apple', 5, 500),
}


def buy():
    car = {}
    totalPrice = 0
    while True:

        #add a switch and change query for product, and query would be sometn else...
        #query =
        product = input("What product would u like to buy?")

        if product == '':
            break

        if product in Products:
            try:
                quant = int(input("How much would you like? "))
            except ValueError:
                print("Please enter a valid integer amount.")
                continue
            prod = Products[product]
            if prod.Quantity >= quant:
                prod.Quantity -= quant
                totalPrice += prod.Price * quant
                car[product] = totalPrice

            else:
                print('Theres not enough products!')
        else:
            print('Invalid Product, it doesnt exist!')
        #Add exceptions! asap


    print(totalPrice)
    print(car)
    ShowInventory()

def ShowInventory():
    print("Inv Logic")
    for key,prod in Products.items():
        print(key,'Quantity:', prod.Quantity, 'Price:', prod.Price)

def clearScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def Register():
    clearScreen()
    print("Welcome to the register section!")
    print("Please enter your name, id and your phone number :)")
    n = input("Enter your name:")
    idn = input("Enter your id:")
    phoneN = input("Enter your phone number:")
    client = Client(n,idn,phoneN)
    Clients[idn] = client
    countClients = len(Clients) #Quantity of clients
    print(f'You have successfully registered!\n Welcome {n} you are the client #{countClients}!')
    time.sleep(1)
    clearScreen()



#restructure all the menu and how the program will work
def Menu():
    while True:
        print("\n— Welcome to the Menu! —")
        print("1. Buy")
        print("2. See Inventory")
        print("3. Register")
        print('4. Check Client List')
        print("100. Leave")

        option = input("Select an option :D!!! :  ")

        if option == "1":
            buy()               #buy!
        elif option == "2":
            ShowInventory()  #fix
        elif option == "3":
            print('Register')
            Register()
        elif option == "4":
            print('Check Client List')
            for cid, client in Clients.items():
                print(f"- {cid}: {client}")
            input("\nPress Enter to continue...")

        elif option == "100":
            print("See u soon!!!")
            break
        else:
            print("Invalid option! Try again!")

if __name__ == "__main__":
    Menu()

