#ATTEMPT 1
print('input first word')
str1 = input()
print('input second word')
str2 = input()
try:
    str1.index(str2)
except ValueError:
    print('False')
else:
    print('True')

    #correct way
    def near(string_parent, string_child):
    list_parent = list(string_parent)
    list_child = list(string_child)
    for index in range(len(list_parent)):
        item_to_remove = list_parent[index]
        del list_parent[index]
        if list_parent == list_child:
            return True
        list_parent.insert(index, item_to_remove)
    return False

word1 = input('Enter first word: ')
word2 = input('enter second word: ')

print(near(word1, word2))
