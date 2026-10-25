# Aula 05: Verificação global do sistema: vento, α e γz

Na aula anterior, aprendemos a transformar o edifício em um modelo. Antes de dimensionar qualquer laje, viga ou pilar, é preciso responder a uma pergunta sobre o **edifício inteiro**: **a estrutura tem rigidez suficiente para resistir às ações horizontais sem que os deslocamentos e os esforços de 2ª ordem fujam do controle?**

A aula começa pelas ações horizontais, o **vento** (NBR 6123) e o **desaprumo**, e mostra como elas entram nas combinações de ações do estado limite último. Em seguida, apresenta os dois indicadores que a NBR 6118 oferece para classificar a estrutura como de **nós fixos** ou de **nós móveis**: o **parâmetro α**, um "termômetro" que depende só da rigidez e do peso da estrutura, e o **coeficiente γz**, que estima de fato o acréscimo de esforços provocado pela deformação lateral. Três exemplos resolvidos e três atividades em sala, com o Ftool, completam a aula.

```{admonition} Objetivos da aula
:class: destaque-azul

- Explicar por que os deslocamentos laterais de um edifício geram efeitos de 2ª ordem e distinguir estruturas de nós fixos e de nós móveis.
- Determinar a velocidade característica e a força do vento por pavimento segundo a NBR 6123.
- Calcular o desaprumo (imperfeição geométrica global) e convertê-lo em forças horizontais.
- Montar as combinações de ações do ELU para a verificação global.
- Montar o pórtico equivalente no Ftool e obter o deslocamento do topo.
- Calcular o parâmetro α e compará-lo com o valor-limite α₁.
- Calcular o coeficiente γz e decidir se os efeitos globais de 2ª ordem podem ser desprezados.
- Verificar os deslocamentos laterais em serviço.
```

## Por que verificar a estabilidade global?

As ações horizontais (vento e desaprumo) deslocam os pavimentos do edifício. Quando a estrutura já deformada continua carregada, as **forças verticais deixam de passar pelo eixo dos pilares**: cada pavimento tem peso $P_i$ e está deslocado $\delta_i$, e o produto $P_i\,\delta_i$ é um **momento adicional**. Esse momento aumenta os deslocamentos, que aumentam o momento, e assim por diante. É o efeito de 2ª ordem **global**, o mesmo mecanismo do pilar em balanço da aula anterior, agora aplicado ao edifício inteiro.

```{figure} ../_static/aulas/verificacao-global/efeito-pdelta-global.png
:alt: Dois pórticos de quatro pavimentos: à esquerda, apenas as forças horizontais sobre a geometria indeformada; à direita, a geometria deformada com os deslocamentos de cada pavimento e as cargas verticais deslocadas
:width: 85%
:align: center

Análise de 1ª ordem (equilíbrio na geometria inicial) e de 2ª ordem global (equilíbrio na geometria deformada).
```

Duas grandezas resumem o efeito, para cada combinação de ações:

$$M_{1,tot,d}=\sum F_{H,i,d}\,z_i \qquad\qquad \Delta M_{tot,d}=\sum P_{i,d}\,\delta_i$$

em que $M_{1,tot,d}$ é o **momento de tombamento** de cálculo, em 1ª ordem, em relação à base, e $\Delta M_{tot,d}$ é o **acréscimo de momento** causado pelos deslocamentos horizontais $\delta_i$ de cada pavimento. Quanto maior a razão $\Delta M_{tot,d}/M_{1,tot,d}$, mais a estrutura "sente" a 2ª ordem.

### A analogia da coluna de Euler

Um edifício se comporta, para as ações horizontais, como um pilar em balanço de altura $H_{tot}$ com a rigidez à flexão equivalente $EI_{eq}$ de todo o sistema de contraventamento. A carga crítica de uma coluna em balanço é

$$N_{cr}=\frac{\pi^2\,EI}{4\,l^2}.$$

Quanto mais próxima a carga vertical está de $N_{cr}$, maior é a amplificação dos deslocamentos. Um edifício muito esbelto, muito pesado e pouco rígido está perto da instabilidade, e um edifício baixo e rígido está longe. Os indicadores $\alpha$ e $\gamma_z$ medem essa distância. Observe que $\alpha=H_{tot}\sqrt{N_k/(EI)}$ vale $\pi/2\approx1{,}57$ quando $N_k=N_{cr}$; a norma exige valores muito menores, da ordem de $0{,}5$ a $0{,}6$.

### Nós fixos e nós móveis

A NBR 6118 (item 15.4) classifica a estrutura conforme a importância dos efeitos globais de 2ª ordem:

| Classificação | Critério | Consequência |
|---|---|---|
| **Nós fixos** | Deslocamentos horizontais pequenos; efeitos globais de 2ª ordem inferiores a $10\%$ dos de 1ª ordem ($\alpha\le\alpha_1$ ou $\gamma_z\le1{,}1$) | Os efeitos globais de 2ª ordem podem ser desprezados. Os efeitos locais (em cada lance de pilar) continuam a ser considerados no dimensionamento dos pilares. |
| **Nós móveis** | Efeitos globais de 2ª ordem superiores a $10\%$ ($\gamma_z>1{,}1$) | Os efeitos globais de 2ª ordem precisam ser considerados no cálculo dos esforços. |

Na prática, o projetista segue um roteiro:

1. Definir as **ações horizontais**: vento e desaprumo.
2. Montar as **combinações de ações** do ELU.
3. Montar o **modelo** do contraventamento (pórtico plano ou equivalente) com a rigidez adequada.
4. Calcular **α** (triagem rápida) e **γz** (estimativa do acréscimo de esforços).
5. **Decidir**: nós fixos, nós móveis com amplificação aproximada ou análise de 2ª ordem completa.
6. Verificar os **deslocamentos laterais** em serviço.

## Ações horizontais: o vento

### Velocidade característica do vento

A NBR 6123 determina a velocidade característica do vento, $V_k$, a partir da **velocidade básica** $V_0$ e de três fatores:

$$V_k=V_0\cdot S_1\cdot S_2\cdot S_3$$

