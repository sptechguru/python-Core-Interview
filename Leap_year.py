# Leap Years check a Program and Not a Leap year

# year = int(input("Enter a Year for your Choice:"))

year = 2024

if( year%4==0 and year%100!=0 or year%400==0):
    print('leap year')
else:
    print("Not a  Leap Year")


# b)
year = int(input("Enter an Years :"))

if year % 400 == 0:
    print("it is a leap year",year)

elif year % 4 == 0:
    print("leap year",year)    

elif year % 100 == 0:
    print("leap year")

else:
    print("Not a Leap year")

# c) Errro this Program 

# l = int(input("Enter an Years :"))
# result = "Leap Year"
# if l % 400 == 0  else "Leap Year "  if l % 4 == 0 and l % 100 != 0 else"Not a Leap Year"
# print(result)