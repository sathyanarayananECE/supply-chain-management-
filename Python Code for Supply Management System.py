
# Define the classes as before

class Product:
def __init__(self, name, price, quantity):
self.name = name
self.price = price
self.quantity = quantity

class Inventory:
def __init__(self):
self.products = []

def add_product(self, product):
self.products.append(product)

def update_product_quantity(self, product_name, quantity):
for product in self.products:
if product.name == product_name:
product.quantity += quantity
break

def sell_product(self, product_name, quantity):
for product in self.products:
if product.name == product_name:
if product.quantity >= quantity:
product.quantity -= quantity
print(f"{quantity} {product_name}(s) sold.")
print(f"Remaining quantity of {product_name}: {product.quantity}")
else:
print("Insufficient stock.")
break
else:
print("Product not found.")

def list_products(self):
for product in self.products:
print(f"Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")

# Example usage with user input
inventory = Inventory()

# Add products to inventory using user input
while True:
name = input("Enter product name (or type 'done' to finish adding products): ")
if name.lower() == 'done':
break
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))
inventory.add_product(Product(name, price, quantity))

# List products
print("\nCurrent inventory:")
inventory.list_products()

# Sell products using user input
while True:
name = input("Enter product name to sell (or type 'done' to finish selling): ")
if name.lower() == 'done':
break
quantity = int(input("Enter quantity to sell: "))
inventory.sell_product(name, quantity)

# List updated inventory
print("\nUpdated inventory:")
inventory.list_products()

