def nb_words(book):
    return len(book.split())

def get_occurence(book):
    occurences = {}
    for char in book:
        char = char.lower()
        if char not in occurences:
            occurences[char] = 1
        else :
            occurences[char] += 1
    
    return occurences

def sort_on(items):
    return items["num"]

def get_sorted_list(occurences):
    sorted_list = []
    for char in occurences:
        sorted_list.append({"char":char, "num":occurences[char]})
        sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list