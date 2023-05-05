def numbers(first_number, second_number):
    get_first_number = first_number * 3
    get_second_number = second_number * 2
    divide = get_first_number / get_second_number
    get_divided_number = divide
    divide_second_number = get_second_number / 3
    the_last = get_divided_number //  divide_second_number
    if the_last % 2 != 0:
        return the_last

print(numbers(50, 2))










