numbers = [2, 2, 2, 5]
for items in numbers:
    output = ''
    for count in range (items):
        output = output + 'x'
    print (output)

prices = [10 ,20 ,30]
total =0
for item in prices :
   total = item + total
print (total)
for x in range (4):
   for y in range (3):
      print (f"({x}, {y})")