
class Dog():
    "A simple attempt to model a dog."

    def __init__(self, name, age):
        "Initialize name and age attributes."
        self.name = name
        self.age = age

    def sit(self):
        "Simulate a dog sitting in response toa command."
        print(self.name.title() + " is now sitting.")

    def roll_over():
        "Simulate rolling over in response toa command."
        print(self.name.title() + " rolled over!")

