def sum(s,t):
    l=len(s)
    for i in range(l):
        for j in range(i+1,l):
            if s[i]+s[j]==t:
                return[i,j]
s=[1,7,8,4]
t=12
r=sum(s,t)
print(r)            