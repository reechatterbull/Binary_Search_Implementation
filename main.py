""" THIS IS A CODE FOR A BINARY SEARCH ALGORITHM """

def binary_search(numbers_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    if mid_index >= len(numbers_list) or mid_index < 0:
        return -1

    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
        return mid_index

    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search(numbers_list, number_to_find, left_index, right_index)
    







if __name__ == '__main__':
  num_list = [-1,0,3,5,9,12]
  find = 9
  print(binary_search(num_list,find,0,len(num_list)))
  