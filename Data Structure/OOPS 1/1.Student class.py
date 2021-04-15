class student:
    pass


s1 = student()
s2 = student()
s3 = student()
# ---------------------------------
s1.name = "Praveen"
s1.rollnum = 12

s2.name = "Hemant"
s2.rollnum = 13

s3.name = "Manish"

# ----------------------------------------------
# print all attributes
print(s1.__dict__)
print(s2.__dict__)
print(s3.__dict__)

# ----------------------------
# has function
print(hasattr(s1, "name"))
print(hasattr(s1, "rollnum"))
print(hasattr(s3, "rollnum"))

# --------------------------------
# get function

print(getattr(s3, "rollnum"))
# gives error 'obj has no attribute'

# if pass default value as "this can be anything" we wont get error but we get output as ""
print(getattr(s3, "rollnum", "does not exist"))
