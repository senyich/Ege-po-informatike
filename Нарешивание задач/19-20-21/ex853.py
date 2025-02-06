

def f(s1,s2,moves):
    if(s1+s2>=77): return moves%2==0
    if(moves == 0): return 0
    h = [f(s1+1,s2,moves-1),
         f(s1,s2+1,moves-1),
         f(s1*2,s2,moves-1),
         f(s1,s2*2,moves-1)]
    return any(h) if(moves)%2!=0 else all(h)

def main():
    s1 = 7
    print([s2 for s2 in range(1,70) if not f(s1,s2,1) and f(s1,s2,2)])
    print([s2 for s2 in range(1,70) if not f(s1,s2,1) and f(s1,s2,3)])
    print([s2 for s2 in range(1,70) if not f(s1,s2,2) and f(s1,s2,4)])


main()