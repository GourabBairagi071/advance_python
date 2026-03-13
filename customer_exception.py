# 5.Custom Exception Framework 
# Create your own custom exceptions for a specific application (like an Inventory Management System). 
# For example: OutOfStockError, InvalidProductIDError, etc.
class InventoryError(Exception):
    pass


class OutOfStockError(InventoryError):
    pass


class InvalidProductIDError(InventoryError):
    pass


class InvalidQuantityError(InventoryError):
    pass


class DuplicateProductError(InventoryError):
    pass


class Inventory:

    def __init__(self):
        self.products = {}

    def add_product(self, pid, name, quantity):
        if pid in self.products:
            raise DuplicateProductError("Product ID already exists")

        if quantity < 0:
            raise InvalidQuantityError("Quantity cannot be negative")

        self.products[pid] = {
            "name": name,
            "quantity": quantity
        }

        print("Product added successfully")

    def update_stock(self, pid, quantity):

        if pid not in self.products:
            raise InvalidProductIDError("Invalid product ID")

        if quantity < 0:
            raise InvalidQuantityError("Quantity cannot be negative")

        self.products[pid]["quantity"] += quantity

        print("Stock updated")

    def sell_product(self, pid, quantity):

        if pid not in self.products:
            raise InvalidProductIDError("Invalid product ID")

        if quantity <= 0:
            raise InvalidQuantityError("Invalid quantity")

        if self.products[pid]["quantity"] < quantity:
            raise OutOfStockError("Not enough stock")

        self.products[pid]["quantity"] -= quantity

        print("Product sold successfully")

    def show_inventory(self):

        print("\nInventory")

        if len(self.products) == 0:
            print("No products available")
            return

        for pid, p in self.products.items():
            print(
                pid,
                p["name"],
                "Stock:", p["quantity"]
            )


inventory = Inventory()


def menu():

    while True:

        print("\n------ Inventory Management ------")
        print("1 Add Product")
        print("2 Update Stock")
        print("3 Sell Product")
        print("4 Show Inventory")
        print("5 Exit")

        choice = input("Enter choice: ")

        try:

            if choice == "1":

                pid = int(input("Product ID: "))
                name = input("Product Name: ")
                qty = int(input("Quantity: "))

                inventory.add_product(pid, name, qty)

            elif choice == "2":

                pid = int(input("Product ID: "))
                qty = int(input("Quantity to add: "))

                inventory.update_stock(pid, qty)

            elif choice == "3":

                pid = int(input("Product ID: "))
                qty = int(input("Quantity to sell: "))

                inventory.sell_product(pid, qty)

            elif choice == "4":

                inventory.show_inventory()

            elif choice == "5":

                print("Exiting system")
                break

            else:
                print("Invalid choice")

        except InventoryError as e:
            print("Inventory Error:", e)

        except Exception as e:
            print("Unexpected Error:", e)


menu()