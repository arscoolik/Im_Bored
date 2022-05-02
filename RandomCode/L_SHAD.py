s = input()
ans = 0
words = []
ln = 0
number_of_letters = ''
for i in range(len(s)):
    if s[i].isdigit():
        ans = ans * 10 + int(s[i])
    else:
        if ans == 0:
            words.append((s[i], 1))
            if not s[i] in number_of_letters:
                number_of_letters += s[i]
            ln += 1
        else:
            words.append((s[i], ans))
            if not s[i] in number_of_letters:
                number_of_letters += s[i]
            ln += ans
            ans = 0
mn = ln
l = 0
r = 1
ln = 2
if len(words) == 1:
    mn = 1
else:
    number_of_letters = len(number_of_letters)
    dct = {words[0][0]: 1, words[1][0]: 1}
while (l < len(words) - 1):
    if len(dct) <= number_of_letters / 2 and (r != len(words) - 1):
        ln += words[r][1]
        r += 1
        if words[r][0] in dct:
            dct[words[r][0]] += 1
        else:
            dct[words[r][0]] = 1
    elif len(dct) > number_of_letters / 2:
        if ln < mn:
            mn = ln
        if dct[words[l][0]] == 1:
            del dct[words[l][0]]
        else:
            dct[words[l][0]] -= 1
        l += 1
        ln -= words[l][1]
    else:
        l += 1
print(mn)