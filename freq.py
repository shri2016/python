""" most frequent element in a list """
a = [1,3, 2,3,4,3,2,3,3,2,2,3,2,4,6,7,8,3,2,4,6]
print(max(set(a), key=a.count))

""" using counter from collections """
from collections import Counter
cnt = Counter(a)
print(cnt.most_common(3))
