

print("x y z w")

for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                f = (((x and(not y))<=(z and w)) and ((y<=z) or (w<=x)))==0
                if(f):
                    print(x,y,z,w)