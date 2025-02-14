def create_mad_lib(adjective, noun, verb):
    """Generates a fun sentence using the provided words."""
    SENTENCE_START = "Code in Place is fun. I learned to program and used Python to make my"
    return f"{SENTENCE_START} {adjective} {noun} {verb}!"

# Running the program with user input
if __name__ == "__main__":
    adjective = input("Please type an adjective and press enter: ")
    noun = input("Please type a noun and press enter: ")
    verb = input("Please type a verb and press enter: ")

    mad_lib_sentence = create_mad_lib(adjective, noun, verb)
    print("\n" + mad_lib_sentence)
