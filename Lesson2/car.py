class Car:
    '''
    A simple attempt to represent a car
    '''
    def read_odometer(self)->None:
        print(f"This car has {self.odometer} miles on it")


    def update_odometer(self,mileage:int)->None:
        if mileage >= self.odometer:
            old_mileage = self.odometer
            self.odometer = mileage
            print(f"The odometer was updated from {old_mileage} to {self.odometer}")
        else:
            print("You cannot roll back an odometer")
    def increment_odometer(slef,miles:int)->None:
        if miles>=0:
            self.odometer += miles
        else:
            print("You cannot roll back an odometer")

    def __init__(self,make:str,model:str,year:int):
        """Constructor

        Args:
            make (str): Make of car
            model (str): Model of car
            year (int): Year the car was made
        """
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self)->str:
        """Returns a nicely formatted description of the car


        Returns:
            str: description of the car formatted in title case
        """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

def main():
    my_new_car = Car('audi','a4',2025)
    print(my_new_car.get_descriptive_name())
    my_new_car.update_odometer(100)
    my_new_car.update_odometer(50)
    my_new_car.increment_odometer(25)
    my_new_car.read_odometer()
    my_new_car.increment_odometer(-20)
    my_new_car.read_odometer()
    

if __name__ == '__main__':
    main()