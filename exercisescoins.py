#Prompts user to accept or deny coins, updates total coin amount.
coins = 0
print(f"You have {coins} coins")

initialAsk = input("Do you want another? ".lower())

while (initialAsk == "yes"):
    coins += 1
    print(f"You have {coins} coins")
    initialAsk = input("Do you want another? ".lower())
print("Bye")
