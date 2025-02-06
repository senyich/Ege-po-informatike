
def checkWin(rocks1,rocks2, moves):
    if(rocks1+rocks2 >=59): return moves%2==0
    if(moves ==0): return 0
    vars = [checkWin(rocks1*2,rocks2,moves-1),
            checkWin(rocks1,rocks2*2,moves-1),
            checkWin(rocks1+1,rocks2,moves-1),
            checkWin(rocks1,rocks2+1,moves-1)]
    return any(vars) if(moves-1)%2==0 else all(vars)
def main():
    s1 = 5
    print("19)",min([s2 for s2 in range(1,54) if checkWin(s1,s2,1)]))
    print("20)",[s2 for s2 in range(1,54) if not checkWin(s1,s2,1) and checkWin(s1,s2,3)])
    print("21)",[s2 for s2 in range(1,54) if not checkWin(s1,s2,2) and checkWin(s1,s2,4)])
if __name__ == "__main__":
    main()