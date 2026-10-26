# Aula 04: Modelos estruturais: edifício, vigas e pilares

Até aqui, a estrutura foi lançada, pré-dimensionada e carregada. Falta responder a uma pergunta que antecede o projeto de qualquer laje, viga ou pilar: **como transformamos um edifício real em um modelo que o engenheiro consiga resolver, e o que esse modelo pode ou não nos dizer?**

A aula começa pelos tipos de análise estrutural previstos na norma, passa pelo modo simplificado de considerar a fissuração do concreto e chega aos modelos usados no edifício: caminho das cargas, pórtico plano e pórtico espacial. Em seguida, escolhe um elemento, a **viga**, e examina como as hipóteses sobre os **pilares** que a sustentam mudam seus esforços. Nas duas atividades em sala, usamos o Ftool para comparar modelos de um mesmo edifício e perceber, em números, o que cada hipótese muda. Os esforços das vigas V1 a V6 do trabalho prático serão obtidos com esses modelos.

```{admonition} Objetivos da aula
:class: destaque-azul

- Distinguir análise linear e não linear e reconhecer as três fontes de não linearidade.
- Explicar, com um exemplo, a diferença entre análise de 1ª e de 2ª ordem.
- Aplicar os coeficientes de rigidez reduzida da NBR 6118 em uma análise global.
- Reconhecer o papel das lajes no sistema estrutural, inclusive como diafragma.
- Comparar os modelos de caminho das cargas, pórtico plano e pórtico espacial.
- Extrair um pórtico plano de um edifício tridimensional e montá-lo no Ftool.
- Montar o modelo de viga contínua e aplicar as correções previstas na NBR 6118.
- Calcular a rigidez de um pilar e seu efeito no momento de extremidade da viga.
- Distinguir os modelos de viga contínua, pórtico H e pórtico plano e avaliar a influência da orientação, da seção e do pé-direito dos pilares.
- Avaliar o efeito de apoios deformáveis (recalque) em uma viga contínua.
```

## O que é analisar uma estrutura?

Analisar uma estrutura é determinar, para um conjunto de ações, os **esforços** (normal, cortante, momento fletor e momento de torção), as **reações de apoio** e os **deslocamentos** dos elementos. O edifício real é complexo demais para ser resolvido diretamente. Por isso, substituímos a estrutura por um **modelo estrutural**: uma idealização com geometria, vínculos, propriedades dos materiais e ações definidos pelo projetista.

Todo modelo é uma lista de decisões:

| Decisão | Pergunta que o projetista responde | Exemplo |
|---|---|---|
| Geometria | Quais elementos entram e como são representados? | Vigas e pilares como barras no eixo; lajes como cargas ou como diafragma. |
| Vínculos | Como a estrutura se liga ao solo e como os elementos se ligam entre si? | Pilar engastado na fundação; viga rotulada ou engastada no pilar. |
| Material | Qual rigidez cada elemento terá? | $E_{ci}I_c$ do concreto bruto ou rigidez reduzida pela fissuração. |
| Ações | Que cargas e em que posição? | Cargas verticais das lajes; vento em cada pavimento. |
| Tipo de análise | O equilíbrio é escrito na posição inicial ou na deformada? O material é linear? | Análise linear de 1ª ordem; análise com efeitos de 2ª ordem. |

Os resultados valem para o modelo, não para o edifício. Um bom projetista conhece as hipóteses do modelo que usa e sabe em que situações elas deixam de representar o comportamento real.

## Tipos de análise estrutural

Há duas perspectivas gerais: a análise **linear** e a análise **não linear**. A NBR 6118, no item 14.5, detalha os tipos admitidos: análise linear, análise linear com redistribuição, análise plástica, análise não linear e análise por meio de modelos físicos. Nesta disciplina trabalharemos principalmente com a análise linear, ajustada por coeficientes que representam, de forma simplificada, a não linearidade física.

Na **análise linear**, supõe-se que os deslocamentos sejam pequenos, que o material siga a lei de Hooke e que os apoios não mudem de condição. As equações de equilíbrio são escritas na geometria indeformada e vale a **superposição de efeitos**: dobrar as ações dobra os esforços.

A **análise não linear** abandona uma ou mais dessas hipóteses. Há três fontes de não linearidade:

| Tipo | O que deixa de valer | Exemplo no concreto armado |
|---|---|---|
| Não linearidade **física** | A relação entre tensão e deformação (ou entre momento e curvatura) não é linear. | Fissuração, escoamento do aço, fluência e comportamento não linear do concreto comprimido. |
| Não linearidade **geométrica** | O equilíbrio deve ser escrito na posição deformada. | Efeitos de 2ª ordem em pilares esbeltos e em edifícios altos. |
| Não linearidade de **contato** | A condição de apoio muda durante o carregamento. | Apoio unilateral que se descola, cantos de laje que levantam. |

### Primeira e segunda ordem

Considere um pilar em balanço, de comprimento $l_e$, submetido a uma força horizontal $F_H$ e a uma força vertical $F_V$ no topo.

```{figure} ../_static/aulas/modelos-estruturais/console-1a-2a-ordem.png
:alt: Pilar em balanço com forças horizontal e vertical no topo, em análise de primeira ordem e em análise de segunda ordem
:width: 80%
:align: center

Pilar em balanço sob $F_H$ e $F_V$. À esquerda, o equilíbrio na posição indeformada; à direita, o equilíbrio na posição deformada.
```

