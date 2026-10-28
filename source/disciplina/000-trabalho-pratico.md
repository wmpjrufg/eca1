# Trabalho Prático

## Diretrizes de projeto

O trabalho prático do semestre consiste no dimensionamento das lajes do
pavimento padrão de um edifício residencial de concreto armado. Será tomado
como referência o pavimento padrão apresentado na [Figura 1](#fig-1), com a
identificação das vigas (V1 a V6) e dos vãos entre eixos de pilares.

(fig-1)=
**Figura 1.** Planta de fôrma do pavimento padrão de referência, com vigas.
V1 a V6.
```{figure} ../_static/aulas/trabalho-pratico/pavimento-padrao.png
:alt: Planta de fôrma do pavimento padrão, com vigas V1 a V6 e vãos entre pilares
:width: 85%
:align: center
:class: planta-trabalho
```
(parametros-projeto)=
### Parâmetros do projeto

- Uso: residencial;
- Pavimentos: 7 (térreo + 1º + 2º + 3º + 4º + 5º + cobertura);
- Pé-esquerdo: $3{,}10\text{ m}$;
- Carga por área de influência para pré-dimensionamento dos pilares:
  - Pavimento-tipo: $10\text{ kN/m}^2$;
  - Cobertura: $7\text{ kN/m}^2$.
- Largura das vigas (V1 a V6): $b_w=15\text{ cm}$. Verificar largura das vigas quanto à segurança à instabilidade lateral;
  conforme o item 15.10 da [ABNT NBR 6118 [1]](#ref-1);
- Taxa de armadura para pré-dimensionamento dos pilares: $\rho = 2\%$;
- Tensão correspondente a $0{,}20\%$ de deformação (aço CA-50): $420\text{ MPa}$;
- Materiais e durabilidade: concreto C30
  ($f_{ck}=30\text{ MPa}$), aço CA-50, classe de agressividade ambiental II e
  cobrimento nominal das lajes de $2{,}5\text{ cm}$, conforme a
  [ABNT NBR 6118 [1]](#ref-1);
- Combinações de ações: ELU com $\gamma_f=1{,}4$;
  ELS com os fatores $\psi_1=0{,}4$ (combinação frequente) e $\psi_2=0{,}3$
  (combinação quase permanente), adotados para edificações residenciais;
- Ocupação das lajes dos pavimentos-tipo: residencial, dormitório;
- Lajes de cobertura: impermeabilização em manta asfáltica com proteção
  mecânica de $15\text{ cm}$, sem revestimento de piso, e contrapiso em
  argamassa de cimento e areia de $4\text{ cm}$. A inclinação da cobertura é de
  $1\%$;
- Vedações: alvenaria em bloco cerâmico vazado com $11{,}5\text{ cm}$ de
  espessura, com reboco (argamassa de cimento e areia) de $2\text{ cm}$ em cada
  face;
- Alvenaria sobre a laje L1: considere um perímetro de alvenaria apoiado
  diretamente na laje, em todo o seu contorno, com altura de $3{,}00\text{ m}$;
- Alvenaria sobre as vigas dos pavimentos-tipo: considere que todas as vigas
  (V1 a V6) recebem carga de alvenaria, com altura de $2{,}80\text{ m}$;
- Platibanda da cobertura: as vigas de contorno da cobertura (V1, V3, V4 e V6)
  recebem platibanda de $1{,}10\text{ m}$ de altura, em bloco cerâmico vazado
  de $14\text{ cm}$ de espessura, com reboco de $2\text{ cm}$ em cada face. As
  vigas V2 e V5 da cobertura não recebem alvenaria;
- Forro: forro de gesso em placas, incluindo a estrutura de suporte;
- Revestimento de piso: revestimentos de pisos de edifícios residenciais e
  comerciais, com espessura de $5\text{ cm}$.

## Roteiro de etapas e entregas do semestre

A [solução do trabalho](000-solucao-trabalho.md) será disponibilizada por
entrega, ao longo do semestre, para conferência dos cálculos e discussão
dos erros mais frequentes.

O trabalho é desenvolvido em cinco entregas sequenciais. Cada entrega usa os
resultados da anterior; se uma verificação posterior exigir alterar uma seção
(por exemplo, a espessura de uma laje), os cálculos das entregas anteriores
afetados devem ser refeitos e reapresentados.

(tabela-1)=
**Tabela 1.** Etapas de entrega do trabalho.
| Entrega | Conteúdo | Arquivos principais |
|---|---|---|
| 1 | Pré-dimensionamento, vãos efetivos e cargas nas lajes | Memória de cálculo (`.md`) e planta de fôrma (`.dwg` e `.pdf`) |
| 2 | Esforços nas lajes e descarregamento nas vigas | Memória (`.md`) e plantas de esforços (`.pdf` e `.dwg`) |
| 3 | Checagens iniciais: cisalhamento, fissuração e flecha com armadura mínima | Memória (`.md`) |
| 4 | Dimensionamento à flexão das lajes, armaduras e flecha final | Memória (`.md`) |
| 5 | Detalhamento das lajes e pranchas finais | Pranchas (`.pdf` e `.dwg`) e relatório final (`.md`) |

### Pré-dimensionamento dos elementos estruturais

A primeira etapa consiste no pré-dimensionamento de vigas, lajes e pilares do
pavimento padrão apresentado na [Figura 1](#fig-1), considerando os
parâmetros informados anteriormente. Os critérios de pré-dimensionamento constam na
[Aula 02: Lançamento e pré-dimensionamento estrutural](../aulas/002-lanc-pre-dim.md)
e as cargas a considerar constam na
[Aula 03: Ações na estrutura](../aulas/003-carregamentos.md).

```{admonition} Entrega 1: Pré-dimensionamento, vãos efetivos e cargas nas lajes
:class: destaque-verde

A **Entrega 1** contempla as etapas de pré-dimensionamento dos elementos estruturais, definição dos vãos efetivos e levantamento das cargas nas lajes, apresentadas no roteiro de projeto.

**Pré-dimensionamento dos elementos estruturais:** pré-dimensionar as seções de vigas (V1 a V6), lajes e pilares do pavimento padrão, aplicando os critérios apresentados na [Aula 02: Lançamento e pré-dimensionamento estrutural](../aulas/002-lanc-pre-dim.md).

**Definição dos vãos efetivos:** a partir das seções obtidas no pré-dimensionamento, determinar os vãos efetivos ($l_x$ e $l_y$) de cada laje do pavimento padrão.

**Cargas nas lajes:** levantar as cargas variáveis e permanentes atuantes em cada laje do pavimento padrão (pavimentos-tipo e cobertura), conforme a [ABNT NBR 6120 [2]](#ref-2).

**Apresentação e arquivos obrigatórios:**

- Entregar a **memória de cálculo em Markdown (extensão .md)**, apresentando o pré-dimensionamento de todas as vigas (V1 a V6), lajes e pilares do pavimento padrão, com as equações utilizadas, os valores adotados e a seção final ($b \times h$) de cada elemento.
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
| Arquivos entregues | Memória de cálculo em Markdown (`.md`) e planta com as seções finais, completos e acessíveis. | 1,0 |
| Pré-dimensionamento das vigas | Aplicação do critério de instabilidade lateral (item 15.10 da NBR 6118) e definição das seções $b \times h$ de V1 a V6. | 1,5 |
| Pré-dimensionamento das lajes | Aplicação dos critérios de Rebello para a altura das lajes maciças/nervuradas do pavimento. | 1,5 |
| Pré-dimensionamento dos pilares | Determinação da área de influência, da carga estimada e da seção transversal dos pilares. | 1,5 |
| Vãos efetivos das lajes | Determinação correta dos vãos efetivos $l_x$ e $l_y$ de cada laje, a partir das seções pré-dimensionadas. | 1,0 |
| Cargas nas lajes | Levantamento correto das cargas variáveis e permanentes de cada laje, conforme a ABNT NBR 6120. | 1,5 |
| **Total** | | **10,0** |

**Regra de pontuação:** cada critério recebe 100% dos pontos quando atendido integralmente, 50% quando atendido parcialmente e zero quando ausente, incorreto ou impossível de verificar. A falta de identificação completa de todos os integrantes zera o critério de identificação e organização. Arquivos ausentes ou que não abrem não pontuam no conteúdo que depender deles para ser verificado. A nota final corresponde à soma dos critérios.
```

### Esforços nas lajes e descarregamento nas vigas

Com as cargas definidas, o próximo passo é obter os esforços que cada laje
precisa resistir e conduzir as ações das lajes até as vigas. Os critérios
constam na [Aula 05: Esforços em lajes](../aulas/005-esforcos-lajes.md) e, para o
caminho das cargas, na [Aula 03: Ações na estrutura](../aulas/003-carregamentos.md). Os modelos de
viga e de rigidez dos pilares usados para obter os esforços das vigas constam na
[Aula 04: Modelos estruturais](../aulas/004-modelos-estruturais.md).

**Esforços nas lajes.** Para cada laje, registre o croqui com os eixos e os
vínculos de cada borda, os vãos efetivos, o caso de apoio da tabela adotada, o
valor de $\lambda=l_y/l_x$, a carga do caso analisado, os coeficientes (com
interpolação, quando necessária) e os momentos $m_x$, $m_y$, $X_x$ e $X_y$.
Em cada borda interna, compatibilize os momentos negativos dos dois lados e
corrija os momentos positivos, indicando a borda física e a direção
envolvidas. Indique a combinação usada: os momentos de cálculo ($M_d$) para a
flexão e os momentos em serviço para as verificações de ELS.

**Reações das lajes nas vigas.** Determine, para cada borda de cada laje, a
carga linear transmitida à viga de apoio ($\mathrm{kN/m}$). Use as áreas de
influência definidas pelas charneiras plásticas do item 14.7.6.1 da
[ABNT NBR 6118 [1]](#ref-1): $45^\circ$ entre dois apoios do mesmo tipo,
$60^\circ$ a partir do apoio engastado quando o outro é simplesmente apoiado e
$90^\circ$ a partir do apoio quando a borda vizinha é livre. Em lajes
armadas em uma direção, as reações concentram-se nas bordas paralelas ao vão
principal. Em lajes em balanço, além da carga linear, considere o momento de
engastamento transmitido à viga. Confira o equilíbrio de cada laje: a soma das
reações deve ser igual à carga total aplicada.

**Esforços nas vigas.** Para cada viga (V1 a V6), componha a carga linear
total: reações das lajes de cada lado, peso próprio da viga, alvenaria apoiada
diretamente sobre ela e cargas vindas de outras vigas, quando houver. Defina o
esquema estático (apoios, balanços e vãos) e determine os diagramas de esforço
cortante e momento fletor e as reações nos pilares, por processo manual ou por
programa de análise de vigas e pórticos planos. Confira o equilíbrio: a soma das
reações nos apoios deve ser igual à carga total da viga.

```{admonition} Entrega 2: Esforços nas lajes e descarregamento nas vigas
:class: destaque-verde

A **Entrega 2** contempla a determinação dos esforços em todas as lajes do pavimento padrão (pavimentos-tipo e cobertura), das cargas que as lajes transmitem às vigas e dos esforços resultantes nas vigas V1 a V6.

**Apresentação e arquivos obrigatórios:**

- Entregar a **memória de cálculo em Markdown (extensão .md)** com, para cada laje: croqui de vínculos, vãos efetivos, caso de apoio, $\lambda$, carga, coeficientes, momentos positivos e negativos iniciais e valores finais após a compatibilização.
- Incluir, para cada borda interna, um **quadro de compatibilização** com os negativos dos dois lados, o valor comum e os positivos corrigidos.
- Incluir a **memória das reações das lajes nas vigas**, com o desenho das charneiras e as áreas de influência de cada laje, e a carga linear resultante em cada borda.
- Incluir, para cada viga V1 a V6, a **composição da carga linear total**, o esquema estático, os **diagramas de esforço cortante e momento fletor** com os valores nos apoios e no meio dos vãos e as **reações nos pilares**.
- Entregar a **planta de esforços nas lajes** (PDF e DWG), baseada na planta da Entrega 1, com os momentos positivos e negativos finais de cada laje, indicados na direção correspondente, com unidades.
- Entregar a **planta de descarregamento nas vigas** (PDF e DWG), com as cargas lineares transmitidas por cada laje a cada viga e as reações nos pilares.
- Apresentar ao final da memória um **resumo gráfico dos esforços**: a planta de esforços das lajes e os diagramas de $V$ e $M$ das vigas V1 a V6.
- Identificar a memória de cálculo e as plantas com **nome completo e matrícula de todos os integrantes**, identificação da entrega e do projeto.
- Corrigir e reapresentar os itens da Entrega 1 que tenham sido alterados.

**Critérios de avaliação da Entrega 2 (10,0 pontos):**

| Critério | O que será avaliado | Pontuação máxima |
|---|---|---:|
| Identificação e organização | Nome completo e matrícula de todos os integrantes, identificação do projeto e organização geral dos arquivos. | 1,0 |
| Apresentação da memória de cálculo | Clareza, unidades, convenção de sinais, notas explicativas e legibilidade das equações e resultados. | 1,0 |
| Momentos nas lajes | Escolha correta do caso de apoio, $\lambda$, coeficientes, interpolação e momentos de cada laje. | 2,5 |
| Compatibilização dos momentos | Momento negativo comum nas bordas internas e correção dos positivos. | 1,5 |
| Reações das lajes nas vigas | Charneiras plásticas, áreas de influência, cargas lineares e equilíbrio de cada laje. | 1,5 |
| Esforços nas vigas | Composição da carga linear total, esquema estático, diagramas de $V$ e $M$, reações nos pilares e equilíbrio. | 1,5 |
| Representação gráfica final | Planta de esforços nas lajes, planta de descarregamento e diagramas das vigas, completos e legíveis. | 1,0 |
| **Total** | | **10,0** |

**Regra de pontuação:** a mesma da Entrega 1.
```

### Checagens iniciais do sistema

Antes de calcular as armaduras, verifica-se se as espessuras adotadas
conduzem a um sistema viável. Nesta etapa, cada laje é verificada considerando
apenas a **armadura mínima** de flexão da
[ABNT NBR 6118 [1]](#ref-1) (Tabela 19.1; armadura positiva de lajes armadas em duas
direções com $\rho_s\geq0{,}67\rho_{min}$, armadura negativa e armadura
positiva de lajes armadas em uma direção com $\rho_s\geq\rho_{min}$, e armadura
secundária conforme a mesma tabela). O resultado indica as lajes que já
atendem com armadura mínima e as que exigem armadura calculada ou aumento de
espessura.

**Propriedades dos materiais.** Calcule e registre $f_{cd}$, $f_{ctm}$,
$f_{ctk,inf}$, $f_{ctd}$, $E_{ci}$ e $E_{cs}$ para o concreto adotado, e a
armadura mínima por metro, $A_{s,min}$, de cada laje, com a altura útil $d$
correspondente ao cobrimento e à bitola assumidos.

**Cisalhamento.** Verifique cada laje sem armadura transversal, conforme o
item 19.4.1 da norma: $V_{Sd}\leq V_{Rd1}$ por unidade de largura, usando como
$V_{Sd}$ a reação de cálculo em cada borda (da Entrega 2) e considerando, na taxa
de armadura longitudinal, a armadura mínima. Apresente a razão
$V_{Sd}/V_{Rd1}$ por borda.

**Fissuração.** Para a combinação frequente de ações ($\psi_1=0{,}4$), compare o
momento solicitante com o momento de fissuração $M_r$. Se $M_{d,freq}<M_r$, a
seção não fissura. Caso contrário, calcule a tensão na armadura no Estádio II
($\sigma_s$) e a abertura característica $w_k$ pelo item 17.3.3, comparando-a
com o limite da classe de agressividade (para CAA II em concreto armado,
$w_k\leq0{,}3\text{ mm}$, Tabela 13.4).

**Flecha.** Calcule a flecha imediata de cada laje para a combinação quase
permanente ($\psi_2=0{,}3$) com a rigidez equivalente de Branson ($I_{eq}$,
item 17.3.2.1), a partir do momento de fissuração calculado com $f_{ctm}$.
Calcule a flecha diferida pelo fator $\alpha_f=\Delta\xi/(1+50\rho')$, admitindo
$\rho'=0$, retirada do escoramento aos 28 dias ($t_0=1$ mês) e $t_\infty\geq70$ meses
($\xi=2{,}0$). Compare a flecha total com os limites da Tabela 13.3: $l/250$ para
aceitabilidade visual e $l/350$ para a parcela devida às cargas acidentais
(vibrações), com $l$ igual ao menor vão efetivo da laje. O método de cálculo da
flecha imediata será o apresentado em aula.

```{admonition} Entrega 3: Checagens iniciais do sistema
:class: destaque-verde

A **Entrega 3** contempla a verificação de todas as lajes do pavimento padrão ao cisalhamento, à fissuração e à flecha, adotando a armadura mínima de flexão.

**Apresentação e arquivos obrigatórios:**

- Entregar a **memória de cálculo em Markdown (extensão .md)** com os parâmetros, as propriedades dos materiais e as equações utilizadas, apresentando um exemplo de cálculo completo para uma laje e a mesma sequência resumida para as demais.
- Incluir a **tabela de armadura mínima** de cada laje, com $A_{s,min}$ (em $\mathrm{cm^2/m}$) nas duas direções, bitola e espaçamento adotados para atender a esse valor, e a altura útil $d$ correspondente.
- Incluir a **verificação ao cisalhamento** de cada laje (razão $V_{Sd}/V_{Rd1}$ em cada borda).
- Incluir a **verificação da fissuração** de cada laje: $M_r$, $M_{d,freq}$ e, quando necessário, $\sigma_s$ e $w_k$.
- Incluir a **verificação da flecha** de cada laje: $I_{eq}$, flecha imediata, flecha diferida, flecha total e limites.
- Apresentar uma **tabela-síntese** com, para cada laje, as razões de utilização de cada verificação e a conclusão (atende com armadura mínima ou exige armadura calculada, aumento de espessura ou outra providência).
- Quando for adotada **nova espessura** de laje, refazer as cargas (peso próprio), os esforços e as reações afetados e reapresentar a tabela correspondente.
- Identificar a memória de cálculo com **nome completo e matrícula de todos os integrantes**, identificação da entrega e do projeto, incluindo **notas de cálculo** com hipóteses e critérios adotados.

**Critérios de avaliação da Entrega 3 (10,0 pontos):**

| Critério | O que será avaliado | Pontuação máxima |
|---|---|---:|
| Identificação e organização | Nome completo e matrícula de todos os integrantes, identificação do projeto e organização geral dos arquivos. | 1,0 |
| Apresentação da memória de cálculo | Clareza, unidades, notas explicativas e legibilidade das equações e resultados. | 1,0 |
| Materiais e armadura mínima | Propriedades do concreto e $A_{s,min}$ de cada laje conforme a Tabela 19.1 da NBR 6118. | 1,5 |
| Cisalhamento | Cálculo de $V_{Rd1}$, $V_{Sd}$ e razão de utilização nas bordas de cada laje. | 2,0 |
| Fissuração | Momento de fissuração, combinação frequente, $\sigma_s$ e $w_k$ quando necessário, e comparação com o limite. | 2,0 |
| Flecha | Rigidez equivalente, flecha imediata, flecha diferida, flecha total e comparação com os limites. | 2,0 |
| Síntese e providências | Tabela-síntese correta e providências coerentes com os resultados (e revisão de espessuras, se for o caso). | 0,5 |
| **Total** | | **10,0** |

**Regra de pontuação:** a mesma da Entrega 1.
```

### Dimensionamento à flexão das lajes

Com as lajes verificadas, calcula-se a armadura de flexão necessária em cada
direção e em cada borda engastada, e confere-se a flecha final com a armadura
efetivamente adotada.

**Armadura de flexão.** Para uma faixa de largura $b_w=1\text{ m}$, a partir dos
momentos de cálculo $M_d$ da Entrega 2, determine a altura útil $d=h-c-\phi/2$, a
posição da linha neutra ($x/d$, verificando o limite do item 14.6.4.3 da
[ABNT NBR 6118 [1]](#ref-1)) e a área de aço $A_s$ em cada região (positivos nas
duas direções e negativos nas bordas). Quando o valor calculado for inferior ao
mínimo, adote $A_{s,min}$.

**Escolha das barras.** Defina, para cada armadura, a bitola e o espaçamento
que forneçam $A_{s,ef}\geq A_s$, respeitando as disposições do item 20.1: bitola
máxima de $h/8$, espaçamento máximo da armadura principal de $2h$ ou $20\text{ cm}$ (o
menor) e da armadura secundária de $33\text{ cm}$, além do espaçamento mínimo para a
concretagem. Nas lajes armadas em uma direção, dimensione também a armadura de
distribuição. Defina as armaduras de canto e de borda quando o caso de apoio as
exigir.

**Flecha final.** Refaça a verificação de flecha com $A_{s,ef}$ e a altura útil
efetiva ($I_{eq}$, flecha imediata, flecha diferida e total), com o mesmo
procedimento da Entrega 3. Verifique também o cisalhamento e a fissuração com
$A_{s,ef}$. Se a flecha total exceder o limite, aumente a armadura ou a
espessura e refaça os cálculos afetados.

```{admonition} Entrega 4: Dimensionamento à flexão das lajes
:class: destaque-verde

A **Entrega 4** contempla o dimensionamento à flexão de todas as lajes do pavimento padrão, a definição das armaduras e a verificação final de flecha.

**Apresentação e arquivos obrigatórios:**

- Entregar a **memória de cálculo em Markdown (extensão .md)** com as equações utilizadas, um exemplo de cálculo completo para uma laje (positivos e negativos) e a mesma sequência resumida para as demais.
- Incluir a **tabela de dimensionamento** com, para cada laje e cada região: $M_d$, $d$, $x/d$, $A_s$ calculada, $A_{s,min}$, bitola, espaçamento e $A_{s,ef}$ (em $\mathrm{cm^2/m}$).
- Incluir o **dimensionamento das armaduras secundárias, de distribuição, de canto e de borda**, quando aplicáveis, com a verificação das disposições construtivas do item 20.1 da NBR 6118.
- Incluir a **verificação final da flecha** de cada laje com $A_{s,ef}$ e a reverificação do cisalhamento e da fissuração.
- Apresentar um **quadro-resumo** das armaduras adotadas por laje, na forma de croqui em planta (esquema de armação sem escala) ou tabela, que será a base do detalhamento da Entrega 5.
- Identificar a memória de cálculo com **nome completo e matrícula de todos os integrantes**, identificação da entrega e do projeto, incluindo **notas de cálculo**.

**Critérios de avaliação da Entrega 4 (10,0 pontos):**

| Critério | O que será avaliado | Pontuação máxima |
|---|---|---:|
| Identificação e organização | Nome completo e matrícula de todos os integrantes, identificação do projeto e organização geral dos arquivos. | 1,0 |
| Apresentação da memória de cálculo | Clareza, unidades, notas explicativas e legibilidade das equações e resultados. | 1,0 |
| Armaduras positivas | $d$, $x/d$, $A_s$ e comparação com $A_{s,min}$ nas duas direções de cada laje. | 2,0 |
| Armaduras negativas | Dimensionamento nas bordas contínuas e engastadas, com os momentos compatibilizados. | 1,5 |
| Escolha das armaduras | Bitolas, espaçamentos, $A_{s,ef}$, armaduras secundárias, de distribuição, de canto e de borda, conforme o item 20.1. | 1,5 |
| Flecha final | Flecha com $A_{s,ef}$, comparação com os limites e reverificação do cisalhamento e da fissuração. | 2,0 |
| Quadro-resumo e conclusões | Quadro-resumo das armaduras e conclusões coerentes com os resultados. | 1,0 |
| **Total** | | **10,0** |

**Regra de pontuação:** a mesma da Entrega 1.
```

### Detalhamento das lajes e entrega final

A etapa final transforma o dimensionamento em desenhos executivos. As
armaduras definidas na Entrega 4 são posicionadas e numeradas, e seus comprimentos
são definidos considerando ancoragem e decalagem (itens 9.4 e 18.3 da
[ABNT NBR 6118 [1]](#ref-1)), e os quantitativos de materiais são levantados. Os critérios de detalhamento das barras positivas, negativas, de borda e de canto, e a
montagem da tabela de aço, constam na [Aula 09: Detalhamento de lajes maciças](../aulas/009-detalhamento-lajes.md).

```{admonition} Entrega 5: Detalhamento das lajes e pranchas finais
:class: destaque-verde

A **Entrega 5** contempla o detalhamento completo das lajes do pavimento padrão e a entrega final do projeto.

**Pranchas obrigatórias** (em **PDF** e em **DWG**, em formato ABNT A1, A2 ou A3, com carimbo):

- **Prancha 1: Fôrma do pavimento padrão.** Planta de fôrma com lajes numeradas e suas espessuras, vigas e pilares com as seções finais, cotas gerais e de eixo, níveis e notas gerais (concreto, aço, classe de agressividade, cobrimentos, cargas adotadas).
- **Prancha 2: Armação positiva.** Planta com todas as armaduras positivas, com posição, bitola, espaçamento, quantidade e comprimento (por exemplo, N1 Ø8,0 c/15 C=...), e cortes.
- **Prancha 3: Armação negativa.** Planta com todas as armaduras negativas, incluindo as de borda, de canto e de balanço (quando houver), com posição, bitola, espaçamento, comprimento, ancoragem e cortes.
- **Prancha 4: Quadro de ferros e resumo de materiais.** Quadro com posição, bitola, quantidade, comprimento unitário e total e massa de aço por bitola, além do resumo do volume de concreto, da área de fôrma e da taxa de aço ($\mathrm{kg/m^3}$).

**Relatório final em Markdown (extensão .md):**

- Reunir, em um único arquivo, a memória de cálculo final: resumo dos dados e critérios de projeto, os resultados consolidados de cada entrega (pré-dimensionamento, vãos efetivos, cargas, esforços, verificações e armaduras) com as correções incorporadas, e a tabela de correspondência entre as armaduras calculadas e as posições das pranchas.
- Incluir as **referências** utilizadas, as notas de cálculo e as hipóteses adotadas.

**Organização dos arquivos:**

- Identificar as pranchas e o relatório com **nome completo e matrícula de todos os integrantes**, identificação da entrega e do projeto.
- Nomear os arquivos de modo que seja possível identificar o grupo e o conteúdo, por exemplo `ECA1_grupoXX_E5_prancha1.pdf`, `ECA1_grupoXX_E5_pranchas.dwg` e `ECA1_grupoXX_E5_relatorio.md`. Conferir se todos os arquivos abrem corretamente e se os desenhos em PDF correspondem ao DWG entregue.

**Critérios de avaliação da Entrega 5 (10,0 pontos):**

| Critério | O que será avaliado | Pontuação máxima |
|---|---|---:|
| Identificação e organização | Nome completo e matrícula de todos os integrantes, identificação do projeto e organização geral dos arquivos. | 1,0 |
| Prancha de fôrma | Lajes, vigas e pilares com seções, cotas, níveis e notas gerais. | 1,5 |
| Armação positiva | Posicionamento, numeração, bitolas, espaçamentos e comprimentos coerentes com a Entrega 4. | 2,0 |
| Armação negativa | Armaduras negativas, de borda e de canto, ancoragens e comprimentos coerentes com a Entrega 4. | 2,0 |
| Quadro de ferros e resumo de materiais | Quadro completo, massa de aço, volume de concreto, área de fôrma e taxa de aço. | 1,5 |
| Relatório final | Consolidação das entregas anteriores com correções, referências e correspondência com as pranchas. | 1,0 |
| Normas gráficas e arquivos | Legibilidade, escalas, legendas, carimbo, coerência entre DWG e PDF, e arquivos que abrem corretamente. | 1,0 |
| **Total** | | **10,0** |

**Regra de pontuação:** a mesma da Entrega 1.
```

## Referências

(ref-1)=
[1] ABNT — ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. *NBR 6118: Projeto de estruturas de concreto*. 4. ed. Rio de Janeiro, 2023.

(ref-2)=
[2] ABNT — ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. *NBR 6120: Ações para cálculo de estruturas de edificações*. 2. ed. Rio de Janeiro, 2019.
