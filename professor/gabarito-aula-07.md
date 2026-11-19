# Gabarito e notas do professor: Aula 07

Material de uso do professor. Este arquivo fica fora de `source/` e não integra o site.

## Recorte didático

A aula foi criada para antecipar, antes do dimensionamento da Aula 08, o que no semestre aparecia espalhado: as hipóteses do ELU e as fronteiras entre domínios (antes na Aula 08) e o Estádio II (usado na Aula 06 sem apresentação). A ordem é a da exposição em sala: ensaio de Stuttgart, estádios, premissas e domínios.

Pontos a conferir com o material de sala:

- O texto descreve o *ensaio de Stuttgart* como o ensaio de flexão em quatro pontos associado à escola de Stuttgart (Mörsch, Leonhardt). Se a sua apresentação usou outro arranjo, outras dimensões ou outra atribuição, ajustar a seção "O ensaio de Stuttgart".
- As referências de Leonhardt e Mönnig e de Carvalho e Figueiredo Filho foram incluídas de memória, sem páginas nem edição. Conferir antes de publicar.
- A subdivisão em Estádio Ia e Ib aparece em uma frase. Se não for usada em sala, pode ser removida.
- A figura da curva momento–curvatura é esquemática. As proporções entre $M_r$, $M_y$ e $M_u$ não representam uma viga específica.

## Exemplo 1: cargas do ensaio

Dados: C30, $b_w=200$ mm, $h=500$ mm, $d=450$ mm, $A_s=10{,}73$ cm², $L=4{,}50$ m, $a=1{,}50$ m.

| Grandeza | Resultado |
|---|---:|
| $f_{ctm}=0{,}3f_{ck}^{2/3}$ | 2,896 MPa |
| $I_c$ | $2{,}0833\times10^9$ mm⁴ |
| $M_r=1{,}5f_{ctm}I_c/y_t$ | 36,2 kN m |
| $P/2$ na fissuração | 24,1 kN |
| $P$ na fissuração | 48,3 kN |
| $M_{Rd}$ (igual a $M_d$ da Aula 08) | 180 kN m |
| $P/2$ na ruína | 120 kN |
| $P$ na ruína | 240 kN |
| $P_r/P_u$ | 0,20 |

O peso próprio foi desprezado. Com o peso próprio de $25\times0{,}20\times0{,}50=2{,}5$ kN/m, o momento da carga permanente no meio do vão é $2{,}5\times4{,}5^2/8=6{,}3$ kN m e reduziria a carga de fissuração.

## Exemplo 2: três estádios

| Grandeza | Resultado |
|---|---:|
| $E_{ci}=5600\sqrt{f_{ck}}$ | 30 672 MPa |
| $\alpha_i=0{,}8+0{,}2f_{ck}/80$ | 0,875 |
| $E_{cs}=\alpha_iE_{ci}$ | 26 838 MPa |
| $\alpha_e=E_s/E_{cs}$ | 7,825 |
| $x_{II}$ | 156,9 mm |
| $I_{II}$ | $9{,}78\times10^8$ mm⁴ ($0{,}47I_c$) |
| $\sigma_c$ a $M=60$ kN m | 9,6 MPa |
| $\sigma_s$ a $M=60$ kN m | 140,7 MPa |
| $\xi$ no ELU ($M_d=180$ kN m) | 0,3556 |
| $x$ no ELU | 160,0 mm |
| $\varepsilon_s$ no ELU | 6,34‰ |

Nota: $\sigma_c=9{,}6$ MPa é menor que a faixa em que o diagrama de compressão deixa de ser linear. Com $M=100$ kN m, $\sigma_c$ chegaria a 16 MPa e a hipótese linear já seria questionável. Por isso o exemplo usa 60 kN m.

## Exemplo 3 e Exercícios 1 e 3

$\xi=\varepsilon_c/(\varepsilon_c+\varepsilon_s)$, com fronteiras $0{,}167$, $0{,}259$ e $0{,}628$ (C20 a C50, CA-50, $\varepsilon_{yd}=2{,}07$‰).

