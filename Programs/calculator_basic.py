#basic calculator +-/*
print("CALCULATOR APP")
print("\n1. Add\n2. Subtract \n3. Divide\n4. Multiply")
x=int(input("\nCHOOSE ONE OPERATION:"))
a=int(input("Enter Number A:"))
b=int(input("Enter Number B:"))

if x==1:
    print(a+b)
elif x==2:
    print(a-b)
elif x==3:
    print(a/b)
elif x==4:
    print(a*b)
else:
    print("Invalid Input")


