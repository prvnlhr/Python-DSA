class student:
    def __init__(self, name, rollnum):
        self.name = name
        self.rollnum = rollnum


s1 = student("Praveen", 12)
s2 = student("Manish", 14)
print(s1.__dict__)
print(s2.__dict__)
