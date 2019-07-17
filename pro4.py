p,q=map(str,input().split())
temp=0
if len(p)>len(q):
  p,q=q,p
r=0
while r<len(p):
  temp+=(ord(q[r])-ord(p[r]))
  r+=1
for r in range(r,len(q)):
  temp+=ord(q[r])-ord('a')+1
print(temp)
