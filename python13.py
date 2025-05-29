amount=int(input("Enter the cost prize: "))
hello=int(input("Enter the sell prize: "))
if hello > amount:
    print("You have made a profit of", hello - amount)
elif hello < amount:
    print("You have made a loss of", amount - hello)
else:
    print("You have neither made a profit nor a loss")