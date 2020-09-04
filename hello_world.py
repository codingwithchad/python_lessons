x = 5
y = 2
myList = [10, 11, 12, 13, 14, 15]

# print(x * y)  # Should print 10
# print(x + y)  # Should print 7
# print(x / y)  # Should print 2.5
# print(x // y)  # Should print 2
# print(x % 2)  # Should print 1
# print("hello world")  # Should print hello world
#
# # should print the numbers 10 through 15
# for number in myList:
#     print(number)
len(myList)
print(myList[3])  # should print 13
try:
    print(myList[6]) # Should throw error
except IndexError as e:
    print(e)



