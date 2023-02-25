txt = list()
for i in range(int(input())):
    inpt = list(input().split())
    txt += inpt
print(len(set(txt)))