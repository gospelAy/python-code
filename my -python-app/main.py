import math
# how to DC variable in PY
print("Hello Gospel")
name, age = "gospel", 20
# age: int = 20
number = [1, 2, 3, 4]
number.clear()
pi = math.pi
is_Boy = True
# if you want to say the method will return a String;
# def hello() -> str:
#     return "hello"

print(pi)
print(name)
print(age)
print(number)
print(type(name))
print(type(number))
print(type(age))
print(type(pi))
print(type(is_Boy))

# This is a string
brand = "Learning programming"
print(brand.upper())
# you can also do something like replace
brand2 = "Programming is easy always believe in your self "
print(brand2.upper().replace('A', 'a'))
print(len(brand2))
print(brand2 == "Programming is easy always believe in your self" )

# another take home on String today
print("easy" in brand2)
print("easy" not in brand2)

comment = """
================
what would you like to do 
1, check balance
2, Airtime
3, Data 
4, Transfer
5, Deposit to another account;
"""
print(comment)

first_Name = "Blessing"
email = """
hello {}
you are welcome
"""
print(email.format(first_Name))


# This is another way of doing it
the_Second_Name = "Glory"
the_Second_Email = f"""
hello {the_Second_Name}
Welcome to python programming
"""
print(the_Second_Email)
print(number)
