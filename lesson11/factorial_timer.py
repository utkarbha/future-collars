"""
Alternative task:
Write code implementing factorial and a decorator measuring the execution time.
Save the results for different calls in a text file in the format:
"The calculation time of the factorial for the value {value} is {calculation_time}".
Add a caching mechanism.

Factorial for value 3: 1 * 2 * 3
Factorial for value 7: 1 * 2 * 3 * 4 * 5 * 6 * 7

The task should be tested for values: 1, 9, 23, 88, 175, 299, 512, 1024.
Steps:
    - Implement function to calculate factorial
    - Measure time of calculation
    - Save the results to a file
    - Add a caching mechanism
"""

import time


factorial_cache = {}

def timing_decorator(func):
    def wrapper(n):
        if n in factorial_cache:
            result = factorial_cache[n]
            elapsed = 0.0
        else:
            start = time.time()
            result = func(n)
            elapsed = time.time() - start
            factorial_cache[n] = result

        # Save to file
        with open("factorial_timings.txt", "a") as f:
            f.write(
                f"The calculation time of the factorial for the value {n} is {elapsed:.6f} seconds\n"
            )
        return result
    return wrapper

@timing_decorator
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    chain = " * ".join(str(i) for i in range(1, n + 1))
    print(f"Factorial for value {n}: {chain}")

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


test_values = [1, 9, 23, 88, 175, 299, 512, 1024]


open("factorial_timings.txt", "w").close()


for value in test_values:
    factorial(value)