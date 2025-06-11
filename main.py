from stats import get_word_count
from stats import get_letter_counts
from stats import sort_list_by_value
import sys


def get_book_text(filePath):
    with open(filePath) as f:
        file_contents = f.read()
        return file_contents

def validate_args():
    if len(sys.argv) == 2:
        return True
    else:
        return False

def main():
    is_valid = validate_args()

    if is_valid is False:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
        return
    

    book_text = get_book_text(sys.argv[1])
    word_count = get_word_count(book_text)
    
    print(f'{word_count} words found in the document')
    for k, v in get_letter_counts(book_text):
        print(f'\'{k}\': {v}')

    sortedList = sort_list_by_value(get_letter_counts(book_text))
    
    print(f'''============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------''')
    for dict in sortedList:
        print(f'{dict['char']}: {dict['num']}')


if __name__ == '__main__':
    main()