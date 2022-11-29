count = 1
with open(r'words.dat', 'r') as file:

    data = file.read()

    lines = data.split()
    for line in lines:

        print(f"{count}:{line}")
        count += 1
