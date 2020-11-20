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

# direction key to the right function
directions_dict = {"u": read_up, "d": read_down,
                   "r": read_right, "l": read_left,
                   "w": read_up_right_diagonal, "x": read_up_left_diagonal,
                   "y": read_down_right_diagonal, "z": read_down_left_diagonal}


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


def read_wordlist(word_file):
    """receives a file name and returns a list of all the words in the file"""
    word_file = open(word_file)
    wordlist = []
    for word in word_file:
        wordlist.append(word.replace("\n", ""))
    return wordlist


def read_matrix(matrix_file):
    """receives a file name and returns a list of lists (matrix) according to its content"""
    matrix_file = open(matrix_file)
    matrix = []
    for line in matrix_file:
        line = line.replace("\n", "")
        line = line.replace(",", "")
        mat_line = []
        for lettr in line:
            mat_line.append(lettr)
        matrix.append(mat_line)
    return matrix


def run_wordsearch(arguments_list):
    """main function that calls all the functions"""
    if not valid_input_len(arguments_list):
        return
    else:
        word_file = arguments_list[1]
        matrix_file = arguments_list[2]
        output_file = arguments_list[3]
        directions = remove_dup_directions(arguments_list[4])
    if not valid_input_content(word_file, matrix_file):
        return
    elif not valid_directions(directions):
        return
    else:
        wordlist = read_wordlist(word_file)
        matrix = read_matrix(matrix_file)


if __name__ == "main":
    run_wordsearch(sys.argv)  # this is the arguments, should be a list of strings:
    # [program name, word_file, matrix_file, output_file, directions]
