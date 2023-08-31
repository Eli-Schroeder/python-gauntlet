class DifficultyTwo:

    # Given list "a", get the last item in the list
    # https://www.practicepython.org/solution/2014/05/15/12-list-ends-solutions.html

    def get_last_item(self, a):
        length = len(a)
        return length # todo <- replace this return statement to make it return the last item in the list

    # Given list "a" and element "element", which will be an element inside of "a",
    # return the next element in the list that comes after "element".

    # you may assume that "element" is not the last item in the list.

    def get_next_element(self, a, element):
        # initialize an index variable
        index = -1
        # todo create a 'for' loop that counts from 0 to the length of "a"
        # ^ (refer to cows_and_bulls to recall how to do this)
        # todo check whether the element at the position corresponding to your iterator in "a" is equal to "element"
        # todo if it is equal to "element", then set your index variable to the value of your iterator
        # finally, given that "index" is the value of "element", return the element at "index + 1"
        return a[index + 1]

    # Given a string containing multiple words, return a string in which the word order is
    # reversed.
    # https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html

    # Example:
    # Given "I have a cat", your program must return "cat a have I"

    # Use the string.split() function to separate the string into a list of multiple strings
    # as separated by spaces. The string.split() function will take a delimeter and return a list
    # of strings.

    # Example of string.split()
    # Given
    # a = "cat;dogs;rooster calls"
    # a.split(";")
    # returns
    # ['cats', 'dogs', 'rooster calls']

    # keep in mind the split() function can be used with any delimeter, including spaces.

    # Note: the psuedocode implementation below does not use the string.join function.

    def reverse_word_order(self, sentence):
        output = ""
        # todo use "split" to get a list of words
        # todo iterate over the length of the words list.
        # todo convert your index iterator into the index from the end of the list instead of
        # todo ...the start. You can do this by simply subtracting it from the length of the list.
        # todo get the word corresponding to your new index and add it to output with a space before it.
        return output[1:len(output)]