"""
@author Anirudh Sharma

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing
a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any
profit, return 0.

Constraints:

1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4
"""


def maxProfit(prices):
    # Base condition
    if prices is None or len(prices) < 2:
        return 0
    # Minimum value of the stock
    minimum = prices[0]
    # Maximum profit
    maximumProfit = 0
    # Loop for the remaining stocks
    for i in range(1, len(prices)):
        maximumProfit = max(maximumProfit, prices[i] - minimum)
        minimum = min(minimum, prices[i])
    return maximumProfit


if __name__ == "__main__":
    print("Single Day buy")
    print(maxProfit([1,2,9,2,5,7,3]))
    print("Single Day Sell")
    print(maxProfit([0,4,2,5,7,7,8,4,3,5,6,2,2,4,9,6,5,4,2]))
