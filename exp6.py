weights = [2, 3, 4]
values = [40, 50, 60]
capacity = 5

n = len(weights)

# Bottom-Up
dp = [[0] * (capacity + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for w in range(1, capacity + 1):
        if weights[i-1] <= w:
            dp[i][w] = max(dp[i-1][w],values[i-1] + dp[i-1][w-weights[i-1]])
        else:
            dp[i][w] = dp[i-1][w]

print("Bottom-Up:", dp[n][capacity])


# Top-Down
memo = [[-1] * (capacity + 1) for _ in range(n + 1)]

def knapsack(i, w):
    if i == 0 or w == 0:
        return 0

    if memo[i][w] != -1:
        return memo[i][w]

    if weights[i-1] <= w:
        memo[i][w] = max(
            knapsack(i-1, w),
            values[i-1] + knapsack(i-1, w-weights[i-1])
        )
    else:
        memo[i][w] = knapsack(i-1, w)

    return memo[i][w]

print("Top-Down:", knapsack(n, capacity))