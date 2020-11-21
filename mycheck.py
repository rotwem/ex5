def count_word_in_string(word, search_in):
    """receives a word and a string and returns the number of appearances of the word in the string"""
    # This is a big change
    count = 1
    new_search = search_in[search_in.find(word) + len(word) - 1:]
    while len(word) <= len(new_search):
        if word in new_search:
            count += 1
            new_search = new_search[new_search.find(word) + len(word) - 1:]
        else:
            new_search = ""
    return count


def search_up(wordlist, matrix):
    counts = dict()
    for col in range(len(matrix[0])):
        search_in = ""
        for row in range(len(matrix) - 1, -1, -1):
            search_in += matrix[row][col]
        for word in wordlist:
            if word in search_in:
                count = count_word_in_string(word, search_in)
                if word in counts:
                    counts[word] += count
                else:
                    counts[word] = count
    return counts


def search_down(wordlist, matrix):
    counts = dict()
    for col in range(len(matrix[0])):
        search_in = ""
        for row in range(len(matrix)):
            search_in += matrix[row][col]
        for word in wordlist:
            if word in search_in:
                count = count_word_in_string(word, search_in)
                if word in counts:
                    counts[word] += count
                else:
                    counts[word] = count
    return counts


def search_right(wordlist, matrix):
    counts = dict()
    for row in range(len(matrix)):
        search_in = ""
        for col in range(len(matrix[0])):
            search_in += matrix[row][col]
        for word in wordlist:
            if word in search_in:
                count = count_word_in_string(word, search_in)
                if word in counts:
                    counts[word] += count
                else:
                    counts[word] = count
    return counts


def search_left(wordlist, matrix):
    counts = dict()
    for row in range(len(matrix)):
        search_in = ""
        for col in range(len(matrix[0]) - 1, -1, -1):
            search_in += matrix[row][col]
        for word in wordlist:
            if word in search_in:
                count = count_word_in_string(word, search_in)
                if word in counts:
                    counts[word] += count
                else:
                    counts[word] = count
    return counts


def matrix_to_right_up_left_down_diagonals(matrix):
    new_matrix = matrix[::-1]
    dct = dict()
    for i in range(len(new_matrix) - 1, -len(new_matrix[0]), -1):
        dct[i] = []
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[0])):
            dct[i - j].append(new_matrix[i][j])
    diagonals_list = list(dct.values())
    diagonals_list_of_str = []
    for lst in diagonals_list:
        lst_str = ""
        for letter in lst:
            lst_str += letter
        diagonals_list_of_str.append(lst_str)
    return diagonals_list_of_str


def matrix_to_right_down_left_up_diagonals(matrix):
    dct = dict()
    for i in range(len(matrix) - 1, -len(matrix[0]), -1):
        dct[i] = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            dct[i - j].append(matrix[i][j])
    diagonals_list = list(dct.values())
    diagonals_list_of_str = []
    for lst in diagonals_list:
        lst_str = ""
        for letter in lst:
            lst_str += letter
        diagonals_list_of_str.append(lst_str)
    return diagonals_list_of_str


def search_right_down_diagonals(wordlist, matrix):
    strings_to_search = matrix_to_right_down_left_up_diagonals(matrix)
    counts = dict()
    for search_in in strings_to_search:
        for word in wordlist:
            if word in search_in:
                count = count_word_in_string(word, search_in)
                if word in counts:
                    counts[word] += count
                else:
                    counts[word] = count
    return counts


def search_left_up_diagonal(wordlist, matrix):
    strings_to_search = matrix_to_right_down_left_up_diagonals(matrix)
    right_direction_strings_to_search = []
    for line in strings_to_search:
        right_direction_strings_to_search.append(line[::-1])
    counts = dict()
    for search_in in right_direction_strings_to_search:
        for word in wordlist:
            if word in search_in:
                count = count_word_in_string(word, search_in)
                if word in counts:
                    counts[word] += count
                else:
                    counts[word] = count
    return counts


def search_right_up_diagonals(wordlist, matrix):
    strings_to_search = matrix_to_right_up_left_down_diagonals(matrix)
    counts = dict()
    for search_in in strings_to_search:
        for word in wordlist:
            if word in search_in:
                count = count_word_in_string(word, search_in)
                if word in counts:
                    counts[word] += count
                else:
                    counts[word] = count
    return counts


def search_left_down_diagonals(wordlist, matrix):
    strings_to_search = matrix_to_right_up_left_down_diagonals(matrix)
    right_direction_strings_to_search = []
    for line in strings_to_search:
        right_direction_strings_to_search.append(line[::-1])
    counts = dict()
    for search_in in right_direction_strings_to_search:
        for word in wordlist:
            if word in search_in:
                count = count_word_in_string(word, search_in)
                if word in counts:
                    counts[word] += count
                else:
                    counts[word] = count
    return counts


directions_dict = {"u": search_up, "d": search_down,
                   "r": search_right, "l": search_left,
                   "w": search_right_up_diagonals, "x": search_left_up_diagonal,
                   "y": search_right_down_diagonals, "z": search_left_down_diagonals}

wordslist = ["apple", "juice", "bottle", "pancake", "OK", "what", "Cat", "tal", "bob"]
matrix = [["j", "l", "c", "b", "a"],
          ["u", "c", "a", "o", "K"],
          ["i", "b", "t", "b", "K"],
          ["c", "b", "o", "t", "C"],
          ["e", "o", "a", "o", "j"],
          ["b", "b", "t", "t", "b"]]

print("right up: ", search_right_up_diagonals(wordslist, matrix))
print("right down: ", search_right_down_diagonals(wordslist, matrix))
print("left up: ", search_left_up_diagonal(wordslist, matrix))
print("left down: ", search_left_down_diagonals(wordslist, matrix))
print("up: ", search_up(wordslist, matrix))
print("down: ", search_down(wordslist, matrix))
print("left: ", search_left(wordslist, matrix))
print("right: ", search_right(wordslist, matrix))


def find_words(wordlist, matrix, directions):
    result_dict = dict()
    for direction in directions:
        word_search_dict = directions_dict[direction](wordlist, matrix)
        for word, value in word_search_dict.items():
            if word in result_dict:
                result_dict[word] += value
            else:
                result_dict[word] = value
    tuple_list = [(word, count) for word, count in result_dict.items()]
    return tuple_list


find_words(wordslist, matrix, "udr")
