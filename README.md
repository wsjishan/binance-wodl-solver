# Binance WODL Solver

This script finds words from a dictionary file based on specified criteria such as word length, required letters, excluded letters, and fixed positions of letters.

## Usage
1. **Input Parameters**:
   - `word_length`: Specify the length of the word you want to find.
   - `required_letters`: List of letters that must be present in the word (comma-separated).
   - `excluded_letters`: List of letters that must not be present in the word (comma-separated).
   - `positions`: Specific positions and their corresponding letters that the word must match (e.g., 1:h means 'h' must be in the 1st position).

2. **Instructions**:
   - Run the script.
   - Enter the required parameters as prompted.
   - Ensure not to enter the same letter in both the required and excluded letters sections.
   - Choose a unique starting letter (non-repeating) for your game word by googling a suitable letter.

3. **Example**:
   - If you want to find a 5-letter word containing 'a' and 'e', not containing 'b' or 'c', with 'h' in the 1st position and 'l' in the 3rd position, you would input:
     - Word length: 5
     - Required letters: a,e
     - Excluded letters: b,c
     - Position 1:h
     - Position 3:l

4. **Dictionary**:
   - Ensure a dictionary file named `dictionary.txt` is in the same directory. Each word should be on a separate line.
   - This script uses a dictionary of almost 350,000 words sourced from [dwyl/english-words](https://github.com/dwyl/english-words/tree/master), which ensures comprehensive word coverage for most cases, though some searches may require multiple steps.
