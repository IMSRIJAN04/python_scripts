#input
nums=[3,4,7,2,-3,1,4,2]
k=7
#program

n=len(nums)
# General method of calculating the continous sum and storing in prefixsum List
# psum=[]
# sum=0
# psum.append(sum)
# for a in arr:
#     sum+=a
#     psum.append(sum)
# print(psum)

#now in the below approach we are not using prefixsum arr because we are using the dynamically generated "continous sum" values
s=0
count=0
sdict={0:1} #creating the sum dict and since the initial sum value is 0 and it is occuring for the first time we are adding 0 with value 1

#in this approach we are iterating the array only once and counting the no of subarrays with sum=k

for num in nums:
    s+=num
    #checking if the sub array sum equals k or not and incrementing the count using sdict value
    if s-k in sdict:
        count+=sdict[s-k]
    #updating sdict
    if s in sdict:
        sdict[s]+=1
    else:
        sdict[s]=1

print(count)


