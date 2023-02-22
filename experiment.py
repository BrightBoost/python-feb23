class B:
    def __init__(self, name):
        print("in b")
        self.name = name

    def get_name(self):
        print("my name is", self.name)

    def b(self):
        print('b')


class C:
    def __init__(self, name):
        print("in c")
        self.name = name


    def c(self):
        print('c')


class D(B, C):
    def __init__(self):
        super().__init__("raoul")
        super(B, self).__init__("wiljan")
        print("in d")

    def d(self):
        print('d')


d = D()
print(d.name)
d.get_name()
