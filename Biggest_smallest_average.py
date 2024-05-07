numsList = [7, 6, 23, 8.18, 18, 8, 7.2, 85, 915, 12]

# Find the biggest number and its position
max_num = max(numsList)
max_index = numsList.index(max_num)

# Find the smallest number and its position
min_num = min(numsList)
min_index = numsList.index(min_num)

# Calculate the average
average = sum(numsList) / len(numsList)

print(f"Biggest number: {max_num} (position {max_index})")
print(f"Smallest number: {min_num} (position {min_index})")
print(f"Average: {average:.2f}")
