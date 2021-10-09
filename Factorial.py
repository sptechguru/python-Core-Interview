def factorial(n):
    if(n<=1):
        return 1
    else:
        return(n*factorial(n-1))

n = int(input("Enter an Number:"))
print("Factorial number is:", factorial(n))


# Output is:

# Enter a Number : 5

# 1x2x3x4x5 =120

# Factorial number is: 120


