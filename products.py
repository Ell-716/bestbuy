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

        return round(self.price * quantity, 2)  # Return total price rounded to 2 decimal places.
