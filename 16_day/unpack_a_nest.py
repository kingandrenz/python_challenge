nested_list = [[12, 34, 56, 67], [34, 68, 78]]
unpack = []
lst = [34, 67, 78]
for i in nested_list:
    for j in i:
        if j in lst and j not in unpack:
            unpack.append(j)

print(unpack)
