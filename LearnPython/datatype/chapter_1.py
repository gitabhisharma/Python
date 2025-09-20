#  We learn a Mutiable or Not Mutiable datatypes

#  Mutable datatypes are those datatypes whose value can be changed after they have been created.
#  Examples of mutable datatypes are lists, dictionaries, and sets.

#  Immutable datatypes are those datatypes whose value cannot be changed after they have been created.
#  Examples of immutable datatypes are strings, tuples, and frozensets.

# For Example in set

# list_name = set[]
# print(f"The set is {list_name}")
# print(f"Set before the adding value is  {id(set)}")
# print(type(list_name))

# # Add the value in a set of name 
# list_name.append("")
# list_name.append("Mohit")
# print(f"The name of set is {list_name}")
# print(f"Set after change value is {id(set)}")


# For examples of mutable datatype in set 
list_name = []
print(f"The set is {list_name}")
print(f"Set before the adding value is  {id(list_name)}")
print(type(list_name))

# Upadate the set of list_name
list_name.append("Mohit")
print(f"The set after update is {list_name}")
print(f"Set after change value is {id(list_name)}")


# Let's create a disctionary in python 

name_list_city = {
    "Rohit": "Begusaria",
    "Mohit": "Mokama"
}

# And print of dictionary
print(f"The disctionary is {name_list_city}")
