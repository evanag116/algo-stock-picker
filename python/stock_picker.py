def picker(prices):
    l, r = 0, 1
    max_profit = 0
    answer = []

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            if profit > max_profit:
                max_profit = profit
                answer.append([l, r])
        else:
            l = r
        r += 1

    return answer[-1]