- **$V_0$ (velocidade básica)**: velocidade de uma rajada de 3 s, excedida em média uma vez a cada 50 anos, a 10 m de altura, em terreno plano e aberto. Vem do mapa de isopletas. Na região Centro-Oeste do Brasil, fica em torno de $30$ a $35\text{ m/s}$.
- **$S_1$ (fator topográfico)**: vale $1{,}0$ em terreno plano ou pouco ondulado, aumenta em taludes e morros e diminui em vales protegidos.
- **$S_2$ (fator de rugosidade do terreno e de altura)**: considera a rugosidade do terreno, as dimensões da edificação e a altura $z$ do ponto considerado acima do solo.
- **$S_3$ (fator estatístico)**: considera o grau de segurança e a vida útil da edificação.

O fator $S_2$ depende da **categoria do terreno** (rugosidade) e da **classe da edificação** (maior dimensão horizontal ou vertical da superfície frontal):

$$S_2=b\cdot F_r\cdot\left(\frac{z}{10}\right)^{p}$$

| Categoria | Terreno | $b$ | $p$ (classe A) |
|---|---|---:|---:|
| I | Superfícies lisas de grandes dimensões (mar calmo, lagos) | $1{,}10$ | $0{,}06$ |
| II | Terreno aberto, plano ou pouco ondulado, poucos obstáculos | $1{,}00$ | $0{,}085$ |
| III | Terreno plano ou ondulado, obstáculos baixos e esparsos (sebes, muros, casas isoladas) | $0{,}94$ | $0{,}10$ |
| IV | Obstáculos numerosos e pouco espaçados (zona urbanizada, industrial ou florestal) | $0{,}86$ | $0{,}12$ |
| V | Obstáculos numerosos, grandes, altos e pouco espaçados (centros de grandes cidades) | $0{,}74$ | $0{,}15$ |

**Classes**: A (maior dimensão até $20\text{ m}$), B (de $20$ a $50\text{ m}$) e C (acima de $50\text{ m}$). O fator $F_r$ vale $1{,}00$ (classe A), $0{,}98$ (B) e $0{,}95$ (C). Os parâmetros $b$ e $p$ da tabela são os da classe A; para as classes B e C, consulte a norma. Abaixo de $5\text{ m}$ de altura, adota-se o valor de $S_2$ calculado para $z=5\text{ m}$.

O fator estatístico $S_3$ é $1{,}10$ para edificações cuja ruína afeta a segurança ou o socorro (hospitais, quartéis), $1{,}00$ para edificações residenciais, comerciais e hotéis (grupo 2), $0{,}95$ para edificações de baixo fator de ocupação (depósitos, silos), $0{,}88$ e $0{,}83$ para vedações e construções temporárias.

```{admonition} Conferir na norma
:class: destaque-vermelho

Os valores de $b$, $p$, $F_r$ e $S_3$ acima são um resumo didático. Em qualquer projeto real, **confira as tabelas da NBR 6123** na edição em uso.
```

### Pressão dinâmica e força de arrasto

A velocidade característica produz uma **pressão dinâmica**:

$$q=0{,}613\,V_k^2\qquad (q\text{ em N/m}^2,\ V_k\text{ em m/s})$$

e a **força de arrasto** (a componente do vento na direção em que ele sopra) em uma área $A_e$ de superfície frontal é

$$F_a=C_a\cdot q\cdot A_e$$

O **coeficiente de arrasto** $C_a$ vem do gráfico da NBR 6123 para edificações em vento de **baixa turbulência**. Entra-se com a relação entre a altura e a largura frontal, $h/l_1$, e com a relação entre as dimensões em planta, $l_1/l_2$, em que $l_1$ é a dimensão **perpendicular** à direção do vento e $l_2$ é a dimensão **paralela**. Em regiões urbanas densas, o vento tende a ser de alta turbulência e a norma traz outro gráfico, com coeficientes diferentes.

### Força do vento em cada pavimento

A pressão cresce com a altura. Para aplicar o vento no modelo, concentramos a pressão em **forças horizontais nos níveis dos pavimentos**. Cada força atua na **faixa tributária** do pavimento: metade do pé-direito abaixo e metade do pé-direito acima. Para um pavimento $i$ à altura $z_i$, com largura frontal $L$:

$$F_{ve,i}=L\cdot\frac{h_i+h_{i+1}}{2}\cdot C_a\cdot q(z_i)\qquad\text{(pavimento intermediário)}$$

$$F_{ve,n}=L\cdot\frac{h_n}{2}\cdot C_a\cdot q(z_n)\qquad\text{(cobertura)}$$

em que $h_i$ é o pé-direito do lance imediatamente abaixo do pavimento $i$. Na cobertura, a faixa tributária tem apenas a metade de baixo (se houver platibanda ou ático, acrescente-se a sua parcela).

```{figure} ../_static/aulas/verificacao-global/vento-forcas-pavimento.png
:alt: Elevação de um edifício de seis pavimentos com o perfil de pressão do vento à esquerda e uma força horizontal em cada pavimento à direita
:width: 85%
:align: center

Perfil de pressão $C_a\,q(z)$ e forças do vento por pavimento no edifício do Exemplo 1.
```

