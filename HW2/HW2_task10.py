# def find_final_positions(n, a, m, k, x):
#     results = [0] * m
#     for i in range(m):
#         current_index = x[i] - 1
#         current_weight = a[current_index]
#         left_index = current_index
#         same_weight_count = 0
#
#         while left_index > 0:
#             if a[left_index - 1] > current_weight:
#                 results[i] = left_index + 1
#                 break
#             elif a[left_index - 1] == current_weight:
#                 if same_weight_count < k:
#                     same_weight_count += 1
#                     left_index -= 1
#                 else:
#                     results[i] = left_index + 1
#                     break
#             else:
#                 left_index -= 1
#                 current_weight = a[left_index]
#         results[i] = left_index + 1
#
#     return results

def solve(n, a, m, k, x):
    answers = [0] * n
    answers[0] = 1
    current_k = 0
    last_elem_ind = 0
    for i in range(1, n):
        if a[i] > a[i - 1]:
            answers[i] = answers[i - 1]
        elif a[i] < a[i - 1]:
            answers[i] = i + 1
            current_k = 0
            last_elem_ind = i
        else:
            current_k += 1
            if current_k <= k:
                answers[i] = answers[i - 1]
            else:
                while current_k > k:
                    last_elem_ind += 1
                    if a[last_elem_ind] == a[last_elem_ind - 1]:
                        current_k -= 1
                answers[i] = last_elem_ind + 1

    results = [0] * m
    for i in range(m):
        results[i] = answers[x[i] - 1]
    return results



n = int(input())
a = list(map(int, input().split()))
m, k = map(int, input().split())
x = list(map(int, input().split()))

# results = find_final_positions(n, a, m, k, x)

results_2 = solve(n, a, m, k, x)
# print(' '.join(map(str, results)))
print(' '.join(map(str, results_2)))




