def main():
    book_path = "bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    dict_to_list = get_list(chars_dict)
    generate_report(dict_to_list, book_path, num_words)


def get_num_words(text):
    return len(text.split())


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_character_sums(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_list(chars_dict):
    a_list = []
    temp_list = list(zip(chars_dict.keys(), chars_dict.values()))
    for i in temp_list:
        if i[0].isalpha() == True:
            a_list.append(i)
    a_list.sort()
    return a_list

def generate_report(dict_to_list, book_path, num_words):
    print(f'--- Begin report of {book_path} ---')
    print(f'{num_words} words found in the document\n')

    for i in dict_to_list:
        print(f'The "{i[0]}" character was found {i[1]} times')
    print('--- End report ---')


main()