# Define the speed of light as a constant (in meters per second)
C = 299792458  

def mass_to_energy(mass):
    """Calculates energy using E = m * C^2"""
    return mass * C**2

# Running the program in a loop to accept multiple inputs
if __name__ == "__main__":
    while True:
        try:
            mass = float(input("Enter kilos of mass (or type '0' to exit): "))
            if mass == 0:
                print("Exiting program.")
                break
            energy = mass_to_energy(mass)
            print("\ne = m * C^2...\n")
            print(f"m = {mass} kg")
            print(f"C = {C} m/s")
            print(f"{energy} joules of energy!\n")
        except ValueError:
            print("Please enter a valid numerical mass.\n")

