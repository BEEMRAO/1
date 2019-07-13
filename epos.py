x=input()
a=list(map(int,input().split()))
for i in range(len(a)):
  if (i%2 == 0 and a[i]%2 !=0) or (i%2!=0 and a[i]%2 == 0):
    print(a[i],end= " ")
