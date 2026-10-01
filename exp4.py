# Memoization
def fibonacci_memo(n, dp={}):
    if n <= 1:
        return n

    if n in dp:
        return dp[n]

    dp[n] = fibonacci_memo(n - 1, dp) + fibonacci_memo(n - 2, dp)
    return dp[n]


# Tabulation
def fibonacci_tab(n):
    dp = [0] * (n + 1)

    if n >= 1:
        dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

n = 10

print("Fibonacci using Memoization:", fibonacci_memo(n))
print("Fibonacci using Tabulation:", fibonacci_tab(n))