largest = max(45, 89, 54, 116, -12)
numbers = [ 12, 45, 65, 23, 89, 78, 11]
nums = {12, 45, 56, 45, 12, 89}
big_nums = max(nums)
# print(big_nums) 
numbers_rev = reversed(numbers)
# print(list(numbers_rev))
sorted_numbers = sorted(numbers, reverse=True)
# print(sorted_numbers)
actors = [
    {'name': 'Sakib Khan', 'age': 34 },
    {'name': 'Kalman Khan', 'age': 54 },
    {'name': 'Aruk Khan', 'age': 52 },
    {'name': 'Xolaiman Khan', 'age': 23 },
    {'name': 'Bappi khan', 'age': 29 },
]

# sorted_actors = sorted(actors, key = lambda actor: actor['age'], reverse=True)
# sorted_actors = sorted(actors, key = lambda actor: actor['name'], reverse=True)
sorted_actors = sorted(actors, key = lambda actor: actor['name'])
# print(sorted_actors)

friends = ['Kabli', 'Dabul', 'mosharrof', 'Badol', 'Noman']
# sorted_friends = sorted(friends)
sorted_friends = sorted(friends, reverse= True)
print(sorted_friends)