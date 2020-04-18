class node:
    def __init__(self,x):
        self.data=x
        self.next=None
    
class list:
    def __init__(self):
        self.head=self.tail=None
    
    def insertfirst(s,x):
        s.temp=node(x)
        if head==None:
            head=tail=temp
        else:
            temp.next=head
            head=temp
    
    def insertlast(x):
        temp=node(x)
        if head==None:
            head=tail=temp
        else:
            tail.next=temp
            tail=temp
    
    def deletefirst():
        if head==None:
            print("list is empty")
        elif head==tail:
            head=tail=None
        else:
            x=head.data
            head=head.next
            return x
    
    def deletelast():
        if head==None:
            print("list is empty")
        elif head==tail:
            head=tail=None
        else:
            x=tail.data
            t=node()
            t=head
            while t.next!=tail:
                t=t.next
            t.next=None
            tail=t
            return x
    
    def display():
        t=node()
        t=head
        while t!=None:
            print(t.data)
            t=t.next
    
if __name__=='__main__': 
    llist=list()
    llist.head=node(1)
    second=node(2)
    third=node(3)
    llist.head.next=second
    second.next=third
    third.next=None



