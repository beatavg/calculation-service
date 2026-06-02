# 5! = 5 x 4 x 3 x 2 x 1 = 120
def factorial(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be non-negative")
    
    result = 1
    for i in range(2, n + 1): # We don't run first loop, so that 0! will return 1
        result *= i # Each iteration multiplies the current result by the next number.
    
    return result

if __name__ == "__main__": # Do not run when executed by test
    while True:
        user_input = input("Enter a number for factorial (or q to quit): ")
        if user_input.lower() == "q":
                break
        
        # Convert input to integer
        try:
            n = int(user_input)
        except ValueError:
            print("Input must be an integer")
            continue

        # Run factorial and handle validation errors
        try:
            result = factorial(n)
            print(result)
        except (TypeError, ValueError) as e:
            print(e)