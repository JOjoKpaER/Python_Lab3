inpt = list()
for i in range(int(input())):
    inpt.append(input())
st = set(inpt)
res = 0
for i in st:
    if inpt.count(i) > 1:
        res += inpt.count(i)
print(res)
