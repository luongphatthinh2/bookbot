def get_book_text(file_path):
    with open(file_path) as f:
        # f is a file object
        file_contents = f.read()
    return file_contents

def get_num_words(text):
    return len(text.split())

def get_number_of_times_character_appear(text):
    character_appear_dict = {}
    for character in text:
        if character.lower() in character_appear_dict:
            character_appear_dict[character.lower()] += 1
        else:
            character_appear_dict[character.lower()] = 1
    return character_appear_dict

def sort_on(dict):
    return dict["num"]

def get_sorted_list_of_dictionaries(dict):
    list_of_dictionaries = []
    for key, value in dict.items():
        list_of_dictionaries.append({"name": key, "num": value})
    list_of_dictionaries.sort(reverse=True, key=sort_on)    
    return list_of_dictionaries
 

