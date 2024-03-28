'''
Возьмите задачу о банкомате из семинара 2.
Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления
и снятия средств в список.
'''


def print_balance(balance):
    print(f'Current balance {balance}')


def deposit(balance, count, transaction_history):

    summ_50 = int(input('Enter an amount that is a multiple of 50: '))
    if summ_50 % 50 != 0:
        print('an amount that is a multiple of 50!')
        return balance, count, transaction_history
    balance += summ_50
    count += 1
    if count % 3 == 0:
        bonus = balance * 0.03
        balance += bonus
        transaction_history.append(('Replenishment', summ_50))
        transaction_history.append(('Bonus', bonus))
    else:
        transaction_history.append(('Replenishment', summ_50))
    return balance, count, transaction_history


def withdraw(balance, count, transaction_history):

    summ_50 = int(input('Enter an amount that is a multiple of 50: '))
    if summ_50 % 50 != 0:
        print('an amount that is a multiple of 50!')
        return balance, count, transaction_history
    if summ_50 > balance:
        print('Insufficient funds')
        return balance, count, transaction_history
    a = summ_50 * 0.015
    if a < 30:
        a = 30
    elif a > 600:
        a = 600
    balance -= summ_50 + a
    count += 1
    transaction_history.append(('Cash withdrawal', summ_50))
    transaction_history.append(('Commission', a))
    return balance, count, transaction_history


def view_history(transaction_history):

    print("History: ")
    for transaction in transaction_history:
        print(f"{transaction[0]}: {transaction[1]}")


def program():
    global balance, count
    balance = 0
    count = 0
    transaction_history = []

    while True:
        print_balance(balance)
        total_input = input('Select action: top up, withdraw, history, exit\n')

        if total_input == "top up":
            balance, count, transaction_history = deposit(
                balance, count, transaction_history)
        elif total_input == "withdraw":
            balance, count, transaction_history = withdraw(
                balance, count, transaction_history)
        elif total_input == "history":
            view_history(transaction_history)
        elif total_input == "exit":
            print('Current balance:', balance)
            break
        else:
            print('Wrong Action')


program()