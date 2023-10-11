#1, write a python  program to calculate the total number of vowels  and count of each individual vowel A,E,I,O,U in 
# the string "Guvi Geeks Network Private Limited" ?


# You can calculate the total number of vowels and count of each individual vowel 
# (A, E, I, O, U) in the given string using Python. Here's a program to do that:

# Input string
input_string = "Guvi Geeks Network Private Limited"

# Convert the input string to lowercase to make the counting case-insensitive
input_string = input_string.lower()

# Initialize counters for each vowel
count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0

# Iterate through each character in the input string
for char in input_string:
    if char == 'a':
        count_a += 1
    elif char == 'e':
        count_e += 1
    elif char == 'i':
        count_i += 1
    elif char == 'o':
        count_o += 1
    elif char == 'u':
        count_u += 1

# Calculate the total number of vowels
total_vowels = count_a + count_e + count_i + count_o + count_u

# Display the results
print("Total number of vowels:", total_vowels)
print("Count of 'A':", count_a)
print("Count of 'E':", count_e)
print("Count of 'I':", count_i)
print("Count of 'O':", count_o)
print("Count of 'U':", count_u)

# When you run this program,
#  it will count the total number of vowels and the count of each individual vowel in the given string and display the results.

#########################################################################################

#2, create a pyramid of number from 1 to 20 using for loop?

# You can create a pyramid of numbers from 1 to 20 using nested for loops in Python. Here's a simple example:


n = 20  # The number of rows in the pyramid

# Outer loop for rows
for i in range(1, n + 1):
    # Print leading spaces
    for j in range(n - i):
        print(" ", end=" ")
    
    # Print increasing numbers
    for k in range(1, i + 1):
        print(k, end=" ")
    
    # Print decreasing numbers
    for l in range(i - 1, 0, -1):
        print(l, end=" ")
    
    # Move to the next line for the next row
    print()

# This code will produce a pyramid of numbers from 1 to 20 with each row containing increasing and 
# decreasing numbers. Adjust the value of n to change the number of rows in the pyramid.

##########################################################################################

#3, write a function that takes a string and returns a new string with all the vowels removed.

# You can create a Python function that removes all the vowels from a given string. 

# Here's a simple example of such a function:


def remove_vowels(input_string):
    # Initialize an empty string to store the result
    result_string = ""
    
    # Define a set of vowels (both uppercase and lowercase)
    vowels = "AEIOUaeiou"
    
    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is not a vowel
        if char not in vowels:
            # If it's not a vowel, add it to the result string
            result_string += char
    
    return result_string

# Test the function
input_string = "Guvi Geeks Network Private Limited"
result = remove_vowels(input_string)
print(result)  # Output will be "Guvi Geeks Network Private Limited"

# the remove_vowels function iterates through each character in the input string and adds it to the result string only if it's not a vowel. 
# The set vowels contains both uppercase and lowercase vowels for comparison. 
# The resulting string without vowels is returned by the function.

 
########################################################################################################

#4, write a function that takes a string and returns  the number of unique characters in it?

# You can create a Python function to count the number of unique characters in a given string. 
# Here's a sample function to do that:

def count_unique_characters(input_string):
    # Use a set to store unique characters
    unique_chars = set()

    # Iterate through each character in the input string
    for char in input_string:
        unique_chars.add(char)

    # Return the count of unique characters
    return len(unique_chars)

# Test the function
input_string = "Guvi Geeks Network Private Limited"
result = count_unique_characters(input_string)
print("Number of unique characters:", result)  # Output will be 10


# we use a set (unique_chars) to keep track of unique characters encountered in the input string.
# By iterating through the string and adding each character to the set, we ensure that only unique characters are stored. 
# Finally, 
# we return the length of the set, which gives us the count of unique characters in the string.


##########################################################################################################################################

#5, write a function that takes a string and returns true if it is a palindrome, False otherwise.

# You can create a Python function to check if a given string is a palindrome or not. 
# Here's a sample function that does this:

def is_palindrome(input_string):
    # Remove spaces and convert the string to lowercase for a case-insensitive check
    cleaned_string = input_string.replace(" ", "").lower()
    
    # Check if the cleaned string is the same as its reverse
    return cleaned_string == cleaned_string[::-1]

