# Aula 03: Ações na estrutura

## Introdução

Esta aula apresenta os critérios iniciais para determinar as ações que atuam em uma estrutura de concreto armado. O objetivo é transformar o peso dos materiais, as cargas de utilização e as cargas dos elementos construtivos em carregamentos compatíveis com o modelo estrutural de lajes, vigas e pilares. Para isso, será empregada a **ABNT NBR 6120:2019 — Ações para o cálculo de estruturas de edificações** [[1]](#ref-1).

```{admonition} Objetivos da aula
:class: destaque-azul

- identificar as principais fontes de carregamento de uma edificação;
- distinguir cargas por unidade de volume, área e comprimento;
- consultar valores de referência de pesos de alvenarias, revestimentos, coberturas e forros;
- calcular o peso próprio de lajes maciças;
- distribuir cargas de alvenaria sobre lajes;
- revisar a ação do vento no edifício.
```

## As ações no subsistema horizontal

Inicialmente, serão tratadas as ações que ocorrem no subsistema horizontal, formado por lajes e vigas. Essas ações podem ter naturezas diversas, desde o peso de um piano na sala de um edifício até o carregamento produzido por um elemento construtivo, como uma parede revestida de uma sala de raios X. Na maioria dos casos, essas cargas podem ser avaliadas com base na ABNT NBR 6120 [[1]](#ref-1).

```{admonition} Atenção
:class: destaque-vermelho

No caso de carregamentos específicos, como os produzidos por máquinas, consulte o catálogo do fabricante e verifique também, quando possível, a posição dos pontos de apoio. Essa é uma situação comum na avaliação das ações geradas por equipamentos.
```

### Peso específico aparente dos materiais

O peso específico aparente, representado por $\gamma_{ap}$, expressa o peso do material por unidade de volume. Sua unidade usual é $\mathrm{kN/m^3}$. Neste caso, são utilizados os valores do item 5.3 da ABNT NBR 6120 [[1]](#ref-1), parcialmente reproduzidos na Tabela 1.

**Tabela 1 — Peso específico aparente dos materiais de construção. Adaptado da ABNT NBR 6120, Tabela 1 [[1]](#ref-1).**

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

```{admonition} Atenção
:class: destaque-vermelho

Os valores entre parênteses são valores médios indicados na tabela de origem.
```

### Cargas de utilização e de cobertura

As cargas de utilização estão relacionadas ao uso previsto para cada ambiente da edificação. Por esse motivo, seus valores variam de acordo com a ocupação e com as atividades desenvolvidas no local. A Tabela 2 apresenta alguns valores de cargas uniformemente distribuídas estabelecidos pela ABNT NBR 6120 [[1]](#ref-1).

**Tabela 2 — Cargas uniformemente distribuídas em função da ocupação do ambiente.**

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

**Fonte:** adaptada da ABNT NBR 6120:2019 [[1]](#ref-1).

No caso das coberturas, a carga uniformemente distribuída $q$ pode ser determinada pela Equação (1):

$$
q = 0{,}50\,\alpha
\tag{1}
$$

em que $q$ é a carga de cobertura, expressa em $\mathrm{kN/m^2}$, e $\alpha$ é um coeficiente que depende da inclinação $i$ do telhado, conforme a Equação (2):

$$
\alpha =
\begin{cases}
1{,}00, & 1\% < i \leq 2\%,\\
2{,}00 - 0{,}50i, & 2\% < i < 3\%,\\
0{,}50, & i \geq 3\%.
\end{cases}
\tag{2}
$$

**Fonte:** ABNT NBR 6120:2019 [[1]](#ref-1).

(sec-pesos-elementos)=
### Pesos de elementos construtivos

Além do peso próprio da estrutura, devem ser consideradas as cargas de alvenarias, divisórias, caixilhos, revestimentos, impermeabilizações, telhas, telhados e forros, entre outros elementos construtivos, conforme a ABNT NBR 6120 [[1]](#ref-1) [[2]](#ref-2). As tabelas a seguir reúnem valores de referência para esses elementos. Na aplicação em projeto, devem ser identificadas as características reais dos materiais e dos componentes construtivos adotados.

Para alvenaria estrutural (blocos portantes), os pesos de referência constam na figura a seguir.

```{figure} ../_static/aulas/carregamentos/tabela-alvenaria-estrutural.png
:alt: Tabela de pesos de alvenaria estrutural
:width: 75%
:align: center

Pesos de alvenaria estrutural em função do tipo de bloco, da espessura e do revestimento. [[1]](#ref-1)
```

A Tabela 3 apresenta os pesos de paredes de alvenaria de **vedação** em função da espessura e do revestimento. Os valores incluem o peso do bloco ou tijolo e, nas colunas correspondentes, o revestimento aplicado em cada face.

**Tabela 3 — Peso de paredes de alvenaria de vedação em função da espessura e do revestimento.**

| Material | Espessura nominal do elemento (cm) | Sem revestimento (kN/m²) | Revestimento de 1 cm por face (kN/m²) | Revestimento de 2 cm por face (kN/m²) |
|---|---:|---:|---:|---:|
| Bloco de concreto vazado (Classe C — ABNT NBR 6136) | 6,5 | 1,0 | 1,4 | 1,8 |
| Bloco de concreto vazado (Classe C — ABNT NBR 6136) | 9 | 1,1 | 1,5 | 1,9 |
| Bloco de concreto vazado (Classe C — ABNT NBR 6136) | 11,5 | 1,3 | 1,7 | 2,1 |
| Bloco de concreto vazado (Classe C — ABNT NBR 6136) | 14 | 1,4 | 1,8 | 2,2 |
| Bloco de concreto vazado (Classe C — ABNT NBR 6136) | 19 | 1,8 | 2,2 | 2,6 |
| Bloco cerâmico vazado, furo horizontal (ABNT NBR 15270-1) | 9 | 0,7 | 1,1 | 1,6 |
| Bloco cerâmico vazado, furo horizontal (ABNT NBR 15270-1) | 11,5 | 0,9 | 1,3 | 1,7 |
| Bloco cerâmico vazado, furo horizontal (ABNT NBR 15270-1) | 14 | 1,1 | 1,5 | 1,9 |
| Bloco cerâmico vazado, furo horizontal (ABNT NBR 15270-1) | 19 | 1,4 | 1,8 | 2,3 |
| Bloco de concreto celular autoclavado (Classe C25 — ABNT NBR 13438) | 7,5 | 0,5 | 0,9 | 1,3 |
| Bloco de concreto celular autoclavado (Classe C25 — ABNT NBR 13438) | 10 | 0,6 | 1,0 | 1,4 |
| Bloco de concreto celular autoclavado (Classe C25 — ABNT NBR 13438) | 12,5 | 0,8 | 1,2 | 1,6 |
| Bloco de concreto celular autoclavado (Classe C25 — ABNT NBR 13438) | 15 | 0,9 | 1,3 | 1,7 |
| Bloco de concreto celular autoclavado (Classe C25 — ABNT NBR 13438) | 17,5 | 1,1 | 1,5 | 1,9 |
| Bloco de concreto celular autoclavado (Classe C25 — ABNT NBR 13438) | 20 | 1,2 | 1,6 | 2,0 |
| Bloco de vidro (decorativo, sem resistência ao fogo) | 8 | 0,8 | — | — |

**Nota:** os valores das três últimas colunas são pesos por unidade de área da parede. A espessura do revestimento indicada é considerada em cada face da parede.

**Tabela 4 — Divisórias e caixilhos.**

| Material | Espessura nominal do elemento (cm) | Peso (kN/m²) |
|---|---:|---:|
| *Drywall* (montantes metálicos, quatro chapas de 12,5 mm e isolamento acústico com lã de rocha ou lã de vidro de 50 mm) | 7 a 30 | 0,5 |
| Divisórias retráteis, exceto divisórias com vidro | 7 a 12 | 0,6 |
| Caixilhos de alumínio, incluindo vidro simples de 4 mm | — | 0,2 |
| Caixilhos de ferro, incluindo vidro simples de 4 mm | — | 0,3 |
| Caixilhos que vão de piso a piso, com $h \leq 4,0\ \mathrm{m}$ | — | 0,5 |
| Fachadas com pele de vidro e fachadas unitizadas | Validar conforme o caso | — |

**Nota:** para fachadas com pele de vidro ou fachadas unitizadas, o peso deve ser determinado de acordo com a composição efetiva do sistema.

**Tabela 5 — Revestimentos de pisos e impermeabilizações.**

| Material | Espessura (cm) | Peso (kN/m²) |
|---|---:|---:|
| Impermeabilização com manta asfáltica simples, sem camada de regularização nem proteção mecânica | 0,3 | 0,08 |
| Impermeabilização com manta asfáltica simples, sem camada de regularização nem proteção mecânica | 0,4 | 0,10 |
| Impermeabilização com manta asfáltica simples, sem camada de regularização nem proteção mecânica | 0,5 | 0,11 |
| Piso elevado interno com placas de aço, sem revestimento, até 30 cm de altura | — | 0,5 |
| Piso elevado interno com placas de polipropileno, sem revestimento, até 30 cm de altura | — | 0,15 |
| Revestimentos de pisos de edifícios residenciais e comerciais ($\gamma_{ap-m} = 20\ \mathrm{kN/m^3}$) | 5 | 1,0 |
| Revestimentos de pisos de edifícios residenciais e comerciais ($\gamma_{ap-m} = 20\ \mathrm{kN/m^3}$) | 7 | 1,4 |
| Revestimentos de pisos de edifícios industriais ($\gamma_{ap-m} = 34\ \mathrm{kN/m^3}$) | 5 | 1,7 |
| Revestimentos de pisos de edifícios industriais ($\gamma_{ap-m} = 34\ \mathrm{kN/m^3}$) | 7 | 2,4 |
| Impermeabilização em cobertura com manta asfáltica e proteção mecânica, sem revestimento ($\gamma_{ap-m} = 18\ \mathrm{kN/m^3}$) | 10 | 1,8 |
| Impermeabilização em cobertura com manta asfáltica e proteção mecânica, sem revestimento ($\gamma_{ap-m} = 18\ \mathrm{kN/m^3}$) | 15 | 2,7 |

**Nota:** os pesos devem ser calculados caso a caso quando forem conhecidas as espessuras dos componentes e seus respectivos pesos específicos. Na ausência de informações mais precisas, podem ser utilizados os valores médios indicados.

**Tabela 6 — Telhas, considerando o peso na superfície inclinada.**

| Material | Peso na superfície inclinada (kN/m²) |
|---|---:|
| Telha cerâmica em geral, exceto tipo germânica e colonial | 0,45 |
| Telha cerâmica tipo germânica ou colonial | 0,60 |
| Telha de fibrocimento ondulada com espessura de 4 mm | 0,14 |
| Telha de fibrocimento ondulada com espessura de 5 mm | 0,16 |
| Telha de fibrocimento ondulada com espessura de 6 mm | 0,18 |
| Telha de fibrocimento ondulada com espessura de 8 mm | 0,24 |
| Telha de fibrocimento modulada com espessura de 8 mm | 0,26 |
| Telha de fibrocimento tipo canalete com espessura de 8 mm | 0,25 |
| Telha de alumínio com espessura de 0,6 mm | 0,025 |
| Telha de alumínio com espessura de 0,8 mm | 0,035 |
| Telha plástica em geral, exceto tipo colonial | 0,05 |
| Telha plástica tipo colonial | 0,15 |
| Telha de aço ondulada ou trapezoidal com espessura de 0,5 mm | 0,06 |
| Telha de aço ondulada ou trapezoidal com espessura de 0,8 mm | 0,10 |
| Telha de aço ondulada ou trapezoidal com espessura de 1,25 mm | 0,14 |
| Telha de vidro | 0,45 |

**Nota:** os valores correspondem ao peso por metro quadrado de telha na superfície inclinada, incluindo a sobreposição, os elementos de fixação e a absorção de água.

**Tabela 7 — Telhados, considerando o peso na superfície horizontal, incluindo a estrutura de suporte.**

| Composição | Peso na superfície horizontal (kN/m²) |
|---|---:|
| Telhas cerâmicas em geral, exceto tipo germânica e colonial, com estrutura de madeira e inclinação $\leq 40\%$ | 0,70 |
| Telhas cerâmicas tipo germânica ou colonial, com estrutura de madeira e inclinação $\leq 40\%$ | 0,85 |
| Telhas de fibrocimento onduladas, com espessura de até 5 mm, e estrutura de madeira | 0,40 |
| Telhas de alumínio, com espessura de até 0,8 mm, e estrutura metálica de aço | 0,30 |
| Telhas de alumínio, com espessura de até 0,8 mm, e estrutura metálica de alumínio | 0,20 |
| Telhas de fibrocimento tipo canalete, com espessura de 8 mm, e estrutura de madeira | 0,35 |

**Nota:** os valores correspondem ao peso por metro quadrado de telhado na superfície horizontal, incluindo a estrutura de suporte, como tesouras, terças, caibros e ripas.

**Tabela 8 — Forros, dutos e redes de distribuição de chuveiros automáticos (*sprinklers*).**

| Material | Peso (kN/m²) |
|---|---:|
| Forro de fibra mineral, incluindo estrutura de suporte | 0,10 |
| Forro de gesso acartonado, incluindo estrutura de suporte | 0,25 |
| Forro de gesso em placas, incluindo estrutura de suporte | 0,15 |
| Forro de PVC, incluindo estrutura de suporte | 0,10 |
| Forro de placas de alumínio, incluindo estrutura de suporte | 0,10 |
| Dutos de ventilação, sem isolamento térmico | 0,20 |
| Dutos de ar-condicionado, com isolamento térmico | 0,30 |
| Rede de distribuição de chuveiros automáticos (*sprinkler*) com diâmetro nominal de até 65 mm | 0,10 |
| Rede de distribuição de chuveiros automáticos (*sprinkler*) com diâmetro nominal de até 80 mm | 0,15 |

## Representação das cargas

No modelo estrutural, a forma de representar a ação depende da geometria do elemento que a recebe:

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

## Peso próprio das lajes

### Laje maciça

Para uma laje maciça de espessura constante, o peso próprio por unidade de área é dado por:

$$
G_{pp}^{\mathrm{laje}} = h_{\mathrm{laje}}\,\gamma_c
\tag{3}
$$

[[1]](#ref-1)

em que:

- $G_{pp}^{\mathrm{laje}}$ é o peso próprio da laje, em $\mathrm{kN/m^2}$;
- $h_{\mathrm{laje}}$ é a espessura da laje, em $\mathrm{m}$;
- $\gamma_c$ é o peso específico do concreto, em $\mathrm{kN/m^3}$.

```{admonition} Exemplo rápido
:class: destaque-azul

Para uma laje maciça de concreto armado com $h=0{,}12\,\mathrm{m}$ e $\gamma_c=25\,\mathrm{kN/m^3}$, resulta $G_{pp}=0{,}12\times25=3{,}00\,\mathrm{kN/m^2}$.
```

### Laje nervurada

Nas lajes nervuradas, o peso próprio deve considerar o volume efetivo de concreto e os elementos de enchimento ou as fôrmas incorporadas. Os catálogos dos fabricantes fornecem dimensões, volume de vazio, consumo de concreto e peso por unidade de área.

[[1]](#ref-1) [[3]](#ref-3)

```{figure} ../_static/aulas/carregamentos/laje-nervurada-atex.png
:alt: Dados geométricos de fôrmas Atex para laje nervurada
:width: 100%
:align: center

Exemplo de dados de catálogo usados para determinar o peso próprio de uma laje nervurada. Fonte: catálogo Atex 600 [[3]](#ref-3).
```

## Carga de alvenaria sobre lajes

Quando uma parede de alvenaria se apoia diretamente sobre a laje, e não sobre vigas, o seu peso próprio deve ser convertido em uma ação equivalente, a ser somada às demais ações permanentes da laje. Considere uma parede com altura $H_{alv}$, espessura $e_{alv}$, comprimento $l_{alv}$ e peso específico $\gamma_{alv}$ (ver [Pesos de elementos construtivos](#sec-pesos-elementos)). A forma de distribuir sua carga depende da relação entre os vãos do painel:

$$
\lambda = \frac{l_y}{l_x}, \qquad l_y \geq l_x.
\tag{4}
$$

[[1]](#ref-1)

### Painéis armados em duas direções ($\lambda \leq 2$)

O peso da parede é espraiado por toda a área do painel, resultando em uma carga equivalente uniformemente distribuída:

$$
G_{EC}^{alv} =
\frac{(a+b)\,H_{alv}\,e_{alv}\,\gamma_{alv}}
{l_x\,l_y}.
\tag{5}
$$

Os comprimentos $a$ e $b$ representam os trechos de alvenaria considerados no pavimento.

```{admonition} Pendente
:class: destaque-azul

Falta uma figura ilustrando o espraiamento do peso da parede por toda a área do painel armado em duas direções ($\lambda\leq2$). As duas figuras já disponíveis (`alvenaria-parede-paralela.png` e `alvenaria-parede-perpendicular.png`) ilustram os dois casos do painel armado em [**uma** direção](#sec-paineis-uma-direcao), não este caso.
```

(sec-paineis-uma-direcao)=
### Painéis armados em uma direção ($\lambda > 2$)

Para $\lambda>2$, o espraiamento do peso da parede por toda a área do painel deixa de ser uma aproximação razoável, pois a laje passa a trabalhar predominantemente em uma única direção. Nesse caso, o efeito da parede sobre a laje depende da orientação da parede em relação ao vão principal $l_x$.

#### Parede paralela ao vão principal

A parede é considerada apenas na faixa da laje diretamente sob ela, de largura de influência:

$$
l_{inf} = e_{alv} + h_{\mathrm{laje}}.
\tag{6}
$$

Essa faixa (identificada como B na figura a seguir) recebe uma carga adicional $g_{par}$, somada à carga de utilização $p=g+q$ que atua no restante do painel (faixas A):

$$
G_{EC}^{alv} =
\frac{H_{alv}\,e_{alv}\,l_{alv}\,\gamma_{alv}}
{l_x\,l_{inf}}.
\tag{7}
$$

```{figure} ../_static/aulas/carregamentos/alvenaria-parede-paralela.png
:alt: Distribuição de carga de parede paralela ao vão principal de uma laje armada em uma direção
:width: 32%
:align: center

Painel dividido nas faixas A (carga $p=g+q$) e B (faixa de influência $l_{inf}$, com carga adicional $g_{par}$) e diagramas de carregamento das faixas de laje analisadas como vigas.
```

[[1]](#ref-1)

#### Parede perpendicular ao vão principal

O peso da parede não se distribui ao longo do vão: ele atua como uma carga concentrada $G$ na faixa de laje analisada como viga, aplicada na posição em que a parede cruza a laje:

$$
G_{EC}^{alv} = H_{alv}\,e_{alv}\,\gamma_{alv}.
\tag{8}
$$

```{figure} ../_static/aulas/carregamentos/alvenaria-parede-perpendicular.png
:alt: Distribuição de carga de parede perpendicular ao vão principal de uma laje armada em uma direção
:width: 28%
:align: center

Painel com a faixa A (carga $p=g+q$) e a carga concentrada $G$ aplicada na posição da parede, e diagrama de carregamento da faixa de laje analisada como viga.
```

[[1]](#ref-1)

```{admonition} Verificação de unidades
:class: destaque-vermelho

As Equações (5) e (7) resultam em carga superficial ($\mathrm{kN/m^2}$), somada a $p=g+q$. A Equação (8) resulta em uma carga linear ($\mathrm{kN/m}$), tratada como concentrada na faixa de laje analisada como viga.
```

## Carga de alvenaria sobre vigas

Quando a parede está apoiada diretamente em uma viga, sua carga é tratada como uma ação linear:

$$
G_{EC}^{alv} = \left(H_{alv}\,e_{alv}\right)\gamma_{alv}.
\tag{9}
$$

[[1]](#ref-1)

O resultado é expresso em $\mathrm{kN/m}$. Se houver aberturas, revestimentos ou variações de altura, esses efeitos devem ser incorporados ao cálculo do trecho correspondente.

```{figure} ../_static/aulas/carregamentos/caminho-das-cargas.png
:alt: Caminho das cargas em uma estrutura formada por lajes, vigas e pilares
:width: 48%
:align: center

Caminho das cargas: as lajes recebem ações superficiais, transferem-nas às vigas e estas as conduzem aos pilares.
```

[[1]](#ref-1)

## Síntese

```{admonition} Caminho básico para determinar os carregamentos
:class: destaque-azul

1. Identificar todos os materiais e elementos construtivos.
2. Obter seus pesos específicos e cargas de utilização na norma aplicável (ver [Pesos de elementos construtivos](#sec-pesos-elementos) para alvenarias, revestimentos, telhas, telhados e forros).
3. Calcular as cargas permanentes da estrutura e dos revestimentos.
4. Converter as ações para a representação adequada: superficial, linear ou concentrada.
5. Distribuir as cargas de alvenaria conforme o sistema resistente da laje.
6. Transferir as ações das lajes para as vigas e, em seguida, para os pilares.
```

## Referências

(ref-1)=
**[1]** ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **ABNT NBR 6120**: Ações para o cálculo de estruturas de edificações. 2. ed. Rio de Janeiro: ABNT, 2019.
