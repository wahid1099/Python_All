# lst=[(5,10),(50,100)]
arr = [["Empty" for i in range(5)] for j in range(5)]

print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in arr]))



# arr=[]
# rows, cols=5,5
# for i in range(rows):
#     col = []
#     for j in range(cols):
#         col.append(ord("a")+'0')
#     arr.append(col)
# print(arr)