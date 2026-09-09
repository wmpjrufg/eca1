# **Trabalho Prático**

## 1. Diretrizes de projeto

O trabalho prático do semestre consiste no pré-dimensionamento da estrutura e
no dimensionamento das lajes do pavimento padrão de um edifício residencial.
A [Figura 1](#fig-1) apresenta a planta de fôrma de referência do pavimento
padrão, com a identificação das vigas (V1 a V6) e dos vãos entre eixos de
pilares.

(fig-1)=
```{figure} ../_static/aulas/trabalho-pratico/pavimento-padrao.svg
:alt: Planta de fôrma do pavimento padrão, com vigas V1 a V6 e vãos entre pilares
:width: 85%

**Figura 1** – Planta de fôrma do pavimento padrão de referência, com vigas
V1 a V6 e vãos entre eixos de pilares de 5,85 m e 6,20 m (direção horizontal)
e 5,10 m e 4,85 m (direção vertical).
```

```{admonition} Objetivos do trabalho
:class: destaque-azul

- pré-dimensionar vigas, pilares e lajes para uma edificação residencial;
- definir os vãos efetivos de cada elemento estrutural a partir das seções
  pré-dimensionadas;
- levantar as cargas variáveis e permanentes atuantes nas lajes;
- dimensionar as lajes do pavimento padrão.
```

## 2. Pré-dimensionamento dos elementos estruturais

A primeira etapa consiste no pré-dimensionamento de vigas, pilares e lajes do
pavimento padrão apresentado na [Figura 1](#fig-1), considerando uma
edificação de uso residencial. Para a estimativa das cargas por área de
influência utilizada no pré-dimensionamento dos pilares, devem ser adotados
os seguintes valores de referência:

- **Piso (pavimento-tipo):** $10\text{ kN/m}^2$
- **Cobertura:** $7\text{ kN/m}^2$

```{admonition} Atenção
:class: destaque-vermelho

Esses valores são estimativas expeditas de carga total por m² (peso próprio
+ permanentes + variáveis), usadas apenas para o pré-dimensionamento inicial
das seções. As cargas efetivas das lajes devem ser recalculadas conforme o
item 4.
```

## 3. Definição dos vãos efetivos

A partir das seções de vigas e pilares obtidas no pré-dimensionamento (item
2), devem ser definidos os vãos efetivos de cada viga e de cada painel de
laje do pavimento padrão, descontando a influência das dimensões dos apoios
sobre os vãos entre eixos indicados na [Figura 1](#fig-1).

## 4. Cargas nas lajes

Definidos os vãos efetivos, o próximo passo é o levantamento das cargas
variáveis e permanentes atuantes nas lajes do pavimento padrão.

### 4.1 Carga variável

$$
q = 1{,}50\text{ kN/m}^2
$$

referente ao uso residencial do pavimento, conforme a Tabela 2 da
[Aula 02 — Ações na estrutura](002-carregamentos.md).

### 4.2 Carga permanente

$$
g = 1{,}20\text{ kN/m}^2
$$

Esse valor deve ser complementado pelo levantamento detalhado dos elementos
construtivos que compõem o pavimento, cujos pesos devem ser obtidos a partir
dos pesos específicos apresentados na Tabela 1 da
[Aula 02 — Ações na estrutura](002-carregamentos.md):

- **Vedações:** alvenaria em bloco cerâmico vazado com $11{,}5\text{ cm}$ de
  espessura, com reboco (argamassa de cimento e areia) de $2\text{ cm}$ em
  cada face.
- **Impermeabilização:** manta asfáltica com $10\text{ cm}$ de espessura,
  revestida com argamassa de cimento e areia de $2{,}5\text{ cm}$ de
  espessura.
- **Forro:** forro de gesso em placas, incluindo a estrutura de suporte, e
  argamassa de cimento e areia com $2{,}5\text{ cm}$ de espessura na face
  inferior da laje.
- **Revestimento de piso:** espessura de $5\text{ cm}$, conforme pesos
  específicos apresentados na Tabela 4.

```{admonition} Pendente
:class: destaque-azul

A Tabela 4, referente aos pesos específicos do revestimento de piso, será
disponibilizada na Aula 02 — Ações na estrutura.
```
