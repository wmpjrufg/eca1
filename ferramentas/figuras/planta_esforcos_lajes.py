"""Figuras: planta de esforços nas lajes do pavimento padrão (Entrega 2).

Mostra, para o pavimento-tipo e para a cobertura, os momentos fletores de
cálculo antes (Tabela 18) e depois da compatibilização (Tabela 20 da solução
da Entrega 2): positivos no vão (mx, my) e negativos nas bordas contínuas V2 e
V5 (m'x, m'y), cada um na direção correspondente. Na planta "depois", o valor
anterior aparece em cinza onde a compatibilização o alterou. O eixo x é
vertical e o eixo y é horizontal.

Uso: python planta_esforcos_lajes.py PASTA_DE_SAIDA
Gera planta-esforcos-lajes-{tipo,cobertura}-{antes,depois}.png.
"""
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

SAIDA = Path(sys.argv[1] if len(sys.argv) > 1 else ".")

# ---- Dados: Tabela 20 (kN m/m), momentos de cálculo compatibilizados -------
# (mx, m'x, my, m'y). Os m' são módulos; na planta recebem o sinal negativo.
MOMENTOS = {
    "tipo": {
        "L1": (17.898, 25.263, 14.572, 22.973),
        "L2": (9.038, 17.996, 6.346, 22.973),
        "L3": (7.892, 25.263, 5.762, 14.719),
        "L4": (8.516, 17.996, 5.716, 14.719),
    },
    "cobertura": {
        "L1": (10.564, 21.603, 8.189, 20.322),
        "L2": (11.502, 22.902, 8.188, 20.322),
        "L3": (10.043, 21.603, 7.332, 18.731),
        "L4": (10.837, 22.902, 7.274, 18.731),
    },
}
# Tabela 18: momentos de cálculo ANTES da compatibilização, (mx, m'x, my, m'y).
MOMENTOS_ANTES = {
    "tipo": {
        "L1": (14.740, 31.579, 11.701, 28.717),
        "L2": (8.808, 18.457, 6.346, 16.146),
        "L3": (7.892, 16.585, 5.762, 14.585),
        "L4": (8.516, 17.536, 5.649, 14.853),
    },
    "cobertura": {
        "L1": (10.315, 22.100, 8.189, 20.097),
        "L2": (11.209, 23.488, 8.076, 20.547),
        "L3": (10.043, 21.106, 7.332, 18.560),
        "L4": (10.837, 22.315, 7.189, 18.902),
    },
}
NOME_PAV = {"tipo": "pavimento-tipo", "cobertura": "cobertura"}
FASES = {
    "antes": "antes da compatibilização",
    "depois": "após a compatibilização",
}

# ---- Geometria entre eixos (m), x vertical (para cima) e y horizontal -------
XS = (0.0, 6.000, 12.350)          # eixos dos pilares/vigas verticais (V4, V5, V6)
YS = (0.0, 5.000, 10.250)          # eixos das vigas horizontais (V3, V2, V1)
BW = 0.15                          # largura das vigas
# Vãos efetivos (Tabela 7) e lambda
VAOS = {"L1": (5.172, 5.922), "L2": (5.172, 6.272),
        "L3": (4.922, 5.922), "L4": (4.922, 6.272)}
# Pilares padronizados (Tabela 4): (x, y, h horizontal em m); b = 0,19 m vertical
PILARES = {
    "P1": (XS[0], YS[2], 0.25), "P2": (XS[1], YS[2], 0.45), "P3": (XS[2], YS[2], 0.25),
    "P4": (XS[0], YS[1], 0.45), "P5": (XS[1], YS[1], 0.75), "P6": (XS[2], YS[1], 0.45),
    "P7": (XS[0], YS[0], 0.25), "P8": (XS[1], YS[0], 0.45), "P9": (XS[2], YS[0], 0.25),
}
B_PILAR = 0.19

# Cada laje: caixa (x0, x1, y0, y1) em coordenadas de planta (px = horizontal,
# py = vertical), posição da borda contínua V2 ('inf' ou 'sup') e de V5 ('esq' ou 'dir').
LAJES = {
    "L1": dict(px=(XS[0], XS[1]), py=(YS[1], YS[2]), v2="inf", v5="dir"),
    "L2": dict(px=(XS[1], XS[2]), py=(YS[1], YS[2]), v2="inf", v5="esq"),
    "L3": dict(px=(XS[0], XS[1]), py=(YS[0], YS[1]), v2="sup", v5="dir"),
    "L4": dict(px=(XS[1], XS[2]), py=(YS[0], YS[1]), v2="sup", v5="esq"),
}

