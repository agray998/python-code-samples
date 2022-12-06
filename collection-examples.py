# Lists: ordered, mutable
my_list = ["apple", "pear", "strawberry", "banana"]
my_list.append("grape")
my_list.insert(2, "blackcurrant")
my_list.extend(["cherry", "plum", "orange"]) # can also use addition operator

fruit_2 = my_list.pop(2)
my_list.remove("pear")
del my_list[4] # not common, usually just use pop or remove

print(my_list[::-1]) # slice is list[start:stop:step]

my_list[2] = "tangerine"

print(fruit_2)
print(my_list)
print(len(my_list))

# list methods
# append: add to end of list
# insert: add at specified index
# extend: append elements from another list
# pop: removes and returns element at index
# remove: removes first instance of specified value
# index: returns index of first occurence of element
# count: return number of occurences of element in list
# sort: sorts list into specified order

# Tuples:
my_tuple = 5, 3, 7 # can use regular parens or tuple() constructor
print(my_tuple[1])
x, y, z = 5, 3, 7
print(x, y, z)

# Dictionaries:
my_dict = {"uk":"london", "france":"paris"} # dict(uk="london", france="paris")
my_dict.update(germany="berlin", italy = "rome")
my_dict["spain"] = "madrid"
city_1 = my_dict.pop("germany")
print(my_dict)
print(my_dict.get("belgium", "not found"))
# print(my_dict["belgium"])
print(my_dict.items())
print(city_1)

# Dict methods
# update: assigns values to keys
# pop: remove key-value pair and return value
# get: get value associated to key, or default if key is not found
# keys: returns a collection of all the keys in the dict
# values: returns a collection of all the values in the dict
# items: returns key-value pairs as tuples

# sets:
# don't preserve order
# don't store duplicates
# cannot contain: lists, dictionaries, sets
my_set = {3, 5, 1, 6, 2, 3, 9, 4}
print(my_set)