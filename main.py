def get_word_count(contents):
    return len(contents.split())

def sort_on(dic):
    return dic

def get_letter_counts(contents):
    dic = {}

    for l in contents.lower():
        if l.isalpha() is not True:
            continue

        if l in dic:
            dic[l] += 1
        else:
            dic[l] = 0
    
    return dic.sort(key='')

def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        print(get_word_count(file_contents))
        for k, v in get_letter_counts(file_contents).items():
            print(f'{k}: {v}')


if __name__ == '__main__':
    main()