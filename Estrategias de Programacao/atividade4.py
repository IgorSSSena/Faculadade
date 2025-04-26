import math

tempos = {
    "1 segundo": 10**6,
    "1 minuto": 60 * 10**6
}

funcoes = {
    "n log n": lambda n: n * math.log2(n),
    "n^2": lambda n: n ** 2,
    "n^3": lambda n: n ** 3,
    "2^n": lambda n: 2 ** n,
    "n!": lambda n: math.factorial(n)
}

def busca_max_n(func, limite, forca_bruta=False):
    if forca_bruta:
        n = 1
        while True:
            try:
                if func(n) > limite:
                    return n - 1
                n += 1
            except OverflowError:
                return n - 1
    else:
        low = 1
        high = 10**9  
        while low < high:
            mid = (low + high + 1) // 2
            try:
                if func(mid) <= limite:
                    low = mid
                else:
                    high = mid - 1
            except:
                high = mid - 1
        return low

for nome_funcao, func in funcoes.items():
    print(f"\nFunção: {nome_funcao}")
    for nome_tempo, limite in tempos.items():
        brute = nome_funcao in ["2^n", "n!"]
        max_n = busca_max_n(func, limite, forca_bruta=brute)
        print(f"  {nome_tempo}: n = {max_n}")
