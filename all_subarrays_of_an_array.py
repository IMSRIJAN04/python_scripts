arr=[1,2,3,4,5]
n=len(arr)
size=1
for k in range(n):
    for i in range(k,n):
        print("@@@@@")
        for j in range(k,i+1):
            print(arr[j])
        

