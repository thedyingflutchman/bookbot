from collections import Counter

def get_word_count(content):
    words= content.split()
    return len(words)

def get_character_count(content):
    character_count_dictionary={}
    for c in content.lower():
        if c not in character_count_dictionary:
            character_count_dictionary[c] = 1
        else:
            character_count_dictionary[c] += 1
    return character_count_dictionary

def sort_on(items):
    return items["count"]

def sort_dictionaries(dictionary):
    dictionary_list=[]
    for character in dictionary:
        if character.isalpha():
            count = dictionary[character]
            character_dictionary= {
                "char": character,
                "count": count
            }
            dictionary_list.append(character_dictionary)
    dictionary_list.sort(reverse=True, key=sort_on)
    return dictionary_list        
