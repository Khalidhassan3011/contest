balance = float("{:.2f}".format(float(input())))


def calculate_percent(amount, percent):
    return amount * percent / 100


vat = 0
if balance > 4500:
    vat = calculate_percent((balance - 4500), 28) + calculate_percent(1500, 18) + calculate_percent(1000, 8)
elif balance > 3000:
    vat = calculate_percent((balance - 3000.01), 18) + calculate_percent(1000, 8)
elif balance > 2000:
    vat = calculate_percent((balance - 2000.01), 8)

print("Isento" if vat == 0 else "R$ {:.2f}".format(vat))
