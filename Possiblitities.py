def dice_distribution():
    """Calculates and displays the distribution of dice roll combinations."""

    # Create a 6x6 matrix to store the sums
    matrix = [[0 for _ in range(6)] for _ in range(6)]

    # Fill the matrix with the sums
    for i in range(6):
        for j in range(6):
            matrix[i][j] = i + j + 2  # +2 because dice start at 1

    # Print the matrix
    print("Dice Roll Distribution Matrix:")
    for row in matrix:
        print(" ".join(map(str, row)))

dice_distribution()