import numpy

list_of_numbers = [1, 2, 3, 4, 5]

for number in list_of_numbers:
    print(number)
    if (number % 2 == 0):
        print("is even.")
    else:
        print("is odd.")
print("All done.")