#Prompts user to input one dimension of square, then draws said square.
squareInput = int(input("How big is one side of the square? "))
square = "*" * squareInput
userList = range(squareInput)

for numbers in userList:
    print(square)