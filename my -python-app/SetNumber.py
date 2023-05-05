# numbersList = [1, 4, 5, 56, 67]
# numbersSet = {1, 1}
# lettersSet = {"A", "A", "B", "C", "C"}
# print(numbersList)
# print(numbersSet)
# print(lettersSet)
# print(len(lettersSet))
# numbersList.sort()
# print(numbersList)

# this are the list methods
number = [1, 3, 4, 5, 543, 54]
# number.pop()
# # number.clear()
# number.sort()
# number.reverse()
# number.remove(1)
# number.append(4000)
# number.append(34445)
# number.clear()
# print(len(number))
# print(5 in number)
# print(563 not in number)

# delete items from list
# number.remove(5) remove an element from the list which is 5
# number.pop() the method pop remove the last element in the list
# print(type(number))
# del number[0] this del method delete the value at index 0
# del number[0:3] this del method delete the number form index 0 to index 3
print(number)
numberListSet = {1, 23, 4, 4, 1, 1, 2, 2, 3, 3, 4, 4}
# The different between List and set is LIST accept duplicate value/ But SET do not accept duplicate value
# numberListSet = {1, 23, 4, 4, 1, 1, 2, 2, 3, 3, 4, 4} This is a set
# number = [4, 4, 5, 5, 8, 8, 4, 4, 4, 4, 4, ] This is a list
print(numberListSet)

# this is union in python
# numberSetA = {"A", "B", "C", "D", "E"}
# numberSetB = {"F", "G", "H", "I", "J"}
# union = numberSetA | numberSetB
# print(union)

# if any set has the same letter that is called intersect
# and also the difference that the first and second set has different letter that is the different
numberSetA = {"A", "B", "C", "D", "E", "F"}
numberSetB = {"F", "G", "H", "I", "J", "E"}
union = numberSetA | numberSetB
intersection = numberSetA & numberSetB
different = numberSetA - numberSetB
print(f"union = {union}")
print(f"intersection = {intersection}")
print(f"The different is {different}")

# this is dictionary in python
person = {
    "name": "gospel",
    "age": 20,
    "address": "Sabo yaba lagos"
}
# print(person["name"])
# print(person["age"])
# print(person["address"])
# print(person.keys())
# print(person.values())
# print(person.clear())
# so if i want to update age
# print(person.get("age"))
# person["age"] = 100
# print(person)
# for Key in person:
#     print(Key)
#     print(f"key: {Key} value: {person[Key]}")
# or we can actually do this
print(person.items())
for key, value in person.items():
    print(f"key:{key} value: {person[key]}")