Na análise de **1ª ordem**, o equilíbrio é escrito na posição inicial. O momento no engaste vale

$$
M_1=F_H\,l_e .
$$

Na análise de **2ª ordem**, o equilíbrio é escrito na posição deformada. O topo se desloca $u$ e a força vertical passa a ter excentricidade em relação ao engaste:

$$
M_2=F_H\,l_e+F_V\,u .
$$

O deslocamento $u$ depende de $M_2$, e $M_2$ depende de $u$: o problema é não linear. Quanto maior $F_V$ em relação à carga crítica do pilar, maior o acréscimo de momento. Em edifícios, os efeitos de 2ª ordem são classificados pela norma (item 15.4) em **globais** (deslocamento horizontal da estrutura como um todo), **locais** (flexão de um lance de pilar entre pavimentos) e **localizados** (por exemplo, em pilares-parede).

### Não linearidade física: o processo simplificado

A fissuração faz a rigidez à flexão do concreto armado cair com o aumento do carregamento. Para uma análise global, a NBR 6118 (item 15.7.3) permite considerar essa não linearidade física de forma aproximada, substituindo a rigidez $E_{ci}I_c$ da seção bruta por uma **rigidez secante** reduzida:

| Elemento | Rigidez secante |
|---|---|
| Lajes | $(EI)_{sec}=0{,}30\,E_{ci}I_c$ |
| Vigas com $A_s'\neq A_s$ | $(EI)_{sec}=0{,}40\,E_{ci}I_c$ |
| Vigas com $A_s'=A_s$ | $(EI)_{sec}=0{,}50\,E_{ci}I_c$ |
| Pilares | $(EI)_{sec}=0{,}80\,E_{ci}I_c$ |

Aqui, $I_c$ é o momento de inércia da seção bruta de concreto e $A_s'$ e $A_s$ são as áreas das armaduras comprimida e tracionada da viga. O módulo de elasticidade inicial é $E_{ci}=5600\sqrt{f_{ck}}$, com $E_{ci}$ e $f_{ck}$ em MPa (para granito e gnaisse).

Os coeficientes representam a perda média de rigidez de cada elemento no estado limite último e são usados na análise global da estrutura, em especial na verificação da estabilidade e dos efeitos de 2ª ordem. Eles **não substituem** o cálculo de flechas de lajes e vigas, que usa a rigidez equivalente de Branson no estado de serviço. A norma restringe o processo a estruturas reticuladas com no mínimo quatro andares; os exemplos desta aula têm menos pavimentos por razões didáticas.

```{admonition} Exemplo: rigidez secante de uma viga e de um pilar
:class: destaque-verde

Concreto C30: $E_{ci}=5600\sqrt{30}\approx30\,672\text{ MPa}=3{,}067\times10^{7}\text{ kN/m}^2$.

**Viga $14\times50$ cm:** $I_c=0{,}14\times0{,}50^3/12=1{,}458\times10^{-3}\text{ m}^4$, logo $E_{ci}I_c\approx44\,730\text{ kN}\cdot\text{m}^2$.
Com $0{,}40$: $(EI)_{sec}\approx17\,890\text{ kN}\cdot\text{m}^2$.

**Pilar $20\times50$ cm** (flexão no plano da dimensão de $50$ cm): $I_c=0{,}20\times0{,}50^3/12=2{,}083\times10^{-3}\text{ m}^4$, logo $E_{ci}I_c\approx63\,900\text{ kN}\cdot\text{m}^2$.
Com $0{,}80$: $(EI)_{sec}\approx51\,120\text{ kN}\cdot\text{m}^2$.
```

## Do edifício ao modelo

O edifício é uma estrutura espacial formada por lajes, vigas e pilares ligados entre si. Para analisá-lo, podemos adotar modelos com graus diferentes de refinamento.

### As lajes no sistema estrutural

Vigas e pilares são representados como barras. As lajes são **elementos de superfície**: têm duas dimensões muito maiores que a espessura. Quando recebem ações perpendiculares ao seu plano, trabalham como **placas**. Quando as ações estão contidas no próprio plano, trabalham como **chapas**. Se a superfície for curva, temos uma **casca**.

```{figure} ../_static/aulas/introducao-lajes/placa-casca-chapa.png
:alt: Representações de placa, casca e chapa para comparação de geometria e direção das ações
:width: 80%
:align: center

Elementos de superfície. Figura do material do professor.
```

Em um edifício com vigamento, os apoios das lajes são, em geral, as vigas que contornam os painéis. Em uma laje lisa, a ligação ocorre diretamente com os pilares. A mudança de sistema altera o comportamento: o apoio pontual exige examinar, entre outras questões, a punção na região do pilar.

A laje também participa da estabilidade do conjunto. Quando possui rigidez no próprio plano e ligações adequadas, o pavimento atua como **diafragma**, vinculando os deslocamentos horizontais dos elementos verticais. É essa hipótese que o pórtico espacial adota, como se verá adiante. Na flexão das vigas, uma parcela da laje pode ainda participar da mesa comprimida de uma seção T. Essa largura colaborante pertence à análise da viga e não deve ser confundida com o vão da laje.

