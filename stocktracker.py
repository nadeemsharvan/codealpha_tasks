prices = {'AAPL': 180, 'TSLA': 250, 'GOOGL': 140, 'MSFT': 330, 'AMZN': 170}
portfolio = {}
total = 0

print('=== Stock Portfolio Tracker ===')
print('Available Stocks:', ', '.join(prices.keys()))

n = int(input('How many stocks do you want to enter? '))

for i in range(n):
    stock = input('Enter stock name: ').upper()
    qty = int(input('Enter quantity: '))

    if stock in prices:
        portfolio[stock] = qty
    else:
        print('Stock not found! Skipped.')

print('\nYour Portfolio:')
for stock, qty in portfolio.items():
    value = prices[stock] * qty
    total += value
    print(stock, '- Qty:', qty, '| Price:', prices[stock], '| Value:', value)

print('\nTotal Investment Value =', total)

with open('portfolio.txt', 'w') as file:
    file.write('Stock Portfolio\n')
    for stock, qty in portfolio.items():
        file.write(f'{stock}, {qty}, {prices[stock]}, {prices[stock]*qty}\n')
    file.write(f'Total Value = {total}')

print('Saved to portfolio.txt')
