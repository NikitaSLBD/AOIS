from hash_table import HashTable

if __name__ == "__main__":

    table = HashTable()

    table.add('Оптика', "Наука, изучающая свет")
    print(table.get('Оптика'))
    table.upd('Оптика', "Раздел физики, изучающий световые явления")
    print(table.get('Оптика'))
    print(table.get('R'))
    print(len(table))
    table.write()    

