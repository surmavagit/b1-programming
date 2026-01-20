import sys


class Product:
    def __init__(self, name, price, category, discount):
        self.name = name
        self.price = price
        self.category = category
        self.discount = discount
        self.total_d = category_discounts[self.category] + \
            tier_discounts[self.discount]

    def get_info(self):
        d_amount = round(self.price * self.total_d / 100, 2)
        return f"""
Product Name: {self.name}
Base Price: {self.price}
Total Discount Percentage: {self.total_d}%
Discount Amount: {d_amount}
Final Price: {round(self.price - d_amount, 2)}
"""


category_discounts = {
    'Electronics': 10,
    'Clothing': 15,
    'Books': 5,
    'Home': 12
}

tier_discounts = {
    'Premium': 5,
    'Standard': 0,
    'Budget': 2
}

product_records = []
try:
    with open('products.txt', 'r') as f:
        product_records = f.readlines()
except FileNotFoundError:
    print('file products.txt not found')
    sys.exit(1)

valid_products = []
for line in product_records:
    name, price, category, discount = line.strip().split(',')
    try:
        price = float(price)
    except ValueError:
        print(f"product {name} has invalid price: {price}")
        continue

    valid_products.append(Product(name, price, category, discount))

print('##### PRODUCT PRICING REPORT #####')

sum_discount = 0
for product in valid_products:
    print(product.get_info())
    sum_discount += product.total_d


print(f"Total products processed: {len(valid_products)}")
print(f"Average discount applied: {sum_discount / len(valid_products)}%")
