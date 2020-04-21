grid=[[1,3,1],
[1,5,1],
[4,2,1]
]
nr=len(grid)
nc=len(grid[0])
mca=[[0 for _ in range(nc)] for _ in range(nr)]
mca[0][0]=grid[0][0]
for i in range(1,nr):
    mca[i][0]=mca[i-1][0]+grid[i][0]
for i in range(1,nc):
    mca[0][i]=mca[0][i-1]+grid[0][i]      
for i in range(1,nr):
    for j in range(1,nc):
        mca[i][j]=grid[i][j]+min(mca[i-1][j],mca[i][j-1])
print(mca[nr-1][nc-1])
