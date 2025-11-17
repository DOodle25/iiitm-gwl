# 0/1 Knapsack (DP) with item tracking
def knapsack_01_dp(weights, values, capacity):
    n = len(weights)
    dp = [[0]*(capacity+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for w in range(capacity+1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    # Trackback
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected.append(i-1)
            w -= weights[i-1]
    selected.reverse()
    return dp[n][capacity], selected

# Greedy Knapsack (Fractional, not 0/1) with item tracking
def knapsack_fractional_greedy(weights, values, capacity):
    n = len(weights)
    items = sorted([(v/w, w, v, i) for i, (w, v) in enumerate(zip(weights, values))], reverse=True)
    total_value = 0
    selected = []
    for ratio, w, v, idx in items:
        if capacity == 0:
            break
        if w <= capacity:
            total_value += v
            selected.append((idx, 1))
            capacity -= w
        else:
            fraction = capacity / w
            total_value += v * fraction
            selected.append((idx, fraction))
            capacity = 0
    return total_value, selected

# Largest Common Subsequence (DP) with trackback
def lcs(X, Y):
    m, n = len(X), len(Y)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m):
        for j in range(n):
            if X[i] == Y[j]:
                dp[i+1][j+1] = dp[i][j]+1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    # Trackback
    i, j = m, n
    seq = []
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            seq.append(X[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    seq.reverse()
    return dp[m][n], seq

# Longest Common Substring (DP) with trackback
def longest_common_substring(X, Y):
    m, n = len(X), len(Y)
    dp = [[0]*(n+1) for _ in range(m+1)]
    length = 0
    end_pos = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
                if dp[i][j] > length:
                    length = dp[i][j]
                    end_pos = i
            else:
                dp[i][j] = 0
    substring = X[end_pos-length:end_pos]
    return length, substring

# Matrix Chain Multiplication (DP)
def matrix_chain_order(p):
    n = len(p)-1
    dp = [[0]*n for _ in range(n)]
    split = [[0]*n for _ in range(n)]
    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i+l-1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + p[i]*p[k+1]*p[j+1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k
    # Trackback for optimal parenthesization
    def get_order(i, j):
        if i == j:
            return f"A{i+1}"
        else:
            k = split[i][j]
            return f"({get_order(i, k)} x {get_order(k+1, j)})"
    return dp[0][n-1], get_order(0, n-1)

# Example usage:
if __name__ == "__main__":
    # Knapsack 0/1
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5
    max_val, selected = knapsack_01_dp(weights, values, capacity)
    print("0/1 Knapsack DP:", max_val, "Selected items:", selected)

    # Fractional Knapsack
    max_val_frac, selected_frac = knapsack_fractional_greedy(weights, values, capacity)
    print("Fractional Knapsack Greedy:", max_val_frac, "Selected items (index, fraction):", selected_frac)

    # LCS
    X = "AGGTAB"
    Y = "GXTXAYB"
    lcs_len, lcs_seq = lcs(X, Y)
    print("LCS length:", lcs_len, "Sequence:", ''.join(lcs_seq))

    # Longest Common Substring
    lcsstr_len, lcsstr_seq = longest_common_substring(X, Y)
    print("Longest Common Substring length:", lcsstr_len, "Substring:", lcsstr_seq)

    # Matrix Chain Multiplication
    p = [30, 35, 15, 5, 10, 20, 25]
    min_cost, order = matrix_chain_order(p)
    print("Matrix Chain Multiplication min cost:", min_cost, "Order:", order)