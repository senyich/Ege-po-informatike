
def met(n):
    s = "1"+("3"*n)
    while("12" in s or "233" in s or "3333" in s):
        if("12" in s):
            s = s.replace("12","332",1)
        if("233" in s):
            s = s.replace("233","23",1)
        if("3333" in s):
            s = s.replace("3333","32",1)
    sum = 0
    for i in s:
        sum+=int(i)
    return sum
M = []
for k in range(6,1000):
    if(met(k)%6==0):
        M.append(k)
print(min(M))