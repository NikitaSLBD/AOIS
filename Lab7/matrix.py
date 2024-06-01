from logicalfunctions import false_constant, repeat_second_arg
import random   

def lists_to_strings(lists: list[list]) -> list[str]:

    strings = []

    for list in lists: 
        string = ''

        for el in list: string += str(el)
        strings.append(string)

    return strings

def strings_to_lists(strings: list[str]) -> list[list]:

    lists = []

    for string in strings: 
        list = []

        for el in string: list.append(int(el))
        lists.append(list)

    return lists

def calculate_diff(word1: list[bool], word2: list[bool]) -> int:

    diff = 0

    for i in range(len(word1)): diff += 1 if word1[i] != word2[i] else 0

    return diff

def adding(bin1: str, bin2: str) -> str:
    result = ""
    carry = False

    max_len = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(max_len)
    bin2 = bin2.zfill(max_len)

    for i in range(max_len - 1, 0, -1):

        if (bin1[i] == "1" and bin2[i] == "1"):
            
            if carry:
                result = "1" + result
            else:
                result = "0" + result
                carry = True
                continue

        elif (bin1[i] == "0" and bin2[i] == "0"):

            if carry:
                result = "1" + result
                carry = False
            else: result = "0" + result 

        else:

            if carry:
                result = "0" + result
            else: result = "1" + result 

    result = result.zfill(31)

    return result

class DiagonalMatrix():

    def __init__(self, values: list[list[bool]]):

        if len(values) != len(values[0]): raise TypeError

        self.matrix = values
        self.len = len(values[0])

    def write(self): 
        for row in self.matrix: print(row)
    
    def read_word(self, index: int) -> list[bool]:

        word = []
        i = index

        while len(word) != self.len:

            if i + 1 > self.len: i = 0

            word.append(self.matrix[i][index])
            i += 1

        return word
    
    def set_word(self, index: int, word: list[bool]):

        if len(word) != self.len: raise TypeError

        i = index

        for chr in word: 

            if i + 1 > self.len: i = 0

            self.matrix[i][index] = chr
            i += 1
    
    def read_address(self, index: int) -> list[bool]:

        address = []

        for i in range(self.len):

            if index + 1 > self.len: index = 0

            address.append(self.matrix[index][i])
            index += 1

        return address
    
    def set_address(self, index: int, address: list[bool]):

         for i in range(self.len):

            if index + 1 > self.len: index = 0

            self.matrix[index][i] = address[i]
            index += 1

    def apply_function(self, index1: int, index2: int, index3: int, func):

        word1 = self.read_word(index1)
        word2 = self.read_word(index2)

        result = list(map(func, word1, word2))
        self.set_word(index3, result)

    def __get_all_words(self) -> list[list[bool]]:

        words = []

        for i in range(self.len): words.append(self.read_word(i))

        return words
    
    def sum_words(self, template: list[bool]=[1, 1, 1]):

        words = list(enumerate(self.__get_all_words()))
        words = list(filter(lambda a: a[1][:3] == template, words))

        parts_a = lists_to_strings(list(map(lambda a: a[1][3:7], words)))
        parts_b = lists_to_strings(list(map(lambda a: a[1][7:11], words)))
        parts_s = strings_to_lists(list(map(lambda a, b: adding('00' + a, '00' + b)[-5:], parts_a, parts_b)))

        for i, word in enumerate(words):
            word[1][-5:] = parts_s[i]
            self.set_word(word[0], word[1])

    def find(self, template: list[bool]) -> list[bool]:

        words = self.__get_all_words()
        diffs = list(map(lambda a: calculate_diff(a, template), words))

        return words[diffs.index(min(diffs))]



