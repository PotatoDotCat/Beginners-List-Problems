iLikePesto = []
otherFoods = []

for _ in range(8):
    food = input("What's your favourite food? ")
    if food.lower() == 'pesto':
        iLikePesto.append(food)
    else:
        otherFoods.append(food)

num_pesto = len(iLikePesto)
print(f"Pesto is loved by {num_pesto} people!")
for _ in range(num_pesto):
    print("I like pesto")

print("\nOther Foods:")
for food in otherFoods:
    print(food)
