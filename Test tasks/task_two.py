# 2. Задан массив из чисел a1... aN, требуется найти границы его строго монотонного подотрезка максимальной длины.
# Если их несколько, вывести границы любого.
# Примеры:
# 1) ввод: -3, 2, 3, 4, 5, 6, 7, 7, 8
# вывод: 0, 6
# 2) ввод: -1, -1, -1, -1, -1, -1, -1, -1, -1
# вывод: 0, 0 (или другой индекс: i, i)


def solve(numbers):
    n = len(numbers)
    answer_inc = [0] * n
    answer_decr = [0] * n
    for i in range(1, n):
        if numbers[i] > numbers[i - 1]:
            answer_inc[i] = answer_inc[i - 1] + 1
        if numbers[i] < numbers[i - 1]:
            answer_decr[i] = answer_decr[i - 1] + 1
    if max(answer_inc) > max(answer_decr):
        return "".join([str(j) for j in answer_inc])[:answer_inc.index(max(answer_inc)) + 1].rfind("0"), \
               answer_inc.index(max(answer_inc))
    else:
        return "".join([str(j) for j in answer_decr])[:answer_decr.index(max(answer_decr)) + 1].rfind("0"), \
               answer_decr.index(max(answer_decr))


if __name__ == "__main__":
    given_list = list(map(int, input().split(",")))
    ans = solve(given_list)
    print(ans[0], ans[1])