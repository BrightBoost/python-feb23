import copy


class Dog:
    defaultSound = "Woof"

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Owner:
    TEST = 3

    def __init__(self, name, dog):
        self.name = name
        self.dog = dog


dog1 = Dog("Bobby", 25)
owner1 = Owner("Raoul", dog1)
owner2 = Owner("Wiljan", dog1)

owner1.dog.weight = 30
Dog.defaultSound = "meow"
owner1.dog.defaultSound = "meh"
print(owner2.dog.defaultSound)
print(owner1.dog.defaultSound)
