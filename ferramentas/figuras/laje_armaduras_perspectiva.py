"""Figura: armaduras típicas de uma laje maciça de concreto armado, em perspectiva.

Estilo semelhante a viga-armaduras-perspectiva.png (aula 01, figura 3).
Uso: python laje_armaduras_perspectiva.py ../../source/_static/aulas/historico_props/laje-armaduras-perspectiva.png
"""
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = sys.argv[1]

# Geometria (cm)
lx, ly = 400.0, 500.0            # vãos livres da laje L1
h = 12.0                         # espessura da laje
bw, hv = 20.0, 45.0              # seção das vigas de apoio
l2 = 170.0                       # trecho representado da laje adjacente L2
s = 35.0                         # espaçamento das barras
ln = 110.0                       # extensão da negativa a partir da face do apoio
K = 2.5                          # exagero da escala vertical

C30, S30 = np.cos(np.radians(30)), np.sin(np.radians(30))


def P(x, y, z):
    """Projeção isométrica: x para a direita, y para a esquerda, z para cima."""
    return np.array([(x - y) * C30, (x + y) * S30 * 0.9 + K * z])


def poly(ax, pts, **kw):
    xy = np.array([P(*p) for p in pts])
    ax.plot(xy[:, 0], xy[:, 1], solid_capstyle="round", solid_joinstyle="round", **kw)


def caixa(ax, x0, x1, y0, y1, z0, z1, **kw):
    for z in (z0, z1):
        poly(ax, [(x0, y0, z), (x1, y0, z), (x1, y1, z), (x0, y1, z), (x0, y0, z)], **kw)
    for x, y in ((x0, y0), (x1, y0), (x1, y1), (x0, y1)):
        poly(ax, [(x, y, z0), (x, y, z1)], **kw)


def barra(ax, pts, lw=2.0):
    poly(ax, pts, color="black", lw=lw, zorder=5)


def barra_cinza(ax, pts, z=4):
    poly(ax, pts, color="#3a3a3a", lw=2.6, zorder=z)
    poly(ax, pts, color="#b5b5b5", lw=1.3, zorder=z + 0.1)


fig, ax = plt.subplots(figsize=(12, 8.5))
ax.set_aspect("equal")
ax.axis("off")

concreto = dict(color="#8c8c8c", lw=0.7, zorder=1)
oculto = dict(color="#8c8c8c", lw=0.7, ls=(0, (5, 3)), zorder=1)

y_fim = ly + bw + l2
# Laje (L1 + trecho de L2) e vigas de apoio sob a laje
caixa(ax, -bw, lx + bw, -bw, y_fim, 0, h, **concreto)
caixa(ax, -bw, 0, -bw, y_fim, -hv + h, 0, **oculto)
caixa(ax, lx, lx + bw, -bw, y_fim, -hv + h, 0, **oculto)
caixa(ax, 0, lx, -bw, 0, -hv + h, 0, **oculto)
caixa(ax, 0, lx, ly, ly + bw, -hv + h, 0, **oculto)

# Armadura positiva (malha inferior) da L1
xs = np.arange(20.0, lx, s)
ys = np.arange(20.0, ly, s)
for y in ys:
    barra(ax, [(-bw + 4, y, 2.0), (lx + bw - 4, y, 2.0)])
for x in xs:
    barra(ax, [(x, -bw + 4, 3.0), (x, ly + bw - 4, 3.0)])

# Armadura de distribuição da negativa
yd = [ly - ln + 15, ly - 60, ly - 20, ly + bw + 20, ly + bw + 60, ly + bw + ln - 15]
for y in yd:
    barra_cinza(ax, [(5, y, h - 3.2), (lx - 5, y, h - 3.2)])

# Armadura negativa sobre o apoio interno, com ganchos nas pontas
for x in xs + s / 2:
    if x > lx - 5:
        continue
    y0, y1 = ly - ln, ly + bw + ln
    barra(ax, [(x, y0, 4.0), (x, y0, h - 2.5), (x, y1, h - 2.5), (x, y1, 4.0)], lw=2.4)

# ---------------------------------------------------------------- rótulos
FONT = dict(fontsize=11.5, family="DejaVu Sans", color="black", linespacing=1.25)


def rotulo(texto, xy_texto, alvos, lado="esq"):
    """Texto com sublinhado e linhas de chamada saindo da extremidade do sublinhado."""
    tx, ty = xy_texto
    t = ax.text(tx, ty, texto, ha="left", va="bottom", **FONT)
    fig.canvas.draw()
    bb = t.get_window_extent().transformed(ax.transData.inverted())
    y_lin = bb.y0 - 3
    x_ini, x_fim = bb.x0 - 3, bb.x1 + 8
    ax.plot([x_ini, x_fim], [y_lin, y_lin], color="black", lw=0.7, zorder=6)
    ponto = (x_fim, y_lin) if lado == "dir" else (x_ini, y_lin)
    for alvo in alvos:
        q = P(*alvo)
        ax.plot([ponto[0], q[0]], [ponto[1], q[1]], color="black", lw=0.7, zorder=6)


ax.set_xlim(-860, 560)
ax.set_ylim(-140, 640)

rotulo("ARMADURA NEGATIVA\nSOBRE O APOIO INTERNO", (-850, 560),
       [(xs[1] + s / 2, ly + bw + 60, h - 2.5), (xs[3] + s / 2, ly + bw + 60, h - 2.5)], lado="dir")
rotulo("ARMADURA DE DISTRIBUIÇÃO\nDA NEGATIVA", (-850, 450),
       [(lx * 0.12, yd[3], h - 3.2), (lx * 0.12, yd[4], h - 3.2)], lado="dir")
rotulo("LAJE ADJACENTE\n(CONTINUIDADE)", (-850, 300), [(0, y_fim, h)], lado="dir")
rotulo("ARMADURA POSITIVA\nNA DIREÇÃO DE $\\ell_y$", (-850, 140),
       [(xs[2], ys[3] + s / 2, 3.0), (xs[3], ys[2] + s / 2, 3.0)], lado="dir")
rotulo("ARMADURA POSITIVA\nNA DIREÇÃO DE $\\ell_x$", (330, 50),
       [(xs[-2] + s / 2, ys[2], 2.0), (xs[-3] + s / 2, ys[3], 2.0)], lado="esq")
rotulo("VIGA DE APOIO", (330, -110), [(lx * 0.75, -bw, -hv + h + 10)], lado="esq")
rotulo("VIGA DE APOIO\nINTERNO", (330, 470), [(lx + bw, ly + bw / 2, -hv + h + 10)], lado="esq")

fig.savefig(OUT, dpi=110, bbox_inches="tight", facecolor="white")
