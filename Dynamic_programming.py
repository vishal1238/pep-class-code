# You are given an integer array prices where prices[i] is the price of a given stock on the i-th day, and an integer k. Find the maximum profit you can achieve. You may complete at most k transactions. (Note: You cannot engage in multiple transactions simultaneously; i.e., you must sell the stock before you buy again).Example:Input: k = 2, prices = [3, 2, 6, 5, 0, 3]Output: 7 (Buy on day 2 [price 2], sell on day 3 [price 6], profit = 4. Then buy on day 5 [price 0], sell on day 6 [price 3], profit = 3. Total profit = 7).


class Solution:
    def maxProfit(self, k, prices):
        if not prices or k == 0:
            return 0

        n = len(prices)

        # If k is large, treat it as unlimited transactions
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit

        buy = [-float('inf')] * (k + 1)
        sell = [0] * (k + 1)

        for price in prices:
            for i in range(1, k + 1):
                buy[i] = max(buy[i], sell[i - 1] - price)
                sell[i] = max(sell[i], buy[i] + price)

        return sell[k]


# Example
k = 2
prices = [3, 2, 6, 5, 0, 3]

obj = Solution()
print(obj.maxProfit(k, prices))