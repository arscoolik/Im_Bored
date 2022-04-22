def countingSort(word): #counting sort, works for O(m), where m is the size pf the word
    alph = [0] * 26
    for i in word:
        alph[ord(i) - 97] += 1
    ans = ''
    for i in range(26):
        if alph[i]:
            for j in range(alph[i]):
                ans += chr(97 + i)
    return ans


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
an = {}
for i in strs:
    tmp = countingSort(i)
    if tmp in an:
        an[tmp].append(i)
    else:
        an[tmp] = [i]
answer = []
for i in an:
    answer.append(an[i])
print(answer)

#final complexity is O(n*m), where n is the list size and m is the words length
