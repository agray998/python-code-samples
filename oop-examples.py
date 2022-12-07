class Animal():
    count = 0
    def make_noise(self):
        print("Grrrr")

class Dog(Animal):
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        Dog.count += 1
    
    def make_noise(self):
        print(self.name, "goes woof!")

    def __str__(self):
        return f"A {self.age}-year-old {self.breed} called {self.name}."
    
    def __int__(self):
        return self.age
    
    def __bool__(self):
        return True
    
    def __add__(self, dog2):
        return Dog(self.name + dog2.name, self.breed + dog2.breed, self.age + dog2.age)

fido = Dog("Fido", "Labrador", 3)

# fido.name = "Fido"
print(Dog.count)
# print(fido.count)
print(fido.name)
print(int(fido))
if fido:
    fido.make_noise()

spot = Dog("Spot", "Dalmatian", 5)
print(spot + fido)