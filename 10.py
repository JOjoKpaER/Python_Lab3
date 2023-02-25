files = dict()
for i in range(int(input())):
    inpt = input().split(" ", 1)
    files.update({inpt[0]: inpt[1].lower()})
for i in range(int(input())):
    inpt = input().split(" ", 1)
    if inpt[0][0] in files[inpt[1]]:
        print("OK")
    else:
        print("Access denied")
