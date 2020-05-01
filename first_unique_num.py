class FirstUnique:
    def __init__(self, nums):
        self.a=nums
        self.m={}
        self.q=[]
        for i in range(len(self.a)):
            x=self.a[i]
            if x in self.m:
                self.m[x]=1+self.m[x]
            else:
                self.m[x]=1
            self.q.append(self.a[i])          
            
    def showFirstUnique(self) -> int:
        while True:
            x=self.q[0]
            z=self.m[x]
            if z==1:
                return self.m[x]
            else:
                if x>=0 and len(self.q)!=0:
                    self.q.remove(x)
                else:
                    return -1
            

    def add(self, value: int) -> None:
        self.m[value]+=1
        self.q.append(value)

