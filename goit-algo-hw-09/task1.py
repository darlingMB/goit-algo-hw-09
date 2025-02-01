import time


# Функція жадібного алгоритму
def find_coins_greedy(amount, coins):
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= count * coin
    return result

# Функція динамічного програмування
def find_min_coins(amount, coins):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [-1] * (amount + 1)
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin
    
    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin != -1:
            result[coin] = result.get(coin, 0) + 1
            amount -= coin
    
    return result


def main():
    coins = [50, 25, 10, 5, 2, 1]
    amounts = [113, 1000, 5000, 10000]

    for amount in amounts:
        # Жадібний алгоритм
        start_time = time.time()
        greedy_result = find_coins_greedy(amount, coins)
        greedy_time = time.time() - start_time
        print("Жадібний алгоритм:", greedy_result)
        print(f"Час виконання жадібного алгоритму: {greedy_time:.6f} секунд")

        # Динамічне програмування
        start_time = time.time()
        dp_result = find_min_coins(amount, coins)
        dp_time = time.time() - start_time
        print("Динамічне програмування:", dp_result)
        print(f"Час виконання динамічного програмування: {dp_time:.6f} секунд")


if __name__ == "__main__":
    main()
