x = int(input())
if x % 2 == 0:
    print(f"{(x * x) // 2} casas brancas e {(x * x) // 2} casas pretas")
else:
    print(f"{((x * x) // 2) + 1} casas brancas e {(x * x) // 2} casas pretas")
