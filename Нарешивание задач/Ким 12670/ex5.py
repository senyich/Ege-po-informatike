M = []
for num in range(1,100000):
    binNum = bin(num)[2:]
    num=num-binNum.count("0")
    R = bin(num)[2:]
    R = R[-3:]+R
    R = int(R,2)
    if(R>224):
        M.append(R)
print(min(M))