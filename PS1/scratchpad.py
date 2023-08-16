import collections


def duplicate_count(text):
    x = collections.Counter(text)
    return x


x = "hello"
print(duplicate_count(x))
