ALL_DAYS = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']

rainfall_data = []

maxrain = 0
minindex = 0

minrain = 100000
maxindex = 0
for days in range(len(ALL_DAYS)):
    data = int(input(f'Enter Rainfall for {ALL_DAYS[days]} in mm :'))
    rainfall_data.append(data)
    if (data < minrain):
        minrain = data
        minindex = days
    if (data > maxrain):
        maxrain = data
        maxindex = days

print("\n")
print('-'*50)
print(f"Maximum rain is on {ALL_DAYS[maxindex]} {maxrain} mm")
print(f"Minimum rain is on {ALL_DAYS[minindex]} {minrain} mm")
