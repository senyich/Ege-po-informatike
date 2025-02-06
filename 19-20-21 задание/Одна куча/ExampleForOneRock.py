def checkWin(rocks, moves):
    if(rocks >= 34): return  moves%2 == 0
    if(moves == 0): return 0
    variantsOfMoves = [checkWin(rocks+1, moves-1),checkWin(rocks+2,moves-1),checkWin(rocks+3, moves-1), checkWin(rocks*2, moves-1)]
    return any(variantsOfMoves) if(moves - 1)%2==0 else all(variantsOfMoves)

def main():
    print("19) ",[s for s in range(1,34) if(checkWin(s,2))])
    print("20) ",[s for s in range(1,34) if(not checkWin(s,1) and checkWin(s,3))])
    print("21) ",[s for s in range(1, 34) if (not checkWin(s,2) and checkWin(s,4))])
if __name__ == "__main__":
    main()