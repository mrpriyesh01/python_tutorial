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
