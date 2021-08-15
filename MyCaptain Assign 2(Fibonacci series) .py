# TASK 1 
n = int(input("Enter the value of n: "))   # n = How many terms the user wants to print
a = 0
b = 1
if n>0:
    if n==1:
        print(a)
    elif n==2:
        print(a,b)

    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a+b
            print(c)
            a,b = b,c

else:
    print("Enter positive number, number cannot be zero or negative")




