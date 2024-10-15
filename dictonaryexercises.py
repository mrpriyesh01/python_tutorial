Write a function that takes a list of strings and returns a dictionary
where the keys are the unique strings and the values are the counts of their occurrences in the list.

code=
def count_occur(list):
    count = {}
    for words in list:
        if words in count:
            count[words] += 1
        else:
            count[words] = 1
    return count
list = ["apple", "banana", "apple", "orange", "banana", "apple"]
print(count_occur(list))



QUESTION=#create a function inside one function create one list[] and dictonary{}
# and update by 1 list and as well as values of key you take any value

code=
def updated(my_list, my_dict):
    # Update list by multiplying each element by 2
    for i in range(len(my_list)):
        my_list[i] = my_list[i] * 2
    # Update dictionary by adding 1 to each value
    for key in my_dict:
        my_dict[key] = my_dict[key] *my_dict[key] 
    # Return both updated list and dictionary
    return my_list, my_dict
    
# Define the list and dictionary
my_list = [10, 20, 30]
my_dict = {'a': 5, 'b': 10, 'c': 15}

# Call the function and print both updated values
updated_list, updated_dict = updated(my_list, my_dict)
print("Updated List:", updated_list)
print("Updated Dictionary:", updated_dict)
