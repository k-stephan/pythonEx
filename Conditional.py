# Conditional Statements

age=18
if age<15:
    print("Below Age")
else:
    print("Correct Age")


n=int(input("Enter Desired Age:"))

if 100==n:
    print("Accepted Age:",n)
else:
    print("Not Accepted Age:",n)


if n%2==0:
    print("Even Number:",n)
else:
    print("Odd Number:",n)

print("Even Number:",n) if n%2==0 else print("Odd Number:",n)

pan=123

{print("If statement") ,print("Even Number:",n)} if pan%2==0 else {print("Odd Number:",n), print("else statement")}


week=2
if (week==1):
    print("First Week")
elif (week==2):
    print("Second Week")
else:
    print("Invalid Week")
