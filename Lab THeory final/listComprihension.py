# x = [i for i in range(1, 10)]
# print(x)


# x = 'hello'

# y = [i for i in x]
# print(y)


# x = [i for i in range(1, 10) if i % 2 == 0]
# print(x)


# lst = ["Even" if x % 2 == 0 else "Odd" for x in range(1, 100)]
# print(lst)


# lst = [(x, y) for x in [1, 2, 3, 4, 5] for y in range(6, 10) if x != y]
# print(lst)

# i = [1, 2, 3, 4, 5]
# j = [1, 2, 3, 4, 5]
# dct = {i: [1, 2, 3, 4, 5] for i in range(1, 6)}
# print(dct)
# lst = [1, 2, 3, 4, 5]
# dct = {i: lst for i in range(1, 6) if i.keys() != lst}
# print(dct)


# dct = {k: v for k, v in range(1, 6) if k != v}
# print(dct)

# [for x in range(1, 6)]


# dct = {}

# for i in range(1, 6):
#     dct[i] = []
#     for j in range(1, 6):
#         if i != j:
#             dct[i].append(j)

# print(dct)
# lst = [1, 2, 3, 4, 5]
# dct = {}
# x = {i: [] for i in range(1, 6) for j in range(1, 6) i != lst[j]}
# x = {i: [j] for i in range(1, 6) for j in range(1, 6) if i != j}
# numbers = [1, 2, 3, 4, 5]
x = {i: [j for j in range(1, 6) if i != j] for i in range(1, 6)}


print(x)
