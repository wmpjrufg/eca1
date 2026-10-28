## Entrega 1 – Pré-dimensionamento, vãos efetivos e cargas nas lajes

### Distâncias entre eixos

As cotas do desenho (510, 585, 620 e 485 cm) são medidas entre faces das
vigas. Como as vigas que contornam os painéis têm $b_w=15\text{ cm}$, cada
cota recebe $7{,}5\text{ cm}$ de cada lado, isto é, somam-se $15\text{ cm}$
para obter a distância entre eixos, usada na [Tabela 1](#tabela-eixos). Por
exemplo, para a cota de $510\text{ cm}$ transforma-se em
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
sustenta todos os pavimentos acima, sendo cinco pavimentos-tipo e a cobertura, logo
$n_{tipo}=5$ e $n_{cob}=1$. O pavimento térreo não entra na contabilidade pois ele não tem um subsistema horizontal de lajes. Para cada pilar, a área de influência $A_i$ segue as
faixas descritas na [Figura 4](../aulas/002-lanc-pre-dim.md#figura4) da [Aula 02](../aulas/002-lanc-pre-dim.md), com os
vãos entre eixos da [Tabela 1](#tabela-eixos). 

Em planta, todos os pilares estão deitados, com a maior dimensão $h$ na
direção horizontal e a menor dimensão $b$ na direção vertical. Pela [Aula 02](../aulas/002-lanc-pre-dim.md), a
divisão das faixas de influência depende dessa orientação, como descrito a seguir.

- Nos pilares de extremidade ou de canto, adota-se $0{,}45\,l$ na direção de $b$
  (vertical) e $0{,}50\,l$ na direção de $h$ (horizontal), tomando-se $l$ apenas
  do lado interno, pois não há vão do lado externo.
- Nos pilares que têm vão dos dois lados em uma direção, usa-se o complemento de
  cada faixa vizinha, isto é, $0{,}50\,l$ de cada lado na horizontal (complemento
  de $0{,}50$) e $0{,}55\,l$ de cada lado na vertical (complemento de $0{,}45$).

Assim, as áreas de influência de P1 (canto) e P5 (intermediário) valem

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
cálculo (Equações (17) e (18) da [Aula 02](../aulas/002-lanc-pre-dim.md)) resultam em

$$
N_k^*=A_i(10\times5+7\times1)=57A_i,\qquad N_d^*=\alpha N_k^*,
$$

com $\alpha=2{,}5$ (canto), $2{,}2$ (extremidade) e $1{,}8$ (intermediário). Para
o concreto C30 e o aço CA-50, com as unidades em kN e m,
$f_{cd}=30000/1{,}4=21428{,}6\text{ kN/m}^2$, $\rho=0{,}02$ e
$\sigma_s=420\,000\text{ kN/m}^2$ (420 MPa), a Equação (15) da
[Aula 02](../aulas/002-lanc-pre-dim.md) resulta em

$$
A_c=\frac{N_d^*}{0{,}85\times21428{,}6+0{,}02\times420000}
=\frac{N_d^*}{26614{,}3}\quad(\text{m}^2,\ N_d^*\text{ em kN}).
$$

Para P1 e P5, obtém-se

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
$h=0{,}0379/0{,}19=0{,}199\to0{,}20\text{ m}$ e, para P5,
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

### Padronização das seções dos pilares

As seções da [Tabela 3](#tabela-pilares-secao) são mínimas, e a planta é
praticamente simétrica, mas o cálculo resultou em seis seções diferentes
(19 × 20, 25, 35, 40, 45 e 75 cm). Cada seção distinta exige uma fôrma própria e
dificulta a execução e o reaproveitamento das fôrmas entre pavimentos. Por isso,
agrupam-se os pilares pela posição (canto, extremidade e intermediário) e adota-se
a maior seção calculada de cada grupo. A [Tabela 4](#tabela-padronizacao)
compara as seções calculadas e as padronizadas.

(tabela-padronizacao)=
**Tabela 4.** Padronização das seções dos pilares.

| Pilar | Grupo | $A_{c,calc}$ (m²) | Seção calculada $b\times h$ (cm) | Seção padronizada $b\times h$ (cm) | $A_{c,adot}$ (m²) | Folga (%) |
|---|---|---:|---|---|---:|---:|
| P1 | Canto | 0,0379 | 19 × 20 | 19 × 25 | 0,0475 | 25 |
| P3 | Canto | 0,0402 | 19 × 25 | 19 × 25 | 0,0475 | 18 |
| P7 | Canto | 0,0361 | 19 × 20 | 19 × 25 | 0,0475 | 31 |
| P9 | Canto | 0,0383 | 19 × 25 | 19 × 25 | 0,0475 | 24 |
| P2 | Extremidade | 0,0687 | 19 × 40 | 19 × 45 | 0,0855 | 24 |
| P4 | Extremidade | 0,0797 | 19 × 45 | 19 × 45 | 0,0855 | 7 |
| P6 | Extremidade | 0,0843 | 19 × 45 | 19 × 45 | 0,0855 | 1 |
| P8 | Extremidade | 0,0655 | 19 × 35 | 19 × 45 | 0,0855 | 31 |
| P5 | Intermediário | 0,1342 | 19 × 75 | 19 × 75 | 0,1425 | 6 |

A [Tabela 4](#tabela-padronizacao) mostra que três seções (19 × 25, 19 × 45 e
19 × 75) atendem a todos os pilares, com folga de 1 % a 31 % em relação à área
necessária.

### Espessura inicial das lajes

Pelo critério de pré-dimensionamento de lajes maciças bidirecionais, dado pela
Equação (5) da [Aula 02](../aulas/002-lanc-pre-dim.md), e usando inicialmente as distâncias entre eixos da [Tabela 1](#tabela-eixos), resulta em

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

A [Tabela 5](#tabela-espessura) resume os resultados.

(tabela-espessura)=
**Tabela 5.** Pré-dimensionamento da espessura das lajes maciças bidirecionais.

| Laje | $h_{est}$ (cm) | $h$ inicial adotado (cm) | $\gamma_n$ |
|---|---:|---:|---:|
| L1 | 11,25 | 12 | 1,00 |
| L2 | 11,60 | 12 | 1,00 |
| L3 | 11,00 | 12 | 1,00 |
| L4 | 11,35 | 12 | 1,00 |

Padroniza-se inicialmente $h=12\text{ cm}$ nos pisos e na cobertura. A
escolha atende aos mínimos geométricos apresentados na [Aula 02](../aulas/002-lanc-pre-dim.md) para lajes
sem balanço.
Como não há lajes em balanço, o coeficiente adicional é $\gamma_n=1{,}00$ em
todas as lajes.

### Pré-dimensionamento da altura das vigas

As vigas V1, V2 e V3 são horizontais, com tramos entre eixos de $6{,}000\text{ m}$
e $6{,}350\text{ m}$ e as vigas V4, V5 e V6 são verticais, com tramos de
$5{,}250\text{ m}$ e $5{,}000\text{ m}$. Adota-se $h_v=l/12$, com $l$ igual ao maior
tramo entre eixos da viga, e uma única altura por viga, arredondada para
múltiplo de 5 cm, o que leva a

$$
h_{v,V1-V3}=\frac{6{,}350}{12}=0{,}529\text{ m}\to55\text{ cm},
\qquad
h_{v,V4-V6}=\frac{5{,}250}{12}=0{,}438\text{ m}\to45\text{ cm}.
$$

As vigas estão travadas lateralmente pelas lajes e, por isso, nesta etapa não se
verifica a estabilidade lateral e a largura permanece $b_w=15\text{ cm}$, sendo
pré-dimensionada apenas a altura. A [Tabela 6](#tabela-vigas-altura) resume as
seções adotadas.

(tabela-vigas-altura)=
**Tabela 6.** Seções pré-dimensionadas das vigas.

| Viga | Direção | Maior tramo (m) | $l/12$ (cm) | Seção $b_w\times h_v$ (cm) |
|---|---|---:|---:|---|
| V1, V2 e V3 | Horizontal | 6,350 | 52,9 | 15 × 55 |
| V4, V5 e V6 | Vertical | 5,250 | 43,8 | 15 × 45 |

### Vãos efetivos das lajes

Na direção estudada, com apoios de $t_1=t_2=0{,}15\text{ m}$ e laje de
$h=0{,}12\text{ m}$, vale

$$
l_{ef}=l_0+a_1+a_2,
\qquad
a_i=\min(t_i/2;\,0{,}3h).
$$

Os dois termos do mínimo valem

$$
\frac{t_i}{2}=\frac{0{,}15}{2}=0{,}075\text{ m},
\qquad
0{,}3h=0{,}3\times0{,}12=0{,}036\text{ m}.
$$

Logo,

$$
a_i=\min(0{,}075;\,0{,}036)=0{,}036\text{ m}.
$$

$l_0=l_{eixos}-0{,}15$ represneta o vão entre faces. Por exemplo, para L1 resulta em:

$$
l_x=5{,}250-0{,}15+2(0{,}036)=5{,}172\text{ m},
\qquad
l_y=6{,}000-0{,}15+2(0{,}036)=5{,}922\text{ m}.
$$

A [Tabela 7](#tabela-vaos) apresenta os vãos efetivos das quatro lajes e a relação entre eles.

(tabela-vaos)=
**Tabela 7.** Vãos efetivos e relação entre vãos das lajes.

| Laje | $l_x$ (m) | $l_y$ (m) | $\lambda=l_y/l_x$ | Comportamento |
|---|---:|---:|---:|---|
| L1 | 5,172 | 5,922 | 1,1450 | Duas direções |
| L2 | 5,172 | 6,272 | 1,2127 | Duas direções |
| L3 | 4,922 | 5,922 | 1,2032 | Duas direções |
| L4 | 4,922 | 6,272 | 1,2743 | Duas direções |

O eixo $x$ é vertical na planta e o eixo $y$ é horizontal. As quatro lajes
possuem apoio nos quatro lados e $\lambda<2$, e não há balanço no desenho. Lembrando que esse padrão só vale para este projeto.

### Vãos efetivos das vigas

Aplica-se a mesma Equação (3) da [Aula 02](../aulas/002-lanc-pre-dim.md), com $t_i$ igual à dimensão do pilar
na direção da viga, tomada nas seções padronizadas da
[Tabela 4](#tabela-padronizacao), e
$a_i=\min(t_i/2;\,0{,}3h_v)$. Como os pilares estão deitados, nas vigas
horizontais $t$ é a dimensão $h$ do pilar e $h_v=55\text{ cm}$ e nas verticais,
$t=19\text{ cm}$ e $h_v=45\text{ cm}$. Por exemplo, para o tramo 1 de V1, entre P1
($t_1=25\text{ cm}$) e P2 ($t_2=45\text{ cm}$), tem-se

$$
l_0=6{,}000-\frac{0{,}25}{2}-\frac{0{,}45}{2}=5{,}650\text{ m},
$$

$$
a_1=\min(0{,}125;\,0{,}165)=0{,}125\text{ m},
\qquad
a_2=\min(0{,}225;\,0{,}165)=0{,}165\text{ m},
$$

$$
l_{ef}=5{,}650+0{,}125+0{,}165=5{,}940\text{ m}.
$$

A [Tabela 8](#tabela-vigas-vaos) apresenta os vãos efetivos de todos os tramos das vigas.

(tabela-vigas-vaos)=
**Tabela 8.** Vãos efetivos dos tramos das vigas.

| Viga | Tramo | Entre eixos (m) | $t_1$ / $t_2$ (cm) | $l_0$ (m) | $a_1$ / $a_2$ (m) | $l_{ef}$ (m) |
|---|---:|---:|---|---:|---|---:|
| V1 e V3 | 1 | 6,000 | 25 / 45 | 5,650 | 0,125 / 0,165 | 5,940 |
| V1 e V3 | 2 | 6,350 | 45 / 25 | 6,000 | 0,165 / 0,125 | 6,290 |
| V2 | 1 | 6,000 | 45 / 75 | 5,400 | 0,165 / 0,165 | 5,730 |
| V2 | 2 | 6,350 | 75 / 45 | 5,750 | 0,165 / 0,165 | 6,080 |
| V4, V5 e V6 | 1 | 5,250 | 19 / 19 | 5,060 | 0,095 / 0,095 | 5,250 |
| V4, V5 e V6 | 2 | 5,000 | 19 / 19 | 4,810 | 0,095 / 0,095 | 5,000 |

Como os pilares de canto e de extremidade foram padronizados, V1 e V3 têm os
mesmos vãos. Nas vigas verticais, como $t/2<0{,}3h_v$ nos dois apoios, $l_{ef}$ coincide
com a distância entre eixos.

### Cargas permanentes dos pavimentos-tipo

Usando os valores das tabelas da [Aula 03](../aulas/003-carregamentos.md) e $h$ em metros, a
[Tabela 9](#tabela-carga-tipo) reúne as cargas permanentes.

(tabela-carga-tipo)=
**Tabela 9.** Cargas permanentes dos pavimentos-tipo, sem paredes sobre a laje.

| Parcela | Cálculo | Carga (kN/m²) |
|---|---|---:|
| Peso próprio | $25\times0{,}12$ | 3,000 |
| Piso residencial, 5 cm | Valor da tabela de revestimentos, que já inclui a argamassa | 1,000 |
| Forro de gesso em placas com suporte | Valor da tabela de forros | 0,150 |
| **Subtotal, sem paredes sobre a laje** | | **4,150** |

Portanto,

$$
g_{k,tipo}=25h+1{,}150+g_{paredes,tipo}
=4{,}150+g_{paredes,tipo}\quad(\mathrm{kN/m^2}).
$$

A sobrecarga de dormitório é $q_{k,tipo}=1{,}50\text{ kN/m}^2$.

### Cargas da cobertura

Adotando também na cobertura o forro descrito no enunciado, obtêm-se as cargas da [Tabela 10](#tabela-carga-cobertura).

(tabela-carga-cobertura)=
**Tabela 10.** Cargas permanentes da cobertura, sem paredes sobre a laje.

| Parcela | Cálculo | Carga (kN/m²) |
|---|---|---:|
| Peso próprio | $25\times0{,}12$ | 3,000 |
| Manta e proteção mecânica, 15 cm, sem piso | Valor da tabela de revestimentos | 2,700 |
| Contrapiso, 4 cm | $21\times0{,}04$ | 0,840 |
| Forro de gesso em placas com suporte | Valor da tabela de forros | 0,150 |
| **Subtotal, sem paredes sobre a laje** | | **6,690** |

$$
g_{k,cob}=25h+3{,}690+g_{paredes,cob}
=6{,}690+g_{paredes,cob}\quad(\mathrm{kN/m^2}).
$$

A parcela de $2{,}70\text{ kN/m}^2$ já inclui a manta e a proteção mecânica, e
não se acrescenta novamente o peso da manta isolada.

Para a ação variável, o enunciado informa inclinação da cobertura de 1%, que
se enquadra na faixa $i\leq2\%$ das Equações (1) e (2) da
[Aula 03](../aulas/003-carregamentos.md), com $\alpha=1{,}00$. Logo,

$$
q_{k,cob}=0{,}50\times1{,}00=0{,}50\text{ kN/m}^2.
$$

### Paredes sobre laje e sobre viga

Para bloco cerâmico vazado de 11,5 cm com reboco de 2 cm em cada face, a
tabela de vedação da [Aula 03](../aulas/003-carregamentos.md) fornece $2{,}10\text{ kN/m}^2$ de **parede**.
Esse valor já inclui os revestimentos. Para altura livre $H_p$, a carga linear é

$$
g_{parede,lin}=2{,}10H_p\quad(\mathrm{kN/m}).
$$

Uma parede sobre uma viga entra diretamente no carregamento dessa viga.
Uma parede sobre uma laje exige registrar sua posição, altura e comprimento.
Quando a distribuição equivalente por área for compatível com o modelo, a carga por área é

$$
g_{paredes}=\frac{\sum_j2{,}10H_{p,j}L_{p,j}}{A_{laje}}.
$$

Conforme o enunciado, a alvenaria dos pavimentos-tipo é de bloco cerâmico vazado
de $11{,}5\text{ cm}$ com reboco de $2\text{ cm}$ em cada face, o que dá
$2{,}10\text{ kN/m}^2$ de parede, e se divide em dois casos. O pé-esquerdo de
3,10 m não é automaticamente a altura livre da alvenaria.

**Alvenaria sobre as vigas dos pavimentos-tipo.** Todas as vigas (V1 a V6)
recebem parede de $2{,}80\text{ m}$ de altura, e a carga linear em cada uma é

$$
g_{parede,viga,tipo}=2{,}10\times2{,}80=5{,}88\text{ kN/m}.
$$

Essa carga entra na composição das vigas na Entrega 2 e não é lançada nas lajes.

**Alvenaria sobre a laje L1.** O enunciado indica um perímetro de 21,90 m de alvenaria apoiado diretamente em L1, com $3{,}00\text{ m}$ de altura.
Tomando as dimensões entre faces das vigas ($5{,}10\text{ m}$ e $5{,}85\text{ m}$),
o comprimento da parede, a carga linear e a carga total são

$$
L_p=21{,}90\text{ m},
\qquad
g_{parede,lin}=2{,}10\times3{,}00=6{,}30\text{ kN/m},
$$

$$
P_{parede}=6{,}30\times21{,}90=137{,}97\text{ kN}.
$$

Distribuindo essa carga na área livre da laje, $A_{L1}=5{,}10\times5{,}85=29{,}835\text{ m}^2$,
obtém-se a carga equivalente por área

$$
g_{paredes,tipo}=\frac{137{,}97}{29{,}835}=4{,}624\text{ kN/m}^2.
$$

Assim, a carga permanente final de L1 nos pavimentos-tipo é

$$
g_{k,tipo,L1}=4{,}150+4{,}624=8{,}774\text{ kN/m}^2.
$$

Nas lajes L2, L3 e L4 não há parede apoiada diretamente, logo
$g_{paredes,tipo}=0$ e $g_{k,tipo}=4{,}150\text{ kN/m}^2$. Na cobertura, também
$g_{paredes,cob}=0$ nas lajes.

**Platibanda da cobertura.** As vigas de contorno da cobertura (V1, V3, V4 e V6)
recebem uma platibanda de $1{,}10\text{ m}$ de altura, em bloco cerâmico vazado
de $14\text{ cm}$ com reboco de $2\text{ cm}$ em cada face. Pela Tabela 3 da
[Aula 03](../aulas/003-carregamentos.md), essa parede pesa $1{,}90\text{ kN/m}^2$,
e a carga linear sobre cada viga de contorno é

$$
g_{platibanda}=1{,}90\times1{,}10=2{,}09\text{ kN/m}.
$$

As vigas internas V2 e V5 não recebem alvenaria na cobertura. Essa carga entra
na composição das vigas de cobertura na Entrega 2.

### Resumo das cargas nas lajes

A [Tabela 11](#tabela-cargas-lajes) reúne as cargas características permanentes ($g_k$) e variáveis ($q_k$) por área que atuam nas lajes, já incluindo a alvenaria apoiada em L1 nos pavimentos-tipo.

Nesta etapa (Entrega 1), não se realizam combinações de ações: as cargas $g_k$ e $q_k$ são mantidas separadas para que os esforços solicitantes devidos a cada ação possam ser determinados individualmente e combinados posteriormente nas etapas seguintes, conforme a necessidade de cada verificação (ELU e ELS).

Os valores globais de 10 e 7 kN/m² do enunciado são estimativas
para o pré-dimensionamento dos pilares e não substituem este levantamento.

(tabela-cargas-lajes)=
**Tabela 11.** Cargas características nas lajes (kN/m²).

| Laje | Pavimento | $g_k$ (kN/m²) | $q_k$ (kN/m²) |
|---|---|---:|---:|
| L1 | Tipo | 8,774 | 1,50 |
| L2, L3 e L4 | Tipo | 4,150 | 1,50 |
| L1, L2, L3 e L4 | Cobertura | 6,690 | 0,50 |

### Resumo das cargas nas vigas

A [Tabela 12](#tabela-cargas-vigas) apresenta as cargas lineares permanentes por
tramo, com os vãos efetivos da [Tabela 8](#tabela-vigas-vaos). O peso próprio é
$25b_wh_v$, com $b_w=0{,}15\text{ m}$, o que dá $2{,}063\text{ kN/m}$ nas vigas de
$55\text{ cm}$ (V1 a V3) e $1{,}688\text{ kN/m}$ nas vigas de $45\text{ cm}$ (V4 a V6).
A alvenaria é de $5{,}88\text{ kN/m}$ nos pavimentos-tipo e a platibanda é de
$2{,}09\text{ kN/m}$ na cobertura, apenas em V1, V3, V4 e V6. As reações das lajes sobre as vigas
serão somadas a estes valores na Entrega 2.

(tabela-cargas-vigas)=
**Tabela 12.** Cargas lineares permanentes nas vigas por tramo (kN/m), sem as reações das lajes.

| Viga | Tramo | $l_{ef}$ (m) | Peso próprio | Alvenaria (tipo) | Total (tipo) | Platibanda (cobertura) | Total (cobertura) |
|---|---:|---:|---:|---:|---:|---:|---:|
| V1 e V3 | 1 | 5,940 | 2,063 | 5,880 | 7,943 | 2,090 | 4,153 |
| V1 e V3 | 2 | 6,290 | 2,063 | 5,880 | 7,943 | 2,090 | 4,153 |
| V2 | 1 | 5,730 | 2,063 | 5,880 | 7,943 | 0,000 | 2,063 |
| V2 | 2 | 6,080 | 2,063 | 5,880 | 7,943 | 0,000 | 2,063 |
| V4 e V6 | 1 | 5,250 | 1,688 | 5,880 | 7,568 | 2,090 | 3,778 |
| V4 e V6 | 2 | 5,000 | 1,688 | 5,880 | 7,568 | 2,090 | 3,778 |
| V5 | 1 | 5,250 | 1,688 | 5,880 | 7,568 | 0,000 | 1,688 |
| V5 | 2 | 5,000 | 1,688 | 5,880 | 7,568 | 0,000 | 1,688 |
