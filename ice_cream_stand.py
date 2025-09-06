"""
STARTER CODE
Homework 2: Ice Cream Stand
Topics Covered:
- Lists (append, pop)
- For and while loops
- Getting user inputs
- Validating user inputs
- Functions and helper functions
- Formatted Strings
"""

# TODO: Students, fill out statement of work header
# Student Name in Canvas: David Williams
# Penn ID: 58041486
# Did you do this homework on your own (yes / no): yes
# Resources used outside course materials: YouTube Videos, Code Academy

# import statements
#Note we use from ... import ... 
#This means you can use randint directly without random.randint()
from random import randint, choice


def print_welcome_and_menu(list_of_flavors, list_of_sizes, list_of_prices):
    print("Welcome to Penn's Student Run Ice Cream Stand!")
    print()
    print("Here are the flavors we have available:")
    print()
    for flavor in list_of_flavors:
        print("–", flavor)
        print()
    print("Here are the sizes and prices:")
    print()
    for i in range(len(list_of_sizes)):
        size = list_of_sizes[i]
        price = list_of_prices[i]
        print("Our", size, "ice cream is $", price)
        print()
        
    """
    Prints the following:
    1. Welcome message (Must contain word 'welcome')
    2. Message on what flavors are available in the ice cream store.
        Hint: Loop through the list_of_flavors
    3. Message on how much each size cost.
        Hint: Loop through the list_of_sizes, list_of_prices
        Format should be: Our {size} ice cream is ${price}.
    """
    # TODO: Write your code here
    pass    # TODO: Remove the pass statement once you have your code written



def get_order_qty(customer_name):
    """
    Ask the customer how many orders of ice cream they want.
    Valid order quantity should be an integer 1-5 inclusive. If outside the range or non-int, re-prompt.
    Hint: When asking for user input, cast it to an integer. If the input cannot be cast-ed to an integer, re-prompt.
    "2.55", "abc", "   ", are a few examples of what should all re-prompt the user.
    Returns: How many orders of ice cream the customer wants.
    """
    order_qty = 0
    # TODO: Write your code here
    while True: #Ask user ntil a valid answers is recieved
        print()
        order_input = input(f"{customer_name}, how may ice creams would you like (1-5)? ")
        print()
        try:
            #Attempting to convert the input into an integer
            order_qty = int(order_input)
            #Determing if the entered input is between 1 and 5)
            if 1 <= order_qty <= 5:
                return order_qty
            else:
                print("Please enter a number between 1 and 5.")
                print()
        except ValueError:
            print()
            #If anything other then an integer is entered
            print("An invalid input was entered. Please enter a whole number between 1 and 5 only.")


def get_ice_cream_flavor(ice_cream_flavors):
    """
    Ask the customer 'Which flavor would you like (v/c/s)? '
    Then, processes and cleans the input and returns the equivalent flavor from ice_cream_flavors list.
    Hint:   Use the indices set in the main function for the flavors.
            Call the get_first_letter_of_user_input function to get and process inputs.
            Note: Only the first letter of the input will be considered so an input of 'Cookies and Cream'
            will be considered as 'c' which corresponds to 'Chocolate'.
            Ask again if it is not a valid flavor.
    Returns: String of ice cream flavor picked (e.g "Vanilla")
    """
    flavor_picked = ""
    # TODO: Write your code here
    while True:
        #Which flavor does the user want?
        first_letter = get_first_letter_of_user_input("Which flavor would you like (v/c/s)? ")
        
        #Only using the first letter of the flavor/input
        
        if first_letter == "v": #For Vanilla flavor
            flavor_picked = ice_cream_flavors[0]
            break
        elif first_letter ==  "c": #For Chocolate flavor
            flavor_picked = ice_cream_flavors[1]
            break
        elif first_letter ==  "s": #For Strawberry flavor
            flavor_picked = ice_cream_flavors[2]
            break
        else:
            print()
            print("Invalid input. Please type v, c, or s.")
            print()
    return flavor_picked


def get_ice_cream_size(ice_cream_sizes):
    """
    Ask the customer 'Which size would you like (s/m/l)? '
    Then, processes and cleans the input and returns the equivalent size from ice_cream_sizes list.
    Hint:   Use the indices set in the main function for the sizes.
            Call the get_first_letter_of_user_input function to get and process inputs.
            Note: Only the first letter of the input will be considered so an input of 'Super Large'
            will be considered as 's' which corresponds to 'Small'.
            Ask again if it is not a valid size.
    Returns: String of Size picked (e.g "Small")
    """
    size_picked = ""
    # TODO: Write your code here
    while True:
        #Asking the user what size ice cream they want
        first_letter = get_first_letter_of_user_input("Which size would you like (s/m/l)? ")

        #Only accpet the first letter
        if first_letter == "s": #Small
            size_picked = ice_cream_sizes[0]
            break
        elif first_letter == "m": #Medium
            size_picked = ice_cream_sizes[1]
            break
        elif first_letter == "l": #Large
            size_picked = ice_cream_sizes[2]
            break
        else:
            print()
            print("Invalid input. Please type s, m, or l.")
            print()
    return size_picked


