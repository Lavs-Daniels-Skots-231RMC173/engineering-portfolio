def get_cents():
    cents = int(input("Change owed: "))
    return cents

def calculate_quarters(change):
    return change // 25

def calculate_dimes(change):
    return change // 10

def calculate_nickels(change):
    return change // 5

def calculate_pennies(change):
    return change // 1

def coin_count(change):
    quarters = calculate_quarters(change)
    change -= quarters * 25
    
    dimes = calculate_dimes(change)
    change -= dimes * 10
    
    nickels = calculate_nickels(change)
    change -= nickels * 5
    
    pennies = calculate_pennies(change)
    change -= pennies * 1
    
    return quarters + dimes + nickels + pennies

def main():
    change = get_cents()
    total_coins = coin_count(change)
    print(total_coins)

if __name__ == "__main__":
    main()