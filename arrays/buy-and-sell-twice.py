# program to make maxium profit. by buy and selling stock twice

# edge case: 
# 1st buy comes always before the second buy


def buy_sell_twice(s):
	mini = s[0]
	max_profit_today = 0
	max_overall_profit = 0


	for price in range(1, len(s)):
		if s[price] > mini:
			max_profit_today = s[price] - mini
		else:
			mini = s[price]






s = [12,11,13,9,12,8,14,13,15]