
def __init__(Card, Pin):
    card = Card
    pin = Pin
    accBalance = 0

def CashWithdrawl(amt):
    accBalance-=amt
    print(accBalance)

def BalanceEnquiry(card, pin, accBalance):
    print(card + pin + accBalance)


