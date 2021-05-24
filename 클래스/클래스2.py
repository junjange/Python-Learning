class Animal:
    
    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Cat(Animal):

    def talk(self):
        return "Meow!"

class Dog (Animal):
    def talk(self):
        return "Woof! Woof!"

animals = [Cat("Missy"), Cat("Mr.Mistoffelees"), Dog("Lassie")]

for animals in animals:
    print(animals.name +": "+ animals.talk())