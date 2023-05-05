# first_input = int(input("Enter the amount you want to invest"))
# second_input = input("enter years to view interest")
# i = 0
# while i <= second_input:
#     percentage = (5 / 100) * first_input
#     second_input = second_input + percentage
#     print(f"year {i}, your ROI amount {first_input}:, .2f ")
#     i = i + 1

# number = int(input("Enter a number: "))
#
# for i in range(1, 13):
#     print(f"{number} times {i} = {number * i}")

def the_invest_function():
    amount_to_invest = int(input("Enter the amount: "))
    numbers_of_years = int(input("Enter the number of years: "))
    for year in range(1, numbers_of_years + 1):
        rio = amount_to_invest * 0.05
        amount_to_invest += rio
        print(f"year {year} is {amount_to_invest}")


the_invest_function()
