def count_word_in_string(word, search_in):
    """receives a word and a string and returns the number of appearances of the word in the string"""
    count = 1
    new_search = search_in[search_in.find(word) + len(word) - 1:]
    while len(word) <= len(new_search):
        if word in new_search:
            count += 1
            new_search = new_search[new_search.find(word) + len(word) - 1:]
            print(new_search)
        else:
            new_search = ""
    return count


result_dict = dict()


def read_up(wordlist, matrix):
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


def read_down(wordlist, matrix):
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


def read_right(wordlist, matrix):
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


def read_left(wordlist, matrix):
    counts = dict()
    for row in range(len(matrix)):
        search_in = ""
        for col in range(len(matrix[0])-1,-1,-1):
            search_in += matrix[row][col]
        for word in wordlist:
            if word in search_in:
                count = count_word_in_string(word, search_in)
                if word in counts:
                    counts[word] += count
                else:
                    counts[word] = count
    return counts


def read_up_right_diagonal(wordlist, matrix):
    pass


def read_up_left_diagonal(wordlist, matrix):
    pass


def read_down_right_diagonal(wordlist, matrix):
    pass


def read_down_left_diagonal(wordlist, matrix):
    pass


directions_dict = {"u": read_up, "d": read_down,
                   "r": read_right, "l": read_left,
                   "w": read_up_right_diagonal, "x": read_up_left_diagonal,
                   "y": read_down_right_diagonal, "z": read_down_left_diagonal}

directions = "u"
wordlist = ["apple", "juice", "water", "Water"]


def find_words(wordlist, matrix, directions):
    result = dict()  # should be a list of tuples (word, num of appearances in matrix)
    for direction in directions:
        directions_dict[direction](wordlist, matrix, result)
