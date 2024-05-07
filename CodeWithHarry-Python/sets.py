# s={1,2,2,3}
# print(s)


s1={1,2,3,4}
s2={2,4,5,6}
# print(s1.union(s2))
# s1.update(s2)
# print(s1)

# print(s1.intersection(s2))
# s1.intersection_update(s2)
# print(s1)
s1.symmetric_difference_update(s2)
print(s1)