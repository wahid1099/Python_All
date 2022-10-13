# sample_dict = {'a': 1000, 'b': 200, 'c': 300}
# # print('val1' in d.values())
# if 100 in sample_dict.values():
#     print("present")
# else:
#     print("Not present!")


sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
keys = ["name", "salary"]
# keys = ["name", "salary"]

newDict = {k: sample_dict[k] for k in keys}
print(newDict)

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# # but this line shows dict comprehension here 
# myDict = { k:v for (k,v) in zip(keys, values)} 
 
# # We can use below too
# # myDict = dict(zip(keys, values)) 
 
# print (myDict)