class User:


    def __init__(self, username):
        self.username = username


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print("Hi! I'm " + self.name)


class Employee(Person, User):
    def __init__(self, name, age, job, username):
        super().__init__(name, age)
        super(Person, self).__init__(username)
        self.job = job

    def say_hi(self):
        print("Hi! I'm", self.name, "and I'm a",
              self.job, ". My username is", self.username)


e1 = Employee("Pascal", 32, "software developer", "patrick123")
e1.say_hi()
print(e1.name, "is", e1.age, "and", e1.job, "with username", e1.username)
