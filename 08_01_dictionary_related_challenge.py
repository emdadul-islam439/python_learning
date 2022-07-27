dictionary = {'I': 'me', "we": 'us', 'they':'them', 'this':'these'}
print('Enter a word: ', end = ' ')
queryWord = input();

if queryWord in dictionary:
    print(dictionary[queryWord])
else:
    print('No words in the dictionary')
    

