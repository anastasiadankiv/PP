from collections import defaultdict
import random

def zavdannia1(filename):
a_file = open('text.txt', 'r')
a = a_file.read()
a.splitlines()
a_file.close
myline =random.choice(lines)
print(myline)


def zavdannia2(filename):
    file = open(filename, 'r')
    count = 0
    file_b1 = open('b1.txt', 'w')
    file_b2 = open('b2.txt', 'w')
    for line in file:
        count += 1
        if count % 2 == 0:
            file_b1.write(line.upper())
        else:
            file_b2.write(line.lower())

    file.close()
    file_b1.close()
    file_b2.close()

zavdannia2('a.txt')

def zavdannia3(filename):
    file = open(filename, 'r')
    separators = [',', ' ', '.', '. ', '\n']
    words = []
    for line in file:
        line = line.replace("\n", "")
        line = "".join((char if char.isalpha() else " ") for char in line)
        words = words + line.split()

    count_words = defaultdict(int)
    for word in words:
        count_words[word] += 1

    f = open("c.xml", "w")
    for key in count_words:
        f.write(f'{key}{str(count_words[key])}\n' )
    return count_words

zavdannia3('a.txt')

def zavdannia4(filename):
    file = open(filename, 'r')
    file_ending = open('ending.xml', 'w')
    separators = [',', ' ', '.', '. ', '\n']
    words = []
    line_num = {}
    i=0
    for line in file:
        i += 1
        line = line.replace("\n", "")
        line = "".join((char if char.isalpha() else " ") for char in line)
        words = words + line.split()
        for word in line.split():
            line_num[word] = i

    ending_count = defaultdict(int)
    index={}
    for word in words:
        if len(word)>3:
            ending = word[len(word)-3:]
            index[word] = words.index(word)
            ending_count[ending] += 1
            file_ending.write(f'Слово:{word}, Закінчення: {ending}, Кількість: {ending_count[ending]},Рядок:{line_num[word]}, Індекс слова:{index[word]} \n')

    return ending_count

zavdannia4('a.txt')
