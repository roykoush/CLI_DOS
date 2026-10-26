def print_butterfly(n):
    for i in range(1, n + 1):
        stars = "*" * i
        spaces = " " * (2 * (n - i))
        print(stars + spaces + stars)

    for i in range(n, 0, -1):
        stars = "*" * i
        spaces = " " * (2 * (n - i))
        print(stars + spaces + stars)

print_butterfly(5)