```{figure} ../_static/aulas/introducao-lajes/efeito-difragama-rigido.png
:alt: Comparação do comportamento de uma estrutura sob ação lateral, destacando a ligação proporcionada pelo pavimento
:width: 75%
:align: center

Participação do pavimento como diafragma. Figura do material do professor.
```

### Caminho das cargas

No modelo mais simples, o edifício é decomposto em subsistemas resolvidos em sequência: as **lajes** são resolvidas por métodos aproximados (tabelas), suas reações são aplicadas nas **vigas**, que são analisadas como vigas contínuas, e as reações das vigas são as cargas dos **pilares**. Cada elemento é analisado isoladamente, e as ações horizontais não são tratadas. É o modelo que usamos no pré-dimensionamento e na [Aula 03](003-carregamentos.md), e continua útil para conferência e ensino.

### Pórtico plano

Vigas e pilares de um mesmo alinhamento formam um **pórtico plano**. Nele, as vigas e os pilares trabalham juntos: a rigidez dos pilares restringe a rotação das vigas e, em contrapartida, as vigas introduzem momentos nos pilares. O pórtico plano permite incluir as **ações horizontais** (vento, desaprumo) e estimar os deslocamentos laterais.

### Pórtico espacial

O **pórtico espacial** representa vigas e pilares como barras em três dimensões, com flexão nos dois eixos e torção. Capta a interação entre pórticos de direções diferentes, a torção de vigas e o efeito de plantas assimétricas. Nele, as lajes costumam ser consideradas como um **diafragma rígido**: um elemento indeformável em seu plano, que obriga os nós de um mesmo pavimento a se deslocarem juntos na horizontal.

### Comparação dos modelos

| Modelo | O que representa | Ações horizontais | Interação viga-pilar | Quando usar |
|---|---|---|---|---|
| Caminho das cargas (lajes + vigas contínuas) | Subsistemas isolados, em sequência | Não | Aproximada, por correções da norma | Pré-dimensionamento, conferência, ensino |
| Pórtico plano | Vigas e pilares de um alinhamento | Sim, no plano do pórtico | Sim, no plano | Edifícios regulares de pequeno porte; estudo de tendências |
| Pórtico espacial | Toda a estrutura de barras, com diafragmas | Sim, nas duas direções | Sim, completa, com torção | Projeto de edifícios, análise de estabilidade global |

A escolha depende do porte e da regularidade do edifício e da fase de projeto. Na prática, usam-se vários modelos: o espacial para o comportamento global e os modelos simplificados para conferir ordens de grandeza.

## De um pórtico 3D a um pórtico plano

Muitas vezes é necessário obter um pórtico plano a partir de um edifício tridimensional, seja para conferir os resultados de um programa, seja para estudar o comportamento lateral em uma direção. O procedimento tem cinco passos.

**1. Escolher o alinhamento e a direção.** Define-se um eixo da planta (por exemplo, o eixo 2 da figura abaixo), que reúne os pilares e vigas do pórtico.

**2. Definir a geometria.** Os elementos são barras no eixo: pilares verticais, vigas horizontais e nós nas interseções. O comprimento das barras vai de eixo a eixo, e o pé-direito entre pavimentos define a altura dos pilares.

**3. Atribuir rigidezes.** Cada barra recebe área $A$ e momento de inércia $I$ **na direção do plano do pórtico**. Um pilar $20\times50$ cm tem $I=0{,}20\times0{,}50^3/12$ se a dimensão de $50$ cm estiver no plano do pórtico, e $I=0{,}50\times0{,}20^3/12$ se estiver perpendicular a ele. Pode-se ainda aplicar os coeficientes da rigidez secante.

**4. Transferir as ações.** As cargas das lajes chegam às vigas como cargas lineares, determinadas pelas áreas de influência. As vigas perpendiculares ao pórtico entregam **cargas concentradas** nos nós. As ações horizontais são aplicadas no nível de cada pavimento.

**5. Definir os vínculos.** A base dos pilares é engastada na fundação (hipótese a ser avaliada) ou apoiada, conforme a rigidez da fundação.

```{figure} ../_static/aulas/modelos-estruturais/planta-exemplo-portico.png
:alt: Planta de um pavimento com eixos A, B e C e eixos 1, 2 e 3, com o pórtico do eixo 2 destacado e sua faixa de influência
:width: 75%
:align: center

Planta do pavimento-tipo do exemplo. O pórtico plano do eixo 2 recebe a carga da faixa de influência de $4{,}0\text{ m}$ de largura.
```

```{admonition} Limites do pórtico plano
:class: destaque-azul

O pórtico plano **não** representa a torção das vigas, a ação conjunta de pórticos de direções diferentes nem o comportamento de plantas muito assimétricas. Ao isolar um alinhamento, a laje deixa de ser modelada e passa a ser apenas um carregamento. Os resultados são válidos para o pórtico, e comparações com o modelo espacial exigem que as hipóteses sejam equivalentes.
```

## Uso do Ftool

O **Ftool** (*Two-dimensional Frame Analysis Tool*) é um programa gratuito de análise de estruturas planas desenvolvido na PUC-Rio. Trabalha com barras, nós, apoios e carregamentos em um plano, e fornece diagramas de esforços, deslocamentos e reações. Os dados são informados em kN e m. A sequência usual é:

