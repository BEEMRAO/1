x=input()
a=list(map(int,input().split()))
b=False
for i in b:
  if b.count(i)>1:
    b=True
    break
print(i if b else "unique")    
