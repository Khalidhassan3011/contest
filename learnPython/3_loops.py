# while
i = 0

if i is True:
    print(True)

while True:
    i += 1
    if i == 5:
        continue
    elif i == 10:
        break

for i in range(5):  # default interval
    print(i, end=" ")  # print 0 to 4

print("")
for i in range(0, 10, 2):  # (start, end, interval)
    print(i, end=" ")

print("")
for i in range(5, -1, -1):
    print(i, end=" ")

print("")
for i in [1, 2, 3, 4, 5]:
    if i == 3:
        break
    else:
        print("only executed when no item of the list is equal to 3")
