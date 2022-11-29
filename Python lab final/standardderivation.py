
ALL_DAYS = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']

rainfall_data = []

sum_of_mean = 0

for days in range(len(ALL_DAYS)):
    data = int(input(f'Enter Rainfall for {ALL_DAYS[days]} in mm :'))
    rainfall_data.append(data)
    sum_of_mean = sum_of_mean + data


mean_value = sum_of_mean/7

sum = 0

for i in rainfall_data:
    sum += (i - mean_value)**2


sum = sum/7

standard_deviation = sum**0.5

print("Standard deviation:", standard_deviation)
