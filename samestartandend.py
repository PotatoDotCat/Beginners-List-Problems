stringsList = ["abc", "123", "2332", "aBBA", "heelloo", "1212", "DcEfD"]
matching_count = 0

for s in stringsList:
    s_lower = s.lower()
    
    if s_lower[0] == s_lower[-1]:
        matching_count += 1

print(f"Number of strings with the same character at the start and end: {matching_count}")
