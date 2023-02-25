synonyms = dict()
for i in range(int(input())):
    inpt = input().split()
    synonyms.update({inpt[0]: inpt[1]})
    synonyms.update({inpt[1]: inpt[0]})
try:
    print(synonyms[input()])
except KeyError:
    print("N/A")