def get_word_count(contents):
    return len(contents.split())

def get_letter_counts(contents):
    dic = {}

    for l in contents.lower():
        if l.isalpha() is not True:
            continue

        if l in dic:
            dic[l] += 1
        else:
            dic[l] = 1
    
    return dic.items()

def sort_on(dict):
    return dict['num']

def sort_list_by_value(dict):
    list = []

    for k, v in dict:
        newDict = {
            'char': k,
            'num': v
        }

        list.append(newDict)
    
    list.sort(reverse=True, key=sort_on)
    return list