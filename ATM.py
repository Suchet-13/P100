class ATM():
    def __init__(self, card_number, pin):
        self.card_number = card_number
        self.pin = pin

    def balance(self):
        print('Your balance is: 90001584')

    def withdrawal(self, amount):
        balanceAmount = 90001584 - amount
        print('You have withdrawn: '+str(amount))
        print('Remaining Balance: '+str(balanceAmount))

def main():
    card_number = input("Enter Card Number: ")
    pin = input("Enter Pin: ")
    user = ATM(card_number, pin)
    print('Choose Activity:')
    print("1: Balance Enquiry 2: Withdrawal")
    activity = int(input('Enter Activity Number: '))
    if (activity == 1):
        user.balance()
    elif(activity == 2):
        amount = int(input("Enter amount to withdraw: "))
        user.withdrawal(amount)
    else:
        print("Enter a valid input")

if __name__ == "__main__":
    main()