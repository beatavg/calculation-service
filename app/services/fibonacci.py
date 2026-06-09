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
