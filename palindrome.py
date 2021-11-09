x = int(input())
y = x
sum = 0
while x>0:
    rem = x%10
    x=x//10
    sum = sum*10 + rem
print(sum)
if(y == sum):
    print("pallindromr")
else:
    print("not a pallindromr")
