"""Figura: armaduras típicas de um pilar de concreto armado, em perspectiva.

Estilo semelhante a viga-armaduras-perspectiva.png (aula 01, figura 3).
Uso: python pilar_armaduras_perspectiva.py ../../source/_static/aulas/historico_props/pilar-armaduras-perspectiva.png
"""
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = sys.argv[1]

# Geometria (cm)
b, h, H = 30.0, 60.0, 300.0      # seção b x h e altura do lance
c = 4.0                          # posição do eixo das barras a partir da face
z_bloco = -70.0                  # fundo do bloco de fundação
esp = 75.0                       # comprimento da espera acima do lance
s = 20.0                         # espaçamento dos estribos

C30, S30 = np.cos(np.radians(30)), np.sin(np.radians(30))


def P(x, y, z):
    """Projeção isométrica: x para a direita, y para a esquerda, z para cima."""
    return np.array([(x - y) * C30, (x + y) * S30 * 0.9 + z])


def poly(ax, pts, **kw):
    xy = np.array([P(*p) for p in pts])
    ax.plot(xy[:, 0], xy[:, 1], solid_capstyle="round", solid_joinstyle="round", **kw)


def caixa(ax, x0, x1, y0, y1, z0, z1, **kw):
    for z in (z0, z1):
        poly(ax, [(x0, y0, z), (x1, y0, z), (x1, y1, z), (x0, y1, z), (x0, y0, z)], **kw)
    for x, y in ((x0, y0), (x1, y0), (x1, y1), (x0, y1)):
        poly(ax, [(x, y, z0), (x, y, z1)], **kw)


def barra(ax, pts):
    poly(ax, pts, color="black", lw=2.6, zorder=5)


def estribo_linha(ax, pts, z=4):
    poly(ax, pts, color="#3a3a3a", lw=2.6, zorder=z)
    poly(ax, pts, color="#b5b5b5", lw=1.3, zorder=z + 0.1)


fig, ax = plt.subplots(figsize=(9.2, 10.5))
ax.set_aspect("equal")
ax.axis("off")

concreto = dict(color="#8c8c8c", lw=0.7, zorder=1)
oculto = dict(color="#8c8c8c", lw=0.7, ls=(0, (5, 3)), zorder=1)

# Bloco de fundação (tracejado) e pilar (contorno fino)
caixa(ax, -35, b + 35, -30, h + 30, z_bloco, 0, **oculto)
caixa(ax, 0, b, 0, h, 0, H, **concreto)
# Viga do pavimento superior chegando ao pilar (tracejado)
caixa(ax, 0, b, -90, 0, H - 50, H, **oculto)

# Estribos e grampos
xs0, xs1 = c - 1.0, b - c + 1.0
ys0, ys1 = c - 1.0, h - c + 1.0
zs = np.arange(8.0, H - 4.0, s)
for z in zs:
    estribo_linha(ax, [(xs0, ys0, z), (xs1, ys0, z), (xs1, ys1, z), (xs0, ys1, z), (xs0, ys0, z),
                       (xs0 + 4, ys0 + 4, z)])
    estribo_linha(ax, [(xs0 - 1.5, h / 2 - 3, z), (xs0, h / 2, z), (xs1, h / 2, z), (xs1 + 1.5, h / 2 + 3, z)],
                  z=4.5)

# Barras longitudinais: 4 de canto + 2 intermediárias na face maior
posicoes = [(c, c), (b - c, c), (b - c, h - c), (c, h - c), (c, h / 2), (b - c, h / 2)]
for x, y in posicoes:
    # dobra horizontal no fundo do bloco, apontando para fora
    dx = -18 if x < b / 2 else 18
    barra(ax, [(x + dx, y, z_bloco + 10), (x, y, z_bloco + 10), (x, y, H + esp)])

# ---------------------------------------------------------------- rótulos
FONT = dict(fontsize=11.5, family="DejaVu Sans", color="black", linespacing=1.25)


def rotulo(texto, xy_texto, alvos, lado="esq"):
    """Texto com sublinhado e linhas de chamada saindo da extremidade do sublinhado."""
    tx, ty = xy_texto
    ha = "left"
    t = ax.text(tx, ty, texto, ha=ha, va="bottom", **FONT)
    fig.canvas.draw()
    bb = t.get_window_extent().transformed(ax.transData.inverted())
    y_lin = bb.y0 - 2
    x_ini, x_fim = bb.x0 - 2, bb.x1 + 6
    ax.plot([x_ini, x_fim], [y_lin, y_lin], color="black", lw=0.7, zorder=6)
    ponto = (x_fim, y_lin) if lado == "dir" else (x_ini, y_lin)
    for alvo in alvos:
        q = P(*alvo)
        ax.plot([ponto[0], q[0]], [ponto[1], q[1]], color="black", lw=0.7, zorder=6)


# limites da figura (para posicionar textos)
ax.set_xlim(-260, 250)
ax.set_ylim(-110, 440)

rotulo("ESPERA PARA O LANCE\nSUPERIOR (EMENDA\nPOR TRASPASSE)", (95, 395),
       [(b - c, c, H + 45), (b - c, h / 2, H + 50)], lado="esq")
rotulo("VIGA DO\nPAVIMENTO", (110, 290), [(b, -65, H - 25)], lado="esq")
rotulo("ARMADURA\nLONGITUDINAL", (95, 215), [(b - c, c, 170), (b - c, h / 2, 185)], lado="esq")
rotulo("ESTRIBO\n(ARMADURA\nTRANSVERSAL)", (95, 70),
       [(xs1, ys0 + 6, z) for z in zs[2:6]], lado="esq")
rotulo("GRAMPO\nSUPLEMENTAR", (-250, 150),
       [(xs0 + 8, h / 2, z) for z in zs[5:8]], lado="dir")
rotulo("BLOCO DE\nFUNDAÇÃO", (-250, -15), [(-35, -30, z_bloco + 30)], lado="dir")
rotulo("ARRANQUE COM\nDOBRA NO BLOCO", (95, -75), [(b - c + 18, c, z_bloco + 10), (b - c + 18, h / 2, z_bloco + 10)],
       lado="esq")

fig.savefig(OUT, dpi=110, bbox_inches="tight", facecolor="white")
