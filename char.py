x,y=input("").split()
a=list(x)
b=list(y)
count=0
for i in range(0,len(a)):
  if(a[i]!=b[i]):
    count+=1
if(count==1):
  print("yes")
