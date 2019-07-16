x,y=input().strip().split(" ")
y=int(y)
z=0
while z<len(x)-1 and y:
  if(x[z]>x[z+1]):
    y-=1
    x=x[:z]+x[z+1:]
    if(z!=0):
            z-=1
  else:
    z+=1
m=x[:len(x)-y]
print(m)
