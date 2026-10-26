## Entrega 1: Pré-dimensionamento, vãos efetivos e cargas nas lajes

### Distâncias entre eixos

As cotas do desenho (510, 585, 620 e 485 cm) são medidas entre faces das
vigas. Como as vigas têm $b_w=15\text{ cm}$, somam-se $7{,}5\text{ cm}$
a cada cota para obter a distância entre eixos, usada na
[Tabela 1](#tabela-eixos). Por exemplo, para a cota de $510\text{ cm}$:
$5{,}10+0{,}075=5{,}175\text{ m}$.

(tabela-eixos)=
**Tabela 1.** Distâncias entre eixos das lajes do pavimento padrão.
| Laje | Posição | Vigas de contorno | Dimensões entre eixos (m) |
|---|---|---|---|
| L1 | Superior esquerda | V1, V2, V4 e V5 | 5,175 × 5,925 |
| L2 | Superior direita | V1, V2, V5 e V6 | 5,175 × 6,275 |
| L3 | Inferior esquerda | V2, V3, V4 e V5 | 4,925 × 5,925 |
| L4 | Inferior direita | V2, V3, V5 e V6 | 4,925 × 6,275 |

### Pré-dimensionamento dos pilares

A planta tem nove pilares, numerados de P1 a P9 da esquerda para a direita e de
cima para baixo. Toma-se como referência o nível do térreo, em que cada pilar
sustenta todos os pavimentos acima: cinco pavimentos-tipo e a cobertura, logo
$n_{tipo}=5$ e $n_{cob}=1$. Para cada pilar, a área de influência $A_i$ segue as
faixas de Bacarji da Figura 4 da [Aula 02](../aulas/002-lanc-pre-dim.md), com os
vãos entre eixos da [Tabela 1](#tabela-eixos): $l_1=5{,}925\text{ m}$ e
$l_2=6{,}275\text{ m}$ na direção horizontal; $l_3=5{,}175\text{ m}$ e
$l_4=4{,}925\text{ m}$ na direção vertical. Na direção horizontal as faixas são
$0{,}45\,l$ (lado externo) e $0{,}55\,l$ (lado interno); na vertical, $0{,}5\,l$
para cada lado do pilar.

Por exemplo, para o pilar de canto P1 e para o pilar intermediário P5:

$$
A_{P1}=(0{,}45\times5{,}925)(0{,}5\times5{,}175)=2{,}666\times2{,}588=6{,}899\text{ m}^2,
$$

$$
A_{P5}=0{,}55(5{,}925+6{,}275)\times0{,}5(5{,}175+4{,}925)=6{,}710\times5{,}050=33{,}886\text{ m}^2.
$$

(tabela-pilares-areas)=
**Tabela 2.** Áreas de influência dos pilares.

| Pilar | Posição | Faixa horizontal (m) | Faixa vertical (m) | $A_i$ (m²) |
|---|---|---:|---:|---:|
| P1 | Canto | 2,666 | 2,588 | 6,899 |
| P2 | Extremidade | 6,710 | 2,588 | 17,362 |
| P3 | Canto | 2,824 | 2,588 | 7,306 |
| P4 | Extremidade | 2,666 | 5,050 | 13,465 |
| P5 | Intermediário | 6,710 | 5,050 | 33,886 |
| P6 | Extremidade | 2,824 | 5,050 | 14,260 |
| P7 | Canto | 2,666 | 2,463 | 6,566 |
| P8 | Extremidade | 6,710 | 2,463 | 16,523 |
| P9 | Canto | 2,824 | 2,463 | 6,953 |

Com as cargas de 10 e 7 kN/m² do enunciado, a carga característica e a carga de
cálculo (Equações (17) e (18) da Aula 02) são:

$$
N_k^*=A_i(10\times5+7\times1)=57A_i,\qquad N_d^*=\alpha N_k^*,
$$

com $\alpha=2{,}5$ (canto), $2{,}2$ (extremidade) e $1{,}8$ (intermediário). Para
o concreto C30 e o aço CA-50, $f_{cd}=3{,}0/1{,}4=2{,}143\text{ kN/cm}^2$ e, com
$\rho=0{,}02$ e $\sigma_s=42\text{ kN/cm}^2$, a Equação (15) fica:

$$
A_c=\frac{N_d^*}{0{,}85\times2{,}143+0{,}02\times42}
=\frac{N_d^*}{2{,}661}\quad(\text{cm}^2,\ N_d^*\text{ em kN}).
$$

Para P1 e P5:

$$
N_{d,P1}^*=2{,}5\times57\times6{,}899=983{,}1\text{ kN},
\qquad
A_{c,P1}=\frac{983{,}1}{2{,}661}=369{,}4\text{ cm}^2,
$$

$$
N_{d,P5}^*=1{,}8\times57\times33{,}886=3476{,}7\text{ kN},
\qquad
A_{c,P5}=\frac{3476{,}7}{2{,}661}=1306{,}3\text{ cm}^2.
$$

Adota-se a menor dimensão $b=19\text{ cm}$, a menor dimensão usual da NBR 6118,
na direção horizontal da planta, e a maior dimensão $h$ na direção vertical,
múltipla de 5 cm, de modo que $19h\geq A_c$ e $19h\geq360\text{ cm}^2$. Para P1,
$h=369{,}4/19=19{,}4\to20\text{ cm}$; para P5, $h=1306{,}3/19=68{,}8\to70\text{ cm}$.
Como $b\geq19\text{ cm}$, $\gamma_n=1{,}00$ em todos os pilares.

(tabela-pilares-secao)=
**Tabela 3.** Cargas e seções pré-dimensionadas dos pilares.

| Pilar | $N_k^*$ (kN) | $\alpha$ | $N_d^*$ (kN) | $A_c$ (cm²) | Seção $b\times h$ (cm) | $\gamma_n$ |
|---|---:|---:|---:|---:|---|---:|
| P1 | 393,2 | 2,5 | 983,1 | 369,4 | 19 × 20 | 1,00 |
| P2 | 989,6 | 2,2 | 2177,2 | 818,1 | 19 × 45 | 1,00 |
| P3 | 416,5 | 2,5 | 1041,2 | 391,2 | 19 × 25 | 1,00 |
| P4 | 767,5 | 2,2 | 1688,5 | 634,4 | 19 × 35 | 1,00 |
| P5 | 1931,5 | 1,8 | 3476,7 | 1306,3 | 19 × 70 | 1,00 |
| P6 | 812,8 | 2,2 | 1788,2 | 671,9 | 19 × 40 | 1,00 |
| P7 | 374,2 | 2,5 | 935,6 | 351,5 | 19 × 20 | 1,00 |
| P8 | 941,8 | 2,2 | 2072,0 | 778,5 | 19 × 45 | 1,00 |
| P9 | 396,3 | 2,5 | 990,9 | 372,3 | 19 × 20 | 1,00 |

### Espessura inicial das lajes

Pelo critério de pré-dimensionamento de lajes maciças bidirecionais, dado pela
Equação (5) da [Aula 02](../aulas/002-lanc-pre-dim.md), e usando inicialmente as distâncias entre eixos da [Tabela 1](#tabela-eixos):

$$
h_{est,L1}=0{,}02\frac{5{,}175+5{,}925}{2}=0{,}1110\text{ m}=11{,}10\text{ cm},
$$

$$
h_{est,L2}=0{,}02\frac{5{,}175+6{,}275}{2}=0{,}1145\text{ m}=11{,}45\text{ cm},
$$

$$
h_{est,L3}=0{,}02\frac{4{,}925+5{,}925}{2}=0{,}1085\text{ m}=10{,}85\text{ cm},
$$

$$
h_{est,L4}=0{,}02\frac{4{,}925+6{,}275}{2}=0{,}1120\text{ m}=11{,}20\text{ cm}.
$$

A [Tabela 4](#tabela-espessura) resume os resultados.

(tabela-espessura)=
**Tabela 4.** Pré-dimensionamento da espessura das lajes maciças bidirecionais.
| Laje | $h_{est}$ (cm) | $h$ inicial adotado (cm) | $\gamma_n$ |
|---|---:|---:|---:|
| L1 | 11,10 | 12 | 1,00 |
| L2 | 11,45 | 12 | 1,00 |
| L3 | 10,85 | 12 | 1,00 |
| L4 | 11,20 | 12 | 1,00 |

Padroniza-se inicialmente $h=12\text{ cm}$ nos pisos e na cobertura. A
escolha atende aos mínimos geométricos apresentados na Aula 02 para lajes
sem balanço. A aprovação da espessura depende das verificações posteriores.
Como não há lajes em balanço, o coeficiente adicional é $\gamma_n=1{,}00$ em
todas as lajes.

### Pré-dimensionamento da altura das vigas

As vigas V1, V2 e V3 são horizontais, com tramos entre eixos de $5{,}925\text{ m}$
e $6{,}275\text{ m}$; as vigas V4, V5 e V6 são verticais, com tramos de
$5{,}175\text{ m}$ e $4{,}925\text{ m}$. Adota-se $h_v=l/12$, com $l$ igual ao maior
tramo entre eixos da viga, e uma única altura por viga, arredondada para
múltiplo de 5 cm:

$$
h_{v,V1-V3}=\frac{6{,}275}{12}=0{,}523\text{ m}\to55\text{ cm},
\qquad
h_{v,V4-V6}=\frac{5{,}175}{12}=0{,}431\text{ m}\to45\text{ cm}.
$$

**Estabilidade lateral.** A largura mínima das vigas segue as Equações (1) e (2)
da Aula 02: $b_{w,min}=\max(l_0/50;\,\beta_{fl}h_v)$, com $\beta_{fl}=0{,}40$ para
seção retangular ou T. Tomando de forma conservadora $l_0$ igual ao maior tramo
entre eixos:

$$
V1\text{ a }V3:\quad b_{w,min}=\max\left(\frac{6{,}275}{50};\,0{,}40\times0{,}55\right)
=\max(0{,}126;\,0{,}220)=22{,}0\text{ cm},
$$

$$
V4\text{ a }V6:\quad b_{w,min}=\max\left(\frac{5{,}175}{50};\,0{,}40\times0{,}45\right)
=\max(0{,}104;\,0{,}180)=18{,}0\text{ cm}.
$$

A condição $b_w\geq l_0/50$ é atendida com $b_w=15\text{ cm}$, mas a condição
$b_w\geq\beta_{fl}h_v$ **não é atendida**: $15\text{ cm}<22{,}0\text{ cm}$ e
$15\text{ cm}<18{,}0\text{ cm}$. A largura de $15\text{ cm}$ só se mantém se a
zona comprimida estiver travada lateralmente pelas lajes; caso contrário, é
preciso aumentar $b_w$ ou reduzir $h_v$ e justificar a escolha.

(tabela-vigas-altura)=
**Tabela 5.** Seções pré-dimensionadas e verificação da largura mínima das vigas.

| Viga | Direção | Maior tramo (m) | $l/12$ (cm) | Seção $b_w\times h_v$ (cm) | $b_{w,min}$ (cm) | $b_w\geq b_{w,min}$ |
|---|---|---:|---:|---|---:|---|
| V1, V2 e V3 | Horizontal | 6,275 | 52,3 | 15 × 55 | 22,0 | Não |
| V4, V5 e V6 | Vertical | 5,175 | 43,1 | 15 × 45 | 18,0 | Não |

### Vãos efetivos das lajes

Na direção estudada, com apoios de $t_1=t_2=0{,}15\text{ m}$:

$$
l_{ef}=l_0+a_1+a_2,
\qquad
a_i=\min(t_i/2;0{,}3h)=\min(0{,}075;0{,}036)=0{,}036\text{ m}.
$$

Como $l_0=l_{eixos}-0{,}15$, resulta

$$
\boxed{l_{ef}=l_{eixos}-0{,}078\text{ m}}.
$$

Por exemplo, para L1:

$$
l_x=5{,}175-0{,}15+2(0{,}036)=5{,}097\text{ m},
\qquad
l_y=5{,}925-0{,}15+2(0{,}036)=5{,}847\text{ m}.
$$

(tabela-vaos)=
**Tabela 6.** Vãos efetivos e relação entre vãos das lajes.

| Laje | $l_x$ (m) | $l_y$ (m) | $\lambda=l_y/l_x$ | Comportamento |
|---|---:|---:|---:|---|
| L1 | 5,097 | 5,847 | 1,1471 | Duas direções |
| L2 | 5,097 | 6,197 | 1,2158 | Duas direções |
| L3 | 4,847 | 5,847 | 1,2063 | Duas direções |
| L4 | 4,847 | 6,197 | 1,2785 | Duas direções |

O eixo $x$ é vertical na planta e o eixo $y$ é horizontal. As quatro lajes
possuem apoio nos quatro lados e $\lambda<2$; não há balanço no desenho.

### Vãos efetivos das vigas

Aplica-se a mesma Equação (3) da Aula 02, com $t_i$ igual à dimensão do pilar
na direção da viga ([Tabela 3](#tabela-pilares-secao)) e
$a_i=\min(t_i/2;\,0{,}3h_v)$. Nas vigas horizontais, $t=19\text{ cm}$ e
$h_v=55\text{ cm}$; nas verticais, $t$ é a dimensão $h$ do pilar e
$h_v=45\text{ cm}$. Por exemplo, para o tramo 1 de V4, entre P1
($t_1=20\text{ cm}$) e P4 ($t_2=35\text{ cm}$):

$$
l_0=5{,}175-\frac{0{,}20}{2}-\frac{0{,}35}{2}=4{,}900\text{ m},
$$

$$
a_1=\min(0{,}100;\,0{,}135)=0{,}100\text{ m},
\qquad
a_2=\min(0{,}175;\,0{,}135)=0{,}135\text{ m},
$$

$$
l_{ef}=4{,}900+0{,}100+0{,}135=5{,}135\text{ m}.
$$

(tabela-vigas-vaos)=
**Tabela 7.** Vãos efetivos dos tramos das vigas.

| Viga | Tramo | Entre eixos (m) | $t_1$ / $t_2$ (cm) | $l_0$ (m) | $a_1$ / $a_2$ (m) | $l_{ef}$ (m) |
|---|---:|---:|---|---:|---|---:|
| V1, V2 e V3 | 1 | 5,925 | 19 / 19 | 5,735 | 0,095 / 0,095 | 5,925 |
| V1, V2 e V3 | 2 | 6,275 | 19 / 19 | 6,085 | 0,095 / 0,095 | 6,275 |
| V4 | 1 | 5,175 | 20 / 35 | 4,900 | 0,100 / 0,135 | 5,135 |
| V4 | 2 | 4,925 | 35 / 20 | 4,650 | 0,135 / 0,100 | 4,885 |
| V5 | 1 | 5,175 | 45 / 70 | 4,600 | 0,135 / 0,135 | 4,870 |
| V5 | 2 | 4,925 | 70 / 45 | 4,350 | 0,135 / 0,135 | 4,620 |
| V6 | 1 | 5,175 | 25 / 40 | 4,850 | 0,125 / 0,135 | 5,110 |
| V6 | 2 | 4,925 | 40 / 20 | 4,625 | 0,135 / 0,100 | 4,860 |

Nas vigas horizontais, como $t/2<0{,}3h_v$ nos dois apoios, $l_{ef}$ coincide
com a distância entre eixos.

### Cargas permanentes dos pavimentos-tipo

Usando os valores das tabelas da Aula 03 e $h$ em metros, a
[Tabela 8](#tabela-carga-tipo) reúne as cargas permanentes:

(tabela-carga-tipo)=
**Tabela 8.** Cargas permanentes dos pavimentos-tipo, sem paredes sobre a laje.

| Parcela | Cálculo | Carga (kN/m²) |
|---|---|---:|
| Peso próprio | $25\times0{,}12$ | 3,000 |
| Piso residencial, 5 cm | Valor da tabela de revestimentos | 1,000 |
| Argamassa inferior, 2,5 cm | $21\times0{,}025$ | 0,525 |
| Forro de gesso em placas com suporte | Valor da tabela de forros | 0,150 |
| **Subtotal, sem paredes sobre a laje** | | **4,675** |

Portanto,

$$
g_{k,tipo}=25h+1{,}675+g_{paredes}
=4{,}675+g_{paredes}\quad(\mathrm{kN/m^2}).
$$

A sobrecarga de dormitório é $q_{k,tipo}=1{,}50\text{ kN/m}^2$.

### Cargas da cobertura

Adotando também na cobertura o acabamento inferior e o forro descritos no
enunciado, obtêm-se as cargas da [Tabela 9](#tabela-carga-cobertura):

(tabela-carga-cobertura)=
**Tabela 9.** Cargas permanentes da cobertura, sem paredes sobre a laje.

| Parcela | Cálculo | Carga (kN/m²) |
|---|---|---:|
| Peso próprio | $25\times0{,}12$ | 3,000 |
| Manta e proteção mecânica, 15 cm, sem piso | Valor da tabela de revestimentos | 2,700 |
| Contrapiso, 4 cm | $21\times0{,}04$ | 0,840 |
| Argamassa inferior, 2,5 cm | $21\times0{,}025$ | 0,525 |
| Forro de gesso em placas com suporte | Valor da tabela de forros | 0,150 |
| **Subtotal, sem paredes sobre a laje** | | **7,215** |

$$
g_{k,cob}=25h+4{,}215+g_{paredes,cob}
=7{,}215+g_{paredes,cob}\quad(\mathrm{kN/m^2}).
$$

A parcela de $2{,}70\text{ kN/m}^2$ já inclui a manta e a proteção mecânica;
não se acrescenta novamente o peso da manta isolada.

Para a ação variável, mantenha $q_{k,cob}$ identificado até definir o caso
normativo da cobertura. O enunciado informa **inclinação exatamente igual a
1%**, enquanto a expressão transcrita na Aula 03 inicia em $1\%<i\leq2\%$.
Não se deve aplicar essa faixa ao limite de 1% sem verificar seu enquadramento
e as condições de drenagem na referência adotada.

### Paredes: distinguir carga na laje e carga na viga

Para bloco cerâmico vazado de 11,5 cm com reboco de 2 cm em cada face, a
tabela de vedação da Aula 03 fornece $2{,}10\text{ kN/m}^2$ de **parede**.
Esse valor já inclui os revestimentos. Para altura livre $H_p$:

$$
g_{parede,lin}=2{,}10H_p\quad(\mathrm{kN/m}).
$$

Uma parede sobre uma viga entra diretamente no carregamento dessa viga.
Uma parede sobre uma laje exige registrar sua posição, altura e comprimento.
Quando a distribuição equivalente por área for compatível com o modelo:

$$
g_{paredes}=\frac{\sum_j2{,}10H_{p,j}L_{p,j}}{A_{laje}}.
$$

Conforme a definição do professor, **todas as paredes estão apoiadas nas
vigas**. Portanto, $g_{paredes}=g_{paredes,cob}=0$ nas lajes deste trabalho.
As cargas lineares das paredes entram na composição das vigas na Entrega 2.
O pé-esquerdo de 3,10 m não é automaticamente a altura livre da alvenaria.

### Combinações para as etapas seguintes

Para o pavimento-tipo sem paredes diretamente sobre a laje:

$$
p_k=4{,}675+1{,}50=6{,}175\text{ kN/m}^2,
$$

$$
p_d=1{,}4(g_k+q_k)=8{,}645\text{ kN/m}^2,
$$

$$
p_{freq}=g_k+0{,}4q_k=5{,}275\text{ kN/m}^2,
\qquad
p_{qp}=g_k+0{,}3q_k=5{,}125\text{ kN/m}^2.
$$

Para a cobertura, empregam-se as mesmas expressões com $g_{k,cob}$ e
$q_{k,cob}$. Os valores globais de 10 e 7 kN/m² do enunciado são estimativas
para o pré-dimensionamento dos pilares; não substituem este levantamento.

### Erros frequentes nesta entrega

- Usar 585 como vão em metros ou empregar 14 cm para a largura das vigas.
- Confundir distância entre eixos, vão livre e vão efetivo.
- Usar $h$ em centímetros na expressão $25h$ que exige metros.
- Contar duas vezes o reboco ou a manta, já incluídos nos valores tabelados.
- Distribuir na laje uma parede que foi contabilizada diretamente na viga.
- Tratar a espessura de pré-dimensionamento como resultado definitivo.
