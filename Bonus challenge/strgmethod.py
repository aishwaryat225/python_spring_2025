import re

def count_vowels_consonants(text):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    vowel_count = sum(1 for char in text if char in vowels)
    consonant_count = sum(1 for char in text if char in consonants)
    print(f"Vowels: {vowel_count}")
    print(f"Consonants: {consonant_count}")

def is_palindrome(word):
    return word == word[::-1]

def remove_spaces(text):
    return text.replace(" ", "")

def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

def capitalize_first_letter(text):
    return text.title()

# Test cases
text = "Python is fun!"
count_vowels_consonants(text)

print(is_palindrome("madam"))  # Expected Output: True
print(is_palindrome("hello"))  # Expected Output: False

text_with_spaces = " Python  is  awesome! "
print(remove_spaces(text_with_spaces))  # Expected Output: "Pythonisawesome!"

sentence = "Artificial Intelligence is transforming the world"
print(longest_word(sentence))  # Expected Output: "Intelligence"

sentence_to_capitalize = "machine learning is the future."
print(capitalize_first_letter(sentence_to_capitalize))  # Expected Output: "Machine Learning Is The Future."