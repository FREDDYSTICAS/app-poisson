import math
import matplotlib.pyplot as plt
import os

def calcular_poisson(lam, k):
    return (math.exp(-lam) * lam**k) / math.factorial(k)

def generar_grafica(lam):
    x_vals = list(range(0, int(lam)+10))
    y_vals = [calcular_poisson(lam, k) for k in x_vals]

    plt.bar(x_vals, y_vals, color='skyblue')
    plt.title(f'Distribución de Poisson (λ = {lam})')
    plt.xlabel('Número de eventos (k)')
    plt.ylabel('Probabilidad P(k)')
    plt.tight_layout()

    ruta = 'static/poisson.png'
    plt.savefig(ruta)
    plt.close()
    return ruta
