def add_two_numbers() -> int:
    line = input()

    line_list = line.split(",")
    num_list = []
    result = 0

    for num in line_list:
        num_list.append(int(num))
    
    for i in range(len(num_list)):
        result += num_list[i]
    
    return result

# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
