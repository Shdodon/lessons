# В большой текстовой строке подсчитать количество
# встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

import string


text = 'As a Python developer who wants to harness the power of object-oriented programming, \
        you’ll love to learn how to customize your classes using special methods, also known \
        as magic methods or dunder methods. A special method is a method whose name starts and \
        ends with a double underscore. These methods have special meanings for Python. \
        Python automatically calls magic methods as a response to certain operations, \
        such as instantiation, sequence indexing, attribute managing, and much more. \
        Magic methods support core object-oriented features in Python, so learning about \
        them is fundamental for you as a Python programmer. \
        In this tutorial, you’ll: \
        Learn what Python’s special or magic methods are \
        Understand the magic behind magic methods in Python \
        Customize different behaviors of your custom classes with special methods \
        To get the most out of this tutorial, you should be familiar with general Python programming. \
        More importantly, you should know the basics of object-oriented programming and classes in Python.'

tags = string.punctuation + "\n"
print(tags)
for tag in tags:
    text = text.replace(tag, "")
print(text)
list_for_count = text.lower().split()
dict_count_words = {}
for val in set(list_for_count):
    dict_count_words[val] = list_for_count.count(val)
sorted_tuples = sorted(dict_count_words.items(), key = lambda item: item[1], reverse=True)
for i in range(10):
    print (sorted_tuples[i])