AZUL, VERMELHO, CINZA = "#1f4e9a", "#b3261e", "#6b6b6b"


def num(valor, casas=2):
    return f"{valor:.{casas}f}".replace(".", ",")


def seta(ax, p0, p1, cor, lw=1.8):
    ax.annotate("", xy=p1, xytext=p0, zorder=6,
                arrowprops=dict(arrowstyle="<|-|>", color=cor, lw=lw,
                                shrinkA=0, shrinkB=0, mutation_scale=11))


def desenhar_estrutura(ax):
    """Vigas, pilares, bordas contínuas hachuradas e rótulos."""
    h = BW / 2
    # vigas horizontais (V3, V2, V1) e verticais (V4, V5, V6)
    for y, nome in zip(YS, ("V3", "V2", "V1")):
        ax.add_patch(Rectangle((XS[0] - h, y - h), XS[2] - XS[0] + BW, BW,
                               fc="#e4e4e4", ec="#555", lw=0.9, zorder=2))
        ax.text(XS[2] + 0.35, y, nome, fontsize=11, fontweight="bold",
                color="#333", ha="left", va="center", zorder=7)
    for x, nome in zip(XS, ("V4", "V5", "V6")):
        ax.add_patch(Rectangle((x - h, YS[0] - h), BW, YS[2] - YS[0] + BW,
                               fc="#e4e4e4", ec="#555", lw=0.9, zorder=2))
        ax.text(x, YS[0] - 0.40, nome, fontsize=11, fontweight="bold",
                color="#333", ha="center", va="top", zorder=7)
    # pilares
    for nome, (x, y, hp) in PILARES.items():
        ax.add_patch(Rectangle((x - hp / 2, y - B_PILAR / 2), hp, B_PILAR,
                               fc="#3a3a3a", ec="#111", lw=0.8, zorder=4))
        ax.text(x + hp / 2 + 0.06, y - 0.34 if y == YS[2] else y + 0.12, nome,
                fontsize=7.5, color="#222", ha="left", va="bottom", zorder=7)
    # hachura das bordas contínuas (V2 e V5), nas duas lajes de cada lado
    for cfg in LAJES.values():
        (x0, x1), (y0, y1) = cfg["px"], cfg["py"]
        e = 0.17
        if cfg["v2"] == "inf":
            r = (x0 + h, y0 + h, x1 - x0 - BW, e)
        else:
            r = (x0 + h, y1 - h - e, x1 - x0 - BW, e)
        ax.add_patch(Rectangle(r[:2], r[2], r[3], fc="none", ec=CINZA, lw=0,
                               hatch="////", zorder=3))
        if cfg["v5"] == "dir":
            r = (x1 - h - e, y0 + h, e, y1 - y0 - BW)
        else:
            r = (x0 + h, y0 + h, e, y1 - y0 - BW)
        ax.add_patch(Rectangle(r[:2], r[2], r[3], fc="none", ec=CINZA, lw=0,
                               hatch="////", zorder=3))


