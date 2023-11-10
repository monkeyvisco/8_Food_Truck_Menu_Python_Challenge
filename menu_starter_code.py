## _______ INTRODUCTION

# Description: Interactive ordering system for a food truck menu.

# Functionality:
# initilizes an order list
# prompt user for their 1st item selection
# store users 1st item selection as a variable called 'menu_selection'

## _______ CODE
# 1. Define a top level dictionary, "menu", for the food truck menu. 

# About Dictionaries...

# In Python, a dictionary is a DATA STRUCTURE that allows you to store and 
# manage data in a key-value pair format. example: "Cookie": .99
# Cookie is the key, .99 is the value.

# Dictionaries are composed of key-value pairs,
# where each key is unique and maps to a specific value.

# In the context of dictionaries in programming, "keys" refer to the names or
# labels used to access the associated values within the dictionary.

# The Python code menu = {} creates an empty (contains no key-value pairs) 
# dictionary named menu_items.  The key-value pairs can be set inside of the
# curly brackets {} as shown in the code below.

# Below code ontains nested dictionaries. Example: "Pizza" and "Burger" are
# nested dictionaries within the dictionary "Meals", which is a nested
# dictionary within the dictionary "menu".

# "Snacks," "Meals," "Drinks," and "Dessert" are keys in the top-level
# dictionary, each with its own associated value.

# Within the "Meals" key, you have the "Burrito," "Teriyaki Chicken," "Sushi,"
# "Pad Thai," "Pizza," and "Burger" keys, each with its associated value.

# The "Pizza" and "Burger" keys have their own nested dictionaries that
# specify different varieties and their prices.

menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# TAKE CUSTOMERS SINGLE- or MULTIPLE-ITEM ORDER and STORE IT in a ?LIST?

# OBJECTIVES
# 1. Enable the ability to store the customer's order.
# Define a 'list of dictionaries' called customer_order.
# Dictionaries in the list customer_order list:
#   menu_item_name
#   item_price
#   quantity_ordered
# 2. Enable user to order multiple items. 
# This means we need a continuous loop! But, first we need to set a control
# flag for the while loop so there can be an exit from the loop.
# 
# place_order = True: initializes a boolean variable place_order 
# and sets it to True.
#
# "while place_order:" command starts a while loop that continues as long as 
# the place_order variable is True. Inside the while loop, the user is asked
# for input ("From which menu would you like to order?) and displays options.
# 
# i = 1: initializes a variable i to 1. i will be used to keep track of menu
# item numbers within chosen menu category.
# 
# menu_items = {}: initializes empty dictionary called menu_items.

# Create a variable for the menu item number
i = 1
# Create a dictionary to store the menu for later retrieval
menu_items = {}

# Define an empty order list to store the customer's selections
order = []

# Main ordering loop
while True:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Ask the user for input
    user_choice = int(input("What Snack item would you like to order? Enter the item number: "))

    # Use 'user_choice' to look up the corresponding menu category in 'menu_items' dictionary.
    if user_choice in menu_items:
        selected_category = menu_items[user_choice]
        print(f"You have selected: {selected_category}")
    else:
        print("Invalid choice. Please enter a valid item number.")
        continue  # Start over if the choice is invalid

    # Get the customer's input for the menu item number
    menu_category_name = menu_items[user_choice]

    # Print out the menu options from the selected menu_category_name
    print(f"What {menu_category_name} item would you like to order?")
    i = 1
    menu_items = {}
    print("Item # | Item name                | Price")
    print("-------|--------------------------|-------")

    for key, value in menu[menu_category_name].items():
        # Check if the menu item is a dictionary to handle differently
        if type(value) is dict:
            for key2, value2 in value.items():
                num_item_spaces = 24 - len(key + key2) - 3
                item_spaces = " " * num_item_spaces
                print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                menu_items[i] = {
                    "Item name": key + " - " + key2,
                    "Price": value2
                }
                i += 1
        else:
            num_item_spaces = 24 - len(key)
            item_spaces = " " * num_item_spaces
            print(f"{i}      | {key}{item_spaces} | ${value}")
            menu_items[i] = {
                "Item name": key,
                "Price": value
            }
            i += 1

    # Ask the customer to input the menu item number
    while True:
        menu_item_number = int(input("Enter the item number you want to order: "))

        if menu_item_number in menu_items:
            # Store the item name as a variable
            item_name = menu_items[menu_item_number]["Item name"]

            # Ask the customer for the quantity of the menu item
            quantity = int(input(f"How many {item_name} would you like to order? (Enter a number): "))

            if quantity > 0:
                # Add the item name, price, and quantity to the order list
                order.append({
                    "Item name": item_name,
                    "Price": menu_items[menu_item_number]["Price"],
                    "Quantity": quantity
                })
                print(f"{quantity} {item_name} added to your order.")
            else:
                print("Invalid quantity. Please enter a valid number greater than 0.")
        else:
            print("Invalid item number. Please enter a valid item number.")
            continue  # Start over if the item number is invalid

        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ").strip().lower()

        if keep_ordering == "n":
            break  # Exit the ordering loop if the customer doesn't want to order more

# Print out the customer's order
print("This is what we are preparing for you.\n")

total_price = 0

print("Item name                 | Price  | Quantity | Subtotal")
print("--------------------------|--------|----------|---------")
for item in order:
    item_name = item["Item name"]
    price = item["Price"]
    quantity = item["Quantity"]
    subtotal = price * quantity
    total_price += subtotal
    print(f"{item_name} | ${price:.2f} | {quantity} | ${subtotal:.2f}")

print(f"Total Price: ${total_price:.2f}")

# Check if the order is empty to display the completion message
if not order:
    print("Your complete order has been received.")



# 6. Loop through the items in the customer's order

    # 7. Store the dictionary items as variables


    # 8. Calculate the number of spaces for formatted printing


    # 9. Create space strings


    # 10. Print the item name, price, and quantity


# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.



# Notes
# View menu -> Shift Command P = Command Palette. Sets advanced autofill.
# File -> Auto Save