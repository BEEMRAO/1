a=int(input())
b=list(map(int,input().split()))
c=0
for i in range(0,a):
  for j in range(0,i):
    if(b[j]<b[i]):
      c=c+b[j]
print(c)