# Test the function
input_string = "Guvi Geeks Network Private Limited"
result = is_palindrome(input_string)
print(result)  # Output will be True

# the is_palindrome function first removes spaces and converts the string to lowercase 
# to perform a case-insensitive check. 
# Then, it compares the cleaned string to its reverse using slicing ([::-1]). 
# If the string is the same when reversed, it returns True, indicating that the input is a palindrome; otherwise, 
# it returns False.

##########################################################################################################################################

#6, Write a function that takes two strings and returns the longest common substring between them ?

# You can find the longest common substring between two strings using dynamic programming. Here's a Python function to do that:

def longest_common_substring(str1, str2):
    # Create a table to store the lengths of common substrings
    # Initialize all values to 0
    table = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

    # Variables to keep track of the longest common substring
    max_length = 0
    end_index_str1 = 0

    # Fill in the table
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
                if table[i][j] > max_length:
                    max_length = table[i][j]
                    end_index_str1 = i - 1

    # Extract the longest common substring
    longest_common_sub = str1[end_index_str1 - max_length + 1:end_index_str1 + 1]

    return longest_common_sub

# Example usage:
str1 = "Guvi Geeks Network"
str2 = "Private Limited"
result = longest_common_substring(str1, str2)
print("Longest Common Substring:", result)



# This function initializes a table to store the lengths of common substrings and fills it using dynamic programming. 
# The longest_common_substring function returns the longest common substring found in 
# the given input strings str1 and str2.



######################################################################################################################################



#7, Write a function that takes a string and returns the most frequent character in it ?

# You can create a Python function to find the most frequent character in a string using a dictionary to count 
# the occurrences of each character. 
# Here's a sample function to do that:

def most_frequent_character(input_string):
    # Initialize a dictionary to store character frequencies
    char_frequency = {}

    # Count the frequencies of each character
    for char in input_string:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    # Find the character with the highest frequency
    most_frequent_char = max(char_frequency, key=char_frequency.get)

    return most_frequent_char

# Example usage:
input_str = "Guvi Geeks Network Private Limited"
result = most_frequent_character(input_str)
print("Most frequent character:", result)


# This function iterates through the input string, 
# counts the frequency of each character, and then returns the character with the highest frequency. 
# In the example provided, it would return the most frequent character, 
# which is 'l' with a frequency of 3.

#####################################################################################################################################################


#8, Write a function that takes a string and returns True if it is an anagram of another string, False otherwise ?


# To check if one string is an anagram of another string, you can create a function that compares 
# the sorted versions of both strings. 
# Anagrams have the same characters but in a different order, 
# so sorting the characters will make it easy to compare them. 
# Here's a Python function to do that:



def is_anagram(str1, str2):
    # Remove spaces and convert both strings to lowercase (optional)
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the sorted versions of the strings are the same
    return sorted(str1) == sorted(str2)

# Example usage:
string1 = "Guvi Geeks Network"
string2 = "Private Limited"
result = is_anagram(string1, string2)
print(result)  # True



# This is_anagram function first removes spaces and converts both input strings to lowercase (which is optional, 
# depending on whether you want case-insensitive comparisons). 
# Then, 
# it sorts the characters in both strings and checks if the sorted versions are equal. If they are, 
# the function returns True, 
# indicating that the strings are anagrams of each other; 
# otherwise,
# it returns False.




#########################################################################################################################

#9. Write a function that takes a string and returns the number of words in it ?

# You can write a Python function to count the number of words in a string by splitting 
# the string into words using whitespace as a delimiter and then counting the resulting list's length. 
# Here's a sample function to do that:


def count_words(input_string):
    # Split the input string into words using whitespace as a delimiter
    words = input_string.split()
    
    # Return the number of words in the string
    return len(words)

# Example usage:
input_str = "Guvi Geeks Network Private Limited"
result = count_words(input_str)
print("Number of words:", result)

# In this function, 
# split() is used to break the input string into a list of words based on whitespace (including spaces, tabs, and newlines). 
# The length of this list gives you the number of words in the input string.

#####################################################################################################################################################
