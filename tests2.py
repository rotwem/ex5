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


def read_up_right(wordlist, matrix):
    counts = dict()
    rows = len(matrix)
    cols = len(matrix[0])
    for iter in range(rows + cols):
        search_in = ""
        for i in range(rows):
            for j in range(cols):
                search_in += matrix[i][j]

        search_in = ""
        for j in range(0, i+1):
            search_in += matrix[row][col]
        print(search_in)
        for word in wordlist:
            if word in search_in:
                count = count_word_in_string(word, search_in)
                print(count)
                if word in counts:
                    counts[word] += count
                else:
                    counts[word] = count
    return counts


wordslist = ["apple", "juice", "bottle", "pancake", "OK", "what", "Cat","tal", "bob"]
matrix = [["e", "l", "p", "p", "a"],
          ["p", "g", "e", "o", "k"],
          ["p", "n", "c", "K", "O"],
          ["l", "a", "i", "O", "K"],
          ["j", "u", "i", "c", "e"],
          ["e", "c", "i", "u", "j"]]

print(read_left(wordslist, matrix))
