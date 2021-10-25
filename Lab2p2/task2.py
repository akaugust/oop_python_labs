import os
import re


class StatProcessing:
    """
    Class that performs statistical processing of a text file
    """

    def __init__(self, filename):
        if not os.path.exists(filename):
            raise FileNotFoundError("Can`t open the file!")
        self.__content = filename
        self.__chars = 0
        self.__words = 0
        self.__sentences = 0

    def get_info(self):
        with open(self.__content, 'r') as infile:
            self.__content = infile.read()
            self.__chars = len(self.__content)
            self.__words = len(re.findall("\\w+", self.__content))
            self.__sentences = len(re.findall("[\\w\\s]+[.?!]", self.__content))
        infile.close()

    def count_chars(self):
        return self.__chars

    def count_words(self):
        return self.__words

    def count_sentences(self):
        return self.__sentences

    def __str__(self):
        return f"File has {self.count_chars()} characters, {self.count_sentences()} sentences " \
               f"and {self.count_words()} words"


if __name__ == "__main__":

    example = StatProcessing("random.txt")
    example.get_info()
    print(example)
