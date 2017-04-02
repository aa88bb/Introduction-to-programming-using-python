s = {1,2,4}
s.add(6)
print(s)

s1 = {2}
print(s1.issubset(s))

print(s1.union(s))
print(s1 & s)
print(s ^ s1)