def desenhar_laje(ax, nome, cfg, mom, ant=None):
    """Desenha uma laje. Se `ant` for dado, anota em cinza o valor anterior
    de cada momento que mudou na compatibilização."""
    (x0, x1), (y0, y1) = cfg["px"], cfg["py"]
    cinza = dict(fontsize=8.5, color="#6b6b6b", zorder=7, style="italic",
                 bbox=dict(fc="white", ec="none", pad=0.4, alpha=0.9))

    def mudou(i):
        return ant is not None and abs(mom[i] - ant[i]) > 0.0005

    mx, mpx, my, mpy = mom
    lx, ly = VAOS[nome]
    W, H = x1 - x0, y1 - y0
    xc, yc = (x0 + x1) / 2, (y0 + y1) / 2

    # Título e vãos do lado externo (oposto a V5), junto à borda apoiada
    topo = cfg["v2"] == "inf"                       # L1 e L2: borda externa em cima
    esq = cfg["v5"] == "dir"                        # V5 à direita: título à esquerda
    tx = x0 + 0.30 if esq else x1 - 0.30
    ty = y1 - 0.30 if topo else y0 + 0.30
    ha, va = ("left" if esq else "right"), ("top" if topo else "bottom")
    ax.text(tx, ty, nome, fontsize=17, fontweight="bold", ha=ha, va=va, zorder=7)
    deslocar = -0.62 if topo else 0.62
    ax.text(tx, ty + deslocar,
            f"$l_x$ = {num(lx, 3)} m   $l_y$ = {num(ly, 3)} m\n$\\lambda$ = {num(ly / lx, 3)}",
            fontsize=8.5, color="#333", ha=ha, va=va, linespacing=1.35, zorder=7)

    # Positivos no centro: mx (vertical) e my (horizontal)
    seta(ax, (xc, yc - 0.95), (xc, yc + 0.95), AZUL)
    seta(ax, (xc - 1.30, yc), (xc + 1.30, yc), AZUL)
    ax.text(xc + 0.14, yc + 0.62, f"$m_x$ = {num(mx)}", fontsize=11,
            color=AZUL, fontweight="bold", ha="left", va="center", zorder=7,
            bbox=dict(fc="white", ec="none", pad=0.6, alpha=0.9))
    ax.text(xc + 0.14, yc - 0.14, f"$m_y$ = {num(my)}", fontsize=11,
            color=AZUL, fontweight="bold", ha="left", va="top", zorder=7,
            bbox=dict(fc="white", ec="none", pad=0.6, alpha=0.9))
    # valores anteriores dos positivos (quadrantes da esquerda, livres)
    if mudou(0):
        ax.text(xc - 0.14, yc + 0.62, f"antes: {num(ant[0])}", ha="right",
                va="center", **cinza)
    if mudou(2):
        ax.text(xc - 0.14, yc - 0.14, f"antes: {num(ant[2])}", ha="right",
                va="top", **cinza)

    # Negativo sobre V2 (direção x, vertical): seta saindo da borda para dentro
    xa = x0 + 0.25 * W if esq else x1 - 0.25 * W
    if topo:   # V2 na borda de baixo
        ya, yb = y0 + BW / 2, y0 + BW / 2 + 1.25
    else:      # V2 na borda de cima
        ya, yb = y1 - BW / 2, y1 - BW / 2 - 1.25
    seta(ax, (xa, ya), (xa, yb), VERMELHO)
    ax.text(xa + (0.12 if esq else -0.12), (ya + yb) / 2,
            f"$m'_x$ = −{num(mpx)}", fontsize=11, color=VERMELHO, fontweight="bold",
            ha="left" if esq else "right", va="center", zorder=7,
            bbox=dict(fc="white", ec="none", pad=0.6, alpha=0.9))
    if mudou(1):
        ax.text(xa + (0.12 if esq else -0.12), (ya + yb) / 2 - 0.32,
                f"antes: −{num(ant[1])}", ha="left" if esq else "right",
                va="center", **cinza)

    # Negativo sobre V5 (direção y, horizontal)
    yb_ = y1 - 0.22 * H if topo else y0 + 0.22 * H
    if esq:    # V5 à direita
        xa, xb = x1 - BW / 2, x1 - BW / 2 - 1.45
    else:
        xa, xb = x0 + BW / 2, x0 + BW / 2 + 1.45
    seta(ax, (xa, yb_), (xb, yb_), VERMELHO)
    ax.text(xa + (-0.10 if esq else 0.10), yb_ + 0.12, f"$m'_y$ = −{num(mpy)}",
            fontsize=11, color=VERMELHO, fontweight="bold",
            ha="right" if esq else "left", va="bottom", zorder=7,
            bbox=dict(fc="white", ec="none", pad=0.6, alpha=0.9))
    if mudou(3):
        ax.text(xa + (-0.10 if esq else 0.10), yb_ - 0.12,
                f"antes: −{num(ant[3])}", ha="right" if esq else "left",
                va="top", **cinza)


