import math

print ("welcome to donw payment calculation")

print ("The cost of house 1 is 100000")

print (" lets check if you have a good credit")

x = input ( "Enter y if you have a good score else n :  ")

if x == 'y':
    y = (100000 / 100) * 10

elif x == 'n':
    y= (100000/100) * 20
else:
    print ("give a proper input")

print ("downpayment value " , y)