| $\varepsilon_c$ (‰) | $\varepsilon_s$ (‰) | $\xi$ | Domínio |
|---:|---:|---:|---|
| 1,5 | 10,0 | 0,1304 | 2a |
| 3,0 | 10,0 | 0,2308 | 2b |
| 3,5 | 6,34 | 0,3557 | 3 |
| 3,5 | 1,5 | 0,7000 | 4 |
| 1,0 | 10,0 | 0,0909 | 2a |
| 2,5 | 10,0 | 0,2000 | 2b |
| 3,5 | 4,0 | 0,4667 | 3, acima de 0,45 |
| 3,5 | 1,0 | 0,7778 | 4 |

Exercício 3, deformações a partir de $\xi$: se $\xi<0{,}259$, $\varepsilon_s=10$‰ e $\varepsilon_c=10\xi/(1-\xi)$; se $\xi\geq0{,}259$, $\varepsilon_c=3{,}5$‰ e $\varepsilon_s=3{,}5(1-\xi)/\xi$.

| $\xi$ | Domínio | $\varepsilon_c$ (‰) | $\varepsilon_s$ (‰) |
|---:|---|---:|---:|
| 0,10 | 2a | 1,11 | 10,0 |
| 0,30 | 3 | 3,5 | 8,17 |
| 0,70 | 4 | 3,5 | 1,5 |

## Exercício 2: viga de 15 × 40 cm

$f_{ctm}=2{,}896$ MPa, $I_c=150\times400^3/12=8{,}0\times10^8$ mm⁴, $y_t=200$ mm.

$$
M_r=1{,}5\times2{,}896\times8{,}0\times10^8/200=17{,}4\text{ kN m},
\qquad
\frac{P}{2}=\frac{17{,}4}{1{,}20}=14{,}5\text{ kN},
\qquad
P=29{,}0\text{ kN}.
$$

## Exercício 4

(a) Estádio I; (b) Estádio II; (c) Estádio III; (d) Estádio I ($I_c$) e Estádio II ($I_{II}$), combinados pela expressão de Branson, que depende da razão $M_r/M_a$.

## Conferência dos limites com o capítulo 4

As expressões da aula ($\xi_L=\varepsilon_c/(\varepsilon_c+\varepsilon_s)$ nos pivôs, $\varepsilon_{c2}$ e $\varepsilon_{cu}$ de C55 a C90, $\mu_L=\alpha_c\eta_c\lambda\xi_L(1-\lambda\xi_L/2)$) foram recalculadas para C40, C45, C50 e de C55 a C90 e comparadas com os Quadros 4.1 (CA-50), 4.2, 4.3 e 4.4 do capítulo. A diferença máxima é 0,0005 em $\xi_L$ e em $\mu_L$, devida ao arredondamento dos quadros. Nenhuma fórmula da aula precisou ser corrigida. Foram ajustados três textos: o domínio 4 (a norma não admite em vigas, item 17.2.3), o critério de ductilidade (o capítulo o verifica nas seções sobre apoios; a disciplina o aplica em todas) e o fator 0,85 (perda de resistência sob tensão constante no tempo).

O Quadro 4.1 só traz CA-50 e CA-60. Os $\xi_{L(3/4)}$ da aula valem para CA-50 ($\varepsilon_{yd}=2{,}07$‰). Com CA-60 ($\varepsilon_{yd}=2{,}484$‰) seria 0,585 até C40.

## Exercícios 5 a 10 (variações dos exemplos)

Os Exercícios 1 e 2 foram resolvidos em sala. Os demais são para a turma.

**Exercício 5** (variação do Exemplo 1): C35, $b_w=250$ mm, $h=600$ mm, $L=6{,}00$ m, $a=2{,}00$ m, $M_{Rd}=310$ kN m.

| Grandeza | Resultado |
|---|---:|
| $f_{ctm}=0{,}3\times35^{2/3}$ | 3,210 MPa |
| $I_c$ | $4{,}5\times10^9$ mm⁴ |
| $M_r$ | 72,2 kN m |
| $P/2$ e $P$ na fissuração | 36,1 kN e 72,2 kN |
| $P/2$ e $P$ na ruína | 155 kN e 310 kN |
| $P_r/P_u$ | 0,233 |

