#################################################################
# FILE : wordsearch.py
# WRITER : Rotem Shadur, rotwem, 318416567
# EXERCISE : intro2cs2 ex5 2020
# DESCRIPTION:
# STUDENTS I DISCUSSED THE EXERCISE WITH: none
# WEB PAGES I USED: none
# NOTES: none
#################################################################

import sys
import os.path


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
    """searches for words from the words list in the matrix's cols with up direction"""
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
    """searches for words from the words list in the matrix's cols with down direction"""
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
    """searches for words from the words list in the matrix's rows with right direction"""
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
    """searches for words from the words list in the matrix's rows with left direction"""
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
    """converts the matrix to a list of strings of the diagonals with directions right up / left down"""
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
    """converts the matrix to a list of strings of the diagonals with directions right down / left up"""
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
    """searches for words from the words list in the matrix's diagonals with right down direction"""
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
    """searches for words from the words list in the matrix's diagonals with left up direction"""
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
    """searches for words from the words list in the matrix's diagonals with right up direction"""
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
    """searches for words from the words list in the matrix's diagonals with left down direction"""
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


def valid_input_len(arguments_list):
    """checks if the input length is correct"""
    if len(arguments_list) != 5:
        print("The number of arguments is invalid. Please enter 4 arguments according to the following: "
              "word_file, matrix_file, output_file, directions")
        return False
    return True


def valid_input_content(word_file, matrix_file):
    """checks if the word_file and the matrix_file that were given exists"""
    if not os.path.isfile(word_file):
        print("The word file you entered does not exists")
        return False
    elif not os.path.isfile(matrix_file):
        print("The matrix file you entered does not exists")
        return False
    else:
        return True


def remove_dup_directions(directions_str):
    """returns a new directions string with no duplications"""
    directions = ""
    for direction in directions_str:
        if direction not in directions:
            directions += direction
    return directions


def valid_directions(directions_str):
    """checks if the directions string is valid and according to the dictionary"""
    is_valid = True
    for direction in directions_str:
        if direction not in directions_dict:
            is_valid = False
    if not is_valid:
        print("The directions you entered are invalid. please use the following directions")
        print(directions_dict)
    return is_valid


def read_wordlist(word_file_name):
    """receives a file name and returns a list of all the words in the file"""
    word_file = open(word_file_name)
    wordlist = []
    for word in word_file:
        wordlist.append(word.replace("\n", ""))
    word_file.close()
    return wordlist


def read_matrix(matrix_file_name):
    """receives a file name and returns a list of lists (matrix) according to its content"""
    matrix_file = open(matrix_file_name)
    matrix = []
    for line in matrix_file:
        line = line.replace("\n", "")
        line = line.replace(",", "")
        mat_line = []
        for lettr in line:
            mat_line.append(lettr)
        matrix.append(mat_line)
    matrix_file.close()
    return matrix


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


def write_output(results, output_file_name):
    output_file = open(output_file_name, "w")
    for word, count in results:
        output_file.write("\n".join(["%s,%s" % (word, count)]) + "\n")
    output_file.close()


def run_wordsearch(arguments_list):
    """main function that calls all the functions"""
    if not valid_input_len(arguments_list):
        return
    else:
        word_file_name = arguments_list[1]
        matrix_file_name = arguments_list[2]
        output_file_name = arguments_list[3]
        directions = remove_dup_directions(arguments_list[4])
    if not valid_input_content(word_file_name, matrix_file_name):
        return
    elif not valid_directions(directions):
        return
    else:
        wordlist = read_wordlist(word_file_name)
        matrix = read_matrix(matrix_file_name)
        results = find_words(wordlist, matrix, directions)
        write_output(results, output_file_name)


if __name__ == "main":
    run_wordsearch(sys.argv)  # this is the arguments, should be a list of strings:
    # [program name, word_file, matrix_file, output_file, directions]
