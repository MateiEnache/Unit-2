class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(f"A restaurant called {self.restaurant_name} has {self.cuisine_type} food.")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")
    def set_number_served(self,number):
        self.number_served = number
    def increment_number_served(self,customers):
        self.number_served += customers

restaurant = Restaurant("Luigi's","italian")

print(f"Customers served: {restaurant.number_served}")
restaurant.set_number_served(100)
print(f"Customers served: {restaurant.number_served}")
restaurant.increment_number_served(25)
print(f"Customers served: {restaurant.number_served}")


class User:
    def __init__(self,first_name,last_name,password):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.login_attempts = 0
    def describe_user(self):
        print(f"{self.first_name} {self.last_name}'s password is {self.password}")
    def greet_user(self):
        print(f"Welcome, {self.first_name} {self.last_name}!!")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User("Alex","Pop","qwerty")
user2 = User("Matei","Enache","123456")
user3 = User("David","Borcila","password")

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print(f"Login attempts: {user1.login_attempts}")

user1.reset_login_attempts()

print(f"Login attempts: {user1.login_attempts}")
