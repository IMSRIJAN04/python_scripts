m=5
n=7
c=0
while m!=n:
    m=m>>1
    n=n>>1
    c+=1
solution=m<<c
print(solution)
