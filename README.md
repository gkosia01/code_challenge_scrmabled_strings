# code_challenge_scrmabled_strings
The repository contains the solution for code challenge ["scrambled string"](https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edf/0000000000051004) using python.

Use the Docker file to build and run the project.

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
