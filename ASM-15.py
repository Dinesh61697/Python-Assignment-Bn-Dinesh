class BalanceError(Exception):
    pass

balance = 10000
withdraw = int(input("Enter a withdraw amount: "))

try:
    if withdraw > balance:
        raise BalanceError("insufficient balance")

    else:
        print("Transaction successful")

except BalanceError as e:
    print("Error:",e)

\
