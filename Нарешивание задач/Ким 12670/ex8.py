from itertools import permutations

alf = "МАРИНА"
counter = 0
for i in set(permutations(alf)):
    s = "".join(i)
    if(i[0] not in "АИA"):
        counter+=1

print(counter)