print(list(range(10)))
print(list(range(4,10)))
print(list(range(1,10,3)))

print(list(range(-4,10)))
print(list(range(-4,10,5)))

print(list(range(15,5,-2)))

i=5

while i>=1:
    print(i)
    i=i-1


for i in range(0,11,2):
    print(i)

for i in range(1,10):
    if (i==5):
        break
    print(i)
print("Program exited at 5")


for i in range(1,10):
    if i==5 or i==7:
        continue
    print(i)
print("Program will not print  5 & 7")

name="stephen"
print(name+"Hello")
print(name*5)

print(name[1:4])
print(name[:-3])
print(name[4:])

print(ord('A'))
print(chr(65))

print(len("steve"))
print(max(12,22,1))
print(min(12,22,1))

print("hen" in name)
print("eve" in name)
print("eve" not in name)

s="stephen"
rev=""
for i in s:
    rev=i+rev
print(rev)

print(s[::-1])