# This program is an inventory presentation.

# Creating a class named Shoes with the relevant attributes.

#========The beginning of the class==========

class Shoe:

    def __init__(self, country, code, product, cost, quantity):

        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

# Defining methods inside the class.

    def get_cost(self):

        return self.cost

    def get_quantity(self):
        
        return self.quantity

    def __str__(self):

        return f"Country: {self.country} Code: {self.code} Name: {self.product} Cost: {self.cost} Quantity: {self.quantity}"

# Creating empty list variable to store a list of shoes objects.

#=============Shoe list===========

shoe_list = []

# Creating the appropriate functions outside the class.

#==========Functions outside the class==============

# Function to read information from the file and to store it in created empty list.
# Reading from the second line in the file and using try-except block in case the file is missing.

def read_shoes_data():

    try:
        with open ("inventory.txt", "r") as warehouses:
            next(warehouses)
            for product in warehouses:
                product = product.split(",")
                shoe_list.append(Shoe(product[0], product[1], product[2], int(product[3]), int(product[4])))
    except FileNotFoundError as error:
        print("The file you were trying to open does not exist.")
        print(error)

# Function to add a new shoe object into the list and to write it in the file. 

def capture_shoes():

    country_ = input("Enter the country where the product is located: ")
    code_ = input("Enter the code of the product: ")
    product_ = input("Enter the name of the product: ")

    while True:
        try:
            cost_ = int(input("Enter the cost of the product: "))
            break
        except ValueError:
            print("Try entering a valid number.")
    while True:
        try:
            quantity_ = int(input("Enter the quantity of the product: "))
            break
        except ValueError:
            print("Try entering a valid number.")
    shoe_list.append(Shoe(country_, code_, product_, cost_, quantity_))

    with open ("inventory.txt", "a") as file:
        file.write(f"\n{country_},{code_},{product_},{cost_},{quantity_}")

    print("Your input was added to the inventory.")

# Function to display all the objects stored in the file with all the relevant data.
   
def view_all():

    shoe_number = 0

    for shoes in shoe_list:
        shoe_number += 1
        print("_______________________________________________________________________________________\n")
        print(f"Shoe number [{shoe_number}] details:\n\n{shoes}")

# Function that identifies the lowest quantity shoe objects in the stock.
# Low quantity products are displayed and then an option to add more stock is offered.
# Finally, the new value is updated and written to the file.  

def re_stock():

    list_to_be_sorted = []

    for shoes in shoe_list:
        list_to_be_sorted.append(shoes.get_quantity())

    sortlist = sorted(list_to_be_sorted)
    minquantity = sortlist[0]

    print("Below are the product(s) with the lowest quantity:")

    shoe_number = 0
    
    for shoes in shoe_list:
        shoe_number += 1
        if minquantity == shoes.get_quantity():
            print("_______________________\n")
            print(f"Shoe number [{shoe_number}] details:\n\n{shoes}")
            print("_______________________")

    print("Select your option:\na - add stock\ne - exit")

    user_stock_selection = input("Enter you selection: ")
    replaced = []

    if user_stock_selection == "a":
        while True:
            try:
                user_stock_quanitity = int(input("Product(s) quantity increase number by: "))
                break
            except ValueError:
                print("Try entering a valid number.")
        for shoes in shoe_list:
            if minquantity == shoes.get_quantity():
                shoes.quantity += user_stock_quanitity
                replaced.append(shoes)
            else:
                replaced.append(shoes)
        with open ("inventory.txt", "w") as file:
            file.write("Country,Code,Product,Cost,Quantity")
        for shoes in replaced:
            with open ("inventory.txt", "a") as file:
                file.write(f"\n{shoes.country},{shoes.code},{shoes.product},{shoes.cost},{shoes.quantity}")
        print("Stock was updated.")
    elif user_stock_selection == "e":
        print("Low stock was not changed.")
    else:
        print("Wrong input.")

# Function that allows to search apropriate shoe objects by their shoe code and displays them.

def search_shoe():

    shoe_code = input("Enter the code of the product: ")
    counter = 0
    shoe_number = 0

    for shoes in shoe_list:
        shoe_number += 1
        if shoe_code == shoes.code:
            print("_______________________\n")
            print(f"Shoe number [{shoe_number}] details:\n\n{shoes}")
            print("_______________________")
            counter += 1

    if counter == 0:
        print("No such code.")

# Function that returns/displays the value for every shoe object and a total value of the stock.

def value_per_item():

    shoe_number = 0
    total_value = 0

    for shoes in shoe_list:
        value = shoes.get_cost() * shoes.get_quantity()
        total_value += value
        shoe_number += 1
        print("_______________________\n")
        print(f"Shoe number [{shoe_number}] details and value:\n{shoes}\nStock value: {value}")
        print("_______________________")
        print()
    print(f"Total value of {shoe_number} shoe types is {total_value}.")   

# Function that indentifies/displays highest quantity shoe objects. 
# It prints out the information abot them being on sale.

def highest_qty():

    list_to_be_sorted_and_reversed = []

    for shoes in shoe_list:
        list_to_be_sorted_and_reversed.append(shoes.get_quantity())

    sortedlist = sorted(list_to_be_sorted_and_reversed)
    reversedlist = sortedlist[::-1]
    maxquantity = reversedlist[0]

    shoe_number = 0

    for shoes in shoe_list:
        shoe_number += 1
        if maxquantity == shoes.get_quantity():
            print("_______________________\n")
            print(f"Shoe number [{shoe_number}] details:\n\n{shoes}")
            print("_______________________")
            print("The sale is on for above product(s).")

# Creating main menu for the inventory presentation.
# Utilising all the above created functions in order to have fully functional program.

#==========Main Menu=============

read_shoes_data()

while True:

    print("\nPlease select one of the following options:\n\n[1] - view the whole stock\n[2] - add a new shoe product to the stock")
    print("[3] - re-stock low volume product(s)\n[4] - display highest volume product(s)\n[5] - search for a product by the shoe code ")
    print("[6] - display value of each item and all items in total\n[7] - exit")

    menu = input("\nEnter your selection: ")

    if menu == "1":
        
        view_all()

    elif menu == "2":

        capture_shoes()
    
    elif menu == "3":
        
        re_stock()
    
    elif menu == "4":

        highest_qty()

    elif menu == "5":

        search_shoe()
    
    elif menu == "6":

        value_per_item()

    elif menu == "7":

        print("Bye, bye!")

        exit()
    
    else:

        print("Wrong selection. Try again.")