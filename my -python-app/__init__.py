import keyword


def my_first_function():
    name = "gospel"
    age = 30
    return name, age


print(my_first_function())
print(keyword.kwlist)


def number_function(first_number, second_number):
    return first_number + second_number


print(number_function(20, 30))


def my_second_function(number1, number2) -> str:
    return number1 * number2


print(my_second_function(20, 20))
# Assignment operator
number = 0
number += 1
print(number)

second_number = 2
second_number **= 2
print(second_number)

the_last_number = 3
the_last_number = the_last_number + 4
print(the_last_number)

