

def find_salary_threshold(target_payroll, current_salaries):
	# custom algorithm, not from the book

	# first i take avg salary based on payroll and total number of current_salaries in current_salaries list
	# residue is the remainder left after comparing salary with avg_target for any salary that's more than avg_target, those will need to be adjusted later to the 'capped' salary, 
	# since for salary below cap, nothing is changed

	# finally we compute cap by adding avg_target, k times for each count of salaries more than avg, 
	# we divide this by the same count of salaries more than avg_target


	avg_target = target_payroll // len(current_salaries)
	residue = 0
	i = 0
	while i < len(current_salaries):
		if current_salaries[i] < avg_target:
			residue += avg_target - current_salaries[i]
			i += 1
		else:
			break
	cap_salary = (residue + avg_target*(len(current_salaries) - i)) // (len(current_salaries) - i)
	print(cap_salary)



# best case: O(1), avg case: o(k) for a[k] < avg_target, worst case: O(n)
# if input is sorted, try utilizing binary sort


A = [20, 30, 40, 90, 100]
target_payroll = 210

find_salary_threshold(target_payroll, A)