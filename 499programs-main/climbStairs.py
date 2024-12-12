def climb_stairs(n):
    if n < 3:
        return n
    cache = [0] * n
    cache[0], cache[1] = 1, 2
    for i in range(2, n):
        cache[i] = cache[i - 1] + cache[i - 2]
    return cache[n - 1]

def climb_stairs_variation(n):
    if n < 3:
        return n
    cache = [0] * n
    cache[0], cache[1], cache[2] = 1, 2, 4
    for i in range(3, n):
        cache[i] = cache[i - 1] + cache[i - 2] + cache[i - 3]
    return cache[n - 1]

if __name__ == "__main__":
    n = int(input("Enter the number of steps: "))
    print("Choose the type of problem:")
    print("1. Climb stairs with 1 or 2 steps at a time")
    print("2. Climb stairs with 1, 2, or 3 steps at a time")
    choice = int(input("Enter your choice (1 or 2): "))
    if choice == 1:
        print(f"Number of distinct ways to climb {n} steps (1 or 2 at a time): {climb_stairs(n)}")
    elif choice == 2:
        print(f"Number of distinct ways to climb {n} steps (1, 2, or 3 at a time): {climb_stairs_variation(n)}")
    else:
        print("Invalid choice. Please enter 1 or 2.")
