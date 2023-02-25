import random

num_list0 = list()
num_list1 = list()
for i in range(random.randint(1, 10)):
    num_list0.append(random.randint(0, 10))
    num_list1.append(random.randint(0, 10))

print(num_list0, "\n", num_list1, sep='')

print(*sorted(set(num_list0).union(set(num_list1))))
