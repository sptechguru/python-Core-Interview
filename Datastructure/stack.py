
# stack is follow of lifo (last in first output) Ex Disk ,Books 

# Stack is opertion perform push() & pop() & isEmpyty() & isFull() in Buit  method

def PushData(arr,val):
    arr.append(val)
    return arr

def PopData(arr):
    if isEmpty(arr):
        print('stack is empty')
        return False
    else:
        arr.pop()
        return arr    

def isEmpty(arr):
    if not arr:
        return True
    else:
        return False    

# creting Blank List as array
list = []

# list = [1,5,7,9,72,56]

print(PushData(list,12))
print(PushData(list,13))
print(PushData(list,120))
print(PopData(list))


