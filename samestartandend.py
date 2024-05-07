stringsList = ["abc", "123", "2332", "aBBA", "heelloo", "1212", "DcEfD"]

# Initialize a counter for matching strings
matching_count = 0

# Check each string in the list
for s in stringsList:
    # Convert the string to lowercase for case-insensitive comparison
    s_lower = s.lower()
    
    # Check if the first and last characters are the same
    if s_lower[0] == s_lower[-1]:
        matching_count += 1

print(f"Number of strings with the same character at the start and end: {matching_count}")