```{admonition} Exemplo 1: força do vento por pavimento
:class: destaque-verde

Edifício de 6 pavimentos com pé-direito de $3{,}0\text{ m}$ ($H=18\text{ m}$) e planta quadrada de $6\times6\text{ m}$, em zona urbana. Dados: $V_0=35\text{ m/s}$; $S_1=1{,}0$; terreno de categoria IV; classe A; $S_3=1{,}0$ (grupo 2).

**Coeficiente de arrasto.** $h/l_1=18/6=3$ e $l_1/l_2=6/6=1$. Lendo o gráfico de baixa turbulência, $C_a\approx1{,}2$ (leitura aproximada; no gráfico, a posição exata entre as curvas depende da escala).

**Exemplo de cálculo, pavimento 3** ($z=9\text{ m}$):

$$S_2=0{,}86\cdot1{,}00\cdot\left(\frac{9}{10}\right)^{0{,}12}=0{,}849$$

$$V_k=35\cdot1{,}0\cdot0{,}849\cdot1{,}0=29{,}7\text{ m/s}\ \Rightarrow\ q=0{,}613\cdot29{,}7^2=541\text{ N/m}^2=0{,}542\text{ kN/m}^2$$

$$F_{ve,3}=6{,}0\cdot\frac{3{,}0+3{,}0}{2}\cdot1{,}2\cdot0{,}542=11{,}7\text{ kN}$$

| Pavimento | $z$ (m) | $S_2$ | $V_k$ (m/s) | $q$ (kN/m²) | $C_a\,q$ (kN/m²) | $F_{ve}$ (kN) |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 3 | $0{,}791$ | $27{,}7$ | $0{,}470$ | $0{,}564$ | $10{,}16$ |
| 2 | 6 | $0{,}809$ | $28{,}3$ | $0{,}491$ | $0{,}590$ | $10{,}61$ |
| 3 | 9 | $0{,}849$ | $29{,}7$ | $0{,}542$ | $0{,}650$ | $11{,}70$ |
| 4 | 12 | $0{,}879$ | $30{,}8$ | $0{,}580$ | $0{,}696$ | $12{,}53$ |
| 5 | 15 | $0{,}903$ | $31{,}6$ | $0{,}612$ | $0{,}735$ | $13{,}22$ |
| 6 (cobertura) | 18 | $0{,}923$ | $32{,}3$ | $0{,}640$ | $0{,}767$ | $6{,}91$ |

A soma das forças é $65{,}1\text{ kN}$ e o momento de tombamento na base é $\sum F_{ve,i}z_i=672\text{ kN}\cdot\text{m}$. Pequenas diferenças na terceira casa decimal vêm do arredondamento.

**Comparação.** Uma estimativa rápida de pressão uniforme de $0{,}80\text{ kN/m}^2$ (valor usado no Exemplo 3) daria $0{,}80\cdot6\cdot3=14{,}4\text{ kN}$ por pavimento ($7{,}2\text{ kN}$ na cobertura), soma de $79{,}2\text{ kN}$ e momento de $778\text{ kN}\cdot\text{m}$: cerca de $20\%$ a mais na soma das forças e $16\%$ a mais no momento. É uma estimativa **a favor da segurança**, comum em pré-dimensionamento.
```

### Desaprumo

Mesmo sem vento, o edifício não é executado perfeitamente vertical. A NBR 6118 (item 11.3.3.4.1) manda considerar essa **imperfeição geométrica global** como um ângulo de desaprumo:

$$\theta_1=\frac{1}{100\sqrt{H}}\qquad\text{com}\qquad \frac{1}{300}\le\theta_1\le\frac{1}{200}\quad(H\text{ em m})$$

e, para uma estrutura com $n$ prumadas de pilares (as prumadas contínuas, do topo à fundação),

$$\theta_a=\theta_1\sqrt{\frac{1+1/n}{2}}.$$

```{figure} ../_static/aulas/verificacao-global/desaprumo.png
:alt: À esquerda, um pórtico de três prumadas fora de prumo com o ângulo θa; à direita, o mesmo pórtico vertical com forças horizontais FD em cada pavimento
:width: 85%
:align: center

O desaprumo é equivalente a forças horizontais proporcionais ao peso de cada pavimento.
```

O efeito do desaprumo é representado por **forças horizontais fictícias** em cada pavimento, proporcionais à carga vertical $P_i$ do pavimento:

$$F_{D,i}=\theta_a\cdot P_i$$

```{admonition} Vento e desaprumo não se somam
:class: destaque-azul

Considere o vento e o desaprumo em combinações **separadas**, e use, no cálculo dos esforços, o que produzir o **maior momento total na base**. Em geral, nos edifícios de alguns pavimentos, o vento é bem maior que o desaprumo. O desaprumo é mais importante em edifícios altos e leves, ou na direção em que o vento é pouco intenso.

Como valor mínimo de $\theta_1$, adotamos $1/300$, como nos exemplos da disciplina. A norma admite $1/400$ para estruturas de nós fixos: confira o item 11.3.3.4.1 da edição em uso.
```

Para o edifício do Exemplo 1 ($H=18\text{ m}$, cinco prumadas, $432\text{ kN}$ de carga característica por pavimento), $1/(100\sqrt{18})=1/424<1/300$; adota-se $\theta_1=1/300$. Então $\theta_a=\dfrac{1}{300}\sqrt{\dfrac{1+1/5}{2}}=2{,}58\times10^{-3}$ e $F_{D,i}=2{,}58\times10^{-3}\cdot432=1{,}12\text{ kN}$ por pavimento. O momento do desaprumo na base é $1{,}12\cdot(3+6+9+12+15+18)=70\text{ kN}\cdot\text{m}$, dez vezes menor que o do vento ($672\text{ kN}\cdot\text{m}$). O **vento governa**.

## Combinações de ações no ELU

Para a verificação global usamos as combinações últimas normais:

$$F_d=\gamma_g\,F_{gk}+\gamma_q\left(F_{q1k}+\sum\psi_{0j}\,F_{qjk}\right),\qquad\gamma_g=\gamma_q=1{,}4$$

em que $F_{gk}$ é a ação permanente (peso próprio e permanentes), $F_{q1k}$ é a ação variável **principal** e $\psi_{0j}F_{qjk}$ são as demais ações variáveis, reduzidas pelo fator $\psi_0$. Com carga de utilização e vento, há duas combinações a verificar:

| Combinação | Ação variável principal | Ação variável secundária | Cargas verticais de cálculo | Vento de cálculo |
|---|---|---|---|---|
| **1** | Utilização (carga acidental) | Vento, $\psi_0=0{,}6$ | $1{,}4\,G_k+1{,}4\,Q_k$ | $1{,}4\cdot0{,}6\,F_{ve,k}$ |
| **2** | Vento | Utilização, $\psi_0=0{,}5$ (residencial) | $1{,}4\,G_k+1{,}4\cdot0{,}5\,Q_k$ | $1{,}4\,F_{ve,k}$ |

Os coeficientes $\psi_0$ das cargas acidentais dependem do uso: $0{,}5$ em edifícios residenciais e $0{,}7$ em edifícios comerciais ou de escritórios; para o vento, $\psi_0=0{,}6$ (tabela de coeficientes $\psi$ na seção 11 da norma). A combinação 1 dá mais peso às cargas verticais e menos ao vento, e a combinação 2 faz o contrário. **Nenhuma das duas é sempre a mais crítica**, e por isso as duas são verificadas.

## O sistema de contraventamento e o pórtico equivalente

Os elementos que **resistem às ações horizontais**, em geral os pórticos formados por vigas e pilares e, quando existem, os pilares-parede e núcleos, formam o **sistema de contraventamento**. Em um pavimento com lajes rígidas no seu plano, todos os pórticos de uma direção sofrem o **mesmo deslocamento horizontal**, e a força do vento se distribui entre eles segundo suas rigidezes.

