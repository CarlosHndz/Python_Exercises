class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant's Name: " + self.restaurant_name.title())
        print("Restaurant's Cuisine: " + self.cuisine_type.title())

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open.")

restaurant1 = Restaurant("venice", "italian")
restaurant2 = Restaurant("mexico city", "mexican")
restaurant3 = Restaurant("great wall", "chinese")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
restaurant1.open_restaurant()
restaurant2.open_restaurant()
restaurant3.open_restaurant()
 
