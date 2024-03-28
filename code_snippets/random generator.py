# Generate a random whole number depending upon user's bounds

import random

lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

generated_number = random.randrange(lower_bound, upper_bound)
print(generated_number)