r,z = 0,0
x = int(input())
pal = x
while(x!=0):
    y = x%10
    r = z+y
    z = r*10
    x = int(x/10)
if pal == r:
    print("true")
else:
    print("false")