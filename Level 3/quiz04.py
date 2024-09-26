# Function accepts list of words from a file
#       and letter to search for.
# Returns count of a particular letter in that list.
def count_letter(letter, word_list):
    count = 0
    #Your Answer
        #Your Answer
            count += 1
    return count

word_list = ['aaa'] # word_list is populated from a file. Code not shown.
letter = input("which letter would you like to count")
letter_count = count_letter(letter, word_list)
print("Theke are: ", letter_count, " instances of " + letter)

