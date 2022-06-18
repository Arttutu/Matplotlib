import matplotlib.pyplot as plt
import numpy as np

# criar figuras e eixos #
fig, ax = plt.subplots(figsize=(9, 6))
xlab = 'Concentração/g . L^-1'
ylab = 'Densidade/g . ml^-1'
fsize, lsize = '22', '16'

# dados
x = np.array([0, 30, 60, 90, 120, 150, 180, 210])
y = np.array([1.007, 1.014, 1.015, 1.034, 1.044, 1.066, 1.070, 1.078])

# Colocar figura no gráfico
# marker = tipo de ponto, lw = tamanho da linha, # ls = tipo da linha, ms = tamanho dos pontos
ax.plot(x, y, label='dados', marker='o', lw='3', ls='-', ms='10')

# configurar gráfico
plt.xticks([0, 30, 60, 90, 120, 150, 180, 210])
ax.set_xlabel(xlab, fontsize=fsize)  # setado o marcador do x
ax.set_ylabel(ylab, fontsize=fsize)  # setado o marcador do y
plt.title('Densidade x Concentração', fontsize=22)
ax.tick_params(labelsize=lsize, width=2)
ax.grid()
# Nome da figura
nomeFig = 'nome.png'

# Mostrar a figura
plt.show()
