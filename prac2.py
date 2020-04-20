s="apple"
n=len(s)
val=6
if val>=n:
    val=val%n

print("left+++++++ "+str(val))
print(s[val:]+s[:val])
print("right+++++++ "+str(val))
print(s[n-val:]+s[:n-val])
# for val in range(len(s)):
#     print("left+++++++ "+str(val))
#     print(s[val:]+s[:val])
#     print("right+++++++ "+str(val))
#     print(s[n-val:]+s[:n-val])