print("Amount Due: 50")

amount_due = 50
payment = 0

accepted_payment = [25, 10, 5]

while True:
    coin = int(input("Insert Coin: "))
    if coin in accepted_payment:
        amount_due -= coin
        payment += coin

    if payment >= 50:
        print(f"Change Owed: {payment - 50}")
        break
    else:
        print(f"Amount Due: {amount_due}")
