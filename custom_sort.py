custom_sort = lambda x: (len(x), x)

list = ["basketball", "soccer", "football", "tennis", "hockey", "baseball"]

sorted_list = sorted(list, key=custom_sort)

print(sorted_list)