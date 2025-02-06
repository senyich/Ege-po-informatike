def checkWin(rocks1,rocks2, moves):
    if(rocks1+rocks2 >=59): return moves%2==0
    if(moves ==0): return 0
    vars = [checkWin(rocks1*2,rocks2,moves-1),
            checkWin(rocks1,rocks2*2,moves-1),
            checkWin(rocks1+1,rocks2,moves-1),
            checkWin(rocks1,rocks2+1,moves-1)]
    return any(vars) if(moves-1)%2==0 else all(vars)
