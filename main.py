def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n_terms = int(input("Enter the number of terms: "))

for i in range(n_terms):
    print(fibonacci(i))
