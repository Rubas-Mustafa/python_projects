from collections import Counter

nums = [1, 1, 8, 1, 8, 6, 7, 8 ,8 , 8, 6, 7]
mode = Counter(nums).most_common()[0][0]
print (mode)