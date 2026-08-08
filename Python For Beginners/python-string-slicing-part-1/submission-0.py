def get_substring(input_string: str, start: int, end: int) -> str:
    last_index = len(input_string)
    
    if end > last_index:
        return ""
    else:
        sub_string = input_string[start:end]
        return sub_string




# do not modify below this line
print(get_substring("NeetCode", 1, 7))
print(get_substring("NeetCode", 1, 8))
print(get_substring("NeetCode", 1, 9))
print(get_substring("NeetCode", 0, 2))
print(get_substring("NeetCode", 0, 7))
print(get_substring("NeetCode", 4, 8))
