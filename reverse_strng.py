def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit

if __name__ == "__main__":
    print("Q7 - Buy & Sell Stock Output:", maxProfit([7, 1, 5, 3, 6, 4]))