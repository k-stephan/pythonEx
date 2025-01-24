class a:
    def m1(self):
        print("Method 1 from parent class")

class b(a):
    def m2(self):
        print("Method 2 from child class")

#obj1=b()
#obj1.m1()
#obj1.m2()


class a1:
    a,b=(11,22)
    def m1(self):
        print("Method 1 from parent class")
        print(self.a+self.b)

class b1(a1):
    x, y = (111, 222)
    def m2(self):
        print("Method 2 from child class")
        print(self.x+self.y)


class c1(b1):
    xx, yy = (1111, 2222)
    def m3(self):
        print("Method 3 from multi level child class")
        print(self.xx+self.yy)

#obj11=b1()
#obj11.m1()
#obj11.m2()

obj111=c1()
obj111.m1()
obj111.m2()
obj111.m3()

# Method override

class a11:
    def m11(self):
        print("Method 1 from parent class")

class b11(a11):
    def m11(self):
        print("Method 2 from child class override from parent")


obj1111=b11()
obj1111.m11()

#  Super Keyword for override: Calling parent method using child class


class a11:
    def m11(self):
        print("Method 1 from parent class")

class b11(a11):
    def m11(self):
        print("Method 2 from child class override from parent")
        super().m11()


obj1111=b11()
obj1111.m11()

#