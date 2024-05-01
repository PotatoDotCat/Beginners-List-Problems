cerealList = []

while True:
    cereal = input("Enter a cereal: ")
    if cereal.lower() not in ['sultana and bran', 'weetbix']:
        cerealList.append(cereal)
    else:
        break

print("List of (good) Cereals:")
for c in cerealList:
    print(c)
