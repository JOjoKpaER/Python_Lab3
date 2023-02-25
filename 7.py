inpt = list(input().split())
st = set(inpt)
for i in st:
    print(i, ":", inpt.count(i), sep=' ', end=' ')
