def calculate_total_average(mark1, mark2, mark3):
	total = mark1 + mark2 + mark3
	average = total / 3
	return total, average
total, average = calculate_total_average(85, 90, 78)
print("Total:", total)
print("Average:", average)