import time
import os
from model.product import Product
from model.client import Client
from model.dataStore import LoadClients, LoadProducts, SaveClients, SaveProducts

Clients  = LoadClients()    # carga desde data/clients.json (o {} si no existe)
Products = LoadProducts()   # carga desde data/products.json (o inventario por defecto)


def buy():
    car = {}
    totalPrice = 0
    while True:
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
                SaveProducts(Products)
            else:
                print('Theres not enough products!')
        else:
            print('Invalid Product, it doesnt exist!')

    print(totalPrice)
    print(car)
    ShowInventory()


def ShowInventory():
    print("Inv Logic")
    for key, prod in Products.items():
        print(key, 'Quantity:', prod.Quantity, 'Price:', prod.Price)


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
    client = Client(n, idn, phoneN)
    Clients[idn] = client
    SaveClients(Clients)        # guardamos nuevo cliente
    countClients = len(Clients) # cant clientes
    print(f'You have successfully registered!\n Welcome {n} you are the client #{countClients}!')
    time.sleep(1)
    clearScreen()


def Menu():
    while True:
        print("\n— Welcome to the Menu! —")
        print("1. Buy")
        print("2. See Inventory")
        print("3. Register")
        print("4. Check Client List")
        print("100. Leave")

        option = input("Select an option :D!!! :  ")

        if option == "1":
            buy()
        elif option == "2":
            ShowInventory()
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
    SaveClients(Clients)        # guardado final al salir
    SaveProducts(Products)

