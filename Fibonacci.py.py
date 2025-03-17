def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Example usage:
if __name__ == "__main__":
    fib_gen = fibonacci_generator()
    for _ in range(10):  # Generate first 10 Fibonacci numbers
        print(next(fib_gen))
