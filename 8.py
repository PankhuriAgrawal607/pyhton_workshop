class Animal:
    def __init__(self,name):
        self.name=name
    def speaks(self):
        pass

class Dog(Animal):
        def speak(self):
            return "woof"
        
class Cat(Animal):
        def speak(self):
            return "meww"
dog = Dog("buddy")
cat= Cat("whiskars")
print(dog.name,dog.speak())
print(cat.name,cat.speak())