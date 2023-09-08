def maxprofit(prices):
    profit = 0


    for i in range(1, len(prices)):
        if prices[i]> prices[i-1]:
            profit += prices[i] - prices[i-1]

    return profit

if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    val = maxprofit(prices)
    print(val)