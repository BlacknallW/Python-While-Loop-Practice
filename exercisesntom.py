#Prompt the user for a starting number and ending number, print all numbers inbetween.
start = int(input("Input a number. "))
end = int(input("Input another number, greater than the last "))

while (start < end + 1):
    print(start)
    start+= 1