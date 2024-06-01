
def get_hash(element: str) -> int:

    if not element: return None
    elif len(element) == 1: return ord(element)
    return ord(element[0]) * 33 + ord(element[1]) 

class HashTable():

    def __init__(self, size: int=20):
        self.__table = [None] * size

    def __len__(self) -> int: return len(self.__table)

    def write(self): 
        for i, el in enumerate(self.__table): print(i, el)

    def __incr_size(self): self.__table += [None]

    def add(self, key_word: str, value): 
        
        index = get_hash(key_word) % len(self)
        try:

            while self.__table[index]: 
                index += 1

        except IndexError: self.__incr_size()

        self.__table[index] = [key_word, value] 

    def __find_key_index(self, key_word: str) -> int:

        index = get_hash(key_word) % len(self)

        while self.__table[index][0] != key_word: index += 1

        return index

    def get(self, key_word: str) -> str:
        try: return self.__table[self.__find_key_index(key_word)][1]
        except TypeError: return None
    
    def rem(self, key_word: str):
        try: self.__table[self.__find_key_index(key_word)] = None
        except TypeError: print("This writing not in HashTable")

    def upd(self, key_word: str, new_value):
        try: self.__table[self.__find_key_index(key_word)][1] = new_value
        except TypeError: print("This writing not in HashTable")

    



    
    




    






