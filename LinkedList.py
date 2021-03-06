#Basic implementation of linked list
class node:
    def __init__(self,x):
        self.data=x
        self.next=None
    
class List:
    def __init__(self):
        self.head = None
        self.tail=None
    
    def insertfirst(self,x):
        temp=node(x)
        if self.head is None:
            self.head=self.tail=temp
        else:
            temp.next=self.head
            self.head=temp
    
    def insertlast(self,x):
        self.temp=node(x)
        if self.head==None:
            self.head=self.tail=self.temp
        else:
            self.tail.next=self.temp
            self.tail=self.temp
    
    def deletefirst(self):
        if self.head==None:
            print("list is empty")
        elif self.head==self.tail:
            self.head=self.tail=None
        else:
            x=self.head.data
            self.head=self.head.next
            return x
    
    def deletelast(self):
        if self.head==None:
            print("list is empty")
        elif self.head==self.tail:
            self.head=self.tail=None
        else:
            x=self.tail.data
            t=node(0)
            t=self.head
            while t.next!=self.tail:
                t=t.next
            t.next=None
            self.tail=t
            return x
    
    def display(self):
        t=node(0)
        t=self.head
        while t!=None:
            print(t.data)
            t=t.next
    
if __name__=='__main__': 
    llist=List()
    llist.insertfirst(1)
    llist.insertfirst(2)
    llist.insertfirst(5)
    llist.insertlast(9)
    llist.deletefirst()
    llist.deletelast()
    llist.display()



