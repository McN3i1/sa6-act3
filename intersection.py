intersection = lambda x: x in list_2

list_1 = [1, 2, 3, 4, 5]
list_2 = [3, 4, 5, 6, 7]

intersection = list(filter(intersection, list_1))

print(intersection)