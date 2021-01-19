def get_words():
    with open('words.txt', "r") as words_list:
        words = []
        for line in words_list:
            new_line = line[:len(line) - 1]
            words.append(new_line)
    return words

def congugation(word_1):
    all_words = get_words()
    list_of_valid_subwords = []
    for word in all_words:
        if word_1.find(word)  >= 0:
            list_of_valid_subwords.append(word)
    msg = f"{len(list_of_valid_subwords)}: They are: {list_of_valid_subwords}"
    return msg

print(congugation("awesomeness")) 
