# read the text
def get_book_text(path):
    with open(path) as f:
        return f.read()

# count the words
def process_text(text):
    word_count = len(text.split())
    return word_count

# make a dictionary counting the characters
def count_characters(text):
    character_count = {}
    for char in text.lower():
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

# Function to use as the key for sorting
def sort_on(item):
    return item["count"]

# Prepare and sort the character data
def prepare_and_sort_character_data(character_count):
    char_data = [{"char": char, "count": count} for char, count in character_count.items()]
    return sorted(char_data, key=sort_on, reverse=True)

# Generates the report
def generate_report(sorted_characters, word_count, path):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")
    for item in sorted_characters:
        if item['char'].isalpha():
            print(f"The '{item['char']}' character was found {item['count']} times")
    print("---End report---")

# The main function
def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    word_count = process_text(text)
    character_count = count_characters(text)
    sorted_characters = prepare_and_sort_character_data(character_count)  # Sort the characters
    generate_report(sorted_characters, word_count, path_to_file)
    print(f"The book contains {word_count} words.")

main()
