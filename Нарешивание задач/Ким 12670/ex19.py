

def f(s,m):
    if(s>=129): return m%2==0
    if(m==0): return 0
    h = [f(s+1,m-1),f(s*2,m-1)]
    return any(h) if m%2!=0 else all(h)

print([s1 for s1 in range(1, 129) if not f(s1, 1) and f(s1,2)])
print([s1 for s1 in range(1, 129) if not f(s1, 1) and f(s1,3)])
print([s1 for s1 in range(1, 129) if not f(s1, 2) and f(s1,4)])
