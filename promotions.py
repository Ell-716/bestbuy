from abc import ABC, abstractmethod


class Promotion(ABC):
    """
    Abstract base class for promotions.
    Attributes:
        name (str): The name of the promotion.
    """

    def __init__(self, name: str):
        """
        Initializes a Promotion instance.
        Args:
            name (str): The name of the promotion.
        """
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
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
            raise ValueError("The quantity should be a positive number.")


class SecondHalfPrice(Promotion):
    """
    Represents a promotion where the second item is sold at half price.
    In this promotion, for every two items purchased, the second item is at half price.
    """

    def apply_promotion(self, product, quantity):
        """
        Applies the second item at half price promotion to a product.
        Args:
            product: The product instance on which the promotion is applied.
            quantity (int): The quantity of the product being purchased.
        Returns:
            float: The total cost after applying the promotion.
        """
        full_price_items = quantity // 2
        half_price_items = quantity // 2
        remaining_items = quantity % 2
        total_cost = (((full_price_items + remaining_items) * product.price) +
                      (half_price_items * (product.price * 0.5)))

        return total_cost


class ThirdOneFree(Promotion):
    """
    Represents a promotion where the third item is free.
    In this promotion, for every three items purchased, one item is free.
    """

    def apply_promotion(self, product, quantity):
        """
        Applies the buy two, get one free promotion to a product.
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
    In this promotion, a specified percentage discount is applied to the total cost of the product.
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
        self.percent = percent

    def apply_promotion(self, product, quantity):
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
        # Check if the product price is zero
        if product.price == 0:
            raise ValueError("The product price cannot be zero.")

        total_price = quantity * product.price
        discount_amount = total_price * (self.percent / 100)
        final_price = total_price - discount_amount
        return final_price
