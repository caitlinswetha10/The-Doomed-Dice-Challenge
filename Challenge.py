def calculate_sum_probabilities(die_a, die_b):
    # Initialize a dictionary to count occurrences of each sum
    sum_counts = {i: 0 for i in range(2, 13)}
    
    # Count occurrences of each sum
    for a in die_a:
        for b in die_b:
            sum_value = a + b
            sum_counts[sum_value] += 1
            
    # Calculate total combinations
    total_combinations = len(die_a) * len(die_b)
    
    # Calculate probabilities
    probabilities = {sum_value: count / total_combinations for sum_value, count in sum_counts.items()}
    return probabilities

def transform_dice(die_a, die_b):
    # Calculate original probabilities
    original_probabilities = calculate_sum_probabilities(die_a, die_b)
    
    # New Die A: Constrained to max 4 spots
    new_die_a = [1, 2, 3, 4, 4, 4]  # Example transformation for Die A
    
    # New Die B: Start with the same as original for Die B
    new_die_b = [1, 2, 3, 4, 5, 6]  # This will be adjusted
    
    # Adjust Die B to maintain the same probabilities
    # We will need to ensure that the sums match the original probabilities
    # Here we will adjust Die B based on the original probabilities
    
    # Calculate new probabilities
    new_probabilities = calculate_sum_probabilities(new_die_a, new_die_b)
    
    # Check if the probabilities match
    for sum_value in range(2, 13):
        if original_probabilities[sum_value] != new_probabilities[sum_value]:
            print(f"Probabilities do not match for sum {sum_value}.")
            return None, None
    
    return new_die_a, new_die_b

# Original Dice
Die_A = [1, 2, 3, 4, 5, 6]
Die_B = [1, 2, 3, 4, 5, 6]

# Transform the dice
New_Die_A, New_Die_B = transform_dice(Die_A, Die_B)

print("New Die A:", New_Die_A)
print("New Die B:", New_Die_B)