def build_pyramid(n, current=1):
    if current > n:
        return
    # Print spaces and stars
    spaces = ' ' * (n - current)
    stars = '*' * (2 * current - 1)
    print(spaces + stars)

    # Recursive call for next level
    build_pyramid(n, current + 1)

# Example: Build a pyramid with 5 levels
levels = int(input("Enter the number of levels for the pyramid: "))
print("\nHere is your pyramid:\n")
build_pyramid(levels)
