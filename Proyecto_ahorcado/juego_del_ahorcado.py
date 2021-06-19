import os
import random


def read():
    with open('./data.txt','r', encoding='utf-8') as words:
        # print(list(enumerate(words)))
        my_words = {(int(i) + 1):j.replace('\n', '') for i,j in list(enumerate(words))}
        # for i,j in my_words.items():
        #     my_words[i] = j.replace('\n', '')
        print(my_words)


def run():
    read()


if __name__ == '__main__': 
    run()