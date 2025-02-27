# We have two six-sided dice. Each can give any number between 1 to 6.
# First die can have 6 poosible outcomes when it is rolled seperately.
#Second die can have 6 possible outcomes when it is rolled seperately.
# When both the die are rolled together the pair-up with one-another to give the required output. This is achieved my the use of multiplication.
#Total combinations =(no.of possible outcomes by first die * no.of possible outcomes by second die)= 6*6=36.
import itertools

# Find all possible combinations of dice rolls
dice_rolls = list(itertools.product(range(1, 7), range(1, 7)))

# Calculate the number of combinations
num_combinations = len(dice_rolls)

print(f"Total number of combinations: {num_combinations}")