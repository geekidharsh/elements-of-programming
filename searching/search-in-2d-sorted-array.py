"""
A 2D sorted array is sorted row and column wise. 
i.e whose rows and columns are in a non decreasing order.

example = [ [-1, 2, 4,5,6],
			[1,5,5,9,21],
			[3,6,6,9,22],
			[3,6,8,10,24],
			[6,8,9,12,25],
			[8,10,12, 13,40]]

given a 2D array A, and a value x. Find if x in A. 
"""

# solution:
# ----------
# use binary search technique
# start from top right corner. explain this to the interviewer
# eliminate each row or column upon each iteration 


# assumptions:
# ----------
# arr is only integers values, x is only integer
# item is 2d sorted
# sample 2d arr is given
# only return first occurance of x, if multiple x values are found


A = [ 
	[-1, 2, 4,5,6],
	[1,5,5,9,21],
	[3,6,6,9,22],
	[3,6,8,10,24],
	[6,8,9,12,25],
	[8,10,12, 13,40]]


def search_2d_sorted_arr(A, x):
	row = 0
	col = len(A[0])-1

	while row < len(A) and col >=0:
		if A[row][col] == x:
			return True
		elif A[row][col] < x:
			row += 1
			# verify movement using print
			# print('down')
		else: 
			col -= 1
			# verify movement using print
			# print('left')
	return False



	# print(A[row][col])
	print(len(A))

"""
time complexity is O(row+col)
since at every operation binary search is getting rid of either a row or a column
"""


x = 7
print(search_2d_sorted_arr(A,x))