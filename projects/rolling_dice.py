# Step 1: Import the random module
# This gives us access to functions that generate random numbers.
# We'll use random.randint() to simulate dice rolls.
import random

# Step 2: Define a function to roll dice
def roll_dice(num):
    # Create an empty list to store each dice result
    results = []
    
    # Step 3: Loop 'num' times (the number of dice the user wants to roll)
    # The underscore (_) is used when we don't care about the loop variable itself.
    for _ in range(num):
        # Generate a random integer between 1 and 6 (inclusive)
        # This mimics the face of a real dice.
        roll = random.randint(1,6)
        
        # Add this dice roll to our results list
        results.append(roll)
    
    # Step 4: After the loop finishes, return the full list of dice rolls
    return results

# Step 5: Ask the user how many dice they want to roll
# input() always returns a string, so we wrap it in int() to convert to a number.
num = int(input("How many dice to roll? "))

# Step 6: Call our function with the user's number and print the results
# The output will be a list of dice values, e.g. [3, 5, 2]
print("Results:", roll_dice(num))

