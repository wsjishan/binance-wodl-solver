def load_words():
    with open("dictionary.txt") as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


def find_words(word_length, required_letters, excluded_letters, positions):
    english_words = load_words()

    # Filter words based on length
    words = [word for word in english_words if len(word) == word_length]

    # Filter words based on required letters
    required_letters = set(required_letters.split(","))
    words = [word for word in words if required_letters <= set(word)]

    # Filter words based on excluded letters
    excluded_letters = set(excluded_letters.split(","))
    words = [
        word for word in words if not any(letter in word for letter in excluded_letters)
    ]

    # Filter words based on fixed positions
    for position, letter in positions.items():
        words = [word for word in words if word[position - 1] == letter]

    return words


if __name__ == "__main__":
    # Input parameters
    word_length = int(input("Enter the word length: "))
    required_letters = input("Enter the required letters (comma-separated): ")
    excluded_letters = input("Enter the excluded letters (comma-separated): ")
    positions = {}
    while True:
        position = input(
            "Enter the position (1-based) and letter (e.g., '1:h'), or enter 'done' to finish: "
        )
        if position.lower() == "done":
            break
        pos, letter = position.split(":")
        positions[int(pos)] = letter.strip()

    # Find words
    matching_words = find_words(
        word_length, required_letters, excluded_letters, positions
    )

    # Print the results
    print("Matching words:", matching_words)
