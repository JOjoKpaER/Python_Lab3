inpt = input().split()
for i in range(len(inpt)):
    if inpt[i] in inpt[0:i]:
        print("YES ", end='')
    else:
        print("NO ", end='')
