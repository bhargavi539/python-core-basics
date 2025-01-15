print(type("This is a String"))

a="Welcome to Automation"
print(a)

b='Welcome to Automation'
print(b)

'''

Hey, My name is "Lakshmi"

'''

print('Hey, My name is "Lakshmi"')


e = "Hey" \
    "My name is" \
    "Lakshmi"


print(e)


g = """

Hey

My Name is:

Lakshmi



"""

print(g)


print("Copenhagen is the Denmark's Captial. It is one of the \"*happiest*\" country in the world.")


name="Ananas Banana"

print("Sliced name:",name[1:6:])
print("reversed name",name[::-1])

print(len(name))

abc = "  Hello, World!  "





print(abc.strip())


print(name.lower())


print(name.upper())


b = abc.split(",")
print("Split name",b)
print("split name:",b[1].strip())


ab = "Hi"
cd = " Way2Automation"

print(ab+cd)


print("10"+"10")


a="10"*4
print(a)

print("ba"+"na"*2)


city="New Delhi"

print("Hey, I live in ",city)

# f-Strings
# format()
# %
Age=35
id=10.12

print(f"Hey, I live in {city}, My Age is {Age} and id is {id}")


print("Hey, I live in {}, My Age is {} and id is {}".format(city,Age,id))


print("Hey, I live in %s, My Age is %d and id is %f"%(city,Age,id))