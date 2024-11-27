def sum_of_triple_products(n, a):
    MOD = 1000000007
    result = 0
    pref = [0] * (n + 1)
    for i in range(1, n + 1):
        pref[i] = pref[i - 1] + a[i - 1]
    # print(pref)
    pref_second = [0] * (n - 1)
    for i in range(1, n - 1):
        pref_second[i] = a[i] * (pref[-1] - pref[i + 1])
    # print(pref_second)
    pref_second_sum = [0] * (len(pref_second) + 1)
    for i in range(1, len(pref_second) + 1):
        pref_second_sum[i] = pref_second_sum[i - 1] + pref_second[i - 1]
    # print(pref_second_sum)
    for i in range(n - 2):
        result += (a[i] * (pref_second_sum[-1] - pref_second_sum[i + 1])) % MOD
    return result % MOD


n = int(input())
a = list(map(int, input().split()))
print(sum_of_triple_products(n, a))
