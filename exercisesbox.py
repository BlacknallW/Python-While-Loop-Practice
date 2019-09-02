#Prompts user for height and width of box, then prints box with given dimensions.
width = int(input("Input your box's width. "))
height = int(input("Input your box's height. "))


def boxBuilder(width,height):
    lineCounter = 0
    while lineCounter < height + 1:
        if lineCounter == 0 or lineCounter == height:
            print("*" * width)
        else:
            print("*" + (" " * (width -2)) + "*")
        lineCounter += 1

boxBuilder(width,height)