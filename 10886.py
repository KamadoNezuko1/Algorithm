a = int(input())
one = 0
zero = 0
for i in range(a):
    b = int(input())
    if b == 1:
        one += 1 
    else:
        zero += 1
if one > zero:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")