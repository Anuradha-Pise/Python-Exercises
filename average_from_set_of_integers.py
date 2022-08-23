# Python program to find out the average of a set of integers

count = int(input("Enter the count of numbers:"))
sum=0
for i in range(count):
    x = int(input("Enter the " + str(i+1) + " integer:"))  #x = int(input("Enter the " + str(i) + " integer:"))
    sum += x

avg = sum/count
print("The average is :", avg)