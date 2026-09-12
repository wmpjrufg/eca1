# Trabalho Prático

## Diretrizes de projeto

O trabalho prático do semestre consiste no dimensionamento das lajes do
pavimento padrão de um edifício residencial de concreto armado. Será tomado
como referência o pavimento padrão apresentado na [Figura 1](#fig-1), com a
identificação das vigas (V1 a V6) e dos vãos entre eixos de pilares.

(fig-1)=
**Figura 1** – Planta de fôrma do pavimento padrão de referência, com vigas
V1 a V6.
```{figure} ../_static/aulas/trabalho-pratico/pavimento-padrao.png
:alt: Planta de fôrma do pavimento padrão, com vigas V1 a V6 e vãos entre pilares
:width: 85%
```

### Parâmetros base do projeto

- Uso: residencial;
- Pavimentos: 7 (térreo + 1º + 2º + 3º + 4º + 5º + cobertura);
- Pé-esquerdo: $3{,}10\text{ m}$;
- Carga por área de influência para pré-dimensionamento dos pilares:
  - Piso (pavimento-tipo): $10\text{ kN/m}^2$;
  - Cobertura: $7\text{ kN/m}^2$.
- Taxa de armadura para pré-dimensionamento dos pilares: $\rho = 2\%$;
- Tensão correspondente a $0{,}20\%$ de deformação (aço CA-50): $420\text{ MPa}$;
- Largura das vigas: critério de instabilidade lateral do item 15.10 da
  [[ABNT NBR 6118 1]](#ref-1).

## Roteiro de etapas e entregas do semestre

### Pré-dimensionamento dos elementos estruturais

A primeira etapa consiste no pré-dimensionamento de vigas, lajes e pilares do
pavimento padrão apresentado na [Figura 1](#fig-1), considerando os
parâmetros informados anteriormente. Os critérios de pré-dimensionamento constam na
[Aula 02: Pré-dimensionamento dos elementos estruturais](../aulas/002-pre-dimensionamento.md).

### Definição dos vãos efetivos

A partir das seções de lajes, vigas e pilares obtidas no pré-dimensionamento, devem ser definidos os vãos efetivos de cada uma das lajes do
pavimento padrão.

### Cargas nas lajes

Definidos os vãos efetivos, o próximo passo é o levantamento das cargas
variáveis e permanentes atuantes nas lajes do pavimento padrão.

Para as lajes dos pavimentos-tipo, considere a ocupação residencial de
dormitório.

Para as lajes de cobertura, considere impermeabilização em manta asfáltica com proteção mecânica de $15\text{ cm}$, sem revestimento de piso, e contrapiso em argamassa de cimento e areia de $4\text{ cm}$. A inclinação da cobertura é de $1\%$.

- **Vedações:** alvenaria em bloco cerâmico vazado com $11{,}5\text{ cm}$ de
  espessura, com reboco (argamassa de cimento e areia) de $2\text{ cm}$ em
  cada face;
- **Impermeabilização:** manta asfáltica, revestida com argamassa de cimento
  e areia de $2{,}5\text{ cm}$ de espessura;
- **Forro:** forro de gesso em placas, incluindo a estrutura de suporte, e
  argamassa de cimento e areia com $2{,}5\text{ cm}$ de espessura na face
  inferior da laje;
- **Revestimento de piso:** espessura de $5\text{ cm}$.

Para a determinação dos carregamentos, consulte a [[ABNT NBR 6120 2]](#ref-2).

```{admonition} Entrega 1: Pré-dimensionamento, vãos efetivos e cargas nas lajes
:class: destaque-verde

A **Entrega 1** contempla as etapas de pré-dimensionamento dos elementos estruturais, definição dos vãos efetivos e levantamento das cargas nas lajes, apresentadas no roteiro de projeto.

**Pré-dimensionamento dos elementos estruturais:** pré-dimensionar as seções de vigas (V1 a V6), lajes e pilares do pavimento padrão, aplicando os critérios apresentados na Aula 02.

**Definição dos vãos efetivos:** a partir das seções obtidas no pré-dimensionamento, determinar os vãos efetivos ($l_x$ e $l_y$) de cada laje do pavimento padrão.

**Cargas nas lajes:** levantar as cargas variáveis e permanentes atuantes em cada laje do pavimento padrão (pavimentos-tipo e cobertura), conforme a ABNT NBR 6120.

**Apresentação e arquivos obrigatórios:**

- Entregar a **memória de cálculo em PDF**, apresentando o pré-dimensionamento de todas as vigas (V1 a V6), lajes e pilares do pavimento padrão, com as equações utilizadas, os valores adotados e a seção final ($b \times h$) de cada elemento.
- Entregar uma **planta do pavimento padrão** (baseada na Figura 1) com a identificação das seções finais adotadas para vigas e pilares e a numeração de todas as lajes.
- Incluir na memória de cálculo uma **tabela com os vãos efetivos** ($l_x$ e $l_y$) de cada laje, indicando a direção de armação (uma ou duas direções) e, quando for o caso, a condição de balanço.
- Incluir na memória de cálculo o **levantamento das cargas variáveis e permanentes** de cada laje, com a memória de cálculo do carregamento total considerado.
- Identificar a memória de cálculo e a planta com **nome completo e matrícula de todos os integrantes**, identificação da entrega e do projeto.
- Incluir **notas de cálculo quando necessárias**, esclarecendo unidades, hipóteses e critérios adotados.
- Organizar e nomear os arquivos de modo que seja possível identificar o grupo e o conteúdo correspondente. Conferir se todos os arquivos abrem corretamente.

**Critérios de avaliação da Entrega 1 (10,0 pontos):**

| Critério | O que será avaliado | Pontuação máxima |
|---|---|---:|
| Identificação e organização | Nome completo e matrícula de todos os integrantes, identificação do projeto e organização geral dos arquivos. | 1,0 |
| Apresentação da memória de cálculo | Clareza, unidades, notas explicativas e legibilidade das equações e resultados. | 1,0 |
| Arquivos entregues | Memória de cálculo em PDF e planta com as seções finais, completos e acessíveis. | 1,0 |
| Pré-dimensionamento das vigas | Aplicação do critério de instabilidade lateral (item 15.10 da NBR 6118) e definição das seções $b \times h$ de V1 a V6. | 1,5 |
| Pré-dimensionamento das lajes | Aplicação dos critérios de Rebello para a altura das lajes maciças/nervuradas do pavimento. | 1,5 |
| Pré-dimensionamento dos pilares | Determinação da área de influência, da carga estimada e da seção transversal dos pilares. | 1,5 |
| Vãos efetivos das lajes | Determinação correta dos vãos efetivos $l_x$ e $l_y$ de cada laje, a partir das seções pré-dimensionadas. | 1,0 |
| Cargas nas lajes | Levantamento correto das cargas variáveis e permanentes de cada laje, conforme a ABNT NBR 6120. | 1,5 |
| **Total** | | **10,0** |

**Regra de pontuação:** cada critério recebe 100% dos pontos quando atendido integralmente, 50% quando atendido parcialmente e zero quando ausente, incorreto ou impossível de verificar. A falta de identificação completa de todos os integrantes zera o critério de identificação e organização. Arquivos ausentes ou que não abrem não pontuam no conteúdo que depender deles para ser verificado. A nota final corresponde à soma dos critérios.
```

## Referências

(ref-1)=
**[1]** ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **ABNT NBR 6118**: Projeto de
estruturas de concreto. 4. ed. Rio de Janeiro: ABNT, 2023.

(ref-2)=
**[2]** ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **ABNT NBR 6120**: Ações para o cálculo de estruturas de edificações. 2. ed. Rio de Janeiro: ABNT, 2019.
