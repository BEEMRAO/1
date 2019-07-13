x=int(input())
b=input().split()
b=[int(i) for i in b]
b.sort(reverse=True)
a=int("".join(map(str,b)))
print(a)
