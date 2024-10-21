my_dict = {"Kol" : 2001, "Pasha" : 2005}
print(my_dict)
print(my_dict.get("Pasha", "Такого ключа нет"))
print(my_dict.get("Bob", "Такого ключа нет"))
my_dict.update ({"Anna" : 2002, "Denice" : 2003})
print(my_dict["Anna"])
a = my_dict.pop("Kol")
print(a)
print(my_dict)

my_set = {2, 4, 4, 2, 4, 5, 6, 1, 8}
print(my_set)
my_set.add(10)
my_set.add(13)
my_set.remove(13)
print(my_set)
