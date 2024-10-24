import pytest
from products import Product


def test_creating_product():
    assert isinstance(Product("MacBook Air M2", price=1450, quantity=100), Product)


def test_empty_name():
    with pytest.raises(ValueError, match="The name can't be empty."):
        Product("", price=1450, quantity=100)


def test_negative_price():
    with pytest.raises(ValueError, match="The price should be a positive number."):
        Product("MacBook Air M2", price=-100, quantity=100)


def test_invalid_price_type():
    with pytest.raises(ValueError, match="The price should be a positive number."):
        Product("MacBook Air M2", price="", quantity=100)

    with pytest.raises(ValueError, match="The price should be a positive number."):
        Product("MacBook Air M2", price=None, quantity=100)

    with pytest.raises(ValueError, match="The price should be a positive number."):
        Product("MacBook Air M2", price="string", quantity=100)

    with pytest.raises(ValueError, match="The price should be a positive number."):
        Product("MacBook Air M2", price=[], quantity=100)

    with pytest.raises(ValueError, match="The price should be a positive number."):
        Product("MacBook Air M2", price={}, quantity=100)


def test_invalid_quantity():
    with pytest.raises(ValueError, match="The quantity should be a positive number."):
        Product("MacBook Air M2", price=1450, quantity=None)

    with pytest.raises(ValueError, match="The quantity should be a positive number."):
        Product("MacBook Air M2", price=1450, quantity="string")

    with pytest.raises(ValueError, match="The quantity should be a positive number."):
        Product("MacBook Air M2", price=1450, quantity=-5)


def test_set_quantity():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert isinstance(product, Product)
    assert product.is_active()
    product.set_quantity(0)
    assert not product.is_active()


def test_product_purchase_modifies_quantity_and_returns_right_output():
    product = Product("MacBook Air M2", price=100, quantity=100)
    total_cost = product.buy(5)
    assert total_cost == 500, "Total cost should be 500 for 5 units at $100 each."
    assert product.get_quantity() == 95, "Quantity should be reduced to 95 after purchasing 5 units."


def test_buying_larger_quantity_raises_exception():
    product = Product("MacBook Air M2", price=100, quantity=10)

    with pytest.raises(ValueError, match="The quantity of MacBook Air M2 is bigger than the available stock."):
        product.buy(20)
