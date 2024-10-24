import unittest
from products import Product
from store import Store


class TestProduct(unittest.TestCase):

    def setUp(self):
        """Create a Product instance for testing."""
        self.product = Product("Test Product", price=100.0, quantity=50)

    def test_initialization(self):
        """Test proper initialization of the Product."""
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.price, 100.0)
        self.assertEqual(self.product.quantity, 50)
        self.assertTrue(self.product.is_active())

    def test_buy_valid_quantity(self):
        """Test buying a valid quantity of the product."""
        total_cost = self.product.buy(10)
        self.assertEqual(total_cost, 1000.0)  # 10 * 100.0
        self.assertEqual(self.product.quantity, 40)

    def test_buy_exceeding_quantity(self):
        """Test that buying more than the available quantity raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.product.buy(100)
        self.assertEqual(str(context.exception),
                         "The quantity of Test Product is bigger than the available stock.")

    def test_buy_inactive_product(self):
        """Test that buying from an inactive product raises ValueError."""
        self.product.deactivate()
        with self.assertRaises(ValueError) as context:
            self.product.buy(10)
        self.assertEqual(str(context.exception), "This product is inactive.")

    def test_set_negative_quantity(self):
        """Test that setting a negative quantity raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.product.set_quantity(-10)
        self.assertEqual(str(context.exception), "The quantity should be a positive number.")


class TestStore(unittest.TestCase):

    def setUp(self):
        """Create Store and Product instances for testing."""
        self.product1 = Product("Product 1", price=50.0, quantity=100)
        self.product2 = Product("Product 2", price=150.0, quantity=200)
        self.store = Store([self.product1, self.product2])

    def test_add_product(self):
        """Test adding a product to the store."""
        new_product = Product("Product 3", price=75.0, quantity=150)
        self.store.add_product(new_product)
        self.assertIn(new_product, self.store.list_of_products)

    def test_remove_product(self):
        """Test removing a product from the store."""
        self.store.remove_product(self.product1)
        self.assertNotIn(self.product1, self.store.list_of_products)

    def test_get_total_quantity(self):
        """Test the total quantity of products in the store."""
        self.assertEqual(self.store.get_total_quantity(), 300)

    def test_order_valid_product(self):
        """Test placing a valid order."""
        shopping_list = [(self.product1, 10)]
        total_price = self.store.order(shopping_list)
        self.assertEqual(total_price, 500.0)  # 10 * 50.0
        self.assertEqual(self.product1.quantity, 90)  # Quantity should decrease

    def test_order_inactive_product(self):
        """Test that ordering from an inactive product raises ValueError."""
        self.product2.deactivate()
        shopping_list = [(self.product2, 5)]
        with self.assertRaises(ValueError) as context:
            self.store.order(shopping_list)
        self.assertEqual(str(context.exception),
                         "The product 'Product 2' is not available in the store.")

    def test_order_exceeding_quantity(self):
        """Test that ordering more than available raises ValueError."""
        shopping_list = [(self.product1, 200)]  # Requesting more than available
        with self.assertRaises(ValueError) as context:
            self.store.order(shopping_list)
        self.assertEqual(str(context.exception),
                         "The quantity of Product 1 is bigger than the available stock.")

    def test_get_all_products(self):
        """Test getting all active products from the store."""
        active_products = self.store.get_all_products()
        self.assertEqual(len(active_products), 2)
        self.assertIn(self.product1, active_products)
        self.assertIn(self.product2, active_products)


if __name__ == '__main__':
    unittest.main()
