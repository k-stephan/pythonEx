list1=[1,2,3,"steve"]
print(list1)
print(list1[-1])
print(list1[1:-1])

for i in list1:
    print(i)
    if i==2:
        print("Item Exists")
    else:
        print("Item Doesn't Exists")

if "steve" in list1:
    print("Item Exists")
else:
    print("Item Doesn't Exists")


list1.insert(1,"Raj")
print(list1)