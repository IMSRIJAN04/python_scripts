ransomNote="a"
magazine="b"
for i in range(len(ransomNote)):
    if ransomNote[i] not in magazine:
        print("0")
    elif ransomNote[i] in magazine:
        magazine=magazine.replace("ransomNote[i]","")
    else:
         pass
print("1")