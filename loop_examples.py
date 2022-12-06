# while
i = 0

while i <= 10:
    print(i ** 2)
    i += 1

# for
fruits = ["apple", "pear", "strawberry", "banana"]
for index, fruit in enumerate(fruits):
    print("The ", index, "th fruit is", fruit.capitalize())

cap_cities = dict(uk="london", france="paris", italy="rome")
for country, city in cap_cities.items():
    print("The capital of", country, "is:", city)