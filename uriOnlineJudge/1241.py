x = int(input())
for i in range(x):
    a, b = input().split()
    lenA = len(a)
    lenB = len(b)
    if lenA >= lenB and a[-lenB:] == b:
        print("encaixa")
    else:
        print("nao encaixa")
