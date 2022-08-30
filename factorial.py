def fact(n):
    f=1
    for i in range (0,n):
        f*=(n-i)
        
    print("factorial of",n,"is",f)
fact(int(input("enter number to find factorial ")))