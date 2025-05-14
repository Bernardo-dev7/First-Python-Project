### ATM project

user_pin=1901
amount=100000
entered_pin=int(input("Enter the pin number: "))
for i in range(4):
    if user_pin==entered_pin:
        print("Access granted....")
        withdraw=int(input("Enter the amount you want to withdraw: "))
        break
    else:
        print("try again....")
        entered_pin=int(input("Enter the pin number again: "))
else:
    print("Retry after 5 mins....")

if user_pin==entered_pin:

    if withdraw>0 and withdraw%100==0 and withdraw<amount:

        while amount>0:
            print("Your amount is being processed...")
            amount=amount-withdraw
            print("collect your amount...")
            break

        receipt=input("Do you want receipt? (Y/N): ")
        if receipt=="y":
            print("collect your receipt...")
        elif receipt=="n":
            print("Thank you..")
        else:
            print("Please enter Y or N")

        balance=input("Do you want to check balance? (Y/N): ")
        if balance=="y":
            print("Your balance is: ",amount)
        elif balance=="n":
            print("Thank you..")
        else:
            print("Please enter Y or N")
    else:
        print("Invalid amount...")