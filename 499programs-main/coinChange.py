def coin_change(coins, amount):
    dp = [float('inf') for _ in range(amount + 1)]
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

if __name__ == "__main__":
    coins = list(map(int, input("Enter coin denominations separated by spaces: ").split()))
    amount = int(input("Enter the target amount: "))
    result = coin_change(coins, amount)
    if result == -1:
        print(f"It's not possible to make change for {amount} with the given coins.")
    else:
        print(f"The minimum number of coins required to make {amount} is: {result}")
