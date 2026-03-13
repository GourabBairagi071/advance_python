# 6.Flight Booking System 
# A system to search, book, and cancel flight tickets. 
# Handle exceptions such as seat not available, invalid passenger details, payment failure.

import random


class SeatNotAvailableError(Exception):
    pass


class InvalidPassengerError(Exception):
    pass


class PaymentFailureError(Exception):
    pass


class BookingNotFoundError(Exception):
    pass


class FlightSystem:

    def __init__(self):

        self.flights = {
            101: {"route": "Delhi -> Mumbai", "price": 5000, "seats": 5},
            102: {"route": "Delhi -> Bangalore", "price": 6000, "seats": 4},
            103: {"route": "Mumbai -> Kolkata", "price": 4500, "seats": 6}
        }

        self.bookings = {}

    def generate_booking_id(self):
        return random.randint(10000, 99999)

    def search_flights(self):

        print("\nAvailable Flights")

        for fid, f in self.flights.items():
            print(
                "Flight:", fid,
                "| Route:", f["route"],
                "| Price:", f["price"],
                "| Seats:", f["seats"]
            )

    def process_payment(self, amount):

        success = random.choice([True, True, False])

        if not success:
            raise PaymentFailureError("Payment failed")

        print("Payment successful")

    def book_ticket(self, flight_id, name, age):

        if not name or age <= 0:
            raise InvalidPassengerError("Invalid passenger details")

        if flight_id not in self.flights:
            print("Invalid flight")
            return

        flight = self.flights[flight_id]

        if flight["seats"] <= 0:
            raise SeatNotAvailableError("No seats available")

        self.process_payment(flight["price"])

        booking_id = self.generate_booking_id()

        self.bookings[booking_id] = {
            "name": name,
            "flight": flight["route"],
            "status": "Booked"
        }

        flight["seats"] -= 1

        print("\nTicket booked successfully")
        print("Booking ID:", booking_id)

    def cancel_ticket(self, booking_id):

        if booking_id not in self.bookings:
            raise BookingNotFoundError("Booking not found")

        booking = self.bookings[booking_id]

        if booking["status"] == "Cancelled":
            print("Ticket already cancelled")
            return

        booking["status"] = "Cancelled"

        print("Ticket cancelled successfully")

    def show_bookings(self):

        print("\nBookings")

        if len(self.bookings) == 0:
            print("No bookings yet")
            return

        for bid, b in self.bookings.items():
            print(
                "Booking ID:", bid,
                "| Passenger:", b["name"],
                "| Flight:", b["flight"],
                "| Status:", b["status"]
            )


system = FlightSystem()


def menu():

    while True:

        print("\n------ Flight Booking System ------")
        print("1 Search Flights")
        print("2 Book Ticket")
        print("3 Cancel Ticket")
        print("4 Show Bookings")
        print("5 Exit")

        choice = input("Enter choice: ")

        try:

            if choice == "1":

                system.search_flights()

            elif choice == "2":

                system.search_flights()

                fid = int(input("Flight ID: "))
                name = input("Passenger Name: ")
                age = int(input("Passenger Age: "))

                system.book_ticket(fid, name, age)

            elif choice == "3":

                bid = int(input("Booking ID: "))
                system.cancel_ticket(bid)

            elif choice == "4":

                system.show_bookings()

            elif choice == "5":

                print("Thank you")
                break

            else:
                print("Invalid choice")

        except Exception as e:
            print("Error:", e)


menu()