class Bus:
    def __init__(self, ticket_charges, weekly_collection, weekly_expenses):
        self.__ticket_charges = ticket_charges     # private
        self._weekly_collection = weekly_collection  # protected
        self._weekly_expenses = weekly_expenses      # protected

    def get_ticket_charges(self):
        return self.__ticket_charges

    def calculate_profit(self):
        return self._weekly_collection - self._weekly_expenses


class CityBus(Bus):
    def __init__(self, ticket_charges, weekly_collection, weekly_expenses):
        super().__init__(ticket_charges, weekly_collection, weekly_expenses)

    def __str__(self):
        return (f"CityBus: Ticket={self.get_ticket_charges()}, "
                f"Collection={self._weekly_collection}, "
                f"Expenses={self._weekly_expenses}, "
                f"Profit={self.calculate_profit()}")


class InterCityBus(Bus):
    def __init__(self, ticket_charges, weekly_collection, weekly_expenses):
        super().__init__(ticket_charges, weekly_collection, weekly_expenses)

    def __str__(self):
        return (f"InterCityBus: Ticket={self.get_ticket_charges()}, "
                f"Collection={self._weekly_collection}, "
                f"Expenses={self._weekly_expenses}, "
                f"Profit={self.calculate_profit()}")


class InterStateBus(Bus):
    def __init__(self, ticket_charges, weekly_collection, weekly_expenses):
        super().__init__(ticket_charges, weekly_collection, weekly_expenses)

    def __str__(self):
        return (f"InterStateBus: Ticket={self.get_ticket_charges()}, "
                f"Collection={self._weekly_collection}, "
                f"Expenses={self._weekly_expenses}, "
                f"Profit={self.calculate_profit()}")


# Multiple Inheritance Class
class TransportProfit(CityBus, InterCityBus, InterStateBus):
    def __init__(self, ticket_charges, weekly_collection, weekly_expenses):
        super().__init__(ticket_charges, weekly_collection, weekly_expenses)

    def __str__(self):
        return (f"TransportProfit => Collection={self._weekly_collection}, "
                f"Expenses={self._weekly_expenses}, "
                f"Profit={self.calculate_profit()}")


# ------------------- Object Creation and Calls -------------------

# Create objects for each type
obj_city = CityBus(20, 5000, 3000)
obj_intercity = InterCityBus(50, 10000, 6000)
obj_interstate = InterStateBus(100, 20000, 12000)
obj_transport = TransportProfit(30, 15000, 8000)

# Print details
print(obj_city)
print(obj_intercity)
print(obj_interstate)
print(obj_transport)

# Explicitly call profit calculation
print("\n--- Profit Details ---")
print("City Bus Profit:", obj_city.calculate_profit())
print("InterCity Bus Profit:", obj_intercity.calculate_profit())
print("InterState Bus Profit:", obj_interstate.calculate_profit())
print("Overall Transport Profit:", obj_transport.calculate_profit())