Para obter o deslocamento horizontal da estrutura no Ftool, que só trabalha com pórticos planos, usamos o recurso do **pórtico equivalente**:

1. Modele cada pórtico de contraventamento da direção do vento, lado a lado, com a sua geometria e a sua rigidez no plano.
2. Ligue os pórticos vizinhos, em **cada nível de pavimento**, com uma barra horizontal curta (por exemplo, $1\text{ m}$) com **rótulas nas duas extremidades** e rigidez axial grande. Essa barra (uma **biela**) transmite só força axial e obriga os pórticos a terem o mesmo deslocamento horizontal, como faz a laje.
3. Aplique as forças horizontais em um dos pórticos (por exemplo, no do extremo esquerdo). O resultado é o do conjunto.
4. Atribua às barras os módulos reduzidos da rigidez secante: $0{,}8\,E_{ci}$ aos pilares e $0{,}4\,E_{ci}$ às vigas (ver [Aula 04](004-modelos-estruturais.md)).

Os pilares isolados, sem vigas formando um pórtico na direção considerada, contribuem muito pouco para a rigidez lateral e **não entram** no contraventamento. Isso será conferido no Exercício 5.

## Parâmetro α

### Definição

O parâmetro de instabilidade $\alpha$ da NBR 6118 (item 15.5.2) é

$$\alpha=H_{tot}\sqrt{\frac{N_k}{E_{cs}I_c}}$$

em que:

- $H_{tot}$ é a altura total da estrutura, da fundação (ou de um nível pouco deslocável) ao topo;
- $N_k$ é a **soma de todas as cargas verticais** atuantes na estrutura (valor característico), acima do nível considerado;
- $E_{cs}I_c$ é a **rigidez à flexão equivalente** do sistema de contraventamento, isto é, a rigidez de um **pilar equivalente** de seção constante, engastado na base e livre no topo, com o mesmo deslocamento horizontal de topo que a estrutura real.

Para estruturas reticuladas (pórticos), obtemos $EI_{eq}$ aplicando uma força horizontal unitária no topo do pórtico equivalente e lendo o deslocamento horizontal do topo, $\delta_{topo}$:

$$EI_{eq}=\frac{F\,H_{tot}^{3}}{3\,\delta_{topo}}\qquad\left(\text{pilar em balanço com carga no topo: }\delta=\frac{FH^3}{3EI}\right)$$

```{figure} ../_static/aulas/verificacao-global/portico-equivalente-alfa.png
:alt: Três pórticos planos ligados por bielas, deformados por uma força unitária no topo, e o pilar equivalente com o mesmo deslocamento do topo
:width: 95%
:align: center

Pórtico equivalente com três pórticos ligados por bielas e pilar equivalente de rigidez $EI_{eq}$.
```

### Valor-limite e interpretação

A estrutura pode ser considerada de **nós fixos** se $\alpha\le\alpha_1$, com

| Número de andares $n$ | $\alpha_1$ |
|---|---|
| $n\le3$ | $0{,}2+0{,}1\,n$ |
| $n\ge4$, associação de pilares-parede e pórticos | $0{,}6$ |
| $n\ge4$, só pilares-parede | $0{,}7$ |
| $n\ge4$, só pórticos | $0{,}5$ |

O $\alpha$ é o **termômetro** da análise de 2ª ordem. Ele não depende da intensidade do vento, e sim da relação entre o peso total e a rigidez lateral: é uma característica da estrutura. Serve para uma **triagem rápida**, antes mesmo de definir o vento. Se $\alpha\le\alpha_1$, a estrutura é de nós fixos e a verificação termina. Se $\alpha>\alpha_1$, a estrutura **pode** ser de nós móveis, e calculamos o $\gamma_z$, que estima o acréscimo de esforços.

```{admonition} Qual rigidez usar no cálculo de α?
:class: destaque-vermelho

A expressão do $\alpha$ na NBR 6118 usa o módulo de elasticidade secante e a inércia da **seção bruta** de concreto, $E_{cs}I_c$, enquanto o $\gamma_z$ usa a rigidez reduzida de 15.7.3 (pilares $0{,}8$, vigas $0{,}4$ ou $0{,}5$). Os exemplos da disciplina aplicam a rigidez **reduzida** também no cálculo do $\alpha$, o que é mais conservador (o $\alpha$ resulta maior). Neste material, o Exemplo 2 calcula o $\alpha$ pelo critério da disciplina e confere o resultado com a seção bruta, e a Atividade 2 pede a comparação. **Confira o item 15.5.2 da edição da norma em uso** e adote o critério que o professor indicar.
```

````{admonition} Exemplo 2: determinação do parâmetro α
:class: destaque-verde

**Dados.** Edifício de 4 pavimentos com pé-direito de $3{,}0\text{ m}$ ($H_{tot}=12\text{ m}$), planta de $6\times8\text{ m}$ (área de $48\text{ m}^2$), carga de $10\text{ kN/m}^2$ por pavimento, concreto com $f_{ck}=20\text{ MPa}$ e brita de granito ($\alpha_E=1{,}0$). Pilares de canto ($20\times20$ cm), pilares P2 e P5 ($20\times40$ cm, lado de $40$ cm no plano do pórtico) e vigas $12\times40$ cm. Vento na direção y, em que há três pórticos de $6{,}0\text{ m}$ de vão: P1-P4, P2-P5 e P3-P6.

```{figure} ../_static/aulas/verificacao-global/plantas-exemplos.png
:alt: Plantas dos edifícios dos Exemplos 2 e 3, com a posição e a seção dos pilares e a direção do vento
:width: 95%
:align: center

Plantas dos Exemplos 2 (esquerda) e 3 (direita).
```

**1. Módulos de elasticidade.**

$$E_{ci}=1{,}0\cdot5600\sqrt{20}=25\,043{,}96\text{ MPa}\qquad \alpha_i=0{,}80+0{,}20\frac{20}{80}=0{,}85\qquad E_{cs}=0{,}85\cdot25\,043{,}96=21\,287{,}37\text{ MPa}$$

**2. Rigidez reduzida (processo da disciplina).** Pilares: $0{,}8\,E_{ci}=20\,035{,}17\text{ MPa}$. Vigas: $0{,}4\,E_{ci}=10\,017{,}58\text{ MPa}$.

