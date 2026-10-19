stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150
}

print('\n=== Stock Portfolio Tracker ===')

print('\nAvailable stocks: ',','.join(stock_prices.keys()))



total_investment = 0

portfolio = {}

investment = {}


decision = 'yes'


while decision == 'yes':

    stock_ = input('\nEnter stock symbol: ').upper().strip()
    stp = stock_.strip()
    
    if len(stock_) == 0 :
        print('Invalid input.')

    elif len(stp) == 0:
        print('Please enter a valid input.')

    elif stock_ in stock_prices:

        try:
            quantity_ = int(input('Enter quantity: '))

            if quantity_ < 0:
                print('Quantity cannot be negative.')

            elif quantity_ == 0:
                print('Quantity must be greater than zero.')
                
            else:
                if stock_ in portfolio:
                    portfolio[stock_] += quantity_
                    price_ = stock_prices[stock_]
                    investment_ = quantity_ * price_
                    investment[stock_] += investment_ 
                    total_investment += investment_
    
                    decision = input('\nDo you want to add another stock? (yes/no): ').casefold().strip()

                    if decision not in('yes','no'):
                        print('Enter a valid choice.')
                        while decision not in ('yes','no'):
                           decision = input('\nDo you want to add another stock? (yes/no): ').casefold().strip()

                else:
                    portfolio[stock_] = quantity_
                    price_ = stock_prices[stock_]
            
                    investment_ = quantity_ * price_
            
                    investment[stock_] = investment_ 
            
                    print(f'Added {stock_}:{quantity_} shares x {price_} = {investment_}')
                    total_investment += investment_
            
                    decision = input('\nDo you want to add another stock? (yes/no): ').casefold()  
                    if decision not in('yes','no'):
                        print('Enter a valid choice.')    
                        while decision not in ('yes','no'):
                            decision = input('\nDo you want to add another stock? (yes/no): ').casefold().strip()


        except ValueError:
             print('Please enter a valid number.')
        
    else:
        print('Stock is not available.')

print('\n===== PORTFOLIO SUMMARY =====')

print(f"{'Stock':<12}{'Quantity':<12}{'Price':<12}{'Investment':<12}")
for key in portfolio.keys():
    print(f"{key:<12}{portfolio[key]:<12}{stock_prices[key]:<12}{investment[key]:<12}")

print('-------------------------------')
print('Total Investment: ',total_investment)

print('===============================')

