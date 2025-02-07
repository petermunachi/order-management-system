class User:
    def __init__(self, user_id, name, email, password, role):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.role = role

    def register(self):
        return f"User {self.name} registered successfully."

    def login(self, email, password):
        return self.email == email and self.password == password


class Admin(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password, role="Admin")

    def manage_inventory(self, inventory, product, action):
        if action == "add":
            inventory.add_product(product)
        elif action == "remove":
            inventory.remove_product(product.product_id)


class Customer(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password, role="Customer")

    def place_order(self, order):
        return order.place_order()


class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def get_product_details(self):
        return f"{self.name}: ${self.price}, Stock: {self.stock}"

    def update_stock(self, quantity):
        self.stock -= quantity


class Order:
    def __init__(self, order_id, customer, products, total_amount, status="Pending"):
        self.order_id = order_id
        self.customer = customer
        self.products = products
        self.total_amount = total_amount
        self.status = status

    def place_order(self):
        return f"Order {self.order_id} placed successfully."

    def update_status(self, status):
        self.status = status
        return f"Order {self.order_id} updated to {self.status}."

    def cancel_order(self):
        self.status = "Cancelled"
        return f"Order {self.order_id} has been cancelled."


class Inventory:
    def __init__(self):
        self.inventory_list = {}

    def add_product(self, product):
        self.inventory_list[product.product_id] = product

    def remove_product(self, product_id):
        if product_id in self.inventory_list:
            del self.inventory_list[product_id]

    def check_stock(self, product_id):
        return self.inventory_list[product_id].stock if product_id in self.inventory_list else None


class Payment:
    def __init__(self, payment_id, order, amount, payment_status="Pending"):
        self.payment_id = payment_id
        self.order = order
        self.amount = amount
        self.payment_status = payment_status

    def process_payment(self):
        self.payment_status = "Completed"
        return f"Payment {self.payment_id} processed successfully."

    def refund_payment(self):
        self.payment_status = "Refunded"
        return f"Payment {self.payment_id} has been refunded."

# Example Usage
if __name__ == "__main__":
    # Create an admin and customer
    admin = Admin(1, "Alice", "alice@example.com", "admin123")
    customer = Customer(2, "Bob", "bob@example.com", "cust123")

    # Create inventory and add products
    inventory = Inventory()
    product1 = Product(101, "Laptop", 1200, 10)
    admin.manage_inventory(inventory, product1, "add")

    # Customer places an order
    order = Order(5001, customer, [product1], 1200)
    print(customer.place_order(order))
    
    # Process payment
    payment = Payment(9001, order, 1200)
    print(payment.process_payment())
