import string

# Function to clean and process the list of sentences
def process_sentences(sentences):
    # Initialize an empty list for the words
    words = []

    # Process each sentence
    for sentence in sentences:
        # Clean up the sentence: strip spaces, lowercase, and replace punctuation
        cleaned_sentence = sentence.strip().lower().translate(str.maketrans('', '', string.punctuation))
        # Split the sentence into words and add them to the words list
        words.extend(cleaned_sentence.split())

    # Count total words
    total_words = len(words)

    # Find unique words
    unique_words = set(words)

    # Count unique words
    unique_word_count = len(unique_words)

    # Calculate lexical variety (unique words / total words)
    lexical_variety = unique_word_count / total_words if total_words != 0 else 0

    # Print results
    print("Words List:", words)
    print("Unique Words:", unique_words)
    print("Total Words:", total_words)
    print("Unique Words Count:", unique_word_count)
    print("Lexical Variety:", lexical_variety)

# Test
sentences = [
    "  Python is amazing!  ",
    "I love coding in Python.",
    "Loops, strings, and lists are powerful in Python.",
    "Python is fun!"
]

process_sentences(sentences)
