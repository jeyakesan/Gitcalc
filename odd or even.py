n = int (input ())
odd_or_even= n%2
if odd_or_even == 1:
    print ("weird")
elif odd_or_even == 0:
    if 2<=n<=5:
        print ("Not weird")
    elif 6<=n<=20:
        print ("weird")
    elif n > 20:
        print ("Not weird")

