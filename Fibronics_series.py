def fab(n):
    if(n<=1):
        return n
    else:
        return(fab(n-1) + fab(n-2))

n = int(input("Enter an Number:"))
for i in range(n):
    print( fab(i),end=",")


# Output is:

# Enter a Number : 5

