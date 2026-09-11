# Trabalho Prático

## 1. Diretrizes de projeto

O trabalho prático do semestre consiste no dimensionamento das lajes do
pavimento padrão de um edifício residencial de concreto armado. Será tomado
como referência o pavimento padrão apresentado na [Figura 1](#fig-1), com a
identificação das vigas (V1 a V6) e dos vãos entre eixos de pilares.

(fig-1)=
```{figure} ../_static/aulas/trabalho-pratico/pavimento-padrao.svg
:alt: Planta de fôrma do pavimento padrão, com vigas V1 a V6 e vãos entre pilares
:width: 85%

**Figura 1** – Planta de fôrma do pavimento padrão de referência, com vigas
V1 a V6 e vãos entre eixos de pilares de 5,85 m e 6,20 m (direção horizontal)
e 5,10 m e 4,85 m (direção vertical).
```

### 1.1 Parâmetros base do projeto

- Uso: residencial
- Pavimentos: 7 (térreo + 1º + 2º + 3º + 4º + 5º + cobertura)
- Pé-esquerdo: $3{,}10\text{ m}$
- Carga por área de influência para pré-dimensionamento dos pilares:
  - Piso (pavimento-tipo): $10\text{ kN/m}^2$
  - Cobertura: $7\text{ kN/m}^2$
- Taxa de armadura para pré-dimensionamento dos pilares: $\rho = 2\%$
- Tensão correspondente a $0{,}20\%$ de deformação (aço CA-50): $420\text{ MPa}$
- Largura das vigas: critério de instabilidade lateral do item 15.10 da
  ABNT NBR 6118 [[1]](#ref-1)

## 2. Roteiro de etapas e entregas do semestre

### 2.1 Pré-dimensionamento dos elementos estruturais

A primeira etapa consiste no pré-dimensionamento de vigas, lajes e pilares do
pavimento padrão apresentado na [Figura 1](#fig-1), considerando os
parâmetros da Seção 1.1. Os critérios de pré-dimensionamento constam na
[Aula 02 — Pré-dimensionamento dos elementos estruturais](../aulas/002-pre-dimensionamento.md).

```{admonition} Atenção
:class: destaque-vermelho

Os valores de carga por área de influência indicados na Seção 1.1 são
estimativas expeditas de carga total por m² (peso próprio + permanentes +
variáveis), usadas apenas para o pré-dimensionamento inicial das seções. As
cargas efetivas das lajes devem ser recalculadas conforme o item 2.3.
```

### 2.2 Definição dos vãos efetivos

A partir das seções de lajes, vigas e pilares obtidas no pré-dimensionamento
(item 2.1), devem ser definidos os vãos efetivos de cada uma das lajes do
pavimento padrão.

```{admonition} Entrega 1: Pré-dimensionamento e vãos efetivos
:class: destaque-verde

A **Entrega 1** contempla os itens **2.1 e 2.2** do roteiro de projeto.

**Item 2.1 - Pré-dimensionamento dos elementos estruturais:** pré-dimensionar as seções de vigas (V1 a V6), lajes e pilares do pavimento padrão, aplicando os critérios apresentados na Aula 02.

**Item 2.2 - Definição dos vãos efetivos:** a partir das seções obtidas no pré-dimensionamento, determinar os vãos efetivos ($l_x$ e $l_y$) de cada laje do pavimento padrão.

**Apresentação e arquivos obrigatórios:**

- Entregar a **memória de cálculo em PDF**, apresentando o pré-dimensionamento de todas as vigas (V1 a V6), lajes e pilares do pavimento padrão, com as equações utilizadas, os valores adotados e a seção final ($b \times h$) de cada elemento.
- Entregar uma **planta do pavimento padrão** (baseada na Figura 1) com a identificação das seções finais adotadas para vigas e pilares e a numeração de todas as lajes.
- Incluir na memória de cálculo uma **tabela com os vãos efetivos** ($l_x$ e $l_y$) de cada laje, indicando a direção de armação (uma ou duas direções) e, quando for o caso, a condição de balanço.
- Identificar a memória de cálculo e a planta com **nome completo e matrícula de todos os integrantes**, identificação da entrega e do projeto.
- Incluir **notas de cálculo quando necessárias**, esclarecendo unidades, hipóteses e critérios adotados.
- Organizar e nomear os arquivos de modo que seja possível identificar o grupo e o conteúdo correspondente. Conferir se todos os arquivos abrem corretamente.

**Critérios de avaliação da Entrega 1 (10,0 pontos):**

| Critério | O que será avaliado | Pontuação máxima |
|---|---|---:|
| Identificação e organização | Nome completo e matrícula de todos os integrantes, identificação do projeto e organização geral dos arquivos. | 1,0 |
| Apresentação da memória de cálculo | Clareza, unidades, notas explicativas e legibilidade das equações e resultados. | 1,0 |
| Arquivos entregues | Memória de cálculo em PDF e planta com as seções finais, completos e acessíveis. | 1,0 |
| Pré-dimensionamento das vigas | Aplicação do critério de instabilidade lateral (item 15.10 da NBR 6118) e definição das seções $b \times h$ de V1 a V6. | 2,0 |
| Pré-dimensionamento das lajes | Aplicação dos critérios de Rebello para a altura das lajes maciças/nervuradas do pavimento. | 2,0 |
| Pré-dimensionamento dos pilares | Determinação da área de influência, da carga estimada e da seção transversal dos pilares. | 2,0 |
| Vãos efetivos das lajes | Determinação correta dos vãos efetivos $l_x$ e $l_y$ de cada laje, a partir das seções pré-dimensionadas. | 1,0 |
| **Total** | | **10,0** |

**Regra de pontuação:** cada critério recebe 100% dos pontos quando atendido integralmente, 50% quando atendido parcialmente e zero quando ausente, incorreto ou impossível de verificar. A falta de identificação completa de todos os integrantes zera o critério de identificação e organização. Arquivos ausentes ou que não abrem não pontuam no conteúdo que depender deles para ser verificado. A nota final corresponde à soma dos critérios.
```

### 2.3 Cargas nas lajes

Definidos os vãos efetivos, o próximo passo é o levantamento das cargas
variáveis e permanentes atuantes nas lajes do pavimento padrão.

#### 2.3.1 Carga variável

Para as lajes dos pavimentos-tipo, considere a ocupação residencial de
dormitório:

$$
q = 1{,}50\text{ kN/m}^2
$$

conforme a Tabela 2 da
[Aula 03 — Ações na estrutura](../aulas/003-carregamentos.md).

Para a laje de cobertura, considere uma inclinação $i=2\%$, o que resulta,
pelas Equações (2.1) e (2.2) da
[Aula 03 — Ações na estrutura](../aulas/003-carregamentos.md), em:

$$
q = 0{,}50\text{ kN/m}^2
$$

#### 2.3.2 Carga permanente

$$
g = 1{,}20\text{ kN/m}^2
$$

Esse valor deve ser complementado pelo levantamento detalhado dos elementos
construtivos que compõem o pavimento, cujos pesos devem ser obtidos a partir
dos pesos específicos apresentados na Tabela 1 da
[Aula 03 — Ações na estrutura](../aulas/003-carregamentos.md):

- **Vedações:** alvenaria em bloco cerâmico vazado com $11{,}5\text{ cm}$ de
  espessura, com reboco (argamassa de cimento e areia) de $2\text{ cm}$ em
  cada face, conforme a Tabela 3 da
  [Aula 03 — Ações na estrutura](../aulas/003-carregamentos.md).
- **Impermeabilização:** manta asfáltica, revestida com argamassa de cimento
  e areia de $2{,}5\text{ cm}$ de espessura, conforme a Tabela 5 da
  [Aula 03 — Ações na estrutura](../aulas/003-carregamentos.md).
- **Forro:** forro de gesso em placas, incluindo a estrutura de suporte, e
  argamassa de cimento e areia com $2{,}5\text{ cm}$ de espessura na face
  inferior da laje, conforme a Tabela 8 e a Tabela 1 da
  [Aula 03 — Ações na estrutura](../aulas/003-carregamentos.md).
- **Revestimento de piso:** espessura de $5\text{ cm}$, conforme pesos
  específicos apresentados na Tabela 5 da
  [Aula 03 — Ações na estrutura](../aulas/003-carregamentos.md).

```{admonition} Pendente
:class: destaque-azul

A espessura de $10\text{ cm}$ indicada para a manta asfáltica não corresponde
a nenhuma opção da Tabela 5 da Aula 03 (que vai até $0{,}5\text{ cm}$) —
confirme se a espessura pretendida é essa mesma ou se é um erro de digitação
(por exemplo, $1{,}0\text{ cm}$).
```

## Referências

(ref-1)=
**[1]** ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 6118**: Projeto de
estruturas de concreto. Rio de Janeiro: ABNT, 2023.