**3. Carga vertical total.** $N_k=10\cdot(6\cdot8)\cdot4=1920\text{ kN}$.

**4. Deslocamento do topo.** Monte o pórtico equivalente (três pórticos ligados por bielas, como na figura), aplique $F=1\text{ kN}$ no nível do topo e leia o deslocamento horizontal. O Ftool fornece $\delta_{topo}=9{,}677\times10^{-4}\text{ m}$.

**5. Rigidez equivalente e α.**

$$EI_{eq}=\frac{1\cdot12^3}{3\cdot9{,}677\times10^{-4}}=5{,}95\times10^{5}\text{ kN}\cdot\text{m}^2\qquad\alpha=12\sqrt{\frac{1920}{5{,}95\times10^{5}}}=0{,}68$$

**6. Comparação.** Estrutura só de pórticos com $n=4$: $\alpha_1=0{,}5$. Como $\alpha=0{,}68>0{,}5$, a estrutura **pode ser de nós móveis**: é preciso calcular o $\gamma_z$.

**7. Conferência com a seção bruta.** Com $E_{cs}$ e a inércia bruta em todas as barras, o mesmo procedimento fornece $\delta_{topo}\approx6{,}1\times10^{-4}\text{ m}$ e $\alpha\approx0{,}54$. O valor é menor, mas ainda maior que $0{,}5$, e a conclusão é a mesma.

Os valores de $\delta_{topo}$ obtidos por quem refizer o modelo podem diferir na terceira casa significativa (por exemplo, pelo comprimento da biela ou pela discretização).
````

## Coeficiente γz

### Definição

O $\alpha$ indica se a estrutura é sensível ao efeito de 2ª ordem global; o **$\gamma_z$** (item 15.5.3) estima **quanto** os esforços crescem. Ele usa o **momento de tombamento** $M_{1,tot,d}$ e o **acréscimo de momento** $\Delta M_{tot,d}$ da primeira seção desta aula:

$$\gamma_z=\frac{1}{1-\dfrac{\Delta M_{tot,d}}{M_{1,tot,d}}}$$

com $M_{1,tot,d}=\sum F_{H,i,d}\,z_i$ e $\Delta M_{tot,d}=\sum P_{i,d}\,\delta_i$, em que:

- $F_{H,i,d}$ são as forças horizontais de cálculo (vento ou desaprumo) do pavimento $i$ e $z_i$ a altura do pavimento;
- $P_{i,d}$ é a **soma de todas as cargas verticais de cálculo** do pavimento $i$ (de todos os pilares, também dos que não contraventam);
- $\delta_i$ é o deslocamento horizontal do pavimento $i$ obtido em **análise de 1ª ordem**, com as forças horizontais de cálculo e com a **rigidez reduzida** (pilares $0{,}8\,E_{ci}I_c$; vigas $0{,}4\,E_{ci}I_c$ ou $0{,}5\,E_{ci}I_c$ conforme a armadura; lajes $0{,}3\,E_{ci}I_c$ quando fazem parte do pórtico).

**De onde vem a fórmula.** O momento de 1ª ordem $M_1$ produz deslocamentos que geram o acréscimo $\Delta M=r\,M_1$, com $r=\Delta M/M_1$. Esse acréscimo gera novos deslocamentos, proporcionais, que geram um acréscimo $r\cdot\Delta M=r^2M_1$, e assim por diante. O momento total é a soma de uma progressão geométrica de razão $r<1$:

$$M_{tot}=M_1\,(1+r+r^2+r^3+\dots)=\frac{M_1}{1-r}=\gamma_z\,M_1$$

Por isso, $\gamma_z$ é um **fator de amplificação**: se $\gamma_z=1{,}08$, os momentos finais são cerca de $8\%$ maiores que os de 1ª ordem. Também se vê que a fórmula só faz sentido para $r<1$ e perde precisão quando $r$ se aproxima de $1$.

### Classificação e uso

| $\gamma_z$ | Classificação | O que fazer |
|---|---|---|
| $\le1{,}1$ | Nós fixos | Os efeitos globais de 2ª ordem podem ser desprezados. |
| $1{,}1<\gamma_z\le1{,}3$ | Nós móveis | Multiplicar os esforços **horizontais** (vento) de 1ª ordem por $0{,}95\,\gamma_z$ (item 15.7.2) e somar às cargas verticais. |
| $>1{,}3$ | Nós móveis, muito deslocável | O processo aproximado não vale. É preciso uma análise de 2ª ordem completa (por exemplo, $P$-$\Delta$ iterativo) e, em geral, mais rigidez. |

```{admonition} O que o γz mostra
:class: destaque-azul

1. **O $\gamma_z$ não depende da intensidade do vento**, apenas da razão entre peso e rigidez e da forma como a carga horizontal se distribui em altura. Se o vento dobrasse, $M_1$ e $\Delta M$ dobrariam e a razão não mudaria. Por isso o $\gamma_z$ de um edifício de pórticos usuais é pouco sensível à estimativa do vento.
2. **O $\gamma_z$ muda com a combinação**, pois as cargas verticais de cálculo $P_{i,d}$ mudam. Verifique sempre as duas combinações.
3. Para reduzir o $\gamma_z$, é preciso **aumentar a rigidez lateral** (seção e inércia dos pilares na direção do vento, altura das vigas, pilares-parede) ou reduzir o peso, e não reduzir o vento.
```

````{admonition} Exemplo 3: determinação do coeficiente γz
:class: destaque-verde

**Dados.** Edifício de 6 pavimentos com pé-direito de $3{,}0\text{ m}$ ($H=18\text{ m}$), planta de $6\times6\text{ m}$ com quatro lajes e cinco pilares (figura do Exemplo 2). Concreto com $f_{ck}=20\text{ MPa}$ e brita de granito. Carga estimada no piso de $12\text{ kN/m}^2$, sendo $60\%$ permanente e $40\%$ acidental (residencial). Vento estimado de $0{,}80\text{ kN/m}^2$ na direção y. Todas as vigas $20\times50$ cm. Pilares: P1 e P5 com $70$ cm paralelos a x e $20$ cm paralelos a y; P2 e P4 com $20$ cm paralelos a x e $70$ cm paralelos a y; P3 de $20\times20$ cm. **O pilar P3 não participa do contraventamento.** Direção do vento: y, vertical na planta.

