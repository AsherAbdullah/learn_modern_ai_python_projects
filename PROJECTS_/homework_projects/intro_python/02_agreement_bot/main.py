def favorite_animal_response(favorite_animal):
    return f"My favorite animal is also {favorite_animal}!"

# Test cases
if __name__ == "__main__":
    test_cases = ["dog", "cat", "elephant", "lion", "tiger"]
    
    for animal in test_cases:
        response = favorite_animal_response(animal)
        print(response)
