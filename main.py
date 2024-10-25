import products
import store

MENU = '''
STORE MENU
----------
1. List all products in the store
2. Show total amount in the store
3. Make an order
4. Quit
'''


def display_products(best_buy):
    """
    Displays all active products in the store with their details (name, price, quantity),
    prefixed by a number for easy selection.
    Args:
        best_buy (Store): The store object containing the products.
    """
    print("-" * 6)
    for index, product in enumerate(best_buy.get_all_products(), start=1):
        print(f"{index}. {product.show()}")
    print("-" * 6)


def display_total_items(best_buy):
    """
    Displays the total number of items available in the store.
    Args:
        best_buy (Store): The store object containing the products.
    """
    print(f"Total of {best_buy.get_total_quantity()} items in the store")


def make_order(best_buy):
    """
    Facilitates the ordering process. Displays available products,
    allows the user to select a product and quantity, adds them to the
    order list, and calculates the total payment.
    The user can finish the order by entering empty inputs.
    Args:
        best_buy (Store): The store object containing the products.
    """
    display_products(best_buy)
    print("When you want to finish the order, enter empty text.")

    order_list = []  # List to hold the items being ordered
    total_payment = 0  # Variable to track the total payment

    while True:
        available_products = best_buy.get_all_products()
        if not available_products:
            print("No products available for order.")
            break

        order_item = input("Which product would you like to order? ")
        order_quantity = input("What amount do you want? ")

        # If both inputs are empty, break out of the loop to finish the order
        if order_item == "" and order_quantity == "":
            break

        try:
            # If either input is empty, show an error and continue the loop
            if order_item == "" or order_quantity == "":
                print("Error adding product!\n")
                continue

            # Convert the inputs to integers for further processing
            order_item = int(order_item)
            order_quantity = int(order_quantity)

            # Ensure the selected product number is valid
            if 1 <= order_item <= len(available_products):
                product = available_products[order_item - 1]

                # Check if enough stock is available for the requested quantity
                if order_quantity > product.quantity:
                    print("Not enough stock available.\n")
                else:
                    # Add the product and quantity to the order list
                    order_list.append((product, order_quantity))
                    print("Product added to list!\n")
                    print()
            else:
                print("Invalid product number. Try again!\n")

        except ValueError:
            print("Error adding product!\n")

    # Process the order if the order list is not empty
    try:
        if order_list:
            for product, quantity in order_list:
                total_payment += product.buy(quantity)
            print("*" * 8)
            print(f"Order made! Total payment: ${total_payment:.2f}")
    except ValueError:
        print("Error while making order! Quantity larger than what exists.")


def start(best_buy):
    """
    Displays the main menu and handles user input for different store operations
    such as listing products, showing total quantity, making an order, or quitting.
    Args:
        best_buy (Store): The store object containing the products.
    """
    while True:
        try:
            print(MENU)
            choice = int(input("Please choose a number (1-4): "))

            if choice == 1:
                display_products(best_buy)
            elif choice == 2:
                display_total_items(best_buy)
            elif choice == 3:
                make_order(best_buy)
            elif choice == 4:
                break
            else:
                print("Invalid choice. Try again!")
        except ValueError:
            # Handle non-integer input for menu choices
            print("Invalid choice. Try again!")


def main():
    """
    The main function sets up the initial stock of products and starts the store interface.
    """
    # Setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    products.NonStockedProduct("Windows License", price=125),
                    products.LimitedProduct("Shipping", price=10, quantity=250, max_purchase=1)
                    ]

    # Create a Store object with the product list
    best_buy = store.Store(product_list)

    # Start the store interface
    start(best_buy)


if __name__ == "__main__":
    main()
