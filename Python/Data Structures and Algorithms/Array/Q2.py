# Question Link: https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/2_Arrays/2_arrays_exercise.md
heros=['spider man','thor','hulk','iron man','captain america']

# 1
print(len(heros))

# 2
heros.append("black panther")
print(heros)

# 3
heros.remove("black panther")
heros.insert(3, "black panther")
print(heros)

# 4
heros[1:3] = ["doctor strange"]
print(heros)

# 5
heros.sort()
print(heros)
