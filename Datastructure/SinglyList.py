class Node:
    def __init__(self,data= None):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = Node()


    def Aceept_data(self,data):
        new_node =  Node(data) 
        cur = self.head

        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def display(self):
        list = [] 
        cur = self.head

        while cur.next != None:
            cur = cur.next
            list.append(cur.data)
        print(list)           

obj =  LinkList()

obj.Aceept_data(2)
obj.Aceept_data(22)
obj.Aceept_data(25)
obj.Aceept_data(62)
obj.Aceept_data(82)

obj.display()