**Exercício 6** (variação do Exemplo 2): $b_w=150$ mm, $h=400$ mm, $d=360$ mm, C30, $A_s=628$ mm².

| Grandeza | Resultado |
|---|---:|
| $\alpha_e$ | 7,825 |
| $M_r$ | 17,38 kN m |
| $x_{II}$ | 124,3 mm |
| $I_{II}$ | $3{,}69\times10^8$ mm⁴ ($0{,}461I_c$) |
| $\sigma_c$ e $\sigma_s$ a $M=40$ kN m | 13,5 MPa e 199,9 MPa |
| (para $M=25$ kN m) | 8,4 MPa e 125,0 MPa |
| $R_s=A_sf_{yd}$ | 273,0 kN |
| $x$ no ELU, bloco $0{,}8x$ | 124,9 mm, $\xi=0{,}347$ |
| $\varepsilon_s$ no ELU | 6,59‰ |
| $M_{Rd}=R_s(d-0{,}4x)$ | 84,7 kN m |

A linha neutra do Estádio II (124,3 mm) e a do ELU (124,9 mm) quase coincidem de novo, como no Exemplo 2. Vale comentar que isso é coincidência dos dados: as hipóteses são diferentes.

**Exercício 7** (C60, CA-50): $\varepsilon_{c2}=2+0{,}085\times10^{0{,}53}=2{,}288$‰; $\varepsilon_{cu}=2{,}6+35\times0{,}3^4=2{,}8835$‰.

| Fronteira | $\xi_L$ |
|---|---:|
| 2a / 2b | 0,1862 |
| 2 / 3 | 0,2238 |
| 3 / 4 | 0,5821 |

| $\varepsilon_c$ (‰) | $\varepsilon_s$ (‰) | $\xi$ | Domínio |
|---:|---:|---:|---|
| 2,0 | 10 | 0,1667 | 2a |
| 2,8 | 10 | 0,2188 | 2b |
| 2,8835 | 5,0 | 0,3658 | 3 |
| 2,8835 | 1,5 | 0,6578 | 4 |

**Exercício 8** ($b_w=200$ mm, $d=460$ mm, $b_wd^2=4{,}232\times10^7$ mm³):

| Caso | $M_d$ (kN m) | $f_{cd}$ (MPa) | $\mu$ | Limites $\mu_L$ | Domínio |
|---|---:|---:|---:|---|---|
| (a) C25, 45 + 30 | 105 | 17,86 | 0,1389 | 0,106 / 0,158 / 0,320 | 2b |
| (b) C25, 50 + 45 | 133 | 17,86 | 0,1760 | 0,106 / 0,158 / 0,320 | 3 |
| (c) C50, 50 + 45 | 133 | 35,71 | 0,0880 | 0,098 / 0,147 / 0,297 | 2a |

**Exercício 9** (C25, $M_d=250$ kN m): $\mu=0{,}3308>0{,}320$, domínio 4, e $>0{,}251$. $d_{min,3}=\sqrt{250\times10^6/(0{,}320\times200\times17{,}857)}=467{,}7$ mm; $d_{min,duct}=\sqrt{250\times10^6/(0{,}251\times200\times17{,}857)}=528{,}1$ mm. Com $d=530$ mm, $\mu=0{,}249$, que atende à ductilidade.

**Exercício 10** (laje, C25, $d=110$ mm, $m_d=9$ kN m/m): $\mu=0{,}04165$, domínio 2a. $\xi=1{,}25\left(1-\sqrt{1-2\times0{,}04165/0{,}85}\right)=0{,}0628$ e $\varepsilon_c=10\times0{,}0628/(1-0{,}0628)=0{,}670$‰. Se $m_d=14$ kN m/m, $\mu=0{,}0648$, ainda no 2a. Para sair do domínio 2a seria preciso $\mu\geq0{,}106$, isto é, $m_d\geq22{,}9$ kN m/m com esse $d$.
