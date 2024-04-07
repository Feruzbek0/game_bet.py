import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bets):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += symbol_value[symbol] * bets
            winning_lines.append(line + 1)
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbols_count in symbols.items():
        for _ in range(symbols_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for rows in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[rows], end="  |  ")
            else:
                print(column[rows], end="")
        print()


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("The amount should be more than 0. ")
        else:
            print("Please enter a number.")

    return amount


def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines for bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid amount of lines.")
        else:
            print("Please enter a number.")



def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"The amount should be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount


def spin(balance, lines, bet):
    total_bet = lines * bet
    if total_bet > balance:
        print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        return 0
    elif total_bet <= balance:
        print(f"You're betting ${bet} on {lines} lines. Total bet is ${total_bet}.")
        slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
        print_slot_machine(slots)
        winnings, winning_lines = check_winnings(slots, lines, bet)
        print(f"You won ${winnings}.")
        if winning_lines:
            print(f"You won on lines: ", *winning_lines)
        return winnings - total_bet


def main(balance):
    while True:
        print(f"Current balance is ${balance}")
        # answer = input("Press enter to play or 'q' to quit: ")
        # if answer.lower() == "q":
        #     break
        lines = get_number_of_lines()
        bet = get_bet()
        balance += spin(balance, lines, bet)
    # print(f"You l eft with ${balance}")


if __name__ == "__main__":
    initial_balance = deposit()
    main(initial_balance)
