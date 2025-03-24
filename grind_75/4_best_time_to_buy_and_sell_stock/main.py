# 在逐一確認價格的過程中, 找出第一筆目前最大獲利(目前價格-目前最低價)
# 比較後續獲利(目前價格-目前最低價)是否大於目前最大獲利

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == None or len(prices) == 0: return 0
        
        lowest_buy_in_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            profit = prices[i] - lowest_buy_in_price
            if profit > 0 and profit > max_profit:
                max_profit = profit
            if prices[i] < lowest_buy_in_price:
                lowest_buy_in_price = prices[i]

        return max_profit

def main():
    s = Solution()
    max_profit = s.maxProfit([4,2,3])
    print(max_profit)

if __name__ == '__main__':
    main()