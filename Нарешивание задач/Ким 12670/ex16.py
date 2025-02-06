

def f(n):
    if n <=1: return 1
    if n%2==0 and n>1:return n+f(n-1)
    if n%2!=0 and n>1:return n**2+f(n-2)

print(f(80))