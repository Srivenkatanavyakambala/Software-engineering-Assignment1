import math

def calculate_miss(x, y, n):
    """Calculate the smallest miss and the corresponding z for given x, y, and n."""
    sum_powers = x**n + y**n
    z = int(sum_powers ** (1/n))  # Estimate z by taking the nth root of the sum

    z_power = z**n
    z1_power = (z + 1)**n

    # Determine which z (either z or z+1) is closer to sum_powers
    miss1 = abs(sum_powers - z_power)
    miss2 = abs(z1_power - sum_powers)

    if miss1 < miss2:
        miss = miss1
    else:
        miss = miss2
        z += 1

    # Calculate relative miss
    relative_miss = miss / sum_powers
    return x, y, z, miss, relative_miss

def find_near_misses(n, k):
    """Find and print the smallest relative miss for given n and k."""
    smallest_relative_miss = float('inf')
    best_x, best_y, best_z, best_miss = None, None, None, None

    for x in range(10, k + 1):
        for y in range(10, k + 1):
            x, y, z, miss, relative_miss = calculate_miss(x, y, n)

            if relative_miss < smallest_relative_miss:
                smallest_relative_miss = relative_miss
                best_x, best_y, best_z, best_miss = x, y, z, miss

                # Print current best near miss
                print(f"New smallest miss found: x={best_x}, y={best_y}, z={best_z}, miss={best_miss}, relative miss={smallest_relative_miss:.7f}")

    print("\nFinal smallest miss:")
    print(f"x={best_x}, y={best_y}, z={best_z}, miss={best_miss}, relative miss={smallest_relative_miss:.7f}")

def main():
    print("Welcome to the Fermat's Last Theorem Near Miss Finder!")

    # Get user input for n and k
    n = int(input("Enter the power n (where 2 < n < 12): "))
    k = int(input("Enter the value k (where k > 10): "))

    if n <= 2 or n >= 12:
        print("Error: n must be greater than 2 and less than 12.")
        return

    if k < 10:
        print("Error: k must be greater than 10.")
        return

    find_near_misses(n, k)

    # Keep the console open until a key is pressed
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
