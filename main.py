Products = {

    #Product : {Quantity : q, Price: p},
    'Water': {'Quantity': 10,
              'Price': 3000
    },

    'Apple': {'Quantity': 5,
              'Price': 500},
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
        quant = int(input("How much would you like?"))
        if product in Products and Products[product]['Quantity'] >= quant:
            Products[product]['Quantity'] -= quant
            totalPrice += Products[product]['Price'] * quant
            car[product] = totalPrice
        else:
            print('Theres no products!')
        #Add exceptions! asap


    print(totalPrice)
    print(car)
    print(Products)

def ShowInventory():
    print("Inv Logic")
    print(Products)


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

