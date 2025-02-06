

def check(A):
    checka = []
    for x in range(0,100):
        for y in range(0,100):
            f = (x+2*y>A) or (y<x) or (x<30)
            if f ==1:
                checka.append(1)
            else:
                checka.append(0)
    return all(checka)
for A in range(0,1000):
    if(check(A)):
        print(A)
