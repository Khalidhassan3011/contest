ledNeed = [2, 5, 5, 4, 5, 6, 3, 7, 6, 6]

n = int(input())
for i in range(0, n):
    num = input()

    totalLed = 0

    for j in num:
        totalLed += ledNeed[int(j) - 1]

    print(f"{totalLed} leds")
