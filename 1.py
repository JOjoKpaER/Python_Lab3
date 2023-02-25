import random

num_list = list()
for i in range(random.randint(10, 20)):
    num_list.append(random.randint(0, 10))

print(num_list)

print(*set(num_list))
