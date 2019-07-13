x=int(input())
n=list(map(int,input().split()))
b=max(n)
x,y=0,0
for i in range(0,len(n)-1):
  for j in range(i+1,len(n)):
      if B(n[i]+n[j])<b:
        x,y=n[i],n[j]
        b=B(x+y)
print(x,y)        