def get_ice_cream_order_price(ice_cream_size, ice_cream_prices, ice_cream_sizes):
    """
    Hint:   Use the indices set in the main function for the prices of Small, Medium and Large.
    Returns: The equivalent price of an ice cream size. Example: Returns 4.99 if ice_cream_size is 'Small'
    """
    # TODO: Write your code here
    
    if ice_cream_size == ice_cream_sizes[0]:
        return ice_cream_prices[0]
    elif ice_cream_size == ice_cream_sizes[1]:
        return ice_cream_prices[1]
    elif ice_cream_size == ice_cream_sizes[2]:
        return ice_cream_prices[2]
    else:
        return 0

def take_customer_order(customer_name, ice_cream_flavors, ice_cream_sizes, ice_cream_prices):
    """
    This function runs when a customer reaches the front of the queue. It should print
    the current customer's name being served, and take their order(s).
    If the customer can pay for their order, returns the amount of revenue from the sale.
    If the customer cancels their order, returns 0.
    Hint: Use other helper functions we required you to write whenever needed here.
    This includes the use of help functions like get_first_letter_of_user_input
    Returns: Amount of Revenue from the sale with customer
    """

    total_bill = 0
    #Message showing which customer we are currently serving
    print("Now serving customer:", customer_name)
    
    # TODO: Call the get_order_qty and save the value to order_qty
    order_qty = get_order_qty(customer_name)

    # TODO: For Each order you need to get a flavor, and size
    for order in range(order_qty):
        print("Order No.:", order + 1)
        
        # TODO: Write code to get the ice cream flavor for this order
        flavor_picked = get_ice_cream_flavor(ice_cream_flavors)

        # TODO: Write code to get the ice cream size for this order
        size_picked = get_ice_cream_size(ice_cream_sizes)

        # TODO: Write code to get the price for this order
        order_price = get_ice_cream_order_price(size_picked, ice_cream_prices, ice_cream_sizes)

        # TODO: Update the total_bill
        total_bill += order_price

        # TODO: Print the details for this order
        print("–>", flavor_picked, "–", size_picked, "– $", round(order_price,2))
        print()
    # TODO: Print the customer's total_bill
    print("Total bill for", customer_name, ": $", round(total_bill, 2))

    # TODO: Once orders are all taken, the customer should be asked if they still want to Pay or Cancel
    while True:
        #  "Would you like to pay or cancel the order (p/c)? "
        last_decision = get_first_letter_of_user_input("Would you like to pay or cancel the order (p/c)? ")
        if last_decision == "p":
            print(customer_name, "you have paid successfully.")
            print()
            return total_bill
        elif last_decision == "c":
            print(customer_name, "your order has been cancelled.")
            print()
            return 0
        else:
            print("You've entered an invalid input. Please enter p for pay or c for cancel.")

def get_first_letter_of_user_input(question):
    """
    Takes in a string as its argument, to be used as the question you want the user to be asked.
    Gets input from the user, you must use input() inside this function to pass tests
    Removes whitespace and makes all letters lowercase
    Hint: Use the strip() and lower() functions.
    Note: The question paramter is a string, such as "Which size would you like (s/m/l)?"
    Returns: The first letter of the input the user provides. Ask again if the input is empty.
    """
    first_letter = ""
    # TODO: Write your code here
    while True:
        user_input = input(question)
        if user_input.strip() == "":
            print("Please enter something.")
            continue
        # Removing whitespace and making all lowercase
        user_input = user_input.strip().lower()
        # Taking only the first letter of the user input
        first_letter = user_input[0]
        break
    return first_letter

def are_all_customers_served(customer_queue_length):
    """
    If there are no customers in the queue, returns True, and all customers have been served.
    Otherwise, returns False.
    Hint: The parameter customer_queue_length is of type int.
    Returns: True or False
    """
    # TODO: Write your code here
    if customer_queue_length == 0:
        return True
    else:
        return False

def print_current_status(customers_served, tracking_revenue):
    """
    Prints a message of how many customers have been served and the total sales of the ice cream stand.
    Hint: See https://www.w3schools.com/python/python_string_formatting.asp for string formatting examples on rounding to 2 decimal places
    No Return, only print statements
    """
    # TODO: Write your code here

    print("Customers served so far:", customers_served)
    print("Current total sales : $", round(tracking_revenue, 2))


