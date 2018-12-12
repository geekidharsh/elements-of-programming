# from an array of stock prices, buy and sell stock once so as to make maximum profit. 
# You don't need to sell a stock if you can't make profit



def buy_and_sell_once_custom(stock_prices):
	mini = stock_prices[0]
	days []
	diff = 0
	max_profit = 0

	if len(stock_prices) > 2:
		for i in range(1, len(stock_prices)):
			today_profit = stock_prices[i] - mini
			if mini > stock_prices[i]:
				mini = stock_prices[i]
			if today_profit > max_profit:
				max_profit = today_profit
	return max_profit


# book
def buy_and_sell_once(stock_prices):
	min_price, max_profit = stock_prices[0],0
	days = 0

	if len(stock_prices) > 2:
		for price in range(1, len(stock_prices)):
			max_profit_today = stock_prices[price] - min_price
			min_price = min(stock_prices[price] , min_price)
			max_profit = max(max_profit, max_profit_today)
			print(max_profit)
	else:
		return max(stock_prices)



def main():
	# test case
	s1 =  [100, 180, 260, 310, 40, 535, 650, 400]
	s2 =  [100, 180, 260, 310, 40, 535, 400]
	s3 =  [40, 180, 260, 310, 40, 535, 650, 600]

	print(buy_and_sell_once_custom(s1))






if __name__ == '__main__':
	main()
