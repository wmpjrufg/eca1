"""Figuras da Aula 07: ensaio de flexão em quatro pontos, estádios e domínios.

Gera cinco PNG didáticos (sem escala):
  ensaio-quatro-pontos.png      viga biapoiada, cortante e momento
  curva-momento-curvatura.png   curva M x 1/r esquemática com os três estádios
  estadios-secao.png            seção, deformações e tensões nos estádios I, II e III
  dominios-deformacao.png       retas e domínios de deformação (NBR 6118, 17.2.2)
  diagramas-tensao-deformacao.png  concreto (parábola-retângulo) e aço (bilinear)

Uso: python aula07_estadios_dominios.py PASTA_DE_SAIDA
"""
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle, Circle

SAIDA = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
AZUL, VERMELHO, VERDE, CINZA, LARANJA = "#1f4e9a", "#b3261e", "#2e7d32", "#6b6b6b", "#c25e00"
CONC = "#e9e9e9"


def salvar(fig, nome):
    SAIDA.mkdir(parents=True, exist_ok=True)
    destino = SAIDA / nome
    fig.savefig(destino, dpi=170, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(destino)


def seta(ax, p0, p1, cor=AZUL, lw=1.6, estilo="-|>", ms=10):
    ax.annotate("", xy=p1, xytext=p0, zorder=6,
                arrowprops=dict(arrowstyle=estilo, color=cor, lw=lw,
                                shrinkA=0, shrinkB=0, mutation_scale=ms))


# ---------------------------------------------------------------------------
# Figura 1: ensaio de flexão em quatro pontos
# ---------------------------------------------------------------------------
def fig_ensaio():
    L, a = 9.0, 3.0
    fig, (ax, av, am) = plt.subplots(3, 1, figsize=(9.2, 7.4), sharex=True,
                                     gridspec_kw=dict(height_ratios=[1.35, 1, 1]))
    # viga
    ax.set_xlim(-0.9, L + 0.9)
    ax.set_ylim(-1.3, 2.3)
    ax.axis("off")
    ax.add_patch(Rectangle((0, 0), L, 0.55, fc=CONC, ec="#333", lw=1.4))
    for x in (0, L):  # apoios
        ax.add_patch(Polygon([[x, 0], [x - 0.28, -0.5], [x + 0.28, -0.5]],
                             fc="white", ec="#333", lw=1.3))
    for x in (a, L - a):
        seta(ax, (x, 1.75), (x, 0.58), VERMELHO, lw=2.2, ms=13)
        ax.text(x, 1.85, "$P/2$", ha="center", va="bottom", fontsize=12, color=VERMELHO)
    # armadura (linha tracejada)
    ax.plot([0.15, L - 0.15], [0.12, 0.12], color="#333", lw=2.4)
    # vãos
    for x0, x1, txt in ((0, a, "$a=L/3$"), (a, L - a, "flexão pura"), (L - a, L, "$a=L/3$")):
        ax.annotate("", xy=(x0, -0.95), xytext=(x1, -0.95),
                    arrowprops=dict(arrowstyle="<|-|>", color="#444", lw=0.9,
                                    shrinkA=0, shrinkB=0, mutation_scale=8))
        ax.text((x0 + x1) / 2, -1.2, txt, ha="center", va="top", fontsize=10.5)


    # cortante
    xs = [0, 0, a, a, L - a, L - a, L, L]
    ys = [0, 1, 1, 0, 0, -1, -1, 0]
    av.fill(xs, ys, color="#cfe0f5", ec=AZUL, lw=1.6)
    av.axhline(0, color="#333", lw=0.9)
    av.set_ylim(-1.7, 1.7)
    av.set_ylabel("$V$", rotation=0, fontsize=13, labelpad=14, va="center")
    av.text(a / 2, 1.1, "$+P/2$", ha="center", va="bottom", fontsize=11, color=AZUL)
    av.text(L - a / 2, -1.1, "$-P/2$", ha="center", va="top", fontsize=11, color=AZUL)
    av.text(L / 2, 0.15, "$V=0$", ha="center", va="bottom", fontsize=11, color=AZUL)
    av.set_yticks([])
    for s in ("top", "right", "left", "bottom"):
        av.spines[s].set_visible(False)
    av.tick_params(bottom=False)

    # momento: convenção brasileira, desenhado do lado tracionado (para baixo)
    xm = [0, a, L - a, L]
    ym = [0, -1, -1, 0]
    am.fill(xm, ym, color="#f7d9d6", ec=VERMELHO, lw=1.6)
    am.axhline(0, color="#333", lw=0.9)
    am.set_ylim(-1.65, 0.2)
    am.set_ylabel("$M$", rotation=0, fontsize=13, labelpad=14, va="center")
    am.text(L / 2, -1.07, "$M=\\dfrac{P}{2}\\,a=\\dfrac{PL}{6}$ (constante)",
            ha="center", va="top", fontsize=11.5, color=VERMELHO)
    am.set_yticks([])
    for s in ("top", "right", "left", "bottom"):
        am.spines[s].set_visible(False)
    am.tick_params(bottom=False, labelbottom=False)
    fig.subplots_adjust(hspace=0.12)
    salvar(fig, "ensaio-quatro-pontos.png")


# ---------------------------------------------------------------------------
# Figura 2: curva momento x curvatura esquemática
# ---------------------------------------------------------------------------
def fig_curva():
    fig, ax = plt.subplots(figsize=(9.0, 5.8))
    cr, Mr = 1.0, 1.0           # fissuração
    c2, M2 = 1.45, 1.03         # logo após a fissuração (queda de rigidez)
    cy, My = 5.0, 3.5           # escoamento da armadura
    cu, Mu = 10.0, 4.0          # ruína
    ax.plot([0, cr], [0, Mr], color=AZUL, lw=2.8, zorder=4)
    ax.plot([cr, c2], [Mr, M2], color=AZUL, lw=2.8, zorder=4)
    ax.plot([c2, cy], [M2, My], color=VERMELHO, lw=2.8, zorder=4)
    c3 = np.linspace(cy, cu, 60)
    ax.plot(c3, My + (Mu - My) * (1 - np.exp(-(c3 - cy) / 1.8)) / (1 - np.exp(-(cu - cy) / 1.8)),
            color=VERDE, lw=2.8, zorder=4)
    for x0, x1, cor in ((0, c2, AZUL), (c2, cy, VERMELHO), (cy, cu, VERDE)):
        ax.axvspan(x0, x1, color=cor, alpha=0.07, lw=0)
    # nomes dos estádios no alto de cada faixa
    ax.text(c2 / 2, 5.0, "Estádio I", ha="center", va="top", fontsize=11, color=AZUL, fontweight="bold")
    ax.text(c2 / 2, 4.72, "não\nfissurada", ha="center", va="top", fontsize=9, color=AZUL, linespacing=1.2)
    ax.text((c2 + cy) / 2, 5.0, "Estádio II", ha="center", va="top", fontsize=11, color=VERMELHO, fontweight="bold")
    ax.text((c2 + cy) / 2, 4.72, "fissurada, aço e concreto\nem regime elástico", ha="center", va="top",
            fontsize=9, color=VERMELHO, linespacing=1.2)
    ax.text((cy + cu) / 2, 5.0, "Estádio III", ha="center", va="top", fontsize=11, color=VERDE, fontweight="bold")
    ax.text((cy + cu) / 2, 4.72, "plastificação até a ruína", ha="center", va="top", fontsize=9, color=VERDE)
    # pontos notáveis
    for cx, my_, txt, dx, dy, ha, va in ((cr, Mr, "$M_r$ (fissuração)", 0.15, -0.12, "left", "top"),
                                          (cy, My, "$M_y$ (escoamento da armadura)", -0.15, 0.12, "right", "bottom"),
                                          (cu, Mu, "$M_u$ (ruína)", 0.0, 0.14, "center", "bottom")):
        ax.plot([cx], [my_], "o", color="#222", ms=6, zorder=6)
        ax.plot([cx, cx], [0, my_], ls=":", color="#777", lw=0.9)
        ax.plot([0, cx], [my_, my_], ls=":", color="#777", lw=0.9)
        ax.text(cx + dx, my_ + dy, txt, ha=ha, va=va, fontsize=10.5)
    ax.set_xlim(0, 10.8)
    ax.set_ylim(0, 5.2)
    ax.set_xlabel("curvatura $1/r$ (ou flecha), crescendo com a carga", fontsize=11)
    ax.set_ylabel("momento fletor $M$ na seção", fontsize=11)
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    salvar(fig, "curva-momento-curvatura.png")


# ---------------------------------------------------------------------------
# Figura 3: seção, deformações e tensões nos estádios I, II e III
# ---------------------------------------------------------------------------
H, BW = 2.4, 1.0            # altura e largura desenhadas da seção
YS = 0.28                   # posição da armadura tracionada (medida da base)


def linha_estadio(ax, y0, titulo, xr, ec, larg, estadio):
    """Desenha uma linha (seção, deformações, tensões) com origem vertical y0.

    xr: profundidade relativa da linha neutra; ec: encurtamento no topo (escala
    do desenho); larg: largura do diagrama de compressão (escala do desenho)."""
    xb, xs = 5.8, 9.9       # eixos de referência de deformações e tensões
    ax.text(0.0, y0 + H + 0.30, titulo, fontsize=12, fontweight="bold", va="bottom")
    # seção
    ax.add_patch(Rectangle((0.9, y0), BW, H, fc=CONC, ec="#333", lw=1.3))
    ax.add_patch(Circle((0.9 + BW / 2 - 0.25, y0 + YS), 0.07, fc="#222", ec="#222", zorder=5))
    ax.add_patch(Circle((0.9 + BW / 2 + 0.25, y0 + YS), 0.07, fc="#222", ec="#222", zorder=5))
    yln = y0 + H - xr * H                           # linha neutra
    ax.plot([0.35, 2.5], [yln, yln], ls=(0, (6, 3, 1, 3)), color=CINZA, lw=1.0)
    ax.text(0.30, yln, "LN", fontsize=9, va="center", ha="right", color=CINZA)
    if estadio >= 2:                                 # fissuras
        top = yln - 0.06 if estadio == 2 else yln + 0.10
        for xf in (1.12, 1.4, 1.68):
            ax.plot([xf, xf + 0.04, xf - 0.03], [y0, (y0 + top) / 2, top], color="#c0392b", lw=1.1)
    # deformações
    ax.plot([xb, xb], [y0 - 0.05, y0 + H + 0.05], color="#333", lw=0.8)
    x = xr * H
    e_bot = ec * (x - H) / x                         # negativa (tração)
    pts = [(xb, y0 + H), (xb + ec, y0 + H), (xb + e_bot, y0), (xb, y0)]
    ax.add_patch(Polygon(pts, fc="#f5dfc6", ec=LARANJA, lw=1.6, zorder=3))
    ax.text(xb + ec + 0.08, y0 + H, "$\\varepsilon_c$", fontsize=11, va="center", color=LARANJA)
    ax.text(xb + e_bot - 0.08, y0, "$\\varepsilon_{ct}$" if estadio == 1 else "$\\varepsilon_{s}$",
            fontsize=11, va="center", ha="right", color=LARANJA)
    # tensões
    ax.plot([xs, xs], [y0 - 0.05, y0 + H + 0.05], color="#333", lw=0.8)
    ax.text(xs + 0.08, y0 + H + 0.10, "$\\sigma_c$", fontsize=11, va="bottom", color=AZUL)
    if estadio == 1:
        ax.add_patch(Polygon([(xs, y0 + H), (xs + larg, y0 + H), (xs, yln)], fc="#cfe0f5", ec=AZUL, lw=1.6))
        lt = larg * (H - x) / x * 0.20               # tração no concreto, bem menor
        ax.add_patch(Polygon([(xs, yln), (xs - lt, y0), (xs, y0)], fc="#f7d9d6", ec=VERMELHO, lw=1.6))
        seta(ax, (xs - 0.05, y0 + YS), (xs - 0.55, y0 + YS), VERMELHO, lw=1.8)
        ax.text(xs - 0.60, y0 + YS + 0.12, "$R_s$", fontsize=10.5, color=VERMELHO, ha="right")
        ax.text(xs - 1.3, y0 + 1.0, "concreto tracionado\ncolabora", fontsize=8.5, ha="center", color=VERMELHO)
    elif estadio == 2:
        ax.add_patch(Polygon([(xs, y0 + H), (xs + larg, y0 + H), (xs, yln)], fc="#cfe0f5", ec=AZUL, lw=1.6))
        seta(ax, (xs - 0.05, y0 + YS), (xs - 1.0, y0 + YS), VERMELHO, lw=2.2)
        ax.text(xs - 1.07, y0 + YS + 0.12, "$R_s$", fontsize=10.5, color=VERMELHO, ha="right")
        ax.text(xs - 1.3, y0 + 0.95, "concreto tracionado\nfissurado: $\\sigma_{ct}=0$", fontsize=8.5,
                ha="center", color=VERMELHO)
    else:
        # parábola-retângulo: constante no topo (eps >= 2‰), parábola até a LN
        z2 = x * (1 - 2.0 / 3.5)                    # profundidade onde eps = 2‰ (do topo)
        zs = np.linspace(z2, x, 40)
        eps = 3.5 * (x - zs) / x
        sig = 1 - (1 - eps / 2.0) ** 2
        yy = y0 + H - zs
        curva = [(xs + larg * sv, yv) for sv, yv in zip(sig, yy)]
        pol = [(xs, y0 + H), (xs + larg, y0 + H)] + curva + [(xs, yln)]
        ax.add_patch(Polygon(pol, fc="#cfe0f5", ec=AZUL, lw=1.6))
        yb = y0 + H - 0.8 * x                       # bloco equivalente
        ax.plot([xs + larg * 0.85, xs + larg * 0.85, xs, xs], [y0 + H, yb, yb, y0 + H],
                ls="--", color=VERDE, lw=1.2)
        ax.text(xs + larg + 0.10, (y0 + H + yb) / 2, "bloco\nequivalente\n$0{,}8x$", fontsize=8.5,
                color=VERDE, va="center")
        seta(ax, (xs - 0.05, y0 + YS), (xs - 1.0, y0 + YS), VERMELHO, lw=2.6)
        ax.text(xs - 1.07, y0 + YS + 0.12, "$A_sf_{yd}$", fontsize=10.5, color=VERMELHO, ha="right")
        ax.text(xs - 1.3, y0 + 0.95, "aço escoando; concreto\ntracionado desprezado", fontsize=8.5,
                ha="center", color=VERMELHO)


def fig_estadios():
    passo = H + 0.95
    fig, ax = plt.subplots(figsize=(11.2, 10.8))
    ax.set_xlim(-0.6, 12.4)
    ax.set_ylim(-0.4, 3 * passo + 0.55)
    ax.set_aspect("equal")
    ax.axis("off")
    base = 2 * passo
    linha_estadio(ax, base, "Estádio I: seção não fissurada, material elástico", 0.50, 1.15, 1.05, 1)
    linha_estadio(ax, base - passo, "Estádio II: seção fissurada, compressão ainda linear", 0.34, 0.95, 1.45, 2)
    linha_estadio(ax, base - 2 * passo, "Estádio III: ruína, concreto plastificado e aço escoando", 0.22, 0.80, 1.65, 3)
    for x, t in ((1.4, "seção"), (5.8, "deformações"), (9.9, "tensões")):
        ax.text(x, 3 * passo + 0.20, t, ha="center", fontsize=11.5, color="#333", style="italic")
    salvar(fig, "estadios-secao.png")


# ---------------------------------------------------------------------------
# Figura 4: domínios de deformação
# ---------------------------------------------------------------------------
def fig_dominios():
    eyd = 2.07
    ds = 0.10                      # d'/h e (h-d)/h
    yA = ds                        # armadura tracionada (fração de h a partir da base)
    pB = (3.5, 1.0)
    pA = (-10.0, yA)
    fig, ax = plt.subplots(figsize=(10.8, 7.8))
    ax.set_xlim(-12.2, 7.4)
    ax.set_ylim(-0.36, 1.32)
    ax.axis("off")

    # regiões
    reg = {
        "1": ([pA, (-10, 1.0), (0, 1.0)], "#f3e5f5"),
        "2": ([pA, (0, 1.0), pB], "#e3f2fd"),
        "3": ([pB, pA, (-eyd, yA)], "#e8f5e9"),
        "4": ([pB, (-eyd, yA), (0, yA)], "#fff8e1"),
        "4a": ([pB, (0, yA), (0, 0)], "#fbe9e7"),
        "5": ([pB, (0, 0), (2, 0), (2, 1.0)], "#eceff1"),
    }
    for _, (p, cor) in reg.items():
        ax.add_patch(Polygon(p, fc=cor, ec="none", zorder=1))
    # linhas limite
    kw = dict(color="#333", lw=1.3, zorder=3)
    ax.plot([-10, -10], [0, 1], **kw)                       # reta a
    ax.plot([2, 2], [0, 1], **kw)                           # reta b
    ax.plot([pA[0], 0], [pA[1], 1.0], **kw)                 # 1|2
    ax.plot([pA[0], pB[0]], [pA[1], pB[1]], **kw)           # 2|3
    ax.plot([pB[0], -eyd], [pB[1], yA], **kw)               # 3|4
    ax.plot([pB[0], 0], [pB[1], yA], **kw)                  # 4|4a
    ax.plot([pB[0], 0], [pB[1], 0.0], **kw)                 # 4a|5
    # faces e armadura
    ax.plot([-10, 3.5], [1, 1], color="#333", lw=2.2, zorder=4)
    ax.plot([-10, 2], [0, 0], color="#333", lw=2.2, zorder=4)
    ax.plot([-10.2, 3.7], [yA, yA], ls="--", color=CINZA, lw=0.9, zorder=2)
    ax.plot([0, 0], [-0.06, 1.06], color="#333", lw=0.9, zorder=2)
    ax.text(-10.3, 1.0, "face\ncomprimida", ha="right", va="center", fontsize=9, color=CINZA)
    ax.text(-10.3, 0.0, "face\ntracionada", ha="right", va="center", fontsize=9, color=CINZA)
    ax.text(-10.3, yA, "$d$", ha="right", va="center", fontsize=10, color=CINZA)
    # pivôs
    pC = (2.0, 1 - 3 / 7)
    for p, nome, dx, dy, ha in ((pA, "A", -0.30, 0.0, "right"), (pB, "B", 0.25, 0.0, "left"),
                                (pC, "C", 0.25, 0.0, "left")):
        ax.plot(*p, "o", color="#111", ms=8, zorder=6)
        ax.text(p[0] + dx, p[1] + dy, nome, fontsize=13, fontweight="bold", ha=ha, va="center", zorder=7,
                bbox=dict(fc="white", ec="none", pad=0.8, alpha=0.9))
    ax.text(pC[0] + 0.55, pC[1], "$3h/7$ da face\ncomprimida", fontsize=8.5, color=CINZA, va="center")
    # rótulos das retas e domínios
    ax.text(-10.0, 1.07, "reta a", ha="center", fontsize=10.5, fontweight="bold")
    ax.text(2.0, 1.07, "reta b", ha="center", fontsize=10.5, fontweight="bold")
    rot = {"1": ((-8.2, 0.62), "Domínio 1\ntração\nnão uniforme"),
           "2": ((-3.4, 0.92), "Domínio 2"),
           "3": ((-3.3, 0.34), "Domínio 3")}
    for k, ((x, y), t) in rot.items():
        ax.text(x, y, t, ha="center", va="center", fontsize=10.5, fontweight="bold", color="#222", zorder=7)
    for t, (px, py), (tx, ty) in (("Domínio 4", (0.25, 0.35), (4.3, 0.30)),
                                   ("Domínio 5", (1.45, 0.20), (4.3, 0.12)),
                                   ("Domínio 4a", (0.09, 0.05), (4.3, -0.06))):
        ax.annotate(t, xy=(px, py), xytext=(tx, ty), fontsize=10.5, fontweight="bold", va="center",
                    arrowprops=dict(arrowstyle="-", color="#555", lw=0.9, shrinkA=2, shrinkB=0), zorder=8)
    # eixo de deformações
    yax = -0.16
    ax.annotate("", xy=(-10, yax), xytext=(3.5, yax),
                arrowprops=dict(arrowstyle="<|-|>", color="#333", lw=1, shrinkA=0, shrinkB=0))
    for v, lab in ((-10, "10"), (-eyd, "$\\varepsilon_{yd}$\n(2,07)"), (0, "0"), (2, "2"), (3.5, "3,5")):
        ax.plot([v, v], [yax - 0.015, yax + 0.015], color="#333", lw=1)
        ax.text(v, yax - 0.04, lab, ha="center", va="top", fontsize=9.5)
    ax.text(-5, yax - 0.20, "alongamento ‰ (tração)", ha="center", fontsize=10, color=AZUL)
    ax.text(2.1, yax - 0.20, "encurtamento ‰ (compressão)", ha="center", fontsize=10, color=VERMELHO)
    ax.text(-10, 1.25, "Domínios de deformação no ELU (seção retangular, $f_{ck}\\leq50$ MPa)",
            fontsize=13, fontweight="bold", ha="left")
    ax.text(-10, 1.19, "Flexão simples: domínios 2, 3 e 4. Cada reta é um possível diagrama linear de deformações.",
            fontsize=9.5, color="#333", ha="left")
    salvar(fig, "dominios-deformacao.png")


# ---------------------------------------------------------------------------
# Figura 5: diagramas tensão-deformação de cálculo
# ---------------------------------------------------------------------------
def fig_sigma_epsilon():
    fig, (a, b) = plt.subplots(1, 2, figsize=(10.6, 4.6))
    # concreto: parábola-retângulo, fck <= 50 MPa
    e = np.linspace(0, 2.0, 80)
    a.plot(e, 1 - (1 - e / 2.0) ** 2, color=AZUL, lw=2.6)
    a.plot([2.0, 3.5], [1, 1], color=AZUL, lw=2.6)
    a.plot([2.0, 2.0], [0, 1], ls=":", color="#777", lw=0.9)
    a.plot([3.5, 3.5], [0, 1], ls=":", color="#777", lw=0.9)
    a.plot([0, 3.5], [1, 1], ls=":", color="#777", lw=0.9)
    a.set_xlim(0, 4.1); a.set_ylim(0, 1.25)
    a.set_xticks([0, 2.0, 3.5]); a.set_xticklabels(["0", r"$\varepsilon_{c2}=2{,}0$", r"$\varepsilon_{cu}=3{,}5$"])
    a.set_yticks([1.0]); a.set_yticklabels([r"$0{,}85f_{cd}$"])
    a.set_xlabel(r"encurtamento do concreto $\varepsilon_c$ (‰)", fontsize=11)
    a.set_ylabel(r"tensão de compressão $\sigma_c$", fontsize=11)
    a.set_title("Concreto: parábola-retângulo", fontsize=12, fontweight="bold")
    a.text(0.55, 0.28, r"$\sigma_c=0{,}85f_{cd}\left[1-\left(1-\dfrac{\varepsilon_c}{\varepsilon_{c2}}\right)^2\right]$",
           fontsize=11, color=AZUL)
    a.text(2.75, 0.5, "trecho\nconstante", ha="center", fontsize=9.5, color=AZUL)
    # aço: elastoplástico perfeito
    eyd = 2.07
    b.plot([0, eyd, 10], [0, 1, 1], color=VERMELHO, lw=2.6)
    b.plot([eyd, eyd], [0, 1], ls=":", color="#777", lw=0.9)
    b.plot([10, 10], [0, 1], ls=":", color="#777", lw=0.9)
    b.plot([0, 10], [1, 1], ls=":", color="#777", lw=0.9)
    b.set_xlim(0, 11.5); b.set_ylim(0, 1.25)
    b.set_xticks([0, eyd, 10]); b.set_xticklabels(["0", r"$\varepsilon_{yd}=2{,}07$", r"$\varepsilon_{su}=10$"])
    b.set_yticks([1.0]); b.set_yticklabels([r"$f_{yd}$"])
    b.set_xlabel(r"alongamento da armadura $\varepsilon_s$ (‰)", fontsize=11)
    b.set_ylabel(r"tensão de tração $\sigma_s$", fontsize=11)
    b.set_title("Aço CA-50: elastoplástico perfeito", fontsize=12, fontweight="bold")
    b.text(0.9, 0.35, r"$\sigma_s=E_s\varepsilon_s$", fontsize=11, color=VERMELHO, rotation=0)
    b.text(6.0, 0.80, r"$\sigma_s=f_{yd}$", fontsize=11, color=VERMELHO)
    for ax in (a, b):
        for sp in ("top", "right"):
            ax.spines[sp].set_visible(False)
    fig.tight_layout()
    salvar(fig, "diagramas-tensao-deformacao.png")


if __name__ == "__main__":
    fig_ensaio()
    fig_curva()
    fig_estadios()
    fig_dominios()
    fig_sigma_epsilon()
