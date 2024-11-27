def max_literature_length(n, c, s):
    rudeness = 0
    right = 0
    max_len = 0
    a_array = [0] * n
    b_array = [0] * n
    if s[0] == "a":
        a_array[0] = 1
    for i in range(1, n):
        if s[i] == "a":
            a_array[i] = a_array[i - 1] + 1
        else:
            a_array[i] = a_array[i - 1]

    if s[0] == "b":
        b_array[0] = 1
    for i in range(1, n):
        if s[i] == "b":
            b_array[i] = b_array[i - 1] + 1
        else:
            b_array[i] = b_array[i - 1]

    # print(a_array)
    # print(b_array)

    for left in range(n):
        while rudeness <= c and right < n:
            max_len = max(max_len, right - left)
            # print(left, right, rudeness, max_len)
            if s[right] == "a":
                pass
            elif s[right] == "b":
                if left == 0:
                    rudeness += (a_array[right])
                else:
                    rudeness += (a_array[right] - a_array[left - 1])

            # print(left, right, rudeness, max_len)
            # max_len = max(max_len, right - left + 1)
            right += 1
        if rudeness <= c:
            max_len = max(max_len, right - left)
        if s[left] == "a":

            if left == 0:
                rudeness -= (b_array[right - 1])
            else:
                rudeness -= (b_array[right - 1] - b_array[left])
        # elif s[left] == "b":
        #     rudeness -= (a_array[right - 1] - a_array[left])


    return max_len

n, c = map(int, input().split())
s = input()
print(max_literature_length(n, c, s))