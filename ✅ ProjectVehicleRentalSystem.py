class Vehicle:
    def __init__(self, brand, model, rental_price_per_day):
        self.brand = brand
        self.model = model
        self.rental_price_per_day = rental_price_per_day

    def get_info(self):
        return f"{self.brand} {self.model}"

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

class RentalService:
    def __init__(self):
        self.available_vehicles = []

    def add_vehicle(self, vehicle):
        self.available_vehicles.append(vehicle)

    def display_vehicles(self):
        print("Available Vehicles:")
        for idx, v in enumerate(self.available_vehicles, start=1):
            print(f"{idx}. {v.get_info()} - ${v.rental_price_per_day}/day")

    def rent_vehicle(self, index):
        if 0 <= index < len(self.available_vehicles):
            rented_vehicle = self.available_vehicles.pop(index)
            print(f"You rented {rented_vehicle.get_info()}")
        else:
            print("Invalid selection!")

# Usage
service = RentalService()
service.add_vehicle(Car("Toyota", "Camry", 70))
service.add_vehicle(Bike("Yamaha", "R15", 30))

service.display_vehicles()
service.rent_vehicle(0)
service.display_vehicles()
