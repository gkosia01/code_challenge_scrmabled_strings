# code_challenge_scrmabled_strings
The repository contains the solution for code challenge ["scrambled string"](https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edf/0000000000051004) using python.

In Demo_files folder there are Dictionary files that are not valid based on the following rules:
1. Dictionary words cannot be duplicated
2. Word length must be maximum 105
3. Total words length must be maximum 105

The docker file uses the dictionary_valid.txt file which is valid and return the output as requested.


# Quickstart:
1. Clone the repository
2. Start docker desktop
3. Create the image: execute `docker build -t scrambled_strings .` 
4. Run the app: execute `docker run scrambled_strings`


# Algorith:

* For each word in dictionary build the frequency array.
* The frequency array consists of 26 positions, one for each letter (a-z)
* Then for each input string initiate a sliding window of size same as the searching word.
* If the first and last letters of the word and the window word are the same, create the frequency array for window word
* If the two frequency arrays are the same then the word found in the input string


# Documentation

`parse_args(args)`: 
 </br>&nbsp;&nbsp;&nbsp;***args*** is a list of input parameters used to run the script
 </br>&nbsp;&nbsp;&nbsp;Valid parameters are the `--dictionary` which is the dictionary file path and `--input` which is the input file path
 </br>&nbsp;&nbsp;&nbsp;Return: the dictionary_file_path, input_file_path passed as input to the script
 </br></br>
 `is_valid_dictionary(words_list)`: 
 </br>&nbsp;&nbsp;&nbsp;***words_list*** is the content of dictionary file 
 </br>&nbsp;&nbsp;&nbsp;Return: `True` if the dictionary words are valid based on project limitations else `False`
 </br></br>
 `get_frequency_array(word)`:
 </br>&nbsp;&nbsp;&nbsp;***word*** is a word either from dictionary or a word from input string sliding window
 </br>&nbsp;&nbsp;&nbsp;Return: an array of 26 size which is the frequency of each leter in the word 
 </br></br>
 `count_words_in_string(words_properties_dict, input_string)`:
 </br>&nbsp;&nbsp;&nbsp;***words_properties_dict*** is a dictionary that contains all the words of dictionary and its properties
 ```
 {
	'axpaj': {
			   'first_letter': 'a'
			  ,'last_letter': 'j'
			  ,'word_length': 5
			  ,'frequency_array': [2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,0, 1, 0, 0]
			 }
	, 'apxaj': 
			{
			  'first_letter': 'a'
			 ,'last_letter': 'j'
			 ,'word_length': 5
			 ,'frequency_array':[2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,0, 1, 0, 0]
			}
}
```
&nbsp;&nbsp;&nbsp;***input_string*** is a string from the input file
</br>&nbsp;&nbsp;&nbsp;Return: the number of words from dictionary appears in the input string in its original form or scrambled.
 
