import sys
try:
    a=int(input("enter a number "))
    b=int(input("enter another number "))
    print(a/b)
except TypeError:
    print("oops! type error occured ")
except ZeroDivisionError:
    print("oops! zero division error occured ")
else: 
    print("no error occured ")