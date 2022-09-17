# 1. Расставьте знаки + между некоторыми цифрами числа 12345678910111213...N, чтобы в сумме получилось число M.
# На вход получаем два натуральных числа N и M.
# Вывод: верные примеры в строку.
#
# Примеры:
# 1)Ввод: 5 15
# Вывод: 1+2+3+4+5=15
# 2)Ввод: 4 46
# Вывод: 12+34=46


def decimal_to_binary(n):
    return bin(n).replace("0b","")


def num_to_str(n):
    ans = ''
    for i in range(1, n+1):
        ans += str(i)
    return ans


def solve(n, m):
    num_str = num_to_str(n)
    ln = len(num_str)
    for j in range(pow(2, ln - 1)):
        sm = 0
        cur_num = num_str[0]
        pluses = decimal_to_binary(j).zfill(ln - 1)
        ans = []
        for i in range(ln - 1):
            if pluses[i] == '1':
                sm += int(cur_num)
                ans.append(cur_num)
                cur_num = num_str[i+1]
            else:
                cur_num += num_str[i+1]
            if sm > m:
                break
        sm += int(cur_num)
        ans.append(cur_num)
        if sm == m:
            return "+".join(ans) + "=" + str(m)
    return "There is no possible combination"


if __name__ == "__main__":
    N, M = map(int, input().split())
    solve(N, M)
