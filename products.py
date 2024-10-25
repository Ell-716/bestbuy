class Product:
    """
        Represents a specific type of product available in the store.
        Attributes:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The current quantity of the product available in stock.
            active (bool): Indicates whether the product is active (available for sale).
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initializes a Product instance.
        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product in stock.
        Raises:
            ValueError: If the name is empty or if price/quantity is invalid (negative).
        """
        if not name:
            raise ValueError("The name can't be empty.")
        if not isinstance(price, (float, int)) or price < 0:
            raise ValueError("The price should be a positive number.")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("The quantity should be a positive number.")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True  # Product is active upon initialization.

    def get_quantity(self) -> int:
        """
        Returns the current quantity of the product.
        Returns:
            int: The quantity of the product.
        """
        return self.quantity

    def set_quantity(self, quantity: int):
        """
        Sets the quantity of the product.
        Args:
            quantity (int): The new quantity of the product.
        Raises:
            ValueError: If the quantity is invalid (negative).
        """
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("The quantity should be a positive number.")
        self.quantity = quantity
        # Deactivate the product if the quantity reaches 0.
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """
        Checks if the product is active.
        Returns:
            bool: True if the product is active, False otherwise.
        """
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def show(self) -> str:
        """
        Returns a string representation of the product.
        Returns:
            str: A string showing the product's name, price, and quantity.
        """
        return f"{self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        """
        Buys a given quantity of the product.
        Args:
            quantity (int): The quantity to purchase.
        Returns:
            float: The total price of the purchase.
        Raises:
            ValueError: If the quantity is invalid (negative),
                        exceeds available stock,
                        or if the product is inactive.
        """
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("The quantity should be a positive number.")
        if quantity > self.quantity:
            raise ValueError(f"The quantity of {self.name} is bigger than the available stock.")
        if not self.active:
            raise ValueError("This product is inactive.")

        self.set_quantity(self.quantity - quantity)  # Update quantity after purchase.

        return round(self.price * quantity, 2)


class NonStockedProduct(Product):
    """
        Represents a non-stocked product, typically a digital item that doesn’t require inventory tracking.
        Quantity is always zero for this type of product.
        Attributes:
            name (str): The name of the product.
            price (float): The price of the product.
    """
    def __init__(self, name: str, price: float, quantity=0):
        """
            Initializes a NonStockedProduct instance with a fixed quantity of zero.
            Args:
                name (str): The name of the product.
                price (float): The price of the product.
        """
        super().__init__(name, price, quantity=0)

    def show(self) -> str:
        """
            Returns a string representation of the non-stocked product.
            Returns:
                str: A string showing the product's name and price, without quantity.
        """
        return f"{self.name}, Price: ${self.price:.2f}"


class LimitedProduct(Product):
    """
    Represents a product with a strict purchase limit, restricting the purchase
    to only one unit per transaction.
    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.
        quantity (int): The available quantity of the product in stock.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initializes a LimitedProduct instance with a fixed max_purchase of 1.
        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The available quantity of the product in stock.
        """
        super().__init__(name, price, quantity)
        self.max_purchase = 1  # Fixed to allow only one unit per purchase

    def show(self) -> str:
        """
        Returns a string representation of the limited product.
        Returns:
            str: A string showing the product's name, price, quantity, and maximum purchase limit.
        """
        return (f"{self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}, "
                f"Maximum purchase: {self.max_purchase}")

    def buy(self, quantity: int) -> float:
        """
        Buys a given quantity of the product, ensuring it doesn't exceed the fixed max purchase limit of 1.
        Args:
            quantity (int): The quantity to purchase.
        Returns:
            float: The total price of the purchase.
        Raises:
            ValueError: If the quantity exceeds the max purchase limit.
        """
        if quantity > self.max_purchase:
            raise ValueError("Error while making order! Only 1 unit can be purchased.")

        # Use the parent class's buy() method to complete the purchase
        return super().buy(quantity)
