# input
# 7
# 100 180 260 310 40 535 695
# 10
# 23 13 25 29 33 19 34 45 65 67

def buy_and_sell(stock_price)
	result = 0
	min = 0
	max = 1
	for i in range(0, len(stock_price)):
		while stock_price[i] < stock_price[i+1]:
			min = i