1. Desenhar os nós e as barras com a ferramenta de inserção de barras.
2. Atribuir às barras as propriedades do material (módulo de elasticidade $E$) e da seção (área $A$ e momento de inércia $I$).
3. Definir os apoios e, se necessário, as rótulas.
4. Aplicar as cargas distribuídas e nodais.
5. Visualizar reações, diagramas de $N$, $V$, $M$ e a deformada.

Os valores de $A$ e $I$ das seções usadas nos exemplos desta aula são:

| Seção | $A\ (\text{m}^2)$ | $I\ (\text{m}^4)$ |
|---|---:|---:|
| Viga $14\times50$ | $0{,}070$ | $1{,}458\times10^{-3}$ |
| Pilar $20\times50$ (lado de $50$ cm no plano) | $0{,}100$ | $2{,}083\times10^{-3}$ |
| Pilar $20\times60$ (lado de $60$ cm no plano) | $0{,}120$ | $3{,}600\times10^{-3}$ |

Para o concreto C30, use $E=E_{ci}=3{,}067\times10^{7}\text{ kN/m}^2$. Confira a unidade do módulo de elasticidade exigida pela janela de propriedades do programa antes de digitar o valor.

## Modelos para a viga de edifício

Há diversas formas de tratar as vigas, e o modelo de **viga contínua** ainda é bastante utilizado para conferência e ensino. Na sequência, três níveis de refinamento para a mesma viga.

| Modelo | Como representa a viga e seus apoios | Interação com os pilares |
|---|---|---|
| Viga contínua | Barra horizontal sobre apoios simples (indeslocáveis na vertical) | Nenhuma, salvo correções da norma |
| Pórtico H | Viga ligada a trechos de pilar acima e abaixo | Rigidez dos pilares à flexão |
| Pórtico plano | Viga dentro do pórtico completo do alinhamento | Pórtico completo, com ações horizontais |

```{figure} ../_static/aulas/modelos-vigas-pilares/modelos-viga-pilar.png
:alt: Três esquemas estáticos de uma viga de dois vãos: apoios simples, pórtico H com pilares de meia altura rotulados e pórtico H com pilares de altura inteira engastados
:width: 75%
:align: center

Esquemas estáticos para a mesma viga: apoios simples (modelo A); viga com tramos de pilar de meia altura e extremos rotulados (modelo C); e viga com tramos de pilar de altura inteira e extremos engastados (modelo E).
```

### Viga contínua e as correções da norma

No modelo clássico, a viga é tratada como contínua e simplesmente apoiada sobre os pilares. Os momentos nos apoios internos resultam da continuidade entre os vãos. Para um carregamento uniforme em dois vãos $l_1$ e $l_2$, com apoios simples nas três posições, a equação dos três momentos fornece o momento no apoio interno:

$$
M_B=\frac{q\,(l_1^3+l_2^3)}{8\,(l_1+l_2)} .
$$

Esse modelo ignora que a viga é monolítica com os pilares. Para estruturas usuais de edifícios, a NBR 6118 (item 14.6.6, aproximações permitidas) aceita o modelo de viga contínua para cargas verticais, desde que sejam feitas **correções adicionais**:

- **a)** não podem ser considerados momentos positivos menores que os que se obteriam se houvesse **engastamento perfeito** da viga nos apoios internos;
- **b)** quando a viga for solidária com o pilar intermediário e a **largura do apoio**, medida na direção do eixo da viga, for maior que a quarta parte da altura do pilar, não pode ser considerado momento negativo de valor absoluto menor que o de engastamento perfeito nesse apoio;
- **c)** quando não for calculada a rigidez dos apoios, deve-se considerar, **nos apoios extremos**, um momento igual ao de engastamento perfeito multiplicado por coeficientes que dependem da rigidez da viga e dos pilares.

A correção (a) garante que os momentos positivos não sejam subestimados pela hipótese de apoio simples. Na prática, comparam-se os momentos positivos da viga contínua com os de vãos isolados: o **vão extremo**, com engaste no apoio interno e apoio simples na extremidade, e o **vão interno**, biengastado. A correção (b) trata os apoios largos como engastes: se o apoio for largo, a viga se comporta como dois vãos separados, engastados no pilar.

### Momentos nos apoios extremos

No apoio extremo, a viga está ligada a um pilar que **resiste parcialmente à rotação**. A correção (c) considera esse efeito a partir da rigidez relativa da viga e dos tramos de pilar acima e abaixo do nó. A rigidez relativa de cada barra é

$$
r_i=\frac{I_i}{l_i} ,
$$

em que $I_i$ é o momento de inércia da seção bruta e $l_i$ o comprimento da barra (para a viga, o vão; para o pilar, o pé-direito do lance).

```{figure} ../_static/aulas/modelos-vigas-pilares/ligacao-viga-pilar-extremo.png
:alt: Nó de ligação entre uma viga e os pilares superior e inferior, com meia altura de pilar acima e abaixo e a viga engastada na extremidade oposta
:width: 55%
:align: center

Nó extremo isolado do pórtico: a viga, o pilar superior e o pilar inferior, cada um com sua rigidez relativa $r_i=I_i/l_i$.
```

