# 1. Recursive Approach: Good for setting up the recurrence relation, but never pass the test cases (Time Limit Exceed)
# 2. Top-Down Approach: memoisation; Time complexity and Space complexity O(n)
# 3. Bottom-Up Approach: Tabulation; Time complexity and Space complexity O(n)
# 4. Bottom-Up with constant space: Applicable when there is Fibonacci sequence; Time complexity O(n) and Space complexity O(1)

# Top Down: Start from the big problem and break it down into smaller subproblems (from end to start)
# Bottom Up: Start from the smallest subproblem and build up to the big solution (from start to end)

# LeetCode 70. Climbing Stairs
# Reference: https://www.youtube.com/watch?v=I-R1XsECJu8

# Recursive
def LC70Recursive(n):
    def helper(i):
        if i == 1:
            return 1
        if i == 2:
            return 2

        return helper(i - 2) + helper(i - 1)

    return helper(n)


# Top-Down Approach
def LC70TopDown(n):
    memo = {1: 1, 2: 2}

    def f(n):
        if n in memo:
            return memo[n]
        else:
            memo[n] = f(n - 2) + f(n - 1)
            return memo[n]

    return f(n)


# Bottom-Up Approach
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


# Bottom-Up with constant space
def LC70BottomUpConstantSpace(n):
    # Base cases
    if n == 1:
        return 1
    if n == 2:
        return 2
    # Initially, prev is the steps required for n = 1; cur is the steps required for n =2
    prev, cur = 1, 2

    for _ in range(2, n):
        prev, cur = cur, prev + cur  # simultaneous variable assignment

    return cur


# LeetCode 198. House Robber
# Reference: https://youtu.be/kIII1uT6F8Y?si=s4Xyxzy3zTe0xvKh


# Recursive Approach
def LC198Recursive(nums):
    n = len(nums)

    def helper(i):
        if i == 0:
            return nums[0]

        if i == 1:
            return max(nums[0], nums[1])

        return max(nums[i] + helper(i - 2), helper(i - 1))

    return helper(n - 1)


# Top-Down Approach
def LC198TopDown(nums):
    n = len(nums)

    if n == 1:
        return nums[0]

    if n == 2:
        return max(nums[0], nums[1])

    memo = {0: nums[0], 1: max(nums[0], nums[1])}

    def helper(i):
        if i in memo:
            return memo[i]

        memo[i] = max(nums[i] + helper(i - 2), helper(i - 1))
        return memo[i]

    return helper(n - 1)


# Bottom-Up Approach
def LC198BottomUp(nums):
    n = len(nums)

    if n == 1:
        return nums[0]

    if n == 2:
        return max(nums[0], nums[1])

    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

    return dp[n - 1]


# Bottom-Up with constant space
def LC198BottomUpConstantSpace(nums):
    n = len(nums)

    if n == 1:
        return nums[0]

    if n == 2:
        return max(nums[0], nums[1])

    prev = nums[0]  # rob amount two houses before
    curr = max(nums[0], nums[1])  # rob amount one house before

    for i in range(2, n):
        prev, curr = curr, max(nums[i] + prev, curr)

    return curr


# Bottom-Up Approach
def LC91BottomUp(s: str):
    n = len(s)

    # dp array stores how many ways to decode up till at index i
    # dp[0] = null char; dp[1] = first char

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 0 if s[0] == "0" else 1

    # starts from s[1], the second character
    for i in range(2, n + 1):
        if s[i - 1] == "0":
            dp[i] = 0  # 0 ways if it's zero
        else:
            dp[i] += dp[i - 1]  # we look up ways to decode up till previous char

        consec_digits = int(s[i - 2 : i])  # prevchar + currchar

        # check if in range
        if consec_digits >= 10 and consec_digits <= 26:
            dp[i] += dp[i - 2]

    # return number of ways to decode up till the last character of the string
    return dp[n]
