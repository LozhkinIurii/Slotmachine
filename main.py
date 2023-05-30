import random

MAX_LINES = 5
MAX_BET = 100
MIN_BET = 1
ROWS = 5
COLS = 3
symbols = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}
symbols_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line +1)
    return winnings, winning_lines


def spin_result(rows, cols, symbols):
    all_symbols = []
    for symbol, symbols_count in symbols.items():
        for _ in range(symbols_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, col in enumerate(columns):
            if i != len(columns)-1:
                print(col[row], end=" | ")
            else:
                print(col[row])


def deposit():
    while True:
        amount = input("Enter your deposit in $: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            else:
                print("Amount must be greater than zero.")
        else:
            print("Plese, enter a valid number.")


def get_number_of_lines():
    while True:
        lines = input("Enter number of lines to bet on (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print("Enter a valid number of lines.")
        else:
            print("Plese, enter a valid number.")


def get_bet():
    while True:
        amount = input("How much would you like to bet on each line ($1 - $100)?: ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount
            else:
                print(f"Bet must be in valid range (${MIN_BET} - ${MAX_BET}).")
        else:
            print("Plese, enter a valid number.")


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough money to bet that amount. Your current balance: ${balance}.")
            answer = input("Do you want to deposit more money (y|n): ")
            if answer == "y":
                balance += deposit()
        else:
            break
    print(f"Your bet is ${bet} on {lines} lines. Total bet: ${total_bet}.")
    print(f"Your balance: ${balance}.")
    slots = spin_result(ROWS, COLS, symbols)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbols_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines: ", *winning_lines)
    return balance + winnings - total_bet


def main():
    balance = deposit()
    while True:
        answer = input("Press enter to spin('q' to quit).")
        if answer == "q":
            break
        balance = spin(balance)
        print(f"You have ${balance} left.")
        if balance == 0:
            balance += deposit()


main()