# Task 1

import math
import statistics

numbers = [12, 32, 16, 25]
square_roots = [math.sqrt(num) for num in numbers]
print("Square Roots:", square_roots)
average = statistics.mean(numbers)
print("Average:", average)

# Task 2
from my_package import get_square_roots, get_average

nums = [4, 16, 25, 36]

print("Square Roots:", get_square_roots(nums))
print("Average:", get_average(nums))