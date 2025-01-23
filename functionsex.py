def myfun():
    print("Hello")

myfun()


def myfun1(name):
    print("Hello",name)

myfun1("Steff")

def cal(a,b):
    return (a+b)

a=cal(2,3)
print(a)

print(cal(125,222))

global_var=200

def funcvar():
    local_var=150
    print("Local variable",local_var)
    print("Global variable",global_var)

funcvar()

def addition(i,j=10):
    print(i+j)

addition(23)
