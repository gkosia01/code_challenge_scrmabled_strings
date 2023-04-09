import logging
import sys, getopt
from os.path import exists
import numpy as np


'''
    args:   the list of the arguments passed to the script
    return: If the arguments are correct (-d or --dictionary, -i or --input) return the paths
'''
def parse_args(args):

    dictionary_file_path = None
    input_file_path = None

    try:
        options, arguments = getopt.getopt(args,"d:i:" ,["dictionary=","input="])
    except getopt.GetoptError as err:
        logging.error("Please provide requried arguments, dictionary and input file paths")
        logging.error(err)
        logging.error(f"Parameters passed: {str(args)}")
        quit()

    # if the arguments are correct parse them and return the values to the correct variables
    for opt, val in options:
        if opt in ["-d", "--dictionary"]:
            dictionary_file_path = val
        elif opt in ["-i", "--input"]:
            input_file_path = val

    logging.info(f"Input parameters readed successfully...")
    logging.debug(f"parse_args: dictionary file: {dictionary_file_path}, input file {input_file_path}")
    return dictionary_file_path, input_file_path




''' 
    words_list: the list of words readed from dictionary file
    return: Return True if:
                            There are no duplicates words in dictionary list
                            Each word len is between 2 and 105
                            The sum of len of all words does not exceed 105
            If any of the rules violated return False
'''
def is_valid_dictionary(words_list):

    # find words with not acceptable length
    words_exit_len_limit = [w for w in words_list if len(w)<2 or len(w)>105]
    if(len(words_exit_len_limit) > 0):
        logging.error(f"is_valid_dictionary: Found {str(words_exit_len_limit)} words in dictionary and it is exiting word limit size (105)")
        return False

    # calculate the sum of length of all words
    total_length_of_words = sum(len(i) for i in words_list)
    if(total_length_of_words > 105):
        logging.error(f"is_valid_dictionary: Exiting total number of characters of all words ({total_length_of_words}) in dictionary (limit 105)")
        return False

    # check for duplicates
    # build a set with all words seen until current loop and check if the new word already seen
    words_seen = set()
    duplicate_words = set()
    for w in words_list:
        if(w in words_seen):
            duplicate_words.add(w)
        else:
            words_seen.add(w)
    
    if(len(duplicate_words) > 0):
        logging.error(f"is_valid_dictionary: Dictionary contains duplicate words {str(duplicate_words)}")
        return False

    logging.info(f"Dictionary words passed validation...")
    return True


''' 
    word: a word that contains characters [a-z]
    return: a numpy array of 26 size that contains the frequency of each character
'''
def get_frequency_array(word):
    
    # initiate an array of zeros
    # 26 because the strings can contain [a-z]
    word_freq_array = np.zeros(26, np.int8)

    for letter in word:
        word_freq_array[ord(letter)-97]+=1
    
    logging.debug(f"Word: {word}, frequency_array: {str(word_freq_array)}")
    return word_freq_array


''' 
    words_properties_dict: a dictionary of the words and its properties (first_letter, last_letter, word_length,frequency_array)
    input_string: a string form input file

    reutrn: the number of words appeared in their original or scrabled format in the input string
'''
def count_words_in_string(words_properties_dict, input_string):

    words_found = 0
    for key,word_properties in words_properties_dict.items():
        start_of_window = 0
        end_of_window = word_properties["word_length"]
        length_of_input = len(input_string)

        # loop over the input string and take substrings of length same as searching word
        # if the first and last letters are the same and the frequency arrays are the same means the words is found in the input
        while end_of_window <length_of_input:
            logging.debug(f"Word: {key}, input_substring: {input_string[start_of_window:end_of_window]}")
            
            if word_properties['first_letter'] == input_string[start_of_window] \
               and word_properties['last_letter'] == input_string[end_of_window-1] \
               and np.array_equal(word_properties['frequency_array'],get_frequency_array(input_string[start_of_window:end_of_window])):
                words_found+=1
                break;

            start_of_window+=1
            end_of_window+=1

    return words_found




if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR)

    logging.debug(str(f"Script input {sys.argv}"))
    # parse the input of the script to get the dictionary and input file paths
    dictionary_file_path, input_file_path = parse_args(sys.argv[1:])

    # check if the dictionary and input file paths exists
    if not exists(dictionary_file_path):
        logging.error(f"Dictionary path {dictionary_file_path} does not exists")
        quit()
    elif not exists(input_file_path):
        logging.error(f"Input path {input_file_path} does not exists")
        quit()


    with  open(dictionary_file_path, "r") as dict_file, open(input_file_path, "r") as input_file:
        
        try:
            dict_words = dict_file.read().splitlines()
            input_string_list = input_file.read().splitlines()
        except IOError as io:
            logging.error("Cannot read files")
            logging.error(io)
            quit()
        logging.info(f"Dictionary and input files readed successfully...")


        # validate the dictionary words based on requirments before process the data
        if is_valid_dictionary(dict_words):

            dictionary_words_properties = {}

            for word in dict_words:
                dictionary_words_properties[word] = {
                     "first_letter": word[0]
                    ,"last_letter": word[-1]
                    ,"word_length": len(word)
                    ,"frequency_array": get_frequency_array(word)
                }
            logging.debug(f"Dictionary processing: {str(dictionary_words_properties)}")

            
            for indx, input_line in enumerate(input_string_list):
                logging.info(f"Processing input string {input_line}")
                words_found = count_words_in_string(dictionary_words_properties, input_line)
                
                print(f"Case #{indx+1}: {words_found}")