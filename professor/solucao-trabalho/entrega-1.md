## Entrega 1: Pré-dimensionamento, vãos efetivos e cargas nas lajes

### Geometria e hipóteses da solução

Referências: [Aula 02](../aulas/002-lanc-pre-dim.md) e
[Aula 03](../aulas/003-carregamentos.md).

As cotas da {ref}`Figura 1 do enunciado <fig-1>` estão em
**centímetros**. Adotam-se lajes maciças, vigas com largura de **15 cm** e a
seguinte numeração dos painéis, olhando a planta na posição apresentada:

| Laje | Posição | Vigas de contorno | Dimensões entre eixos (m) | Área entre eixos (m²) |
|---|---|---|---|---:|
| L1 | Superior esquerda | V1, V2, V4 e V5 | 5,10 × 5,85 | 29,8350 |
| L2 | Superior direita | V1, V2, V5 e V6 | 5,10 × 6,20 | 31,6200 |
| L3 | Inferior esquerda | V2, V3, V4 e V5 | 4,85 × 5,85 | 28,3725 |
| L4 | Inferior direita | V2, V3, V5 e V6 | 4,85 × 6,20 | 30,0700 |

A área total entre eixos é $12{,}05\times9{,}95=119{,}8975\text{ m}^2$.
As áreas acima servem à conferência da planta; a área de aplicação das cargas
de cada modelo precisa ser coerente com suas dimensões livres ou efetivas.

### Espessura inicial das lajes

Pelo critério de Rebello para lajes maciças bidirecionais:

$$
h_{est}=0{,}02\frac{l_x+l_y}{2}.
$$

Usando inicialmente as distâncias entre eixos:

| Laje | $h_{est}$ (cm) | $h$ inicial adotado (cm) |
|---|---:|---:|
| L1 | 10,95 | 12 |
| L2 | 11,30 | 12 |
| L3 | 10,70 | 12 |
| L4 | 11,05 | 12 |

Padroniza-se inicialmente $h=12\text{ cm}$ nos pisos e na cobertura. A
escolha atende aos mínimos geométricos apresentados na Aula 02 para lajes
sem balanço. A aprovação da espessura depende das verificações posteriores.

### Vãos efetivos

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
l_x=5{,}10-0{,}15+2(0{,}036)=5{,}022\text{ m},
\qquad
l_y=5{,}85-0{,}15+2(0{,}036)=5{,}772\text{ m}.
$$

| Laje | $l_x$ (m) | $l_y$ (m) | $\lambda=l_y/l_x$ | Comportamento |
|---|---:|---:|---:|---|
| L1 | 5,022 | 5,772 | 1,1493 | Duas direções |
| L2 | 5,022 | 6,122 | 1,2190 | Duas direções |
| L3 | 4,772 | 5,772 | 1,2096 | Duas direções |
| L4 | 4,772 | 6,122 | 1,2829 | Duas direções |

O eixo $x$ é vertical na planta e o eixo $y$ é horizontal. As quatro lajes
possuem apoio nos quatro lados e $\lambda<2$; não há balanço no desenho.

### Cargas permanentes dos pavimentos-tipo

Usando os valores das tabelas da Aula 03 e $h$ em metros:

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
enunciado:

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

### Vigas e pilares na Entrega 1

Nas vigas V1 a V6, registre $b_w=15\text{ cm}$ e justifique a altura
adotada. A Aula 02 fornece as condições $b\geq l_0/50$ e
$b\geq\beta_{fl}h$ para a verificação de instabilidade lateral. O comprimento
$l_0$ depende dos travamentos da zona comprimida; a largura de 15 cm,
isoladamente, não define a altura nem comprova a segurança da viga.

Nos pilares, determine as áreas de influência pelo procedimento da Aula 02 e
use a carga de cada pavimento efetivamente sustentado:

$$
N_k^*=A_i(10n_{tipo}+7n_{cob}),\qquad N_d^*=\alpha N_k^*,
$$

$$
A_c=\frac{N_d^*}{0{,}85f_{cd}+\rho\sigma_s},
\qquad \rho=0{,}02,\quad\sigma_s=420\text{ MPa}.
$$

Compatibilize as unidades de força e tensão, aplique os coeficientes de
posição apresentados na aula e confira as dimensões mínimas. Conte os
níveis realmente apoiados no trecho do pilar; a existência do térreo não
implica, por si só, que seu piso descarregue na estrutura.

### Erros frequentes nesta entrega

- Usar 585 como vão em metros ou empregar 14 cm para a largura das vigas.
- Confundir distância entre eixos, vão livre e vão efetivo.
- Usar $h$ em centímetros na expressão $25h$ que exige metros.
- Contar duas vezes o reboco ou a manta, já incluídos nos valores tabelados.
- Distribuir na laje uma parede que foi contabilizada diretamente na viga.
- Tratar a espessura de pré-dimensionamento como resultado definitivo.
