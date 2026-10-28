## Entrega 1: Pré-dimensionamento, vãos efetivos e cargas nas lajes

### Distâncias entre eixos

As cotas do desenho (510, 585, 620 e 485 cm) são medidas entre faces das
vigas. Como as vigas que contornam os painéis têm $b_w=15\text{ cm}$, cada
cota recebe $7{,}5\text{ cm}$ de cada lado, isto é, somam-se $15\text{ cm}$
para obter a distância entre eixos, usada na [Tabela 1](#tabela-eixos). Por
exemplo, para a cota de $510\text{ cm}$ transforma-se em:
$5{,}10+2\times0{,}075=5{,}25\text{ m}$.

(tabela-eixos)=
**Tabela 1.** Distâncias entre eixos das lajes do pavimento padrão.

| Laje | Posição | Vigas de contorno | Dimensões entre eixos (m) |
|---|---|---|---|
| L1 | Superior esquerda | V1, V2, V4 e V5 | 5,250 × 6,000 |
| L2 | Superior direita | V1, V2, V5 e V6 | 5,250 × 6,350 |
| L3 | Inferior esquerda | V2, V3, V4 e V5 | 5,000 × 6,000 |
| L4 | Inferior direita | V2, V3, V5 e V6 | 5,000 × 6,350 |

### Pré-dimensionamento dos pilares

Toma-se como referência o nível do térreo, em que cada pilar
sustenta todos os pavimentos acima: cinco pavimentos-tipo e a cobertura, logo
$n_{tipo}=5$ e $n_{cob}=1$. O pavimento térreo não entra na contabilidade pois ele não tem um subsistema horizontal de lajes. Para cada pilar, a área de influência $A_i$ segue as
faixas descritas na [Figura 4](../aulas/002-lanc-pre-dim.md#figura4) da [Aula 02](../aulas/002-lanc-pre-dim.md), com os
vãos entre eixos da [Tabela 1](#tabela-eixos). 

Em planta, todos os pilares estão deitados: a maior dimensão $h$ fica na
direção horizontal e a menor dimensão $b$ na direção vertical. Pela [Aula 02](../aulas/002-lanc-pre-dim.md), a
divisão das faixas de influência depende dessa orientação:

- pilares de extremidade ou de canto: $0{,}45\,l$ na direção de $b$ (vertical) e
  $0{,}50\,l$ na direção de $h$ (horizontal), tomando-se $l$ apenas do lado
  interno, pois não há vão do lado externo;
- pilares que têm vão dos dois lados em uma direção: usa-se o complemento de
  cada faixa vizinha, isto é, $0{,}50\,l$ de cada lado na horizontal (complemento
  de $0{,}50$) e $0{,}55\,l$ de cada lado na vertical (complemento de $0{,}45$).

Assim, para P1 (canto) e P5 (intermediário):

$$
A_{P1}=(0{,}50\times6{,}000)(0{,}45\times5{,}250)=3{,}000\times2{,}363=7{,}088\text{ m}^2,
$$

$$
A_{P5}=0{,}50(6{,}000+6{,}350)\times0{,}55(5{,}250+5{,}000)=6{,}175\times5{,}638=34{,}812\text{ m}^2.
$$

A [Tabela 2](#tabela-pilares-areas) apresenta os detalhes da área de influência de cada um dos pilares.

(tabela-pilares-areas)=
**Tabela 2.** Áreas de influência dos pilares.

| Pilar | Posição | Faixa horizontal (m) | Faixa vertical (m) | $A_i$ (m²) |
|---|---|---:|---:|---:|
| P1 | Canto | 3,000 | 2,363 | 7,088 |
| P2 | Extremidade | 6,175 | 2,363 | 14,588 |
| P3 | Canto | 3,175 | 2,363 | 7,501 |
| P4 | Extremidade | 3,000 | 5,638 | 16,913 |
| P5 | Intermediário | 6,175 | 5,638 | 34,812 |
| P6 | Extremidade | 3,175 | 5,638 | 17,899 |
| P7 | Canto | 3,000 | 2,250 | 6,750 |
| P8 | Extremidade | 6,175 | 2,250 | 13,894 |
| P9 | Canto | 3,175 | 2,250 | 7,144 |

Com as cargas de 10 e 7 kN/m² do enunciado, a carga característica e a carga de
cálculo (Equações (17) e (18) da [Aula 02](../aulas/002-lanc-pre-dim.md)) são:

$$
N_k^*=A_i(10\times5+7\times1)=57A_i,\qquad N_d^*=\alpha N_k^*,
$$

com $\alpha=2{,}5$ (canto), $2{,}2$ (extremidade) e $1{,}8$ (intermediário). Para
o concreto C30 e o aço CA-50, com as unidades em kN e m,
$f_{cd}=30000/1{,}4=21428{,}6\text{ kN/m}^2$, $\rho=0{,}02$ e
$\sigma_s=420\,000\text{ kN/m}^2$ (420 MPa), a Equação (15) da
[Aula 02](../aulas/002-lanc-pre-dim.md) fica:

$$
A_c=\frac{N_d^*}{0{,}85\times21428{,}6+0{,}02\times420000}
=\frac{N_d^*}{26614{,}3}\quad(\text{m}^2,\ N_d^*\text{ em kN}).
$$

Para P1 e P5:

$$
N_{d,P1}^*=2{,}5\times57\times7{,}088=1010{,}0\text{ kN},
\qquad
A_{c,P1}=\frac{1010{,}0}{26614{,}3}=0{,}0379\text{ m}^2,
$$

$$
N_{d,P5}^*=1{,}8\times57\times34{,}812=3571{,}7\text{ kN},
\qquad
A_{c,P5}=\frac{3571{,}7}{26614{,}3}=0{,}1342\text{ m}^2.
$$

Adota-se a menor dimensão $b=0{,}19\text{ m}$, a menor dimensão usual da NBR 6118,
na direção vertical da planta, e a maior dimensão $h$ na direção horizontal,
múltipla de $0{,}05\text{ m}$, de modo que $0{,}19h\geq A_c$ e
$0{,}19h\geq0{,}036\text{ m}^2$. Para P1,
$h=0{,}0379/0{,}19=0{,}199\to0{,}20\text{ m}$; para P5,
$h=0{,}1342/0{,}19=0{,}706\to0{,}75\text{ m}$.
Como $b\geq19\text{ cm}$, $\gamma_n=1{,}00$ em todos os pilares. A
[Tabela 3](#tabela-pilares-secao) reúne as cargas, as áreas de concreto e as
seções adotadas para os nove pilares.

(tabela-pilares-secao)=
**Tabela 3.** Cargas e seções pré-dimensionadas dos pilares.

| Pilar | $N_k^*$ (kN) | $\alpha$ | $N_d^*$ (kN) | $A_c$ (m²) | Seção $b\times h$ (cm) | $\gamma_n$ |
|---|---:|---:|---:|---:|---|---:|
| P1 | 404,0 | 2,5 | 1010,0 | 0,0379 | 19 × 20 | 1,00 |
| P2 | 831,5 | 2,2 | 1829,4 | 0,0687 | 19 × 40 | 1,00 |
| P3 | 427,6 | 2,5 | 1068,9 | 0,0402 | 19 × 25 | 1,00 |
| P4 | 964,0 | 2,2 | 2120,8 | 0,0797 | 19 × 45 | 1,00 |
| P5 | 1984,3 | 1,8 | 3571,7 | 0,1342 | 19 × 75 | 1,00 |
| P6 | 1020,2 | 2,2 | 2244,5 | 0,0843 | 19 × 45 | 1,00 |
| P7 | 384,8 | 2,5 | 961,9 | 0,0361 | 19 × 20 | 1,00 |
| P8 | 791,9 | 2,2 | 1742,3 | 0,0655 | 19 × 35 | 1,00 |
| P9 | 407,2 | 2,5 | 1018,0 | 0,0383 | 19 × 25 | 1,00 |

### Espessura inicial das lajes

Pelo critério de pré-dimensionamento de lajes maciças bidirecionais, dado pela
Equação (5) da [Aula 02](../aulas/002-lanc-pre-dim.md), e usando inicialmente as distâncias entre eixos da [Tabela 1](#tabela-eixos):

$$
h_{est,L1}=0{,}02\frac{5{,}250+6{,}000}{2}=0{,}1125\text{ m}=11{,}25\text{ cm},
$$

$$
h_{est,L2}=0{,}02\frac{5{,}250+6{,}350}{2}=0{,}1160\text{ m}=11{,}60\text{ cm},
$$

$$
h_{est,L3}=0{,}02\frac{5{,}000+6{,}000}{2}=0{,}1100\text{ m}=11{,}00\text{ cm},
$$

$$
h_{est,L4}=0{,}02\frac{5{,}000+6{,}350}{2}=0{,}1135\text{ m}=11{,}35\text{ cm}.
$$

A [Tabela 4](#tabela-espessura) resume os resultados.

(tabela-espessura)=
**Tabela 4.** Pré-dimensionamento da espessura das lajes maciças bidirecionais.

| Laje | $h_{est}$ (cm) | $h$ inicial adotado (cm) | $\gamma_n$ |
|---|---:|---:|---:|
| L1 | 11,25 | 12 | 1,00 |
| L2 | 11,60 | 12 | 1,00 |
| L3 | 11,00 | 12 | 1,00 |
| L4 | 11,35 | 12 | 1,00 |

Padroniza-se inicialmente $h=12\text{ cm}$ nos pisos e na cobertura. A
escolha atende aos mínimos geométricos apresentados na [Aula 02](../aulas/002-lanc-pre-dim.md) para lajes
sem balanço. A aprovação da espessura depende das verificações posteriores.
Como não há lajes em balanço, o coeficiente adicional é $\gamma_n=1{,}00$ em
todas as lajes.

### Pré-dimensionamento da altura das vigas

As vigas V1, V2 e V3 são horizontais, com tramos entre eixos de $6{,}000\text{ m}$
e $6{,}350\text{ m}$; as vigas V4, V5 e V6 são verticais, com tramos de
$5{,}250\text{ m}$ e $5{,}000\text{ m}$. Adota-se $h_v=l/12$, com $l$ igual ao maior
tramo entre eixos da viga, e uma única altura por viga, arredondada para
múltiplo de 5 cm:

$$
h_{v,V1-V3}=\frac{6{,}350}{12}=0{,}529\text{ m}\to55\text{ cm},
\qquad
h_{v,V4-V6}=\frac{5{,}250}{12}=0{,}438\text{ m}\to45\text{ cm}.
$$

As vigas estão travadas lateralmente pelas lajes; por isso, nesta etapa não se
verifica a estabilidade lateral e a largura permanece $b_w=15\text{ cm}$, sendo
pré-dimensionada apenas a altura. A [Tabela 5](#tabela-vigas-altura) resume as
seções adotadas.

(tabela-vigas-altura)=
**Tabela 5.** Seções pré-dimensionadas das vigas.

| Viga | Direção | Maior tramo (m) | $l/12$ (cm) | Seção $b_w\times h_v$ (cm) |
|---|---|---:|---:|---|
| V1, V2 e V3 | Horizontal | 6,350 | 52,9 | 15 × 55 |
| V4, V5 e V6 | Vertical | 5,250 | 43,8 | 15 × 45 |

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
l_x=5{,}250-0{,}15+2(0{,}036)=5{,}172\text{ m},
\qquad
l_y=6{,}000-0{,}15+2(0{,}036)=5{,}922\text{ m}.
$$

A [Tabela 6](#tabela-vaos) apresenta os vãos efetivos das quatro lajes e a relação entre eles.

(tabela-vaos)=
**Tabela 6.** Vãos efetivos e relação entre vãos das lajes.

| Laje | $l_x$ (m) | $l_y$ (m) | $\lambda=l_y/l_x$ | Comportamento |
|---|---:|---:|---:|---|
| L1 | 5,172 | 5,922 | 1,1450 | Duas direções |
| L2 | 5,172 | 6,272 | 1,2127 | Duas direções |
| L3 | 4,922 | 5,922 | 1,2032 | Duas direções |
| L4 | 4,922 | 6,272 | 1,2743 | Duas direções |

O eixo $x$ é vertical na planta e o eixo $y$ é horizontal. As quatro lajes
possuem apoio nos quatro lados e $\lambda<2$; não há balanço no desenho.

### Vãos efetivos das vigas

Aplica-se a mesma Equação (3) da [Aula 02](../aulas/002-lanc-pre-dim.md), com $t_i$ igual à dimensão do pilar
na direção da viga ([Tabela 3](#tabela-pilares-secao)) e
$a_i=\min(t_i/2;\,0{,}3h_v)$. Como os pilares estão deitados, nas vigas
horizontais $t$ é a dimensão $h$ do pilar e $h_v=55\text{ cm}$; nas verticais,
$t=19\text{ cm}$ e $h_v=45\text{ cm}$. Por exemplo, para o tramo 1 de V1, entre P1
($t_1=20\text{ cm}$) e P2 ($t_2=40\text{ cm}$):

$$
l_0=6{,}000-\frac{0{,}20}{2}-\frac{0{,}40}{2}=5{,}700\text{ m},
$$

$$
a_1=\min(0{,}100;\,0{,}165)=0{,}100\text{ m},
\qquad
a_2=\min(0{,}200;\,0{,}165)=0{,}165\text{ m},
$$

$$
l_{ef}=5{,}700+0{,}100+0{,}165=5{,}965\text{ m}.
$$

A [Tabela 7](#tabela-vigas-vaos) apresenta os vãos efetivos de todos os tramos das vigas.

(tabela-vigas-vaos)=
**Tabela 7.** Vãos efetivos dos tramos das vigas.

| Viga | Tramo | Entre eixos (m) | $t_1$ / $t_2$ (cm) | $l_0$ (m) | $a_1$ / $a_2$ (m) | $l_{ef}$ (m) |
|---|---:|---:|---|---:|---|---:|
| V1 | 1 | 6,000 | 20 / 40 | 5,700 | 0,100 / 0,165 | 5,965 |
| V1 | 2 | 6,350 | 40 / 25 | 6,025 | 0,165 / 0,125 | 6,315 |
| V2 | 1 | 6,000 | 45 / 75 | 5,400 | 0,165 / 0,165 | 5,730 |
| V2 | 2 | 6,350 | 75 / 45 | 5,750 | 0,165 / 0,165 | 6,080 |
| V3 | 1 | 6,000 | 20 / 35 | 5,725 | 0,100 / 0,165 | 5,990 |
| V3 | 2 | 6,350 | 35 / 25 | 6,050 | 0,165 / 0,125 | 6,340 |
| V4, V5 e V6 | 1 | 5,250 | 19 / 19 | 5,060 | 0,095 / 0,095 | 5,250 |
| V4, V5 e V6 | 2 | 5,000 | 19 / 19 | 4,810 | 0,095 / 0,095 | 5,000 |

Nas vigas verticais, como $t/2<0{,}3h_v$ nos dois apoios, $l_{ef}$ coincide
com a distância entre eixos.

### Cargas permanentes dos pavimentos-tipo

Usando os valores das tabelas da [Aula 03](../aulas/003-carregamentos.md) e $h$ em metros, a
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
1%**, enquanto a expressão transcrita na [Aula 03](../aulas/003-carregamentos.md) inicia em $1\%<i\leq2\%$.
Não se deve aplicar essa faixa ao limite de 1% sem verificar seu enquadramento
e as condições de drenagem na referência adotada.

### Paredes: distinguir carga na laje e carga na viga

Para bloco cerâmico vazado de 11,5 cm com reboco de 2 cm em cada face, a
tabela de vedação da [Aula 03](../aulas/003-carregamentos.md) fornece $2{,}10\text{ kN/m}^2$ de **parede**.
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
