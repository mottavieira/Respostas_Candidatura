def checkForA(s):
    c = 0
    for ch in s:
        if ch == 'a' or ch == 'A':
            c += 1
    return "A letra a aparece " + str(c) + " vezes na string."

checkForA("aaabAc")