class Animal:
    def __init__(self):
        self.eyes = 2

    def breath(self):
        print("intake and outtake")

class Dog(Animal):
    def __init__(self):
        super().__init__()

dog = Dog()
dog.breath()

print(f"Dog has {dog.eyes} eyes")

dog.breath()