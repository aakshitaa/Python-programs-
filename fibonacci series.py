def add():
    n=int(input("enter limit of natural number addition "))
    s=0
    for i in range(1,n+1):
        s+=i
    print("sum of natural numbers upto",n,"is",s)
def fibo():
    n=int(input("enter limit of fibonacci series "))
    s=0
    a=0
    b=1
    if(n==0):
        print(n)
    else:
        for i in range (0,n+1):
            s=a+b
            print( " ",s ,end='')
            a=b
            b=s
choice=int(input("enter choice as 1 for sum of natural numbers and 2 for printing fibonacci series "))
if (choice==1):
    add()
elif (choice==2):
    fibo()
else:
    print("wrong input ")