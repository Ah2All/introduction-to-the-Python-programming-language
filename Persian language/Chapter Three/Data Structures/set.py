my_list = [1, 2, 3, 3, 4, 5, 5]
my_set = set(my_list)
print(my_set)  # Output: {1, 2, 3, 4, 5}


# Union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2)) # Output: {1, 2, 3, 4, 5}

# Intersection of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.intersection(set2)) # Output: {3}

# Difference of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.difference(set2)) # Output: {1, 2}
