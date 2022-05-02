n = int(input())
words = []
fl = True
for i in range(n):
    words.append(input())
m = int(input())
wordle = []
for i in range(m):
    wordle.append(input())
for i in words:
    answer = []
    dct = {}
    for j in words:
        ans = ''
        for k in range(5):
            if i[k] == j[k]:
                ans += 'G'
            elif j[k] in i:
                ans += 'Y'
            else:
                ans += 'W'
        if ans in dct:
            pass
        else:
            dct[ans] = j
    for j in wordle:
        if j in dct:
            answer.append(dct[j])
        else:
            break
    if len(answer) == m:
        fl = False
        print("Yes")
        for i in range(m):
            print(answer[i])
        break
if fl:
    print("No")