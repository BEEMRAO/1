a,b=map(int,input().split())
c=list(input().split())
c=[int(x) for x in c]
sum=0
for j in range(0,n):
  sum=sum+c[j]
print(sum)

