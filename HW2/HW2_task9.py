def study_order(n, a, b, p):
    algorithms = [(a[i], b[i], i + 1) for i in range(n)]

    interest_sorted = sorted(algorithms, key=lambda x: (-x[0], -x[1], x[2]))
    usefulness_sorted = sorted(algorithms, key=lambda x: (-x[1], -x[0], x[2]))

    result = []
    studied = set()

    interest_index = 0
    usefulness_index = 0

    for mood in p:
        if mood == 1:
            while usefulness_index < n:
                if usefulness_sorted[usefulness_index][2] not in studied:
                    result.append(usefulness_sorted[usefulness_index][2])
                    studied.add(usefulness_sorted[usefulness_index][2])
                    usefulness_index += 1
                    break
                usefulness_index += 1
        else:
            while interest_index < n:
                if interest_sorted[interest_index][2] not in studied:
                    result.append(interest_sorted[interest_index][2])
                    studied.add(interest_sorted[interest_index][2])
                    interest_index += 1
                    break
                interest_index += 1

    return result


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
p = list(map(int, input().split()))

result = study_order(n, a, b, p)
print(" ".join(map(str, result)))
