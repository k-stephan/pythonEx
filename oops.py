a,b=(22,33)

class first:
    a,b=(11,12)
    def add(self):
        a,b=24,56
        print(a+b)
        print(self.a+self.b)
        print(globals()['a']+globals()['b'])

m=first()
m.add()


class second:
    def one(self):
        print("Instance Method")
    @staticmethod
    def two(self):
        print("Static Method"+self)

m1=second()
m1.one()
second.two(" steve")


class third:
    a,b=(111,222)
    def __init__(self):
        a,b=(100,200)
        print(a+b)
    def addmethod(self):
        print(self.a+self.b)

m3=third()
m3.addmethod()

