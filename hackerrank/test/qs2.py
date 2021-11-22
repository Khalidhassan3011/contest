
def mosharof_knapsack():
	mosharof_k = [[0 for x in range(mosharof_capacity + 1)] for x in range(mosharof_len + 1)]

	for i in range(mosharof_len + 1):
		for w in range(mosharof_capacity + 1):
			if i == 0 or w == 0:
				mosharof_k[i][w] = 0
			elif mosharof_weight[i-1] <= w:
				mosharof_k[i][w] = max(mosharof_profit[i-1] + mosharof_k[i-1][w-mosharof_weight[i-1]], mosharof_k[i-1][w])
			else:
				mosharof_k[i][w] = mosharof_k[i-1][w]

	res = mosharof_k[mosharof_len][mosharof_capacity]
	print(res)
	print("The most valuable subset is :")
	w = mosharof_capacity
	for i in range(mosharof_len, 0, -1):
		if res <= 0:
			break
		if res == mosharof_k[i - 1][w]:
			continue
		else:

			# This item is included.
			# print(mosharof_weight[i - 1])
			print(f"item {i},", end=" ")

			# Since this weight is included
			# its value is deducted
			res = res - mosharof_profit[i - 1]
			w = w - mosharof_weight[i - 1]


mosharof_profit = []
mosharof_weight = []

mosharof_total = int(input("enter the number of items "))

for i in range(0, mosharof_total):
	mosharof_w, mosharof_p = input(f"enter the weight and profit of the item {i+1}: ").split()
	mosharof_weight.append(int(mosharof_w))
	mosharof_profit.append(int(mosharof_p))

mosharof_capacity = int(input("enter the capacity of the knapsack: "))
mosharof_len = len(mosharof_profit)
mosharof_knapsack()

