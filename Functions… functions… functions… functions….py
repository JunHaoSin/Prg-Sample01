#Functions… functions… functions… functions… | Kong Jun Hao S10275167K

def read_snacks_file(filename):
    snack_names=[]
    snack_prices=[]

    with open(filename, 'r') as file:
        for line in file:
            name, price = line.strip().split(',')
            snack_names.append(name)
            snack_prices.append(float(price))

    return snack_names,snack_prices
        
def get_valid_budget():
    while True:
        budget=float(input('Enter your snack budget: '))
        if budget <= 0:
            print('Your budget is too low! Try asking the office for a raise.')
        else:
            return budget
    
def classify_snack(price):
    if price < 2.0:
        return "Healthy snack"
    elif 2.0 <= price <= 5.0:
        return "Snack of the Gods"
    else:
        return "Luxury snack"

snack_names,snack_prices=read_snacks_file('snack_price.txt')

while True:
    budget= get_valid_budget()
    budget_snacks=[]

    print("Here's what you can buy:")
    for name,price in zip(snack_names,snack_prices):
        if price <= budget:
            label = classify_snack(price)
            print(f'- {name} (${price:.2f}) - {label}')
            budget_snacks.append(f'{name},{price:.2f}')

    with open('snack_list.txt', 'w') as file:
        for line in budget_snacks:
            file.write(line + '\n')

    print("Your snack list has been saved to 'snack_list.txt'. \n")

    with open('snack_list.txt', 'r') as file:
        print(file.read())

    break