from typing import List

def count_unique_words(words: List[str]) -> int:
    my_set = set(words)
    list_with_no_duplicates = list(my_set)
    if list_with_no_duplicates:
        return len(list_with_no_duplicates)
    else:
        return 0

# do not modify code below this line
print(count_unique_words(["hello", "world", "hello", "goodbye"]))
print(count_unique_words(["hello", "world", "i", "am", "world"]))
print(count_unique_words(["hello", "hello", "hello"]))
print(count_unique_words([]))
