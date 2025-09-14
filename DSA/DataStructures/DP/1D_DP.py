# 1. Top-Down Approach: memoisation; Time complexity and Space complexity O(n)
# 2. Bottom-Up Approach: Tabulation; Time complexity and Space complexity O(n)
# 3. Bottom-Up with constant space: Applicable when there is Fibonacci sequence; Time complexity O(n) and Space complexity O(1)

# LeetCode 70. Climbing Stairs
# Reference: https://www.youtube.com/watch?v=I-R1XsECJu8

# Top-Down Approach
def LC70TopDown(n):
    memo = {1:1, 2:2}
    def f(n):
        if n in memo:
            return memo[n]
        else:
            memo[n] = f(n-2) + f(n-1)
            return memo[n]
    return f(n)

def LC70BottomUpTabulation(n):
    # Base cases
    if n == 1:
        return 1
    if n == 2:
        return 2

    dp = [0] * n
    dp[0] = 1
    dp[1] = 2

    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n - 1]  

def LC70BottomUpConstantSpace(n):
    # Base cases
    if n == 1:
        return 1
    if n == 2:
        return 2
    # Initially, prev is the steps required for n = 1; cur is the steps required for n =2
    prev, cur = 1, 2  

    for i in range(2, n):
        prev, cur = cur, prev + cur # simultaneous variable assignment
    
    return cur