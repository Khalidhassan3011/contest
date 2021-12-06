a, b, c = input().split()

numbers = [float(a), float(b), float(c)]
numbers.sort(reverse=True)
a = numbers[0]
b = numbers[1]
c = numbers[2]

if a >= b + c:
    print("NAO FORMA TRIANGULO")
elif a ** 2 == b ** 2 + c ** 2:
    print("TRIANGULO RETANGULO")
elif a ** 2 > b ** 2 + c ** 2:
    print("TRIANGULO OBTUSANGULO")
elif a ** 2 < b ** 2 + c ** 2:
    print("TRIANGULO ACUTANGULO")

if a == b == c:
    print("TRIANGULO EQUILATERO")
if len(list(dict.fromkeys(numbers))) == 2:
    print("TRIANGULO ISOSCELES")


# Triangle Types
