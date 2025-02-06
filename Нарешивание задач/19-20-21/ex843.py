

def f(s1,s2,m):
    if(s1+s2<=20): return m%2==0
    if(m==0): return 0
    h = [f(s1-1,s2,m-1),
         f(s1,s2-1,m-1),
         f((s1+1)//2,s2,m-1),
         f(s1,(s2+1)//2,m-1)]
    return any(h) if(m%2!=0) else all(h)

def main():
    print([s for s in range(11,200) if(f(10,s,2))])
    print([s for s in range(11,200) if(not f(10,s,1) and f(10,s,3))])
    print([s for s in range(11,200) if(not f(10,s,2) and f(10,s,4))])

main()