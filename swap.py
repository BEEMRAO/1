x=list(input())
a=len(x)
for i in range(0,a,2):
  x[i],x[i+1]=x[i+1],x[i]
print(*x,odd="")