**1. Cargas verticais por pavimento.**

$$N_k=12\cdot(6\cdot6)=432\text{ kN}\qquad G_k=0{,}60\cdot432=259{,}2\text{ kN}\qquad Q_k=0{,}40\cdot432=172{,}8\text{ kN}$$

**2. Vento por pavimento** (área frontal $6\cdot3=18\text{ m}^2$ por pavimento):

$$F_{ve,k}=0{,}80\cdot(6\cdot3)=14{,}4\text{ kN}\ (\text{pavimentos }1\text{ a }5)\qquad F_{ve,k}=\frac{14{,}4}{2}=7{,}2\text{ kN}\ (\text{cobertura})$$

**3. Combinações do ELU.**

| | Cargas verticais por pavimento $P_{i,d}$ | Vento por pavimento $F_{H,i,d}$ | Cobertura |
|---|---:|---:|---:|
| Combinação 1 | $1{,}4\cdot259{,}2+1{,}4\cdot172{,}8=604{,}8\text{ kN}$ | $1{,}4\cdot0{,}6\cdot14{,}4=12{,}10\text{ kN}$ | $6{,}05\text{ kN}$ |
| Combinação 2 | $1{,}4\cdot259{,}2+1{,}4\cdot0{,}5\cdot172{,}8=483{,}84\text{ kN}$ | $1{,}4\cdot14{,}4=20{,}16\text{ kN}$ | $10{,}08\text{ kN}$ |

**4. Modelo.** Dois pórticos de $6{,}0\text{ m}$ de vão (P1-P4 e P2-P5), com pilares e vigas de rigidez reduzida: $E_{pilar}=0{,}8\cdot25\,043{,}96=20\,035{,}17\text{ MPa}$ e $E_{viga}=0{,}4\cdot25\,043{,}96=10\,017{,}58\text{ MPa}$. Os pórticos são ligados por bielas em cada pavimento. As forças horizontais são aplicadas no pórtico da esquerda.

```{figure} ../_static/aulas/verificacao-global/deformada-gama-z.png
:alt: Dois pórticos de seis pavimentos ligados por bielas, com as forças horizontais da combinação 1 e a deformada com os deslocamentos de cada pavimento
:width: 90%
:align: center

Pórtico equivalente do Exemplo 3 na combinação 1, com os deslocamentos de cada pavimento.
```

**5. Planilha da combinação 1** ($M_{1,i}=F_{H,i,d}\,z_i$; $\Delta M_i=P_{i,d}\,\delta_i$; $P_{i,d}=604{,}8\text{ kN}$ em todos os pavimentos):

| Pavimento | $\delta_i$ (cm) | $z_i$ (m) | $F_{H,i,d}$ (kN) | $M_{1,i}$ (kN·m) | $\Delta M_i$ (kN·m) |
|---:|---:|---:|---:|---:|---:|
| 1 | $0{,}26$ | 3 | $12{,}10$ | $36{,}3$ | $1{,}57$ |
| 2 | $0{,}75$ | 6 | $12{,}10$ | $72{,}6$ | $4{,}54$ |
| 3 | $1{,}24$ | 9 | $12{,}10$ | $108{,}9$ | $7{,}50$ |
| 4 | $1{,}64$ | 12 | $12{,}10$ | $145{,}2$ | $9{,}92$ |
| 5 | $1{,}92$ | 15 | $12{,}10$ | $181{,}5$ | $11{,}61$ |
| 6 | $2{,}11$ | 18 | $6{,}05$ | $108{,}9$ | $12{,}76$ |
| **Soma** | | | | **$653{,}4$** | **$47{,}9$** |

$$\gamma_z=\frac{1}{1-\dfrac{47{,}9}{653{,}4}}=\frac{1}{1-0{,}0733}=1{,}079\approx1{,}08$$

**6. Combinação 2.** Todas as forças horizontais são multiplicadas por $20{,}16/12{,}10=1{,}667$, e as cargas verticais, por $483{,}84/604{,}8=0{,}8$. Como os deslocamentos são proporcionais à força horizontal, $\Delta M_{tot}$ passa a $47{,}9\cdot1{,}667\cdot0{,}8=63{,}9\text{ kN}\cdot\text{m}$ e $M_{1,tot}$ a $653{,}4\cdot1{,}667=1089\text{ kN}\cdot\text{m}$:

$$\gamma_z=\frac{1}{1-63{,}9/1089}=1{,}06$$

**7. Conclusão.** O maior valor é $\gamma_z=1{,}08\le1{,}1$ (combinação 1). A estrutura é de **nós fixos** nesta direção, e os efeitos globais de 2ª ordem podem ser desprezados.

**8. Deslocamentos em serviço.** Para a combinação frequente, o vento atua com $\psi_1=0{,}3$. Pela proporcionalidade, em relação à combinação 1 (que usa $1{,}4\cdot0{,}6=0{,}84$ do vento característico), o fator é $0{,}3/0{,}84=0{,}357$. O deslocamento do topo é $2{,}11\cdot0{,}357=0{,}75\text{ cm}$, menor que $H/1700=1800/1700=1{,}06\text{ cm}$. O maior deslocamento relativo entre pavimentos é $0{,}49\text{ cm}$ (nos lances entre os pavimentos 1 e 2 e entre 2 e 3), ou $0{,}49\cdot0{,}357=0{,}17\text{ cm}$, menor que $H_i/850=300/850=0{,}35\text{ cm}$. Os dois limites são atendidos, mesmo com a rigidez reduzida do ELU, que é conservadora para esta verificação.
````

### Limitação de deslocamentos

Além da estabilidade, a norma limita os deslocamentos horizontais em serviço para evitar danos a paredes, esquadrias e revestimentos e desconforto aos usuários. Para o movimento lateral devido ao vento, na combinação frequente de ações ($\psi_1=0{,}3$ para o vento), os limites da Tabela 13.3 da NBR 6118 são:

| Deslocamento | Limite |
|---|---|
| Deslocamento horizontal total no topo | $H/1700$ |
| Deslocamento relativo entre dois pavimentos consecutivos | $H_i/850$ |

em que $H$ é a altura total do edifício e $H_i$ é o pé-direito do andar $i$. Confira os valores e as condições de aplicação na edição da norma em uso.

## Atividade em sala 1: ações horizontais

