# Fermat's Last Theorem Near Miss Finder

## Overview

This project is a simple Python program that searches for "near misses" for Fermat's Last Theorem, which states that there are no integer solutions to the equation:

\[
x^n + y^n = z^n
\]

for \( n > 2 \) and integer values of \( x, y, z \). The program aims to find values of \( x \), \( y \), and \( z \) where the sum of \( x^n + y^n \) is almost equal to \( z^n \), with the smallest possible "miss." It calculates both the absolute miss and the relative miss for each pair of values, identifying the smallest relative miss in a specified range.

## How It Works

The program:

1. Prompts the user to input a value for `n` (the power, where \( 2 < n < 12 \)) and `k` (the upper limit for \( x \) and \( y \), where \( k > 10 \)).
2. Calculates the sum \( x^n + y^n \) and estimates the closest value of \( z \) such that \( z^n \) or \( (z+1)^n \) approximates the sum.
3. Computes both the absolute miss (difference between the sum and \( z^n \)) and the relative miss (ratio of the miss to the sum).
4. Prints the smallest relative miss and its corresponding values of \( x \), \( y \), \( z \), and the absolute miss.

## Functions

### `calculate_miss(x, y, n)`
- **Parameters:**
  - `x`: First integer.
  - `y`: Second integer.
  - `n`: Power to which \( x \) and \( y \) are raised.
- **Returns:**
  - The integers \( x \), \( y \), and \( z \), along with the absolute miss and relative miss for the current combination of values.

### `find_near_misses(n, k)`
- **Parameters:**
  - `n`: Power to which integers are raised.
  - `k`: Upper limit for the range of \( x \) and \( y \).
- **Functionality:**
  - Iterates through all pairs of \( x \) and \( y \) between 10 and \( k \), calculates the near miss for each pair, and tracks the smallest relative miss found.
  - Prints details of the current best near miss during the search and the final best result.

### `main()`
- **Functionality:**
  - Handles user input for \( n \) and \( k \).
  - Validates the input to ensure the values fall within the required range.
  - Calls `find_near_misses(n, k)` to perform the search for near misses.

## Usage

1. Clone the repository or download the script.
2. Run the script using Python:

   ```bash
   python fermat_near_miss.py
   ```

3. Enter the values for \( n \) (where \( 2 < n < 12 \)) and \( k \) (where \( k > 10 \)) when prompted.

4. The program will compute and display the smallest relative miss for the specified values.

## Example

```bash
Welcome to the Fermat's Last Theorem Near Miss Finder!
Enter the power n (where 2 < n < 12): 3
Enter the value k (where k > 10): 15

New smallest miss found: x=10, y=10, z=12, miss=44, relative miss=0.030864
New smallest miss found: x=10, y=11, z=13, miss=98, relative miss=0.047085
New smallest miss found: x=11, y=12, z=14, miss=115, relative miss=0.042835

Final smallest miss:
x=11, y=12, z=14, miss=115, relative miss=0.042835
```

## Requirements

- Python 3.x
- No additional dependencies are required.

---