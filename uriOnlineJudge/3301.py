names = ["Huguinho", "Zezinho", "Luisinho"]
x, y, z = input().split()
numbers, sortedNumbers = [x, y, z], [x, y, z]
sortedNumbers.sort(reverse=True)
print(names[numbers.index(sortedNumbers[1])].lower())
