"""
Name: Matei Enache
Date: 3/6/2025
Description: Unit 2 HW 1
"""

class Restaurant:
    """
        Models a restaurant
    """
    def __init__(self,restaurant_name:str,restaurant_cuisine:str):
        """Creates a restaurant

        Args:
            restaurant_name (str): name of restaurant
            restaurant_cuisine (str): cuisine of restaurant
        """
        self.restaurant_name = restaurant_name
        self.restaurant_cuisine = restaurant_cuisine
    def describe_restaurant(self):
        """Prints the description of the restaurant
        """
        print(f"The restaurant name is {self.restaurant_name} and the cuisine is {self.restaurant_cuisine}.")

    def open_restaurant(self):
        """Tells the user that the restaurant is open
        """
        print(f"{self.restaurant_name} is open.")

    def set_num_served(self,num_served:int):
        """Sets the number of costumers served

        Args:
            num_served (int): how many people served
        """
        self.set_num_served = num_served
    
    def increment_served(self):
        print("hja")


which_restaurant = Restaurant("Pizza Place", "Italian")
print(which_restaurant.restaurant_name)
print(which_restaurant.restaurant_cuisine)
which_restaurant.describe_restaurant()
which_restaurant.open_restaurant()

which_restaurant2 = Restaurant("Sushi Place", "Japanese")
which_restaurant3 = Restaurant("Taco Place", "Mexican")

print(which_restaurant2.restaurant_name)
print(which_restaurant2.restaurant_cuisine)
which_restaurant2.describe_restaurant()
print(which_restaurant3.restaurant_name)
print(which_restaurant3.restaurant_cuisine)
which_restaurant3.describe_restaurant()


class User:
    def __init__(self, first_name:str, last_name:str, password:str, hobby:str):
        """Learns information about the user

        Args:
            first_name (str): The first name of the user
            last_name (str): The last name of the user
            password (str): The password of the user
            username (str): The username of the user
        """
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.hobby = hobby
    
    def describe_user(self):
        """Describes the user with information from __init__
        """
        print(f"Your name is {self.first_name} {self.last_name}. Your password is {self.password}. One of your hobbies is to {self.hobby}.")

    def greet_user(self):
        """Greets the user
        """
        print(f"Hello, {self.first_name}, what would you like to do today?")

user1 = User("Matei", "Enache", "123456", "playing videogames")
user2 = User("Alex", "Pop", "qwerty", "building Legos")
user3 = User("David", "Borcila", "abcdefg", "snowboarding because you somehow snapped your skis in half")

print()
print()
user1.describe_user()
user1.greet_user()
print()
user2.describe_user()
user2.greet_user()
print()
user3.describe_user()
user3.greet_user()