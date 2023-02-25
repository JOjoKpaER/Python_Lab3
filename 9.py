jisyo = dict()
for j in range(2):
    for i in range(int(input())):
        inpt = input().split()
        if inpt[0] in jisyo.keys():
            jisyo.update({inpt[0]: int(jisyo[inpt[0]]) + int(inpt[1])})
        else:
            jisyo.update({inpt[0]: int(inpt[1])})
print(jisyo)