### Exercício 1: vento em outro terreno

Repita o Exemplo 1 para o **mesmo edifício**, mas em **terreno de categoria II** (campo aberto), classe A, com $V_0=35\text{ m/s}$, $S_1=S_3=1{,}0$ e $C_a=1{,}2$.

1. Calcule $S_2$, $V_k$, $q$ e $C_a q$ em cada pavimento e a força $F_{ve,i}$.
2. Preencha a tabela e calcule a soma das forças e o momento de tombamento na base.
3. Compare com o resultado do Exemplo 1 (categoria IV) e com a estimativa de $0{,}80\text{ kN/m}^2$. Que categoria de terreno essa estimativa representa melhor?

| Pavimento | $z$ (m) | $S_2$ | $V_k$ (m/s) | $q$ (kN/m²) | $C_a q$ (kN/m²) | $F_{ve}$ (kN) |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 3 | | | | | |
| 2 | 6 | | | | | |
| 3 | 9 | | | | | |
| 4 | 12 | | | | | |
| 5 | 15 | | | | | |
| 6 | 18 | | | | | |
| **Soma** | | | | | | |

### Exercício 2: o vento ou o desaprumo?

Para o edifício do Exemplo 3 (cargas características de $432\text{ kN}$ por pavimento, cinco prumadas de pilares) e o vento do Exercício 1:

1. Calcule $\theta_1$ e $\theta_a$ (verifique em que limite $\theta_1$ cai).
2. Calcule $F_{D,i}$ em cada pavimento e o momento do desaprumo na base.
3. Compare com o momento do vento do Exercício 1. Qual deve ser usado na combinação?
4. Em que tipo de edifício o desaprumo poderia governar?

## Atividade em sala 2: o parâmetro α no Ftool

### Exercício 3: pórtico equivalente e α

Use o edifício do Exemplo 2 (a sua planta está na figura anterior). Seções necessárias:

| Seção | $A\ (\text{m}^2)$ | $I\ (\text{m}^4)$ |
|---|---:|---:|
| Pilar $20\times20$ | $0{,}040$ | $1{,}333\times10^{-4}$ |
| Pilar $20\times40$ (lado de $40$ cm no plano) | $0{,}080$ | $1{,}067\times10^{-3}$ |
| Pilar $20\times40$ (lado de $20$ cm no plano) | $0{,}080$ | $2{,}667\times10^{-4}$ |
| Viga $12\times40$ | $0{,}048$ | $6{,}400\times10^{-4}$ |

Módulos em kN/m²: $E_{ci}=2{,}504\times10^{7}$, $0{,}8E_{ci}=2{,}004\times10^{7}$, $0{,}4E_{ci}=1{,}002\times10^{7}$, $E_{cs}=2{,}129\times10^{7}$.

1. Monte o pórtico equivalente (três pórticos de $6{,}0\text{ m}$ de vão, ligados por bielas de $1{,}0\text{ m}$ com rótulas nas duas extremidades) e aplique $1\text{ kN}$ no topo do primeiro pórtico. Registre $\delta_{topo}$ e calcule $EI_{eq}$ e $\alpha$ com a **rigidez reduzida**.
2. Repita com a **seção bruta** e $E_{cs}$ em todas as barras. Compare os dois valores de $\alpha$ e diga se a conclusão sobre os nós fixos muda.
3. Gire os pilares P2 e P5 (lado de $40$ cm perpendicular ao plano do pórtico). Quanto muda o $\alpha$?
4. A estrutura precisa ficar com $\alpha\le0{,}5$ (critério da disciplina, rigidez reduzida). Teste, uma de cada vez, as intervenções: (i) vigas $12\times50$; (ii) vigas $12\times60$; (iii) vigas $20\times50$; (iv) pilares P2 e P5 com $20\times60$; (v) pilares P2 e P5 com $20\times100$. Qual intervenção é mais eficaz? Qual é mais viável do ponto de vista arquitetônico?

| Caso | $\delta_{topo}$ (m) | $EI_{eq}$ (kN·m²) | $\alpha$ | $\alpha\le0{,}5$? |
|---|---:|---:|---:|---|
| Reduzida, P2 e P5 com $40$ cm no plano | | | | |
| Bruta ($E_{cs}$), P2 e P5 com $40$ cm no plano | | | | |
| Reduzida, P2 e P5 com $20$ cm no plano | | | | |
| Reduzida, vigas $12\times50$ | | | | |
| Reduzida, vigas $12\times60$ | | | | |
| Reduzida, vigas $20\times50$ | | | | |
| Reduzida, P2 e P5 $20\times60$ | | | | |
| Reduzida, P2 e P5 $20\times100$ | | | | |

## Atividade em sala 3: o coeficiente γz no Ftool

### Exercício 4: reproduzir o Exemplo 3

Seções necessárias:

| Seção | $A\ (\text{m}^2)$ | $I\ (\text{m}^4)$ |
|---|---:|---:|
| Pilar com $70$ cm no plano de flexão | $0{,}140$ | $5{,}717\times10^{-3}$ |
| Pilar com $20$ cm no plano de flexão | $0{,}140$ | $4{,}667\times10^{-4}$ |
| Viga $20\times50$ | $0{,}100$ | $2{,}083\times10^{-3}$ |
| Pilar P3 $20\times20$ | $0{,}040$ | $1{,}333\times10^{-4}$ |

Módulos em kN/m²: pilares $2{,}004\times10^{7}$ e vigas $1{,}002\times10^{7}$.

1. No vento na direção y, quais pilares têm $70$ cm no plano de flexão? (Use a figura da planta.) Monte os dois pórticos de $6{,}0\text{ m}$ de vão ligados por bielas.
2. Aplique as forças horizontais da **combinação 1** ($12{,}10\text{ kN}$ nos pavimentos 1 a 5 e $6{,}05\text{ kN}$ na cobertura). Registre os deslocamentos $\delta_i$ e confira a tabela do Exemplo 3 (diferenças de até $0{,}02\text{ cm}$ são esperadas).
3. Calcule $M_{1,tot,d}$, $\Delta M_{tot,d}$ e $\gamma_z$.
4. Repita para a **combinação 2** (basta escalar os resultados, como no exemplo, ou refazer o modelo). Qual combinação governa?
5. Verifique os deslocamentos do ELS-frequente: topo e relativo entre pavimentos.
6. Calcule também o $\alpha$ do edifício ($N_k=432\cdot6=2592\text{ kN}$, $H_{tot}=18\text{ m}$), aplicando $1\text{ kN}$ no topo do pórtico equivalente: (i) com a rigidez reduzida e (ii) com a seção bruta e $E_{cs}$. Compare com $\alpha_1=0{,}5$ e com o $\gamma_z$ do item 3.

