import random

def roll_dice():
    """Simulates rolling a six-sided die."""
    return random.randint(1, 6)

def roll_two_dice():
    """Rolls two dice and returns their values along with the total."""
    die1 = roll_dice()
    die2 = roll_dice()
    total = die1 + die2
    return die1, die2, total

# Running the program
if __name__ == "__main__":
    die1, die2, total = roll_two_dice()
    print(f"Die 1: {die1}")
    print(f"Die 2: {die2}")
    print(f"Total: {total}")
