# >>> point = (2.0,3.0)
# >>> point[0] = 1
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment
# >>> point_3d = point + (4.0,)
# >>> point_3d
# (2.0, 3.0, 4.0)
# >>> x,y,z = point_3d
# >>> x
# 2.0
# >>> y
# 3.0
# >>> z
# 4.0
# >>> print("My name is: %s %s" % ("First","Last")
# ... )
# My name is: First Last
#Tuple should have a comma seperator
tuplelist = (99.9, 100.1, 1.1)
print(tuplelist) #o/p -> (99.9, 100.1, 1.1)
tuplelist_add1 = tuplelist + (2.7,)
print(tuplelist_add1) #o/p -> (99.9, 100.1, 1.1, 2.7)
#common usage
employee = ('ID1109','William Henry', 34, "Security Specialist")
print(employee[1])