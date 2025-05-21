def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def character_count(text):
    unique_characters = dict()
    with open(text, encoding='utf-8') as f:
        file_contents = f.read()
        split_text = file_contents.split()
        for word in split_text:
            word = word.lower()
            for char in word:
                if char in unique_characters:
                    unique_characters[char] += 1
                else:
                    unique_characters[char] = 1
    return unique_characters

def sort_key(dictionay):
    return dictionay["num"]
    

def sort_dict(dictionary):
    list_of_dictionaries = []

    for character in dictionary:
        count = dictionary[character]
        dict = {"char": character, "num": count}
        list_of_dictionaries.append(dict)
    
    list_of_dictionaries.sort(reverse=True, key=sort_key)
    return list_of_dictionaries
    