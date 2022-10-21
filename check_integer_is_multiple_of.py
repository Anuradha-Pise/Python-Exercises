# Python program to check whether the given integer is a multiple of 5

num = int(input("Enter an integer :"))
digit = int(input("Enter the digit you want to check for:"))

if num%digit==0:
    print("The number {0} is the multiple of {1}".format(num, digit))
else:
    print("The number {0} is not the multiple of {1}".format(num, digit))