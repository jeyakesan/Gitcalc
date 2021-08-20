phone = input ("Phone: ")
dict = {
    '1':'one',
    '2':'two',
    '3':'three',
    '4':'four'
}
output = ""
for ch in phone:
    output += dict.get(ch) + ' '
print (output)