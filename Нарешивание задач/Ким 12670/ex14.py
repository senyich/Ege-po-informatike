
for x in "0123456789ABCD":
    a1 = f"4B3{x}1"
    a2 = f"5{x}F83"
    sum = int(a1,14)+int(a2,16)
    if(sum%13==0):
        print(sum/13)