def maxx(A):
    count =0
    for i in range(len(A)):
        if A[i] < 0:
            count+=1
    sum=0
    ans=0
    for i in range(len(A)):
        sum+=A[i]
        if sum<0:
            sum=0
        else:
            if sum>ans:
                ans=sum
    return ans
if __name__ == "__main__":
    A=[1,3,4,-10]
    res=maxx(A)
    print(res)