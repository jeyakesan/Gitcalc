numbers = [1,20,3,400,401,5,5]
unique=[]
for number in numbers:
    if number not in unique:
        unique.append(number)
print (unique)
max =0
for item in unique:
    if max < item:
        max = item
print (max)