A dedução parte de um nó com três barras. Antes da ligação com os pilares, a extremidade da viga está engastada, com o momento de engastamento perfeito $M_{eng}$ (para carga uniforme, $M_{eng}=ql^2/12$). Ao permitir que o nó gire, esse momento é distribuído entre as barras conforme suas rigidezes à rotação:

- viga com a outra extremidade engastada: $K_{vig}=4EI_{vig}/l_{vig}=4E\,r_{vig}$;
- pilar com a outra extremidade na seção de momento nulo, a meia altura (extremo rotulado, comprimento $l/2$): $K_{pil}=3EI/(l/2)=6E\,r_{pil}$.

O momento que permanece na viga é o de engastamento perfeito menos a parcela que ela mesma absorve; o restante vai para os pilares:

$$
M_{viga}=M_{eng}\,\frac{6\,r_{sup}+6\,r_{inf}}{4\,r_{vig}+6\,r_{sup}+6\,r_{inf}},
$$

$$
M_{sup}=M_{eng}\,\frac{6\,r_{sup}}{4\,r_{vig}+6\,r_{sup}+6\,r_{inf}},\qquad
M_{inf}=M_{eng}\,\frac{6\,r_{inf}}{4\,r_{vig}+6\,r_{sup}+6\,r_{inf}} .
$$

Os três momentos satisfazem o equilíbrio do nó: $M_{viga}=M_{sup}+M_{inf}$. Na forma simplificada apresentada pela norma, os coeficientes das rigidezes são tomados iguais, e o momento na viga é $M_{eng}\,(r_{sup}+r_{inf})/(r_{vig}+r_{sup}+r_{inf})$. Pilares muito rígidos em relação à viga tornam o apoio próximo de um engaste, com $M_{viga}\to M_{eng}$; pilares flexíveis aproximam-no do apoio simples, com $M_{viga}\to0$. Para o pilar da cobertura, que só tem tramo inferior, $r_{sup}=0$.

### Vão efetivo da viga

O vão de cálculo da viga é o vão efetivo, definido como na [Aula 02](002-lanc-pre-dim.md) para as lajes: $l_{ef}=l_0+a_1+a_2$, em que $l_0$ é a distância entre as faces dos apoios e cada $a_i$ é o menor valor entre $t_i/2$ e $0{,}3h$, com $t_i$ a largura do apoio na direção da viga (item 14.6.2.4 da norma). Nos exemplos desta aula, usam-se os vãos entre eixos fornecidos.

### Pórtico H

O **pórtico H** é o modelo em que a viga é ligada a trechos de pilar acima e abaixo, com extremos distantes representando o ponto de inflexão da deformada, a aproximadamente meia altura do pé-direito. Esses extremos são rotulados (a rotação é livre, mas os deslocamentos são impedidos). É a versão numérica do nó extremo da seção anterior, com o ganho de que a rigidez dos pilares é considerada em **todos** os apoios, internos e extremos, e a continuidade da viga é resolvida junto.

Uma variante usa tramos de pilar com o **pé-direito inteiro** e extremos engastados. Ela representa pilares contínuos entre pavimentos com os nós vizinhos considerados indeslocáveis e sem rotação. A diferença entre as duas variantes mostra o quanto o resultado depende da hipótese sobre as extremidades dos pilares.

## A rigidez dos pilares

Os pilares influem na viga por duas rigidezes distintas.

**Rigidez à flexão.** Determina a restrição à rotação do nó. Depende do módulo de elasticidade, da inércia da seção **na direção da flexão** e do comprimento do lance:

$$
K=\alpha\,\frac{EI}{l},\qquad \alpha=4\ \text{(outra extremidade engastada)},\ \ \alpha=3\ \text{(outra extremidade rotulada)} .
$$

A orientação do pilar é decisiva. Um pilar $20\times50$ cm tem inércia $I=2{,}083\times10^{-3}\text{ m}^4$ se o lado de $50$ cm estiver no plano da viga, e apenas $I=0{,}333\times10^{-3}\text{ m}^4$ se o lado de $20$ cm estiver nesse plano: a rigidez cai a **16 %** do valor, e o momento transmitido ao pilar cai junto.

**Rigidez axial.** Determina o quanto o pilar encurta e, portanto, o quanto o apoio se desloca sob a carga. Vale $EA/l$. Em geral, é muito maior que a rigidez da viga e o apoio é tratado como indeslocável. Quando os pilares têm diferenças de carga e de comprimento, ou quando há recalque da fundação, o deslocamento diferencial entre apoios altera os momentos e as reações da viga e precisa ser considerado.

```{admonition} Duas perguntas antes de escolher o modelo
:class: destaque-azul

1. **O pilar restringe a rotação da viga?** Compare a rigidez do pilar, $\alpha EI/l$, com a da viga. Se for comparável ou maior, o apoio não é simples.
2. **O apoio se desloca?** Compare a rigidez axial do pilar, $EA/l$, e a deformabilidade da fundação com a rigidez da viga. Se o deslocamento diferencial for da ordem da flecha da viga, o apoio indeslocável deixa de ser razoável.
```

### Efeito da fissuração

