"""
Name : Matei Enache
Date : March 12, 2025
Description : porsche.py
"""

class Porsche:
    """Represents a Porsche 911 GT3 RS with attributes for speed, fuel, and mileage."""

    def __init__(self, model: str, color: str, horsepower: int, top_speed: int, fuel_level: int, mileage: float):
        """Creates a Porsche

        Args:
            model (str): The model of the car
            color (str): The color of the car
            horsepower (int): The horsepower of the engine
            top_speed (int): The top speed of the car
            fuel_level (int): The current fuel level of the car
            mileage (float): The mileage of the car
        """
        self.model = model
        self.color = color
        self.horsepower = horsepower
        self.top_speed = top_speed
        self.fuel_level = fuel_level
        self.mileage = mileage

    def drive(self, distance: float) -> None:
        """Simulates someone driving the Porsche

        Args:
            distance (float): Distance driven in kilometers
        """
        if self.fuel_level > 0:
            self.mileage += distance
            fuel_used = distance * 0.1
            
        self.fuel_level -= fuel_used
        if self.fuel_level < 0:
            self.fuel_level = 0
            print(f"Bob is driving a {self.model}. The distance he has gone is {distance} km. His fuel level is now {self.fuel_level}%. The mileage on his car is {self.mileage} km.")
        else:
            print(f"Oh, no! Bob's {self.model} is out of fuel! Please refuel.")

    def refuel(self, amount: int) -> None:
        """Refuels the car

        Args:
            amount (int): The amount of fuel to add as a percentage
        """
        self.fuel_level = min(100, self.fuel_level + amount)
        print(f"Bob refueled his {self.model}! His car's fuel level is now {self.fuel_level}%.")

    def display_specs(self) -> None:
        """Displayes the info about Bob's car in a readable format
        """
        print(f"""Bob's Porsche {self.model} is {self.color}, with {self.horsepower} horsepower.
              It has a top speed of {self.top_speed} km/h.
              It's fuel level is at {self.fuel_level}% and has a mileage of {self.mileage}.""")

def main() -> None:
    """Creates instances of the Porsche GT3 RS class and demonstrates its methods."""
    porsche1 = Porsche("911 GT3 RS", "Guard's Red", 518, 296, 100, 0)
    porsche2 = Porsche("718 Spyder", "Ruby Star Neo", 493, 308, 75, 1200)

    porsche1.drive(60)
    porsche1.refuel(20)
    porsche1.display_specs()
    porsche2.drive(200)
    porsche2.refuel(10)
    porsche2.display_specs()

if __name__ == "__main__":
    main()
