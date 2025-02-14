# Constants
DAYS_IN_YEAR = 365
HOURS_IN_DAY = 24
MINUTES_IN_HOUR = 60
SECONDS_IN_MINUTE = 60

def calculate_seconds_in_year():
    """Calculates the total number of seconds in a year."""
    return DAYS_IN_YEAR * HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE

# Running the program
if __name__ == "__main__":
    seconds_in_year = calculate_seconds_in_year()
    print(f"There are {seconds_in_year} seconds in a year!")
