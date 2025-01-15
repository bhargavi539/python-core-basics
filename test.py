from selenium.webdriver.support.expected_conditions import element_selection_state_to_be

print(16 and 18)

#Terinary operators

# a = int(input("Enter a"))
# b = int(input("Enter b"))
# print(10/5)
# print(10%5)
# print("Even") if a%b == 0 else print("Odd")

# marks = int(input("enter marks"))
# if marks == 100:
#     print("Grade A+")
# elif 80 < marks < 100:
#     print("Grade A")
# elif 60 < marks < 80:
#     print("Grade B")
# else:
#     print("Failed")

set1 = [10,20,10,30,40,50,60,30.70,80]
i= 0
for s in set1:
    i = i+1
    print("The value at index {} is {}".format(i,s))

for i in range(10):
    print("*#%",i)

print("Multiplication logic using for loop")

# num = int(input("Enter a Number"))
# for i in range(1,11):
#     print(num,"*",i ,"=",num*i)

# text = "This is some random text using ti split into list with the spaces"
# text_list = text.split(" ")
# for t in text_list:
#     print(t)
#

#Find the factorial of a number using while loop
num = int(input("Enter a number to get the factorial"))
fact = num
i = 1
while num > 1:
    num = num -1
    fact = fact * num
print("factorial is {}".format(fact))

































