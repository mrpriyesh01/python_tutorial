#Add a list of elements to a set
my_set={1,2,3,4,5}
my_list=[4,5,6,7]
my_set.update(my_list)
print(my_set)

# Return a new set of identical items from two sets
my_set={122,33,44,555,675,342}
my_Set1={231,231,44,55,122,342}
my_set.intersection(my_Set1)
print(my_set)

# Get Only unique items from two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
result=set1.union(set2)
print(result)


#Update the first set with items that don’t exist in the second set
set1={22,33,44,66,88}
set2={11,33,23,88,99}
result=set1.difference(set2)
print(result)


# Remove items from the set at once
set1={"priyesh","prem","shruti","manish"}
set1.remove("priyesh")
print(set1)

# Return a set of elements present in Set A or B, but not both
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}
result = setA.symmetric_difference(setB)
print(result)



my_list = ["shirt", "shirt", "tshirt"]
count_dict = {}
for item in my_list:
    if item in count_dict:
        count_dict[item] += 1  
    else:
        count_dict[item] = 1   
print(count_dict)
my_dict={1:'a',2:'b',3:'a',4:'b'}
   
#Check if two sets have any elements in common. If yes, display the common elements
my_Set1 = {10, 1, 2, 3, 4, 5}
my_set2 = {20, 30, 40, 44, 10}

if my_set2.isdisjoint(my_Set1):  # Checking if the two sets have no common elements
    print("yes")
else:
    print("no")


# Update set1 by adding items from set2, except common items
set1 = {1, 2, 3}
set2 = {2, 3, 4, 5}
for item in set2:
    if item not in set1:
        set1.add(item)

print(set1)

#Remove items from set1 that are not common to both set1 and set2
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.intersection_update(set2)
print(set1)

my_Set1 = {10, 1, 2, 3, 4, 5}
my_set2 = {20, 30, 40, 44, 10}
if my_set2.isdisjoint(my_Set1):  # Checking if the two sets have no common elements
    print("yes")
else:
    print("no")




dict1 = {"name": "priyesh", "age": 46, "marks": 60}
dict2 = {"name": "adi", "age": 55, "marks": 45}
keys_list = list(dict1.keys()) + list(dict2.keys())
print(keys_list)