def cotas(ax):
    """Cotas entre eixos, fora da planta."""
    c = "#444"
    y = YS[2] + 0.95
    for a, b in ((XS[0], XS[1]), (XS[1], XS[2])):
        ax.annotate("", xy=(a, y), xytext=(b, y),
                    arrowprops=dict(arrowstyle="<|-|>", color=c, lw=0.9,
                                    shrinkA=0, shrinkB=0, mutation_scale=8))
        ax.text((a + b) / 2, y + 0.10, f"{num(b - a, 3)} m", fontsize=9,
                ha="center", va="bottom", color=c)
        for xx in (a, b):
            ax.plot([xx, xx], [YS[2] + 0.30, y + 0.15], color=c, lw=0.7)
    x = XS[0] - 1.05
    for a, b in ((YS[0], YS[1]), (YS[1], YS[2])):
        ax.annotate("", xy=(x, a), xytext=(x, b),
                    arrowprops=dict(arrowstyle="<|-|>", color=c, lw=0.9,
                                    shrinkA=0, shrinkB=0, mutation_scale=8))
        ax.text(x - 0.10, (a + b) / 2, f"{num(b - a, 3)} m", fontsize=9,
                ha="right", va="center", color=c, rotation=90)
        for yy in (a, b):
            ax.plot([XS[0] - 0.40, x - 0.15], [yy, yy], color=c, lw=0.7)


def legenda(ax, fase):
    y = YS[0] - 1.95
    ax.add_patch(Rectangle((XS[0] - 0.6, y - 1.62), XS[2] - XS[0] + 1.2, 2.35,
                           fc="white", ec="#999", lw=0.8, zorder=1))
    seta(ax, (XS[0] - 0.3, y + 0.40), (XS[0] + 0.9, y + 0.40), AZUL)
    ax.text(XS[0] + 1.05, y + 0.40, "momento positivo no vão (módulo na direção da seta)",
            fontsize=9, va="center", color=AZUL)
    seta(ax, (XS[0] - 0.3, y - 0.05), (XS[0] + 0.9, y - 0.05), VERMELHO)
    texto_neg = ("momento negativo nas bordas contínuas V2 e V5 (valor comum $m'_c$ nos dois lados)"
                 if fase == "depois" else
                 "momento negativo nas bordas contínuas V2 e V5 (valores diferentes nos dois lados)")
    ax.text(XS[0] + 1.05, y - 0.05, texto_neg, fontsize=9, va="center", color=VERMELHO)
    ax.add_patch(Rectangle((XS[0] - 0.3, y - 0.62), 1.2, 0.30, fc="none", ec=CINZA,
                           lw=0, hatch="////"))
    ax.text(XS[0] + 1.05, y - 0.47,
            "borda contínua (V2 e V5); demais bordas: apoio simples", fontsize=9,
            va="center", color="#333")
    if fase == "depois":
        linha1 = ("Momentos de cálculo (ELU, $p_d=1{,}4(g_k+q_k)$) compatibilizados, em kN·m/m.\n"
                  "Em cinza, o valor antes da compatibilização (apenas onde mudou).\n")
    else:
        linha1 = ("Momentos de cálculo (ELU, $p_d=1{,}4(g_k+q_k)$) antes da compatibilização, "
                  "em kN·m/m.\n")
    ax.text(XS[0] - 0.3, y - 1.10, linha1 +
            "Eixo $x$ vertical e eixo $y$ horizontal; cotas entre eixos, vãos $l_x$ e $l_y$ efetivos.",
            fontsize=8.5, va="center", color="#333")


def gerar(chave, fase):
    fig, ax = plt.subplots(figsize=(12.4, 11.2))
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(XS[0] - 2.0, XS[2] + 1.2)
    ax.set_ylim(YS[0] - 4.0, YS[2] + 2.15)
    desenhar_estrutura(ax)
    for nome, cfg in LAJES.items():
        if fase == "antes":
            desenhar_laje(ax, nome, cfg, MOMENTOS_ANTES[chave][nome])
        else:
            desenhar_laje(ax, nome, cfg, MOMENTOS[chave][nome],
                          ant=MOMENTOS_ANTES[chave][nome])
    cotas(ax)
    legenda(ax, fase)
    ax.text((XS[0] + XS[2]) / 2, YS[2] + 1.75,
            f"Planta de esforços nas lajes — {NOME_PAV[chave]}, {FASES[fase]}",
            fontsize=14, fontweight="bold", ha="center", va="bottom")
    destino = SAIDA / f"planta-esforcos-lajes-{chave}-{fase}.png"
    fig.savefig(destino, dpi=170, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(destino)


if __name__ == "__main__":
    SAIDA.mkdir(parents=True, exist_ok=True)
    for chave in MOMENTOS:
        for fase in FASES:
            gerar(chave, fase)
