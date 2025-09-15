s="dad"
longest="" 
for i in range(len(s)):
    for j in range(i,len(s)):
        v=s[i:j]
        if v==v[::-1]:
            if len(v)>len(longest):
                longest=v
print(longest)

