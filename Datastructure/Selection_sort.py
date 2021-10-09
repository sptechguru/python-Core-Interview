def selection_sort(arr):
    for i in range(len(arr)):
        var = i
        for j in range(i,len(arr)):
            if arr[var] > arr[j]:
                var = j
                arr[i],arr[var] = arr[var],arr[i]

    return arr

list = [ 3,2,1,5,4]

print(selection_sort(list))