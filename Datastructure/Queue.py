# # Queue is Follows is FIFO (first in first Output)

# 1) enqueue()  is opertion perform insert  Data
# 2) dequeue()  is opertion perform DeleteData  Data


def blankData(que):
    if not que:
        return True
    else:
        return False

def InsertData(que,val):
    que.append(val)
    return que


def DeleteData(que):
    if blankData(que):
        print('Queue is Empty List')
        return False
    else:
        que.pop()
        return que    

mylist = []
print(mylist)

print(InsertData(mylist,23))
print(InsertData(mylist,33))
print(InsertData(mylist,73))
print(InsertData(mylist,43))
print(mylist)
print(DeleteData(mylist))
print(mylist)
