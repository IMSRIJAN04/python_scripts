t1="tabriz"
t2="torino"
n=len(t1)
c=0
res=0
while n!=0:
    c+=1
    for i in range(c):
        for j in range(i,n):
            if t1[i:n]==t2[i:n]:
                if res<(n-1):
                    res=n-1
                    

