#prime num checker
for n in range(100):
        
    num=int(input("Enter a number:\n"))
    count=0
    
    for x in range(1,num+1):
        if num%x==0:
            count=count+1
    if count==2:
        print(num," is PRIME")    
    else:
        print(num,"is not PRIME")