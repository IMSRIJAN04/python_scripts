matrix=[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","0","1"],["0","0","0","0","0"]]
r=len(matrix)
if r==0:
    print(0)
c=len(matrix[0])
s=[[0 for _ in range(c)] for _ in range(r)]
for i in range(c):
    s[0][i]=int(matrix[0][i])
for i in range(r):
    s[i][0]=int(matrix[i][0])
for i in range(1,r):
    for j in range(1,c):
        if matrix[i][j]=='1':
             s[i][j]=min(s[i][j-1],s[i-1][j],s[i-1][j-1])+1
        else:
            s[i][j]=0
print(s)
max_i,max_j,max_e=0,0,s[0][0]
for i in range(r):
    for j in range(c):
        if s[i][j]>max_e:
            max_e=s[i][j]
            max_i=i
            max_j=j
if max_e==1:
    print(1)
else:
    print(max_e*2)