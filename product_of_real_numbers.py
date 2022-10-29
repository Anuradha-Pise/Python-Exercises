# Python program to find the product of a set of real numbers

product = 1
count = int(input("Enter the count of real numbers:"))

for i in range(count):
    x = float(input("Enter the " + str(i+1) + " real number:"))
    product *= x

print("The product of " + str(count) + " real numbers is:", product)