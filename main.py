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


def Menu():
    while True:
        print("\n— Welcome to the Menu! —")
        print("1. Buy")
        print("2. See Inventory")
        print("3. Leave")
        option = input("Select an option :D!!! :  ")

        if option == "1":
            buy()               #buy!
        elif option == "2":
            ShowInventory()  #fix
        elif option == "3":
            print("See u soon!!!")
            break
        else:
            print("Invalid option! Try again!")

if __name__ == "__main__":
    Menu()