Os coeficientes de rigidez secante (seção "Não linearidade física: o processo simplificado") podem ser aplicados ao pórtico H: $0{,}80$ aos pilares e $0{,}40$ ou $0{,}50$ à viga. Como os pilares perdem menos rigidez que a viga, a rigidez **relativa** dos pilares aumenta, e a viga passa a ter momentos de extremidade ligeiramente maiores e momentos positivos menores.

## Quando cada modelo é aceitável?

| Situação | Modelo recomendado | Observação |
|---|---|---|
| Pré-dimensionamento, conferência rápida, apoios muito rígidos | Viga contínua com as correções da norma | Verificar sempre as correções (a), (b) e (c) |
| Viga com pilares de seção e comprimento muito diferentes | Pórtico H | Captura a distribuição de momentos entre viga e pilares |
| Estudo da interação com as ações horizontais e com pavimentos vizinhos | Pórtico plano | Inclui o vento e a rigidez do pavimento acima e abaixo |
| Recalque de fundação ou apoio deformável | Viga com apoios elásticos ou recalques | Verificar o efeito nos momentos e nas reações |
| Plantas assimétricas, vigas com torção importante | Pórtico espacial ou grelha | Fora do alcance do modelo plano |

## Atividade em sala 1: do pórtico 3D ao pórtico plano

### Exercício 1: efeito de 2ª ordem em um pilar em balanço

Um pilar de seção $20\times60$ cm (lado de $60$ cm no plano de flexão), de concreto C30, tem comprimento $l_e=9{,}30\text{ m}$, é engastado na base e está livre no topo. No topo atuam $F_H=20\text{ kN}$ e $F_V=600\text{ kN}$. Use a rigidez secante dos pilares, $(EI)_{sec}=0{,}80\,E_{ci}I_c$.

1. Calcule $(EI)_{sec}$ do pilar.
2. Calcule, em 1ª ordem, o momento no engaste $M_1$ e o deslocamento do topo $u_1=F_Hl_e^3/(3EI)$.
3. Atualize o momento com o deslocamento obtido, $M_2'=F_Hl_e+F_Vu_1$, e compare com $M_1$.
4. No Ftool, modele o pilar e confira $M_1$ e $u_1$.
5. Considere a força horizontal fictícia $H^*=F_H+F_Vu/l_e$, que reproduz no engaste o momento $F_Hl_e+F_Vu$. Aplique $H^*$ no topo, leia o novo deslocamento $u$ e repita o processo até a variação ser inferior a $1\%$. Se a sua versão do Ftool dispuser de análise de 2ª ordem, compare o resultado direto com o iterativo.
6. Calcule o acréscimo percentual de momento em relação a $M_1$ e comente o que ocorreria se $F_V$ fosse maior.

### Exercício 2: do pórtico 3D ao pórtico plano

As lajes do pavimento-tipo da figura são armadas em uma direção, com vão de $4{,}0\text{ m}$ entre os pórticos dos eixos 1, 2 e 3. O edifício tem três pavimentos, com pé-direito de $3{,}10\text{ m}$. Dados (ações de serviço):

- carga total por área nas lajes do pavimento-tipo (incluindo o peso próprio da laje): $p=8{,}0\text{ kN/m}^2$;
- carga total na laje de cobertura: $p=6{,}0\text{ kN/m}^2$;
- vigas $14\times50$ cm, com peso próprio de $0{,}14\times0{,}50\times25=1{,}75\text{ kN/m}$;
- pilares A, C: $20\times50$ cm; pilar B: $20\times60$ cm; o lado maior no plano do pórtico;
- ação horizontal de $20\text{ kN}$ aplicada no nível de cada pavimento, na viga do eixo A;
- base dos pilares engastada.

```{figure} ../_static/aulas/modelos-estruturais/portico-plano-exemplo.png
:alt: Pórtico plano de três pavimentos com vãos de 5,00 e 4,00 metros, cargas distribuídas e forças horizontais
:width: 70%
:align: center

Pórtico plano do eixo 2 com os dados do Exercício 2.
```

1. Determine a carga linear em cada viga do eixo 2, considerando a faixa de influência de $4{,}0\text{ m}$ de largura e o peso próprio da viga. Confira com a figura.
2. Monte o pórtico no Ftool com $E=E_{ci}$ em todas as barras e processe as cargas verticais e horizontais.
3. Registre na tabela abaixo: deslocamento horizontal do topo, momentos na base dos pilares A, B e C, esforços na viga do 1º pavimento (momento no apoio A, momento no apoio B à esquerda e momento máximo no vão A-B) e os esforços normais na base dos pilares.
4. Rode também os casos: (i) apenas as cargas verticais; (ii) apenas a força horizontal. Verifique a superposição dos efeitos, e explique por que ela vale nesta análise.

### Exercício 3: rigidez secante e modelo de viga isolada

1. Repita o pórtico do Exercício 2 aplicando a rigidez secante: $0{,}80$ aos pilares e $0{,}40$ às vigas (reduza o $E$ das barras). Preencha a tabela e comente: o que cresceu mais, o deslocamento ou os momentos? Por quê?
2. Isole a viga do 1º pavimento como viga contínua de dois vãos com apoios simples, com a mesma carga linear. Compare, em uma tabela, o momento no apoio B, o momento máximo no vão A-B e a reação em cada apoio com os resultados do pórtico (apenas cargas verticais). Qual modelo é mais conservador para o momento positivo? E para o momento negativo no apoio A?
3. Escreva três frases sobre o que o modelo de pórtico plano acrescenta em relação ao modelo de viga isolada e o que ele ainda não representa.

