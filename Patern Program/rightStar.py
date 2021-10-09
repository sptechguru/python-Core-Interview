for i  in range(1,5):
    for j in range(1,8):
        if j>=5-i and j<=3+i:
            print("*",end="")
        else:
            print(" ",end="")
    print()


for i  in range(1,5):
    for j in range(1,8):
        if j>=i and j<=8-i:
            print("*",end="")
        else:
            print(" ",end="")
    print()

'''
 
 1st O/p is if j>=5-i and j<=3+i:
 
   *
  ***
 *****
*******

2nd O/p is if j>=i and j<=8-i:
 
*******
 *****
  ***
   *

3rd O/p is 1 prog + 2nd Program tha is print in diamond

   *
  ***
 *****
*******
*******
 *****
  ***
   *

'''                