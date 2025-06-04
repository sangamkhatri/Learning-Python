# Product Inventory with Discount Logic
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price  # price per unit
        self.quantity = quantity  # number of items in stock

    def total_value(self):
        return self.price * self.quantity

    def is_low_stock(self):
        return self.quantity < 5

    def apply_discount(self, percent):
        if percent > 0:
            self.price = self.price * (1 - percent / 100)


# List of product data (each as a dictionary)
product_data = [
    {"name": "Apples", "price": 2.0, "quantity": 10},
    {"name": "Bananas", "price": 1.5, "quantity": 3},
    {"name": "Cherries", "price": 3.0, "quantity": 2},
    {"name": "Dates", "price": 5.0, "quantity": 12},
]

# Convert to list of Product objects
inventory = []
for data in product_data:
    item = Product(data["name"], data["price"], data["quantity"])
    inventory.append(item)

# Apply discount and print info
for item in inventory:
    print(f"Product: {item.name}")
    print(f"  Price: ${item.price}")
    print(f"  Quantity: {item.quantity}")
    print(f"  Total Value: ${item.total_value():.2f}")

    if item.is_low_stock():
        print("  ⚠️ Low Stock! Restock soon.")
        item.apply_discount(10)
        print(f"  Discounted Price: ${item.price:.2f}")

    print()
