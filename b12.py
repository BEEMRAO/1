a=input("")
a=a.casefold()
b=reversed(a)
if list(a) == list(b):
    print("yes")
else:
    print("no")
