# Base class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand  
        self._model = model
        self.__battery = battery  # Private attribute
        self.storage = storage  

    def make_call(self, number):
        print(f"{self.brand} {self._model} is calling {number}...")

    def charge_battery(self, amount):
        self.__battery += amount
        print(f"Battery charged. Current battery: {self.__battery}%")

    def get_battery_status(self):
        return f"Battery is at {self.__battery}%"

# Child class
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery, cooling_system):
        super().__init__(brand, model, storage, battery)
        self.cooling_system = cooling_system

    def start_game(self, game_name):
        print(f"Launching {game_name} on {self.brand} {self._model} with {self.cooling_system} cooling system.")


phone = Smartphone("Samsung", "Galaxy S23", "128GB", 50)
phone.make_call("123-456-7890")
print(phone.get_battery_status())

gaming_phone = GamingSmartphone("ASUS", "ROG Phone 6", "256GB", 80, "Advanced Liquid Cooling")
gaming_phone.start_game("PUBG Mobile")
gaming_phone.charge_battery(20)
