class Food:
    def __init__(self):
        print("Food is created from main class")
    def eat(self):
        print("Eat  Method from the base class")
class Apple(Food):
    def __init__(self):
        print("Apple is created from derived class")

food_two=Apple()
food_two.eat()
