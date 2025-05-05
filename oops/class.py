class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

# Creating objects (instances) of the Dog class
my_dog = Dog("Buddy", "Golden Retriever")
your_dog = Dog("Max", "German Shepherd")

# Accessing attributes of the objects
print(my_dog.name)  # Output: Buddy
print(your_dog.breed) # Output: German Shepherd

# Calling a method on an object
my_dog.bark() # Output: Woof!