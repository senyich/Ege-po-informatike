


def f(s1,s2,m):
    if(s1+s2>=68):return m%2==0
    if(m==0):return 0
    h = [f(s1+1,s2,m-1),
         f(s1,s2+1,m-1),
         f(s1+s2,s2,m-1),
         f(s1,s2+s1,m-1)]
    return any(h) if m%2!=0 else all(h)

def main():
    s1 = 8
    print([s2 for s2 in range(1,60) if not f(s1,s2,2) and f(s1,s2,4)])

main()