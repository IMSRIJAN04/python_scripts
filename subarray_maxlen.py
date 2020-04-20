<<<<<<< HEAD
hash_map={}
sum=0
max_length=0
nums=[1,1,1]

for x in range(len(nums)):
    if nums[x]==0:
        nums[x]=-1
    elif nums[x]==1:
         nums[x]=1
count=0
for i in range(len(nums)):
    sum=sum+nums[i]
    if sum==0:
        max_length=i+1
        if count==0:
            print(count,i) 
    if sum in hash_map:
        if max_length < i-hash_map[sum]:
            max_length=i-hash_map[sum]
    else:
         hash_map[sum]=i
    count=count+1
        
print(max_length)
    
=======
hash_map={}
sum=0
max_length=0
nums=[1,1,1]

for x in range(len(nums)):
    if nums[x]==0:
        nums[x]=-1
    elif nums[x]==1:
         nums[x]=1
count=0
for i in range(len(nums)):
    sum=sum+nums[i]
    if sum==0:
        max_length=i+1
        if count==0:
            print(count,i) 
    if sum in hash_map:
        if max_length < i-hash_map[sum]:
            max_length=i-hash_map[sum]
    else:
         hash_map[sum]=i
    count=count+1
        
print(max_length)
    
>>>>>>> 3aed84638617f13eeb8feedbd02a717452b4d563
