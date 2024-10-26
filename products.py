from promotions import Promotion


class Product:
    """
    Represents a specific type of product available in the store.
    Attributes (accessible via properties):
        name (str): The name of the product.
        price (float): The price of the product.
        quantity (int): The current quantity of the product available in stock.
        active (bool): Indicates whether the product is active (available for sale).
        promotion (Promotion): The current promotion applied to the product.
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
        self._name = name
        self._price = price
        self._quantity = quantity
        self._active = True  # Product is active upon initialization.
        self._promotion = None

    def __lt__(self, product):
        """
        Checks if this product's price is less than the price of another product.
        Args:
            product (Product): The product instance to compare against.
        Returns:
            bool: True if this product's price is less, False otherwise.
        Raises:
            TypeError: If the compared object is not an instance of Product.
        """
        if not isinstance(product, Product):
            raise TypeError("Comparisons must be between Product instances.")

        return self.price < product.price

    def __le__(self, product):
        """
        Checks if this product's price is less than or equal to the price of another product.
        Args:
            product (Product): The product instance to compare against.
        Returns:
            bool: True if this product's price is less than or equal, False otherwise.
        Raises:
            TypeError: If the compared object is not an instance of Product.
        """
        if not isinstance(product, Product):
            raise TypeError("Comparisons must be between Product instances.")

        return self.price <= product.price

    def __gt__(self, product):
        """
        Checks if this product's price is greater than the price of another product.
        Args:
            product (Product): The product instance to compare against.
        Returns:
            bool: True if this product's price is greater, False otherwise.
        Raises:
            TypeError: If the compared object is not an instance of Product.
        """
        if not isinstance(product, Product):
            raise TypeError("Comparisons must be between Product instances.")

        return self.price > product.price

    def __ge__(self, product):
        """
        Checks if this product's price is greater than or equal to the price of another product.
        Args:
            product (Product): The product instance to compare against.
        Returns:
            bool: True if this product's price is greater than or equal, False otherwise.
        Raises:
            TypeError: If the compared object is not an instance of Product.
        """
        if not isinstance(product, Product):
            raise TypeError("Comparisons must be between Product instances.")

        return self.price >= product.price

    def __eq__(self, product):
        """
        Checks if two products are considered equal based on their price.
        Args:
            product (Product): The product instance to compare against.
        Returns:
            bool: True if the prices of the two products are equal, False otherwise.
        Raises:
            TypeError: If the compared object is not an instance of Product.
        """
        if not isinstance(product, Product):
            raise TypeError("Comparisons must be between Product instances.")

        return self.price == product.price

    @property
    def name(self):
        """Public property to access the name of the product."""
        return self._name

    @property
    def price(self):
        """Public property to access the price of the product."""
        return self._price

    @property
    def quantity(self) -> int:
        """Returns the current quantity of the product."""
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: int):
        """
        Sets the quantity of the product.
        Args:
            quantity (int): The new quantity of the product.
        Raises:
            ValueError: If the quantity is invalid (negative).
        """
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("The quantity should be a positive number.")
        self._quantity = quantity
        # Deactivate the product if the quantity reaches 0.
        if self._quantity == 0:
            self.deactivate()

    @property
    def promotion(self) -> Promotion:
        """Returns the current promotion applied to the product."""
        return self._promotion

    @promotion.setter
    def promotion(self, promotion: Promotion):
        """
        Sets the promotion for the product.
        Args:
            promotion (Promotion): The promotion to apply to the product.
        Raises:
            ValueError: If the promotion is not an instance of the Promotion class.
        """
        if not isinstance(promotion, Promotion) and promotion is not None:
            raise ValueError("Promotion must be an instance of the Promotion class or None.")
        self._promotion = promotion

    def is_active(self) -> bool:
        """Checks if the product is active."""
        return self._active

    def activate(self):
        """Activates the product."""
        self._active = True

    def deactivate(self):
        """Deactivates the product."""
        self._active = False

    def __str__(self):
        """Returns a string representation of the product, including its promotion if available."""
        promotion_info = self.promotion.name if self.promotion else "None"
        return f"{self._name}, Price: ${self._price:.2f}, Quantity: {self.quantity}, Promotion: {promotion_info}"

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
            raise ValueError(f"The quantity of {self._name} is larger than available stock.")
        if not self.is_active():
            raise ValueError("This product is inactive.")

        self.quantity -= quantity  # Update quantity after purchase.

        return round(self._price * quantity, 2)


class NonStockedProduct(Product):
    """Represents a non-stocked product, typically a digital item that doesn't require inventory tracking."""
    def __init__(self, name: str, price: float):
        """Initializes a NonStockedProduct instance with a fixed quantity of zero."""
        super().__init__(name, price, quantity=0)

    def __str__(self):
        """Returns a string representation of the non-stocked product, including promotion details if available."""
        promotion_info = self.promotion.name if self.promotion else "None"
        return f"{self._name}, Price: ${self._price:.2f}, Quantity: Unlimited, Promotion: {promotion_info}"

    def buy(self, quantity: int) -> float:
        """
        Buys a given quantity of the non-stocked product without altering quantity.
        Returns:
            float: The total price of the purchase.
        """
        return round(self._price * quantity, 2)


class LimitedProduct(Product):
    """Represents a product with a strict purchase limit, restricting the purchase to only one unit per transaction."""

    def __init__(self, name: str, price: float, quantity: int):
        """Initializes a LimitedProduct instance with a fixed max_purchase of 1."""
        super().__init__(name, price, quantity)
        self._max_purchase = 1  # Fixed to allow only one unit per purchase

    def __str__(self):
        """Returns a string representation of the limited product."""
        promotion_info = self.promotion.name if self.promotion else "None"
        return (f"{self._name}, Price: ${self._price:.2f}, Limited to {self._max_purchase} per order!, "
                f"Promotion: {promotion_info}")

    def buy(self, quantity: int) -> float:
        """
        Buys a given quantity of the product, ensuring it doesn't exceed the
        fixed max purchase limit of 1.
        Raises:
            ValueError: If the quantity exceeds the max purchase limit.
        """
        if quantity > self._max_purchase:
            raise ValueError("Error while making order! Only 1 unit can be purchased.")

        # Use the parent class's buy() method to complete the purchase
        return super().buy(quantity)
