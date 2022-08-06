def remove_char_from_str(given_str, index):
    new_str = ''
    for i in range(len(given_str)):
        if i != index: new_str += given_str[i]
    return new_str

inputNumberStr = input()
last_char_removed_str = remove_char_from_str(inputNumberStr, len(inputNumberStr)-1)
before_last_char_removed_str = remove_char_from_str(inputNumberStr, len(inputNumberStr)-2)

print(max([int(inputNumberStr), int(last_char_removed_str), int(before_last_char_removed_str)]))