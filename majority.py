import collections

a = ['a','a','a','b','b','c']

count = collections.Counter(a)
print(max(count.keys(),key=count.get))