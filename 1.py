def checkFib(n):
    fib = [0, 1]
    c = 0
    tam = len(fib)
    while c < n:
        c = fib[tam-1] + fib[tam-2]
        fib.append(c)
        tam = len(fib)
    if n == fib[tam-1]:
        return "Esse número pertence à sequência de fibonacci."
    else:
        return "Esse número não pertence à sequência de fibonacci."
        

a = checkFib(35)