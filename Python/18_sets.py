# set = collection which is unordered, unindexed. No duplicate value

utensils = {"fork", "spoon", "knife", "knife", "knife"}
dishes = {"bowl", "plate", "cup"}


utensils.add("napkin")

utensils.remove("fork")

# utensils.clear()

utensils.update(dishes)

dinner_table = utensils.union(dishes)


for x in dinner_table:
    print(x)


print(utensils.difference(dishes))
print(utensils.intersection(dishes))