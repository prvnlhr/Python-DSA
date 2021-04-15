class Mother:

    def __init__(self):
        self.name = "Manju"
        super().__init__()

    def print(self):
        print("Print Of Mother called")


class Father:

    def __init__(self):
        self.name = "Ajay"
        super().__init__()

    def print(self):
        print("Print Of Father called")


class Child(Mother, Father):

    def __init__(self):
        super().__init__()

    def print(self):
        print("Name of child is", self.name)


c = Child()
c.print()
print(Child.mro())
