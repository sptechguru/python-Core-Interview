def sum(arr):
    sum = 0
    for i in arr:
        sum =sum + i
    return(sum)
    
#  driver functions is run this code

arr = []

arr = [12,3,4,1]

n = len(arr)

ans = sum(arr)

print('sum of the array is ',ans)

