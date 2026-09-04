# Aula 02 — Ações na estrutura

Esta aula apresenta os critérios iniciais para determinar as ações que atuam em uma estrutura de concreto armado. O objetivo é transformar o peso dos materiais, as cargas de utilização e as cargas de elementos construtivos em carregamentos compatíveis com o modelo estrutural de lajes, vigas e pilares. Nesse caso vamos empregar a normativa NBR 6120 [[1]](#ref-1).

```{admonition} Objetivos da aula
:class: destaque-azul

- compreender o caminho das cargas entre lajes, vigas e pilares.
- identificar as principais fontes de carregamento de uma edificação;
- distinguir cargas por unidade de volume, área e comprimento;
- calcular o peso próprio de lajes maciças;
- distribuir cargas de alvenaria sobre lajes;
- revisão sobre a carga de vento no edifício.
```

## Referência normativa — slide 2

Os valores de peso específico aparente dos materiais e de cargas de utilização
devem ser obtidos na **ABNT NBR 6120 — Ações para o cálculo de estruturas de
edificações**.

[[1]](#ref-1) 

```{admonition} Atenção
:class: destaque-vermelho

Antes de elaborar um projeto, consulte a edição vigente da norma. Os valores
reproduzidos nesta aula correspondem ao material apresentado nos slides e devem
ser confirmados para uso profissional.
```

## Peso específico dos materiais — slide 3

O peso específico aparente, representado por $\gamma_{ap}$, expressa o peso do
material por unidade de volume. Sua unidade usual é $\mathrm{kN/m^3}$.

[[1]](#ref-1) [[2]](#ref-2)

| Grupo | Material | $\gamma_{ap}$ ($\mathrm{kN/m^3}$) |
|---|---|---:|
| Rochas | Arenito | 21 a 27 (24) |
| Rochas | Basalto, diorito e gabro | 28 |
| Rochas | Gnaisse | 30 |
| Rochas | Granito, sienito e pórfiro | 27 a 30 (28,5) |
| Rochas | Mármore e calcário | 28 |
| Blocos artificiais e pisos | Bloco de concreto vazado estrutural | 14 |
| Blocos artificiais e pisos | Bloco cerâmico vazado com paredes vazadas | 12 |
| Blocos artificiais e pisos | Bloco cerâmico vazado com paredes maciças | 14 |
| Blocos artificiais e pisos | Bloco cerâmico maciço | 18 |
| Blocos artificiais e pisos | Lajota cerâmica | 18 |
| Blocos artificiais e pisos | Porcelanato | 23 |
| Revestimentos e concretos | Argamassa de cal, cimento e areia | 19 |
| Revestimentos e concretos | Argamassa de cal | 12 a 18 (15) |
| Revestimentos e concretos | Argamassa de cimento e areia | 19 a 23 (21) |
| Revestimentos e concretos | Argamassa de gesso | 12 a 18 (15) |
| Revestimentos e concretos | Concreto simples | 24 |
| Revestimentos e concretos | Concreto armado | 25 |

Os valores entre parênteses são valores médios indicados na tabela de origem.

## Cargas de utilização e de cobertura — slide 4

As cargas de utilização dependem da finalidade do ambiente. Alguns valores
apresentados no slide são:

[[1]](#ref-1) [[2]](#ref-2)

| Ocupação | Local | Carga uniformemente distribuída ($\mathrm{kN/m^2}$) |
|---|---|---:|
| Áreas técnicas | Barrilete | 1,50 |
| Áreas técnicas | Áreas técnicas em geral | 3,00 |
| Áreas técnicas | Casa de máquinas de elevador de passageiros ($v \leq 1{,}00\,\mathrm{m/s}$) | 30,00 |
| Áreas técnicas | Sala de gerador e transformador, sem leiaute | 10,00 |
| Residencial | Dormitório | 1,50 |
| Residencial | Sala, copa e cozinha | 1,50 |
| Residencial | Despensa, área de serviço e lavanderia | 2,00 |
| Residencial | Academia | 3,00 |
| Residencial | Salão de festas ou de jogos | 3,00 |
| Residencial | Corredor de uso comum | 3,00 |
| Residencial | Corredor dentro de unidade autônoma | 1,50 |
| Comercial | Sala de uso geral e sanitário | 2,50 |
| Comercial | Região de arquivos deslizantes | 5,00 |
| Comercial | *Call center* | 3,00 |
| Comercial | Corredor de uso comum | 3,00 |
| Comercial | Corredor dentro de unidade autônoma | 2,50 |

Para a carga de cobertura indicada no slide, emprega-se:

$$
q = 0{,}50\,\alpha
\tag{4.1}
$$

em que $q$ é a carga, em $\mathrm{kN/m^2}$, e $\alpha$ depende da inclinação
$i$ do telhado:

$$
\alpha =
\begin{cases}
1{,}00, & 1\% < i \leq 2\%,\\
2{,}00 - 0{,}50i, & 2\% < i < 3\%,\\
0{,}50, & i \geq 3\%.
\end{cases}
\tag{4.2}
$$

[[1]](#ref-1)

## Pesos de elementos construtivos — slide 5

Além do peso próprio da estrutura, devem ser considerados os pesos de
alvenarias, telhas, impermeabilizações, contrapisos e revestimentos. As tabelas
do slide foram mantidas como imagens provisórias para posterior redesenho.

[[1]](#ref-1) [[2]](#ref-2)

```{figure} ../_static/aulas/carregamentos/tabela-alvenaria-estrutural.png
:alt: Tabela de pesos de alvenaria estrutural
:width: 75%
:align: center

Pesos de alvenaria estrutural em função do tipo de bloco, da espessura e do
revestimento.
```

[[1]](#ref-1)

```{figure} ../_static/aulas/carregamentos/tabela-alvenaria-vedacao.png
:alt: Tabela de pesos de alvenaria de vedação
:width: 75%
:align: center

Pesos de alvenaria de vedação em função do tipo de bloco, da espessura e do
revestimento.
```

[[1]](#ref-1)

```{figure} ../_static/aulas/carregamentos/tabela-coberturas-revestimentos.png
:alt: Tabelas de pesos de coberturas, impermeabilizações e revestimentos
:width: 75%
:align: center

Pesos de telhas, impermeabilizações, pisos elevados e revestimentos.
```

[[1]](#ref-1)

## Representação das cargas — slide 6

No modelo estrutural, a forma de representar a ação depende da geometria do
elemento que a recebe:

[[1]](#ref-1)

| Elemento | Representação usual | Unidade típica |
|---|---|---|
| Laje | carga distribuída em uma superfície | $\mathrm{kN/m^2}$ |
| Viga | carga distribuída ao longo de uma linha | $\mathrm{kN/m}$ |
| Pilar | força concentrada | $\mathrm{kN}$ |

### Lajes

```{image} ../_static/aulas/carregamentos/carga-em-laje.png
:alt: Carga distribuída em uma laje
:width: 38%
:align: center
```

[[1]](#ref-1)

### Vigas

```{image} ../_static/aulas/carregamentos/carga-em-viga.png
:alt: Carga distribuída em uma viga
:width: 25%
:align: center
```

[[1]](#ref-1)

### Pilares

```{image} ../_static/aulas/carregamentos/carga-em-pilar.png
:alt: Força concentrada em um pilar
:width: 14%
:align: center
```

[[1]](#ref-1)

## Peso próprio das lajes — slide 7

### Laje maciça

Para uma laje maciça de espessura constante, o peso próprio por unidade de área
é dado por:

$$
G_{pp}^{\mathrm{laje}} = h_{\mathrm{laje}}\,\gamma_c
\tag{7.1}
$$

[[1]](#ref-1)

em que:

- $G_{pp}^{\mathrm{laje}}$ é o peso próprio da laje, em $\mathrm{kN/m^2}$;
- $h_{\mathrm{laje}}$ é a espessura da laje, em $\mathrm{m}$;
- $\gamma_c$ é o peso específico do concreto, em $\mathrm{kN/m^3}$.

```{admonition} Exemplo rápido
:class: destaque-azul

Para uma laje maciça de concreto armado com $h=0{,}12\,\mathrm{m}$ e
$\gamma_c=25\,\mathrm{kN/m^3}$, resulta
$G_{pp}=0{,}12\times25=3{,}00\,\mathrm{kN/m^2}$.
```

### Laje nervurada

Nas lajes nervuradas, o peso próprio deve considerar o volume efetivo de
concreto e os elementos de enchimento ou as fôrmas incorporadas. Os catálogos
dos fabricantes fornecem dimensões, volume de vazio, consumo de concreto e peso
por unidade de área.

[[1]](#ref-1) [[3]](#ref-3)

```{figure} ../_static/aulas/carregamentos/laje-nervurada-atex.png
:alt: Dados geométricos de fôrmas Atex para laje nervurada
:width: 100%
:align: center

Exemplo de dados de catálogo usados para determinar o peso próprio de uma laje
nervurada. Fonte indicada no slide: catálogo Atex 600.
```

[[1]](#ref-1) [[3]](#ref-3)

## Carga de alvenaria sobre lajes — slide 8

Considere uma parede com altura $H_{alv}$, espessura $e_{alv}$, comprimento
$l_{alv}$ e peso específico $\gamma_{alv}$. A forma de distribuir sua carga
depende da relação entre os vãos da laje:

[[1]](#ref-1)

$$
\lambda = \frac{l_y}{l_x}, \qquad l_y \geq l_x.
\tag{8.1}
$$

### Laje armada em duas direções: $\lambda \leq 2$

A carga total da parede é distribuída por toda a área da laje:

$$
G_{EC}^{alv} =
\frac{(a+b)\,H_{alv}\,e_{alv}\,\gamma_{alv}}
{l_x\,l_y}.
\tag{8.2}
$$

Os comprimentos $a$ e $b$ representam os trechos de alvenaria considerados no
pavimento.

```{figure} ../_static/aulas/carregamentos/alvenaria-laje-bidirecional.png
:alt: Distribuição de carga de alvenaria em laje armada em duas direções
:width: 32%
:align: center

Distribuição equivalente da alvenaria em uma laje com $\lambda\leq2$.
```

[[1]](#ref-1)

### Laje armada em uma direção: $\lambda > 2$

Para a faixa de influência indicada no slide:

$$
G_{EC}^{alv} =
\frac{H_{alv}\,e_{alv}\,l_{alv}\,\gamma_{alv}}
{l_x\,l_{inf}}.
\tag{8.3}
$$

A largura de influência é:

$$
l_{inf} = e_{alv} + h_{\mathrm{laje}}.
\tag{8.4}
$$

Quando a parede está orientada na direção de distribuição mostrada à direita do
slide, sua carga linear é expressa por:

$$
G_{EC}^{alv} = H_{alv}\,e_{alv}\,\gamma_{alv}.
\tag{8.5}
$$

[[1]](#ref-1)

```{figure} ../_static/aulas/carregamentos/alvenaria-laje-unidirecional.png
:alt: Distribuição de carga de alvenaria em laje armada em uma direção
:width: 28%
:align: center

Representação da parede e da carga aplicada na faixa de influência.
```

[[1]](#ref-1)

```{admonition} Verificação de unidades
:class: destaque-vermelho

As Equações (8.2) e (8.3) resultam em carga superficial
($\mathrm{kN/m^2}$). A Equação (8.5) resulta em carga linear
($\mathrm{kN/m}$).
```

## Carga de alvenaria sobre vigas — slide 9

Quando a parede está apoiada diretamente em uma viga, sua carga é tratada como
uma ação linear:

$$
G_{EC}^{alv} = \left(H_{alv}\,e_{alv}\right)\gamma_{alv}.
\tag{9.1}
$$

[[1]](#ref-1)

O resultado é expresso em $\mathrm{kN/m}$. Se houver aberturas, revestimentos ou
variações de altura, esses efeitos devem ser incorporados ao cálculo do trecho
correspondente.

```{figure} ../_static/aulas/carregamentos/caminho-das-cargas.png
:alt: Caminho das cargas em uma estrutura formada por lajes, vigas e pilares
:width: 48%
:align: center

Caminho das cargas: as lajes recebem ações superficiais, transferem-nas às
vigas e estas as conduzem aos pilares.
```

[[1]](#ref-1)

## Síntese

```{admonition} Caminho básico para determinar os carregamentos
:class: destaque-azul

1. Identificar todos os materiais e elementos construtivos.
2. Obter seus pesos específicos e cargas de utilização na norma aplicável.
3. Calcular as cargas permanentes da estrutura e dos revestimentos.
4. Converter as ações para a representação adequada: superficial, linear ou
   concentrada.
5. Distribuir as cargas de alvenaria conforme o sistema resistente da laje.
6. Transferir as ações das lajes para as vigas e, em seguida, para os pilares.
```

## Referências

(ref-2)=
(ref-1)=
**[1]** ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **ABNT NBR 6120:2019**:
*Ações para o cálculo de estruturas de edificações*. Rio de Janeiro: ABNT,
2019.

(ref-3)=
**[3]** ATEX. *Catálogo Atex 600: fôrmas para lajes nervuradas*. Catálogo
técnico do fabricante.
