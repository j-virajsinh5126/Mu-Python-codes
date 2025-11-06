my_list = [1,2,2,3,3,4,4,4,4]

frequency = {}
for item in my_list:
    frequency[item] = frequency.get(item, 0) + 1
print(frequency)
