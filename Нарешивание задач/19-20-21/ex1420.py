

def f(s1,s2,m):
    if(s1*s2>=63): return m%2==0
    if(m==0):return  0
    h=[f(s1+1,s2,m-1),
       f(s1,s2+1,m-1),
       f(s1*2,s2,m-1),
       f(s1,s2*2,m-1)]
    return any(h) if m%2!=0 else all(h)
def main():
    s1 = 2
    print([s2 for s2 in range(1,32) if  f(s1,s2,2)])
    print([s2 for s2 in range(1,32) if  not f(s1,s2,1) and f(s1,s2,3)])
    print([s2 for s2 in range(1,32) if  not f(s1,s2,2) and f(s1,s2,4)])
main()
