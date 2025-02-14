import random

def roll_dice():
    """Simulates rolling a six-sided die."""
    return random.randint(1, 6)

def roll_two_dice():
    """Rolls two dice and returns their values."""
    die1 = roll_dice()  # Local scope
    die2 = roll_dice()  # Local scope
    return die1, die2

# Rolling dice three times
if __name__ == "__main__":
    for i in range(1, 4):  # Global scope variable 'i'
        die1, die2 = roll_two_dice()
        print(f"Roll {i}: Die 1 = {die1}, Die 2 = {die2}")
