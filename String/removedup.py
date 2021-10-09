names = []
n = int(input("how many names you want to enter ?"))

for i in range(n):
    print(i+0 ,"Enter a name")
    names.append(input())

s=set(names)
names=list(s)
for x in names:
    print(x)


