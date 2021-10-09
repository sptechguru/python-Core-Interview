
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]               
    return arr

mylist = [85,56,3,20,7,6,2,1,0,1000]
alist = ['s','a','n','t','o','s','h']


print(bubble_sort(mylist))
print(bubble_sort(alist))



