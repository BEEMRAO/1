x=int(input())
y=[]
for i in range(x):
  y.append(input())
  a,b,flag ='',0,False
for m in y[0]:
  for n in y[1:]:
    if len(n)==b:
      flag=True
      break
    if n[b]!=m:
      break
  else:
    a+=m
  if flag:
      break
  b+=1
print(a)
  
  
