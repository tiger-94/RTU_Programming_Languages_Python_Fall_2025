"""
Task 4 – Text-based Arithmetic Analyzer
--------------------------------------
Create a text-based analyzer that:
1. Counts non-space characters.
2. Counts words.
3. Extracts numbers and computes their sum and average.
Use helper functions:
- count_characters(text)
- count_words(text)
- extract_numbers(text)
- analyze_text(text)
Print formatted summary in main.
"""

def count_characters(text):
    """Count non-space characters in a string."""
    return sum(1 for c in text if not c.isspace())

def count_words(text):
    """Count number of words in a string."""
    return len(text.split())

def extract_numbers(text):
    """Return list of integers found in text."""
    numbers = []
    for token in text.split():
        if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
            numbers.append(int(token))
    return numbers

def analyze_text(text):
    """Perform text-based arithmetic analysis."""
    chars = count_characters(text)
    words = count_words(text)
    numbers = extract_numbers(text)
    total = sum(numbers)
    avg = total / len(numbers) if numbers else 0
    return chars, words, numbers, total, avg

if __name__ == "__main__":
    text = input("Enter a sentence containing words and numbers: ")
    chars, words, numbers, total, avg = analyze_text(text)

    print("\n--- Text Analysis Summary ---")
    print(f"Non-space characters: {chars}")
    print(f"Word count: {words}")
    print(f"Numbers found: {numbers}")
    print(f"Sum of numbers: {total}")
    print(f"Average of numbers: {avg:.2f}")
