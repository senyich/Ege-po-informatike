
#пример:
#победа при s>=50
#варианты хода: +1, *2

def checkWin(rocks, moves):
    if(rocks >= 50): return  moves%2 == 0
    if(moves == 0): return 0
    variantsOfMoves = [checkWin(rocks+1, moves-1),checkWin(rocks*2,moves-1)]
    return any(variantsOfMoves) if(moves - 1)%2==0 else all(variantsOfMoves)
