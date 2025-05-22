def fibonacci(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    fib_inv = fib[:n][::-1]
    for num in fib_inv:
        print(num)
