weight = int (input ("Weight: "))
measure = str (input ("(L)bs or (K)g: "))
if measure.upper() == 'L':
    print (f"you are {weight * 0.45} Kilograms ")
elif measure.upper() == 'K':
    print (f"you are {weight / 0.45} pounds")
else:
    print ("enter correct value")