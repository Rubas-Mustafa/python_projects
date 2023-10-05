# a function that takes a list and target parameters
# multiple variables middle start end steps
# recursion or while loop
# increase steps each time a split is done
# condition to track targeted position(index)

# element === target 
def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while(start<=end):
        print("Steps",steps, ":", str(list[start:end+1]))

        steps = steps+1
        middle = (start + end) // 2

        if element == list[middle]:
            return middle
        if element < list[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return -1
my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
target = 4

binary_search(my_list, target)