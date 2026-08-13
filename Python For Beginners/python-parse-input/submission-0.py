from typing import List

def read_integers() -> List[int]:

    integer = input().split(",")
    new_list= []

    for num in integer:
        new_list.append(int(num)) 
    
    return new_list



# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
