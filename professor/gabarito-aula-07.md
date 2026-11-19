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