def print_sales_summary(customers_served, tracking_revenue):
    """
    Takes in the arguments customers_served and tracking_revenue. Prints both
    arguments as strings to let the user know what those values are.
    Output should look something like:
        Total customers served: 3
        Total sales           : $xx.xx
    Hint: See https://www.w3schools.com/python/python_string_formatting.asp for string formatting examples on rounding to 2 decimal places
    No Return, only print statements
    """
    # TODO: Write your code here

    print("Total customers served:", customers_served)
    print("Total sales :$", round(tracking_revenue, 2))
    

def random_queue_length():
    """
    Takes no arguments.
    Uses the imported randint function to generate a random integer between 2 and 5 inclusive.
    Hint: See https://www.w3schools.com/python/ref_random_randint.asp
    Returns: The resulting random integer.
    """
    # TODO: Write your code here

    return randint(2,5)


def main():
    """
    Lists of available flavors, sizes and prices. DO NOT CHANGE.
    For sizes and prices, we will use the following convention:
    Index 0 for Small
    Index 1 for Medium
    Index 2 for Large
    """
    ice_cream_flavors = ['Vanilla', 'Chocolate', 'Strawberry']
    ice_cream_sizes = ['Small', 'Medium', 'Large']
    ice_cream_prices = [4.99, 7.49, 8.49]

    #List of names of possible customers
    customer_names = ["Alice", "Bob", "Charlie", "Dan", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"]

    program_running = True
    while program_running:
        # set shop to open
        input('Press enter to open the shop! ')
        queue_is_open = True

        # TODO: Call the print_welcome_and_menu function with the parameters in the following order -
        #  ice_cream_flavors, ice_cream_sizes, ice_cream_prices
        print()
        print_welcome_and_menu(ice_cream_flavors, ice_cream_sizes, ice_cream_prices)


        # set initial values
        tracking_revenue = 0

        # will hold the list of names of the customers in the queue
        customers_in_queue = []
        customers_served = 0

        # TODO: Call the random_queue_length function and save the result to num_of_customers_in_queue
        num_of_customers_in_queue = random_queue_length()

        # TODO: Print how many customers are in the queue
        print("Number of customers are in the queue:", num_of_customers_in_queue)

        # TODO: Call the imported choice function to generate a random name from customer_names.
        #   Then, append each name to the end of the customers_in_queue list.
        #   The total number of customer names added should be equal to num_of_customers_in_queue
        #   Hint: See https://www.w3schools.com/python/ref_random_choice.asp
        #   Note: It is OK to have duplicate names in the queue.
        for i in range(num_of_customers_in_queue):
            random_name = choice(customer_names)
            customers_in_queue.append(random_name)

        while queue_is_open:
            # TODO: Extract the first customer (index 0) from the customers_in_queue and save it to
            #  the current_customer_name variable.
            #  After extraction, the customer should now be removed from the customers_in_queue list.
            #  Hint: Use the pop function with an index argument
            current_customer_name = customers_in_queue.pop(0)

            # TODO: Take a customer at the window and update the revenue by calling the take_customer_order function
            revenue = take_customer_order(current_customer_name, ice_cream_flavors,  ice_cream_sizes, ice_cream_prices)
            tracking_revenue += revenue

            # TODO: Update the customers_served variable
            customers_served += 1

            # TODO: Call the print_current_status
            print_current_status(customers_served, tracking_revenue)
            print()

            # TODO: Call the are_all_customers_served(customer_queue_length) function to check if there are any more
            #  customers in the queue.
            #  If False, continue the loop.
            #  If True, call the print_sales_summary(customers_served, tracking_revenue) and close the queue

            if are_all_customers_served(len(customers_in_queue)):
                print_sales_summary(customers_served, tracking_revenue)
                queue_is_open = False
                
        # TODO: Ask if you want to open the ice cream stand again "Do you want to open again (y/n)? "
        #  Hint: Use the get_first_letter_of_user_input function
        #  Update the program_running variable if you get a valid answer either 'y' or 'n'
        #  Otherwise, re-prompt until a valid answer is given
        while True:
            open_again = get_first_letter_of_user_input("Do you want to open again (y/n)? ")
            if open_again == "y":
                program_running = True
                break
            elif open_again == "n":
                program_running = False
                print("The Ice Cream Shop is now closed for the day. Hope to see you again soon!")
                break
            else:
                print("You've entered an invalid inout. Please enter y or n.")

        
if __name__ == '__main__':
    main()

