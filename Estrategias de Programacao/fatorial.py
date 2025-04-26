import time
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Fatorial iterativo
def fatorial_iterativo(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

# Fatorial recursivo
def fatorial_recursivo(n):
    if n <= 1:
        return 1
    return n * fatorial_recursivo(n - 1)

entradas = list(range(40, 501, 40))
tempos_iterativo = []
tempos_recursivo = []

# Medindo o tempo de execução
for n in entradas:
    # Iterativo
    inicio = time.time()
    fatorial_iterativo(n)
    fim = time.time()
    tempos_iterativo.append(fim - inicio)

    # Recursivo
    inicio = time.time()
    try:
        fatorial_recursivo(n)
        fim = time.time()
        tempos_recursivo.append(fim - inicio)
    except RecursionError:
        tempos_recursivo.append(None)  
df = pd.DataFrame({
    "Entrada": entradas,
    "Iterativo": tempos_iterativo,
    "Recursivo": tempos_recursivo
})
df_melted = df.melt(id_vars="Entrada", var_name="Método", value_name="Tempo")

# Gráfico
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_melted, x="Entrada", y="Tempo", hue="Método", marker="o")
plt.title("Tempo de Execução: Fatorial Iterativo vs Recursivo")
plt.xlabel("Número da Entrada")
plt.ylabel("Tempo (s)")
plt.grid(True)
plt.tight_layout()
plt.show()
