from abc import ABC, abstractmethod


class Promotion(ABC):
    """
    Abstract base class for promotions.
    Attribute (accessible via properties):
        name (str): The name of the promotion.
    """

    def __init__(self, name: str):
        """
        Initializes a Promotion instance.
        Args:
            name (str): The name of the promotion.
        """
        self._name = name

    @property
    def name(self) -> str:
        """Getter for the promotion name."""
        return self._name

    @abstractmethod
    def apply_promotion(self, product, quantity: int):
        """
        Applies the promotion to a product for a given quantity.
        Args:
            product: The product instance on which the promotion is applied.
            quantity (int): The quantity of the product being purchased.
        Returns:
            float: The total cost after applying the promotion.
        Raises:
            ValueError: If the quantity is negative or not an integer.
        """
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("The quantity should be a positive integer.")


class SecondHalfPrice(Promotion):
    """
    Represents a promotion where the second item is sold at half price.
    """

    def apply_promotion(self, product, quantity: int):
        """
        Applies the second-item-at-half-price promotion.
        Args:
            product: The product instance on which the promotion is applied.
            quantity (int): The quantity of the product being purchased.
        Returns:
            float: The total cost after applying the promotion.
        """
        half_price_items = quantity // 2
        remaining_items = quantity % 2
        total_cost = ((half_price_items * (product.price * 0.5)) +
                      ((half_price_items + remaining_items) * product.price))
        return total_cost


class ThirdOneFree(Promotion):
    """
    Represents a promotion where the third item is free.
    """

    def apply_promotion(self, product, quantity: int):
        """
        Applies the buy-two-get-one-free promotion.
        Args:
            product: The product instance on which the promotion is applied.
            quantity (int): The quantity of the product being purchased.
        Returns:
            float: The total cost after applying the promotion.
        """
        free_items = quantity // 3
        paid_items = quantity - free_items
        total_cost = paid_items * product.price
        return total_cost


class PercentDiscount(Promotion):
    """
    Represents a percentage discount promotion.
    """

    def __init__(self, name: str, percent: (int, float)):
        """
        Initializes a PercentDiscount instance.
        Args:
            name (str): The name of the promotion.
            percent (int or float): The discount percentage to apply.
        Raises:
            ValueError: If the percent is not a positive number between 0 and 100.
        """
        super().__init__(name)
        if not isinstance(percent, (int, float)) or not (0 < percent < 100):
            raise ValueError("Percent should be a positive number between 0 and 100.")
        self._percent = percent

    def apply_promotion(self, product, quantity: int):
        """
        Applies the percentage discount promotion to a product.
        Args:
            product: The product instance on which the promotion is applied.
            quantity (int): The quantity of the product being purchased.
        Returns:
            float: The total cost after applying the promotion.
        Raises:
            ValueError: If the product price is zero, which may cause unexpected behavior.
        """
        if product.price == 0:
            raise ValueError("The product price cannot be zero.")

        total_price = quantity * product.price
        discount_amount = total_price * (self._percent / 100)
        final_price = total_price - discount_amount
        return final_price
