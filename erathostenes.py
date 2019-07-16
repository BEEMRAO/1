x,y=map(int,input().split())
z=0
for i in range(x,y+1):
  if a>0:
    for j in range(2,a):
      if a%i==0:
        break
    else:
      z+=1
print(z)
