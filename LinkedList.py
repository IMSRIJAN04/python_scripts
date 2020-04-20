class node:
    def __init__(self,x):
        self.data=x
        self.next=None
    
class list:
    def __init__(self):
        self.head=self.tail=None
    
    def insertfirst(self,x):
        self.temp=node(x)
        if self.head==None:
            self.head=self.tail=self.temp
        else:
            self.temp.next=self.head
            self.head=self.temp
    
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
            self.x=self.head.data
            self.head=self.head.next
            return self.x
    
    def deletelast(self):
        if self.head==None:
            print("list is empty")
        elif self.head==self.tail:
            self.head=self.tail=None
        else:
            self.x=self.tail.data
            t=node(0)
            t=self.head
            while t.next!=self.tail:
                t=t.next
            t.next=None
            self.tail=t
            return self.x
    
    def display(self):
        t=node(0)
        t=self.head
        while t!=None:
            print(t.data)
            t=t.next
    
if __name__=='__main__': 
    llist=list()
    first=node(1)
    second=node(2)
    third=node(3)
    llist.head=first
    print(llist.head)
    # llist.head.next=second
    # second.next=third
    # third.next=None



