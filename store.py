class Store:
    """
    Represents a store that holds a collection of products.
    Attribute (accessible via properties):
        list_of_products (list): A list of Product instances available in the store.
    """

    def __init__(self, list_of_products: list):
        """
        Initializes the Store with a list of products.
        Args:
            list_of_products (list): A list of Product instances to initialize the store.
        """
        self._list_of_products = list_of_products

    def __contains__(self, product):
        """
        Checks if the given product exists in the store.
        Args:
            product (Product): The product instance to check for existence in the store.
        Returns:
            bool: True if the product exists in the store, False otherwise.
        """
        return product in self._list_of_products

    def __add__(self, store):
        """
        Combines two Store instances into a new Store instance containing products from both stores.
        Args:
            store (Store): The Store instance to combine with the current store.
        Returns:
            Store: A new Store instance containing products from both stores.
        Raises:
            TypeError: If the object being added is not an instance of Store.
        """
        if not isinstance(store, Store):
            raise TypeError("Only Store instances can be added together.")

        return Store(self._list_of_products + store.all_products)

    @property
    def list_of_products(self) -> list:
        """Getter for the list of products in the store."""
        return self._list_of_products

    @list_of_products.setter
    def list_of_products(self, products: list):
        """Setter for the list of products in the store."""
        if not isinstance(products, list):
            raise ValueError("Products should be provided as a list.")
        self._list_of_products = products

    def add_product(self, product):
        """
        Adds a new product to the store if it's not already present.
        Args:
            product (Product): The product to add.
        """
        if product not in self._list_of_products:
            self._list_of_products.append(product)
            print(f"The product '{product.name}' has been successfully added to the store.")
        else:
            print(f"The product '{product.name}' is already in the store.")

    def remove_product(self, product):
        """
        Removes a product from the store if it exists.
        Args:
            product (Product): The product to remove.
        """
        if product in self._list_of_products:
            self._list_of_products.remove(product)
            print(f"The product '{product.name}' has been successfully removed from the store.")
        else:
            print(f"There is no product '{product.name}' in the store.")

    @property
    def total_quantity(self) -> int:
        """
        Returns the total quantity of all products in the store.
        Returns:
            int: The total quantity of products.
        """
        return sum(product.quantity for product in self._list_of_products)

    @property
    def all_products(self) -> list:
        """
        Returns all active products in the store.
        Returns:
            list: A list of active Product instances.
        """
        return [product for product in self._list_of_products if product.is_active()]

    def order(self, shopping_list: list) -> float:
        """
        Processes an order for multiple products.
        Args:
            shopping_list (list): A list of tuples where each tuple contains
                                  a Product and the quantity.
        Returns:
            float: The total price of the order.
        Raises:
            ValueError: If a product is not available in the store or if the product is inactive.
        """
        total_price = 0
        for product, quantity in shopping_list:
            if product not in self._list_of_products or not product.is_active():
                raise ValueError(f"The product '{product.name}' is not available in the store.")
            total_price += product.buy(quantity)
        return total_price
