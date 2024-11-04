# BestBuy 🛍️

**BestBuy** project is a command-line-based store inventory management system that allows users to manage 
products, apply promotions, and make purchases. 🛒

> *This project was developed as part of an assignment in the Software Engineer Bootcamp.* 🎓

## Features

- **Product Management**: Add, view, and manage various types of products, including stocked, non-stocked, 
  and limited-quantity products. 📦
- **Promotions**: Apply different promotions, such as second-item-at-half-price, buy-two-get-one-free, 
  and percentage discounts. 💰
- **Order Processing**: Place orders and calculate total payments with applicable promotions. 🧾
- **Store Combination**: Combine inventories of two stores using the `+` operator. ➕
- **Inventory Comparison**: Compare product prices using `>`, `<`, and `==`. ⚖️
- **Python Magic Methods**: Streamlined operations with magic methods like `__str__`, `__contains__`, 
  `__add__`, and more. ✨

## Installation

To get started, clone this repository and install the required package:

```bash
# Clone the repository
git clone https://github.com/yourusername/bestbuy.git

# Navigate into the project directory
cd bestbuy

# Install required dependencies
pip install -r requirements.txt
```

## Usage

### Running the Program

To start the program, execute:

```bash
python main.py
```
You will be presented with a menu to:

1. List all products. 📋
2. Display the total quantity of items. 🔢
3. Place an order. 🛍️
4. Quit the program. ❌


### Product and Promotion Types

- **Products**: Include regular products, non-stocked products (unlimited quantity), and limited products (maximum purchase restriction).
- **Promotions**: Add promotions to products as specified in main.py. Available promotions include:
  - Second item at half price. 💲
  - Buy two get one free. 🆓
  - Percentage discounts. 🎉

### Order Processing

While placing an order, users are guided to select products and specify quantities. The program validates stock availability, applies promotions, and calculates the final total. 💳

## Contribution

Contributions to this project are welcome! If you’d like to contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Make your changes and commit:
   ```bash
    git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```bash
    git push origin feature-branch
   ``` 
5. Open a Pull Request.

Thank you for contributing! ❤️


