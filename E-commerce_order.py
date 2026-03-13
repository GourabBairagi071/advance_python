# 4.E-Commerce Order Management 
# Manage orders, returns, and refunds. 
# Handle cases like invalid coupon code, out-of-stock errors, invalid payment methods. 


import random


class InvalidCoupon(Exception):
    pass


class OutOfStock(Exception):
    pass


class InvalidPaymentMethod(Exception):
    pass


class OrderNotFound(Exception):
    pass


class Ecommerce:

    def __init__(self):

        self.products = {
            1: {"name": "Laptop", "price": 50000, "stock": 5},
            2: {"name": "Phone", "price": 20000, "stock": 10},
            3: {"name": "Headphones", "price": 2000, "stock": 15},
            4: {"name": "Keyboard", "price": 1500, "stock": 20}
        }

        self.orders = {}
        self.coupons = {
            "SAVE10": 0.10,
            "SAVE20": 0.20
        }

        self.payment_methods = ["card", "upi", "netbanking"]

    def generate_order_id(self):
        return random.randint(1000, 9999)

    def show_products(self):

        print("\nAvailable Products")

        for pid, p in self.products.items():
            print(
                pid,
                p["name"],
                "Price:", p["price"],
                "Stock:", p["stock"]
            )

    def apply_coupon(self, price, coupon):

        if coupon == "":
            return price

        if coupon not in self.coupons:
            raise InvalidCoupon("Invalid coupon code")

        discount = self.coupons[coupon]

        new_price = price - price * discount

        return new_price

    def place_order(self, product_id, quantity, coupon, payment):

        if product_id not in self.products:
            print("Invalid product")
            return

        product = self.products[product_id]

        if product["stock"] < quantity:
            raise OutOfStock("Product out of stock")

        if payment not in self.payment_methods:
            raise InvalidPaymentMethod("Invalid payment method")

        total_price = product["price"] * quantity

        total_price = self.apply_coupon(total_price, coupon)

        order_id = self.generate_order_id()

        self.orders[order_id] = {
            "product": product["name"],
            "quantity": quantity,
            "price": total_price,
            "status": "Ordered"
        }

        product["stock"] -= quantity

        print("\nOrder placed successfully")
        print("Order ID:", order_id)
        print("Total Price:", total_price)

    def return_order(self, order_id):

        if order_id not in self.orders:
            raise OrderNotFound("Order not found")

        order = self.orders[order_id]

        if order["status"] == "Returned":
            print("Order already returned")
            return

        order["status"] = "Returned"

        print("Order returned successfully")

    def refund(self, order_id):

        if order_id not in self.orders:
            raise OrderNotFound("Order not found")

        order = self.orders[order_id]

        if order["status"] != "Returned":
            print("Return required before refund")
            return

        order["status"] = "Refunded"

        print("Refund processed:", order["price"])

    def show_orders(self):

        print("\nOrders")

        if len(self.orders) == 0:
            print("No orders yet")
            return

        for oid, o in self.orders.items():
            print(
                "Order ID:", oid,
                "| Product:", o["product"],
                "| Qty:", o["quantity"],
                "| Price:", o["price"],
                "| Status:", o["status"]
            )


store = Ecommerce()


def menu():

    while True:

        print("\n------ E-Commerce System ------")
        print("1 Show Products")
        print("2 Place Order")
        print("3 Return Order")
        print("4 Refund")
        print("5 Show Orders")
        print("6 Exit")

        choice = input("Enter choice: ")

        try:

            if choice == "1":

                store.show_products()

            elif choice == "2":

                store.show_products()

                pid = int(input("Product ID: "))
                qty = int(input("Quantity: "))
                coupon = input("Coupon Code (press enter if none): ")
                payment = input("Payment Method (card/upi/netbanking): ")

                store.place_order(pid, qty, coupon, payment)

            elif choice == "3":

                oid = int(input("Order ID: "))
                store.return_order(oid)

            elif choice == "4":

                oid = int(input("Order ID: "))
                store.refund(oid)

            elif choice == "5":

                store.show_orders()

            elif choice == "6":

                print("Thank you")
                break

            else:
                print("Invalid choice")

        except Exception as e:
            print("Error:", e)


menu()