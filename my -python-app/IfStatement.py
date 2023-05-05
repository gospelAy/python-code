number = 15

if number < 0:
    print(f"number {number} is positive")
elif number <= 15:
    print(f"number {number} is equal to {number}")
else:
    print("It is Negative")

    # so we can combine logical operator
    number2 = 30
    if not (number2 > 5):
        print("Hello")

        # so you can also have & so how do you go about it?
        first_number = 60
        second_number = 70
        third_number = 80

        # if (first_number < second_number or third_number > second_number):
        #      print("true")