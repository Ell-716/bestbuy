class Store:
    """
    Represents a store that holds a collection of products.
    Attributes:
        list_of_products: A list of Product instances available in the store.
    """

    def __init__(self, list_of_products):
        """
        Initializes the Store with a list of products.
        Args:
            list_of_products: A list of Product instances to initialize the store with.
        """
        self.list_of_products = list_of_products

    def add_product(self, product):
        """
        Adds a new product to the store if it's not already present.
        Args:
            product: The product to add.
        """
        if product not in self.list_of_products:
            self.list_of_products.append(product)
            print(f"The product '{product.name}' has been successfully added to the store.")
        else:
            print(f"The product '{product.name}' is already in the store.")

    def remove_product(self, product):
        """
        Removes a product from the store if it exists.
        Args:
            product: The product to remove.
        """
        if product in self.list_of_products:
            self.list_of_products.remove(product)
            print(f"The product '{product.name}' has been successfully removed from the store.")
        else:
            print(f"There is no product '{product.name}' in the store.")

    def get_total_quantity(self):
        """
        Returns the total quantity of all products in the store.
        Returns:
            The total quantity of products.
        """
        return sum(product.quantity for product in self.list_of_products)

    def get_all_products(self):
        """
        Returns all active products in the store.
        Returns:
            A list of active Product instances.
        """
        return [product for product in self.list_of_products if product.is_active()]

    def order(self, shopping_list):
        """
        Processes an order for multiple products.
        Args:
            shopping_list: A list of tuples where each tuple contains
                           a Product and the quantity.
        Returns:
            The total price of the order.
        Raises:
            ValueError: If a product is not available in the store or if the product is inactive.
        """
        total_price = 0
        for product, quantity in shopping_list:
            if product not in self.list_of_products or not product.is_active():
                raise ValueError(f"The product '{product.name}' is not available in the store.")
            total_price += product.buy(quantity)
        return total_price