### Exercício 5: o que muda no γz?

Parta do Exercício 4 e responda, calculando $\gamma_z$ em cada caso:

1. **O pilar P3 contraventa?** Inclua P3 ($20\times20$) como um terceiro "pórtico" de uma única prumada, ligado por biela aos demais. O $\gamma_z$ muda de forma apreciável? A hipótese do enunciado é razoável?
2. **Vento de outro terreno.** Use as forças do Exercício 1 (categoria II), com os mesmos fatores de combinação. O $\gamma_z$ muda? Explique.
3. **Pilares na posição desfavorável.** Gire os quatro pilares (P1, P2, P4, P5) para que todos tenham $20$ cm no plano de flexão. Calcule o novo $\gamma_z$, classifique a estrutura e, se for o caso, calcule o fator $0{,}95\gamma_z$ pelo qual os esforços horizontais de 1ª ordem devem ser multiplicados.
4. **Mais pavimentos.** Mantendo a planta e os pilares do Exemplo 3, aumente o número de pavimentos (8, 10, 12 e 16; $N_k$, $P_{i,d}$ e $F_{H,i,d}$ seguem a mesma lei) e determine o $\gamma_z$ de cada caso. A partir de quantos pavimentos a estrutura deixa de ser de nós fixos? E de quantos o processo aproximado ($\gamma_z\le1{,}3$) deixa de valer?

| Caso | $\delta_{topo}$ (cm) | $M_{1,tot,d}$ (kN·m) | $\Delta M_{tot,d}$ (kN·m) | $\gamma_z$ | Classificação |
|---|---:|---:|---:|---:|---|
| Exemplo 3, comb. 1 | | | | | |
| Exemplo 3, comb. 2 | | | | | |
| P3 contraventando | | | | | |
| Vento da categoria II | | | | | |
| Pilares todos com $20$ cm no plano | | | | | |
| 8 pavimentos | | | | | |
| 10 pavimentos | | | | | |
| 12 pavimentos | | | | | |
| 16 pavimentos | | | | | |

### Para discutir em sala

- No Exemplo 3, o $\alpha$ calculado com a rigidez reduzida resulta acima do limite, enquanto o $\gamma_z$ é inferior a $1{,}1$. Como isso se explica? O que muda se o $\alpha$ for calculado com a seção bruta?
- Por que o $\gamma_z$ não muda quando o vento muda de intensidade, mas muda quando a combinação muda?
- O que o projetista pode fazer, na planta de fôrma, para reduzir o $\gamma_z$? Em que fase do projeto essa decisão deve ser tomada?
- Que hipóteses do pórtico equivalente podem falhar em um edifício real (lajes flexíveis, torção, pilares-parede, fundação deformável)?

## Síntese

```{admonition} O que levar desta aula
:class: destaque-azul

1. Os deslocamentos laterais do edifício, combinados com as cargas verticais, produzem momentos adicionais $\Delta M=\sum P_i\delta_i$: é o efeito de 2ª ordem **global**.
2. As ações horizontais são o **vento** (NBR 6123) e o **desaprumo**. O vento por pavimento depende de $V_k=V_0S_1S_2S_3$, de $q=0{,}613V_k^2$, do coeficiente de arrasto $C_a$ e da faixa tributária. O desaprumo equivale a $F_{D,i}=\theta_aP_i$. As duas ações não se somam, e vale a que gera o maior momento na base.
3. Verificam-se **duas combinações** do ELU: utilização como variável principal (vento com $\psi_0=0{,}6$) e vento como variável principal.
4. O **pórtico equivalente** liga pórticos planos por bielas e permite obter o deslocamento do topo e a rigidez $EI_{eq}=FH^3/(3\delta_{topo})$ no Ftool.
5. O **parâmetro α** depende só da altura, do peso e da rigidez lateral. Se $\alpha\le\alpha_1$, a estrutura é de nós fixos. Ele é um termômetro, não uma medida do acréscimo de esforços.
6. O **$\gamma_z=1/(1-\Delta M/M_1)$** é o fator de amplificação dos esforços. Com $\gamma_z\le1{,}1$ a estrutura é de nós fixos; até $1{,}3$, majoram-se os esforços horizontais por $0{,}95\gamma_z$; acima disso, é preciso uma análise de 2ª ordem completa.
7. O $\gamma_z$ não depende da intensidade do vento, mas da razão peso/rigidez. Para reduzi-lo, aumente a rigidez lateral.
8. Em serviço, os deslocamentos laterais são limitados a $H/1700$ no topo e $H_i/850$ entre pavimentos.
```

Com o sistema verificado, a estrutura de lajes, vigas e pilares pode ser detalhada com a segurança de que as hipóteses de nós fixos (ou o fator de amplificação adotado) estão registradas. As próximas aulas voltam ao estudo das lajes.

## Referências

- PEREIRA JUNIOR, Wanderlei Malaquias. *Carga de vento em edifícios*, *Exemplo 01: determinação do coeficiente alfa* e *Exemplo 02: determinação do gamma z*. Material do professor (Estruturas de Concreto Armado 1, aulas 13, 21 e 22). Base para a organização da aula, os dados dos Exemplos 2 e 3 e as expressões do vento por pavimento e do desaprumo.
- ABNT. *NBR 6123: Forças devidas ao vento em edificações*. Rio de Janeiro, 1988.
- ABNT. *NBR 6118: Projeto de estruturas de concreto*. Rio de Janeiro, 2023. Itens 11.3.3.4 (imperfeições geométricas globais), seção 11 (ações e combinações), 13.3 (deslocamentos-limite), 15.4 (efeitos de 2ª ordem), 15.5 (parâmetro de instabilidade α e coeficiente γz) e 15.7 (processo aproximado e não linearidade física).
- MARTHA, Luiz Fernando. *Ftool: Two-dimensional Frame Analysis Tool*. Grupo de Tecnologia em Computação Gráfica, PUC-Rio. Disponível em: <https://www.tecgraf.puc-rio.br/ftool>.
