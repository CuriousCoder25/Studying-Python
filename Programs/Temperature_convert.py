for x  in range(331):
    i = int(input("choose 0 for celcius or 1 for Farenheit"))
    if i==0:
        C= int(input("Enter temperature in celcius:"))
        F=(C*9/5)+32
        print(F)
    elif i==1:
        F= int(input("Enter temperature in Farenheit:"))
        C=(F-32)*5/9
        print(C)
    else:
        x=330
        print("Invalid choice")
        

