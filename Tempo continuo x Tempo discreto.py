import numpy as np
import matplotlib.pyplot as plt

# Criando o sinal contínuo
t = np.linspace(0, 2 * np.pi, 1000)
x_t = np.sin(2 * t) * np.exp(-0.3 * t)

# Criando o sinal discreto
n = np.arange(0, 7, 1)  # Somente valores inteiros
x_n = np.sin(2 * n) * np.exp(-0.3 * n)

# Definir limites do eixo y com base nos valores do sinal contínuo e discreto
y_min = min(np.min(x_t), np.min(x_n))
y_max = max(np.max(x_t), np.max(x_n))

# Criando os gráficos
fig, axs = plt.subplots(2, 1, figsize=(8, 6))

# Gráfico do tempo contínuo
axs[0].plot(t, x_t, 'k')
axs[0].axhline(0, color='black', linewidth=0.8)  # Linha horizontal no eixo x
axs[0].axvline(0, color='black', linewidth=0.8)  # Linha vertical no eixo y
axs[0].set_ylim(y_min - 0.1, y_max + 0.1)  # Ajustando o eixo y
axs[0].set_title("Tempo Contínuo")
axs[0].set_xlabel("t")
axs[0].set_ylabel("x(t)")
axs[0].grid(True, linestyle='--', alpha=0.6)

# Gráfico do tempo discreto
axs[1].stem(n, x_n, linefmt='k', markerfmt='ko', basefmt='k')
axs[1].axhline(0, color='black', linewidth=0.8)  # Linha horizontal no eixo x
axs[1].axvline(0, color='black', linewidth=0.8)  # Linha vertical no eixo y
axs[1].set_ylim(y_min - 0.1, y_max + 0.1)  # Ajustando o eixo y
axs[1].set_title("Tempo Discreto")
axs[1].set_xlabel("n")
axs[1].set_ylabel("x[n]")
axs[1].grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()