
for i in range(1,5):
    for j in range(1,5):
        if j<=5-i:
            print("*",end="")
        else:
            print(" ", end="")
    print()            




'''  out put is  if j<=i:
1) 

*
**
***
****
*****


2nd output is  if j<=5-i:

*****
****
***
**
*

3rd out put is if j>=i:

*****
 ****
  ***
   **
    *

4th out put is if j>=5-i:

   *
  **
 ***
****



'''



