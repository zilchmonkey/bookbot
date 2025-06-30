def word_count(path):
    with open(path) as f:
        content = f.read()
 
    words = content.split()
    number = 0
    for word in words:
        number += 1
    
    return number


def text_count(path):
    dict = {}
    with open(path) as f:
        content = f.read()

    for character in content:
        updated_character = character.lower()
        if updated_character in dict:
            dict[updated_character] += 1
        else:
            dict[updated_character] = 1

    return dict

def sort_on(items):
    return items["num"]

def sorted_report(path):
    total = word_count(path)
    total_char = text_count(path)
    total_array = []
    for char in total_char:
        if char.isalpha():
            total_array.append({"char": char, "num": total_char[char]})

    total_array.sort(reverse=True, key=sort_on)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {total} total words")
    print("--------- Character Count -------")

    for alpha in total_array:
        print(f"{alpha['char']}: {alpha['num']}")

