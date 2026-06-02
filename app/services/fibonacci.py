def fibonacci(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be non-negative")
    # two first Fibonacci numbers
    a, b = 0, 1 
    for f in range(n):
        a, b = b, a + b # a becomes old b, b gets added with a and creates new b
    return a # return a as it is the current Fibonacci number after n loops

if __name__ == "__main__": # do not run when executed by test
    while True:
        user_input = input("Enter a number (or q to quit): ")
        if user_input.lower() == "q":
                break
        
        # Convert input to integer
        try:
            n = int(user_input)
        except ValueError:
            print("Input must be an integer")
            continue

        # Run fibonacci and handle validation errors
        try:
            result = fibonacci(n)
            print(result)
        except (TypeError, ValueError) as e:
            print(e)