| Resultado | Pórtico, $E_{ci}I_c$ (só V) | Pórtico, $E_{ci}I_c$ (V+H) | Pórtico, rigidez secante (V+H) | Viga isolada (só V) |
|---|---:|---:|---:|---:|
| Deslocamento horizontal do topo (mm) | | | | – |
| Momento na base do pilar A (kN·m) | | | | – |
| Momento na base do pilar B (kN·m) | | | | – |
| Momento na base do pilar C (kN·m) | | | | – |
| Viga do 1º pavimento: momento no apoio A (kN·m) | | | | |
| Viga do 1º pavimento: momento no apoio B, à esquerda (kN·m) | | | | |
| Viga do 1º pavimento: momento máximo no vão A-B (kN·m) | | | | |
| Viga do 1º pavimento: reação em B (kN) | | | | |

## Atividade em sala 2: a viga V1 em cinco modelos

A viga V1 tem dois vãos, com $l_1=5{,}00\text{ m}$ e $l_2=4{,}00\text{ m}$, seção $14\times50$ cm, concreto C30 e carga uniforme de serviço $q=30\text{ kN/m}$, que já inclui o peso próprio. Os pilares têm $3{,}10\text{ m}$ de pé-direito.

```{figure} ../_static/aulas/modelos-vigas-pilares/viga-v1-exemplo.png
:alt: Viga V1 de dois vãos, 5,00 e 4,00 metros, apoiada nos pilares P1, P2 e P3, com carga uniforme de 30 quilonewtons por metro
:width: 75%
:align: center

Viga V1 do exemplo.
```

Os pilares são $20\times50$ cm (P1 e P3) e $20\times80$ cm (P2), com o lado maior no plano da viga. Os dados para o Ftool, com $E=E_{ci}=3{,}067\times10^{7}\text{ kN/m}^2$, são:

| Seção | $A\ (\text{m}^2)$ | $I\ (\text{m}^4)$ |
|---|---:|---:|
| Viga $14\times50$ | $0{,}070$ | $1{,}458\times10^{-3}$ |
| Pilar $20\times50$, lado de $50$ cm no plano | $0{,}100$ | $2{,}083\times10^{-3}$ |
| Pilar $20\times80$, lado de $80$ cm no plano | $0{,}160$ | $8{,}533\times10^{-3}$ |
| Pilar $20\times50$, lado de $20$ cm no plano | $0{,}100$ | $0{,}333\times10^{-3}$ |
| Pilar $20\times80$, lado de $20$ cm no plano | $0{,}160$ | $0{,}533\times10^{-3}$ |
| Pilar $20\times30$, lado de $30$ cm no plano | $0{,}060$ | $0{,}450\times10^{-3}$ |

### Parte 1: viga contínua com apoios simples (modelo A)

1. Calcule $M_B$ pela equação dos três momentos e as reações de apoio.
2. Confira no Ftool: momentos nos apoios, momentos máximos em cada vão e reações. Verifique o equilíbrio: $R_1+R_2+R_3=q(l_1+l_2)$.

### Parte 2: correções da norma

3. Calcule as rigidezes relativas $r_i=I_i/l_i$ de viga e pilares (pé-direito de $3{,}10\text{ m}$) e os momentos de engastamento perfeito $ql^2/12$ de cada vão.
4. Calcule os momentos $M_{viga}$ nos apoios extremos P1 e P3 pela fórmula completa e pela simplificada da norma.
5. Aplique os momentos obtidos como momentos de extremidade no modelo A e recalcule os momentos positivos.
6. Verifique a correção (a): calcule os momentos positivos do vão extremo (engaste interno, apoio simples na extremidade, $9ql^2/128$) e do vão interno biengastado ($ql^2/24$) e adote o maior valor entre eles e os do item 5.
7. Verifique a correção (b) em P2: compare a largura do apoio $b_{int}$ (lado do pilar na direção da viga) com a quarta parte do pé-direito. Qual conclusão você tira?

### Parte 3: pórtico H

8. Monte o **modelo C** (pórtico H): a viga e os três pilares, com tramos de $l/2=1{,}55\text{ m}$ acima e abaixo, extremos rotulados (apoios fixos, rotação livre).
9. Compare, em uma tabela, os momentos de extremidade e os positivos de C com os do item 5. A fórmula do item 4 reproduz o resultado de C? Em quanto difere?
10. Observe que o momento no apoio P2 é diferente à esquerda e à direita. De quanto é a diferença e para onde vai esse momento?
11. Monte o **modelo E**: tramos de pilar de pé-direito inteiro com extremos engastados. Compare com C e comente.

### Parte 4: a rigidez dos pilares

