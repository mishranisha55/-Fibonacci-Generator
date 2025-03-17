fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

if _name_ == "_main_":
    while True:
        print("\nChoose an option:")
        print("1. Generate Fibonacci sequence up to a certain value.")
        print("2. Generate Fibonacci sequence with a fixed number of terms (handling large numbers).")
        choice = input("Enter your choice (1 or 2): ").strip()

        if choice == "1":
            try:
                max_value = int(input("Enter the maximum value: "))
                result = fibonacci_up_to_value(max_value)
                print("Fibonacci sequence:", result)
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        elif choice == "2":
            try:
                n = int(input("Enter the number of terms: "))
                if n < 0:
                    print("Number of terms cannot be negative.")
                else:
                    result = fibonacci_large_numbers(n)
                    print("Fibonacci sequence:", result)
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        else:
            print("Invalid choice. Please enter 1 or 2.")

        another = input("Do you want to try again? (yes/no): ").strip().lower()
        if another != "yes":
            break