12. No modelo C, mude a orientação de todos os pilares (lado de $20$ cm no plano). O que ocorre com os momentos de extremidade, os positivos e as reações? Compare com o modelo A.
13. Volte à orientação original e troque os pilares P1 e P3 por $20\times30$ cm e P2 por $20\times50$ cm. Compare.
14. Para o pilar da **cobertura**, retire os tramos superiores (o nó só tem pilar inferior). Compare com o modelo C e explique a diferença.
15. Aplique a rigidez secante ($0{,}80$ nos pilares, $0{,}40$ na viga) ao modelo C e compare.

### Parte 5: apoio deformável

16. No modelo A, aplique um recalque de $5\text{ mm}$ no apoio P2 (ou substitua o apoio por uma mola de rigidez equivalente, se o recalque prescrito não estiver disponível na sua versão do Ftool). Compare os momentos e as reações com os do modelo A sem recalque.
17. Estime a rigidez axial do pilar P2 ($EA/l$, com $l=3{,}10\text{ m}$) e compare com a rigidez de flexão da viga ($48EI/l^3$ para um vão de $5{,}00\text{ m}$). Em que situação a hipótese de apoio indeslocável é razoável?

### Quadro de resultados

Preencha uma linha por modelo, com momentos em $\text{kN}\cdot\text{m}$ (positivo = tração na face inferior) e reações em $\text{kN}$.

| Modelo | $M$ em P1 | $M^+$ vão 1 | $M$ em P2 (esq.) | $M$ em P2 (dir.) | $M^+$ vão 2 | $M$ em P3 | $R_1$ | $R_2$ | $R_3$ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| A: apoios simples | | | | | | | | | |
| A com momentos de extremidade (item 5) | | | | | | | | | |
| C: pórtico H (meia altura, rotulado) | | | | | | | | | |
| E: pórtico H (altura inteira, engastado) | | | | | | | | | |
| C com pilares na orientação fraca | | | | | | | | | |
| C com pilares $20\times30$ / $20\times50$ | | | | | | | | | |
| C, cobertura (sem tramo superior) | | | | | | | | | |
| C com rigidez secante | | | | | | | | | |
| A com recalque de $5\text{ mm}$ em P2 | | | | | | | | | |

### Para discutir

- Que modelo é conservador para o momento positivo? E para o momento negativo no apoio interno?
- Quanto os modelos divergem entre si e quanto divergem de um modelo A com a correção da norma? O que isso diz sobre a incerteza dos esforços de projeto?
- O que cada modelo exige que você conheça do edifício? Em que fase do projeto cada um é viável?
- Em que momento do projeto você revisaria as seções de pilares por causa do momento que eles recebem das vigas?

## Síntese

```{admonition} O que levar desta aula
:class: destaque-azul

1. Analisar uma estrutura é resolver um **modelo**. Os resultados dependem das hipóteses adotadas para geometria, vínculos, material e ações.
2. A análise **linear** supõe pequenos deslocamentos e material elástico linear. A **não linear** pode ser física, geométrica ou de contato.
3. A 2ª ordem aparece quando o equilíbrio é escrito na posição deformada: $M_2=F_Hl_e+F_Vu$.
4. A não linearidade física é considerada, de forma simplificada, por coeficientes de rigidez secante (NBR 6118, item 15.7.3).
5. Os modelos do edifício vão do caminho das cargas ao pórtico espacial. Cada um tem um alcance e um uso adequado. Um pórtico plano é extraído de um edifício 3D escolhendo o alinhamento, a geometria, as rigidezes no plano, as ações e os vínculos.
6. O modelo de viga contínua com apoios simples é simples e útil, mas **subestima** os momentos positivos e ignora o momento transferido aos pilares. A norma exige correções.
7. A fração do momento de engastamento que fica na viga depende da rigidez relativa $r_i=I_i/l_i$ dos pilares e da viga. O pórtico H considera a rigidez dos pilares em todos os apoios.
8. A orientação e a seção dos pilares mudam bastante os momentos nas extremidades da viga. A rigidez axial e os recalques só importam quando o deslocamento diferencial dos apoios é comparável à deformação da viga.
```

Os esforços das vigas do trabalho prático, assim como as reações das lajes que os produzem, serão determinados após o estudo dos esforços em lajes, nas aulas seguintes.

## Referências

- PEREIRA JUNIOR, Wanderlei Malaquias. *Introdução à análise estrutural do edifício* e *Análise estrutural de vigas e pilares*. Material do professor (Estruturas de Concreto Armado 1, aulas 17 e 19). Base para a organização dos tipos de análise, dos modelos de viga e de pilar e das expressões do nó extremo.
- PEREIRA JUNIOR, Wanderlei Malaquias. *Introdução ao projeto de lajes*. Material do professor, capítulo 1. Origem das figuras sobre elementos de superfície e efeito de diafragma.
- ABNT. *NBR 6118: Projeto de estruturas de concreto*. Rio de Janeiro, 2023. Itens 14.5 (tipos de análise estrutural), 14.6.2.4 (vão efetivo de vigas), 14.6.6 (aproximações permitidas em estruturas usuais de edifícios), 15.4 (efeitos de 2ª ordem) e 15.7.3 (não linearidade física, rigidez secante).
- MARTHA, Luiz Fernando. *Ftool: Two-dimensional Frame Analysis Tool*. Grupo de Tecnologia em Computação Gráfica, PUC-Rio. Disponível em: <https://www.tecgraf.puc-rio.br/ftool>.
