# Aula 02: Lançamento e pré-dimensionamento estrutural

O projeto de uma estrutura começa pela definição de como a edificação será sustentada. Antes de calcular armaduras, é necessário escolher o sistema estrutural, posicionar seus elementos e compreender como as ações chegarão às fundações. Essas decisões constituem a **concepção estrutural** e orientam o lançamento de lajes, vigas e pilares na planta de arquitetura.

Nesta aula, a discussão parte do sistema estrutural e do caminho das cargas, passa pelas observações de lançamento e chega às estimativas iniciais das seções e às dimensões mínimas. A introdução foi adaptada do capítulo *Análise e concepção do sistema estrutural*, do material do professor [Pereira Junior [5]](#ref-5).

## Sistemas estruturais e função dos elementos

O sistema estrutural é o conjunto de elementos e ligações que recebe as ações, resiste aos esforços e os transmite aos apoios. Seu desempenho depende tanto da resistência de cada peça quanto da maneira como elas trabalham em conjunto. Uma viga resistente, por exemplo, não resolve um arranjo em que seu apoio apresente deslocamentos incompatíveis com o uso da edificação.

Nos edifícios usuais de concreto armado, os elementos mais frequentes são:

| Elemento | Participação no sistema |
|---|---|
| Lajes | Formam pisos e coberturas, recebem ações distribuídas e localizadas e as transmitem aos apoios. Trabalham predominantemente à flexão sob cargas transversais. |
| Vigas | Recebem reações das lajes, cargas de paredes e outras ações, transferindo-as aos pilares ou a outros apoios. A flexão e a força cortante são solicitações usuais. |
| Pilares | Recebem as ações dos pavimentos e as conduzem às fundações. Além da compressão, podem estar sujeitos a momentos fletores nas duas direções. |
| Paredes estruturais e núcleos | Podem receber cargas verticais e contribuir para a resistência e a rigidez da edificação diante das ações horizontais. |
| Fundações | Transmitem ao terreno as ações recebidas da superestrutura, conforme a solução estrutural e as condições geotécnicas. |

```{figure} ../_static/aulas/lancamento/elementos-edificio.jpg
:alt: Perspectiva de uma edificação com lajes, vigas, pilares, escada e diferentes elementos de fundação identificados
:width: 70%
:align: center

Elementos de uma estrutura de concreto armado. Imagem reproduzida do material do professor [5], que a atribui a Wight e MacGregor [7].
```

### Arranjos usuais em concreto armado

No **sistema de lajes, vigas e pilares**, as vigas delimitam os painéis de laje e recebem suas reações. Quando vigas e pilares estão ligados de modo a transmitir momentos, formam pórticos que também podem participar da resistência às ações horizontais.

Nas **lajes lisas**, as cargas do piso são transmitidas diretamente aos pilares, sem vigas intermediárias; nas **lajes-cogumelo**, existem capitéis na região dos apoios. Essa mudança altera o caminho das cargas e torna particularmente importante a verificação da ligação laje-pilar, incluindo a punção. A ausência de vigas não elimina a necessidade de um sistema capaz de garantir a estabilidade global.

As **lajes nervuradas** concentram parte do concreto em nervuras associadas a uma mesa. As nervuras e a mesa trabalham em conjunto, e a disposição dos apoios define como suas ações chegam ao restante da estrutura. Assim, a escolha entre laje maciça e nervurada deve ser feita juntamente com a definição dos vãos, das cargas e do processo construtivo.

Essas soluções podem ser combinadas com pórticos, paredes estruturais e núcleos de escadas ou elevadores. O sistema escolhido precisa atender ao uso dos ambientes, à arquitetura, à execução e ao comportamento esperado da edificação.

## Como as cargas caminham

### Ações verticais

Em um pavimento convencional, as lajes recebem seu peso próprio, os revestimentos, as cargas de utilização e as paredes que nelas se apoiam. Ao se deformarem, mobilizam reações nos apoios. Essas reações passam a ser cargas aplicadas às vigas, que, por sua vez, transmitem ações aos pilares.

**Caminho usual: lajes → vigas → pilares → fundações → terreno.**

Esse encadeamento depende da posição efetiva de cada carga. Uma parede apoiada diretamente em uma viga transfere sua carga à viga; em uma laje lisa, a etapa intermediária das vigas não existe. O peso próprio de cada elemento também é acrescentado ao percurso a partir do ponto em que atua.

Nos pilares, as cargas dos pavimentos superiores se acumulam em direção à base. Por isso, a estimativa da força normal em um trecho de pilar deve considerar os pavimentos que ele sustenta, e não somente a laje imediatamente acima.

```{admonition} A carga precisa encontrar um caminho até o terreno
:class: destaque-azul

Ao observar uma planta, escolha uma carga e acompanhe seu percurso: qual elemento a recebe, onde esse elemento se apoia e como a ação chega à fundação? Esse exercício ajuda a identificar apoios indiretos, balanços e elementos de transição ainda na etapa de lançamento.
```

Quando uma viga se apoia em outra viga, há um **apoio indireto**. Quando um pilar termina sobre uma viga ou laje de transferência, há uma **transição estrutural**. Essas soluções são possíveis, mas introduzem concentrações de esforços e exigem atenção à rigidez, às deformações e ao detalhamento das ligações. Um caminho mais direto costuma facilitar a concepção e a execução.

### Ações horizontais

O vento atua nas superfícies da edificação e suas ações são transmitidas à estrutura pelas ligações com fachadas e demais componentes. Os pisos, quando apresentam rigidez e conexões adequadas, podem funcionar como **diafragmas**, distribuindo ações horizontais entre os elementos de contraventamento.

**Caminho usual: fachadas e ligações → pavimentos e elementos de contraventamento → fundações → terreno.**

Pórticos, paredes estruturais e núcleos precisam ser dispostos de modo a fornecer resistência e rigidez nas duas direções principais. Concentrar a rigidez apenas de um lado do edifício pode aumentar a torção global. Portanto, além de resistir às cargas verticais, o lançamento deve considerar a distribuição da rigidez em planta e sua continuidade na altura da edificação.

## Observações para o lançamento estrutural

O lançamento traduz a concepção em posições de elementos na planta de fôrma. Não existe uma sequência única: é possível começar pelos pilares, pelas vigas ou pela modulação das lajes. O importante é revisar as escolhas em conjunto, verificando suas consequências nos demais pavimentos.

### Compatibilização com a arquitetura e as instalações

Antes de lançar a estrutura, devem ser identificados os ambientes, as circulações, as vagas de garagem, as escadas, os elevadores, os reservatórios, os desníveis e as aberturas. Também devem ser examinados os espaços para tubulações e equipamentos. Um pilar bem posicionado no pavimento tipo pode interferir na circulação de veículos no térreo; uma viga pode reduzir o pé-direito ou impedir a passagem de uma instalação.

Em edifícios com pavimentos repetidos, o pavimento tipo é um ponto de partida útil, desde que sua solução seja confrontada com a cobertura, o térreo, os subsolos e as fundações. A verificação em corte é tão importante quanto a verificação em planta.

### Posição dos pilares e continuidade vertical

Procura-se dispor os pilares em posições compatíveis com a arquitetura e com os apoios das vigas, evitando vãos muito desiguais ou concentrações desnecessárias de carga. Cantos e encontros de vigas são posições a examinar, mas não constituem uma obrigação para todo arranjo.

Sempre que possível, mantém-se a continuidade dos pilares até as fundações. A orientação de uma seção retangular também merece atenção: ela altera a rigidez à flexão nas duas direções. A escolha deve considerar o conjunto dos pórticos e dos elementos de contraventamento, além do encaixe do pilar na parede.

### Distribuição das vigas e definição das lajes

Posicionar vigas sob paredes pode favorecer a compatibilização e reduzir a solicitação direta das lajes por essas cargas. Isso não significa que toda parede precise de uma viga: paredes sobre lajes são possíveis, desde que suas cargas e os efeitos das deformações sejam considerados.

Um vigamento que acompanha todas as divisórias pode produzir muitos painéis pequenos, encontros de difícil execução e excesso de fôrmas. Por outro lado, retirar vigas aumenta os vãos e pode exigir lajes mais espessas ou outra solução estrutural. A escolha resulta do equilíbrio entre comportamento, uso e construção.

Ao delimitar cada painel, identificam-se seus apoios, bordas livres, balanços e aberturas. A geometria em planta e as condições de apoio orientam a direção resistente da laje e o procedimento de pré-dimensionamento. A rigidez das vigas de apoio também influencia sua resposta; os elementos não se deformam de maneira independente.

### Regularidade e execução

A repetição de vãos e a padronização de seções facilitam o uso das fôrmas, a montagem das armaduras e a execução. Essa padronização deve ser compatível com os esforços e os deslocamentos: adotar uma única seção para todos os elementos não é, por si só, uma solução econômica.

Na escolha das dimensões, devem caber as armaduras, seus cobrimentos e espaçamentos, além de haver condições para lançamento e adensamento do concreto. Encontros entre vigas e pilares, mudanças de seção e regiões de transição merecem atenção desde o estudo inicial.

### Da arquitetura à planta de fôrma

O exemplo do material do professor, baseado em [Alva [6]](#ref-6), mostra como a distribuição das vigas pode ser revista antes da definição final das seções. Na primeira imagem, as linhas vermelhas indicam um arranjo de vigas que delimita cinco painéis de laje. Algumas paredes permanecem apoiadas nas lajes e suas cargas devem entrar na análise.

```{figure} ../_static/aulas/lancamento/arranjo-vigas-lajes.jpg
:alt: Planta com vigas em vermelho delimitando os painéis de laje L1 a L5 sobre o desenho das paredes
:width: 60%
:align: center

Estudo do posicionamento de vigas e lajes. Fonte: material do professor [5], a partir de Alva [6].
```

A planta de fôrma reúne a posição e a identificação das peças, as cotas, os níveis e as dimensões adotadas. Ela é o registro da solução estrutural, enquanto a planta de armação apresenta as barras e seus detalhes. As dimensões da figura seguinte pertencem ao exemplo do livro e não devem ser transferidas automaticamente para outros projetos.

```{figure} ../_static/aulas/lancamento/planta-forma-exemplo.jpg
:alt: Planta de fôrma com nove pilares, sete vigas e cinco lajes, contendo identificações, cotas e seções do exemplo
:width: 75%
:align: center

Planta de fôrma do exemplo de lançamento. Fonte: material do professor [5], a partir de Alva [6].
```

## Do lançamento ao pré-dimensionamento

Existe uma dependência entre as dimensões e os esforços: as dimensões definem o peso próprio e a rigidez, enquanto os esforços necessários ao dimensionamento dependem dessas propriedades. O pré-dimensionamento permite iniciar esse processo com estimativas e revê-las após a análise.

Uma sequência de trabalho consiste em lançar os elementos, estimar as seções das lajes e vigas, levantar as ações, estimar as cargas e seções dos pilares e montar o modelo estrutural. A análise dos esforços, dos deslocamentos e da estabilidade permite então ajustar o lançamento e as dimensões. A composição das ações será desenvolvida na [Aula 03](003-carregamentos.md).

É necessário distinguir **estimativa de pré-dimensionamento** de **dimensão mínima normativa**. A primeira fornece um ponto de partida; a segunda estabelece um limite geométrico para a situação indicada. Atender ao limite mínimo não comprova que a peça resista às solicitações nem que suas deformações sejam aceitáveis. Nas verificações geométricas a seguir, mantém-se a edição de 2023 da [ABNT NBR 6118 [1]](#ref-1) adotada nesta aula.

Antes do lançamento estrutural definitivo e da análise detalhada de esforços, é usual estimar as dimensões iniciais de vigas, lajes e pilares por meio de critérios práticos de pré-dimensionamento. Essas estimativas permitem montar um modelo estrutural coerente, evitar retrabalho na modelagem e servem como ponto de partida para o dimensionamento final em concreto armado.

## Pré-dimensionamento de vigas

### Largura mínima e espaço para execução

O item 13.2.2 da [ABNT NBR 6118 [1]](#ref-1) estabelece larguras mínimas de 12 cm para vigas e 15 cm para vigas-parede. Excepcionalmente, admite-se redução até 10 cm, desde que sejam atendidas as condições de alojamento das armaduras, cobrimento, espaçamento, lançamento e vibração do concreto.

Esses limites não definem a altura necessária da viga. A seção inicial também depende do vão, da continuidade, das cargas e dos deslocamentos esperados. Ajustar a largura à parede é uma decisão de compatibilização, subordinada às necessidades estruturais e construtivas.

### Segurança à instabilidade lateral

A [ABNT NBR 6118 [1]](#ref-1) faz uma ressalva quanto à largura de vigas de concreto armado ou protendido no item 15.10, que trata da segurança à instabilidade lateral. Segundo a norma, essa segurança deve ser garantida por meio de procedimentos apropriados; para tanto, são estabelecidos critérios que definem uma largura mínima para a viga em função das condições de contraventamento lateral, expressos pelas Equações (1) e (2):

$$
b \geq \frac{l_0}{50}
\tag{1}
$$

$$
b \geq \beta_{fl}\,h
\tag{2}
$$

em que:

- $b$ é a largura da zona comprimida da viga;
- $h$ é a altura total da viga;
- $l_0$ é o comprimento do flange comprimido, medido entre os suportes que garantem o contraventamento lateral;
- $\beta_{fl}$ é um coeficiente que depende da forma da seção transversal da viga presente na Figura [1](#figura1).

(figura1)=
**Figura 1.** Coeficiente $\beta_{fl}$ para seções de viga.
```{figure} ../_static/aulas/pre-dimensionamento/quadro-beta-fl-vigas.png
:alt: Coeficiente beta_fl para seções de viga, em função da tipologia da seção transversal
:width: 75%
:align: center
```

## Pré-dimensionamento de lajes

Diversos autores apresentam procedimentos para a determinação da geometria da forma em lajes maciças e nervuradas. Nesta aula, o foco adotado é o trabalho de [Rebello [2]](#ref-2).

### Lajes maciças

a) Laje armada em duas direções:

$$
h = 2\%\cdot\frac{l_y+l_x}{2}
\tag{3}
$$

b) Laje armada em uma direção:

$$
h = 2\%\cdot l_x
\tag{4}
$$

c) Lajes em balanço:

$$
h = 4\%\cdot l_x
\tag{5}
$$

### Lajes nervuradas moldadas

Como as lajes nervuradas se dividem em diversos grupos, adotam-se critérios distintos para as lajes unidirecionais e para as lajes bidirecionais.

a) Laje armada em uma direção:

$$
h = 4\%\cdot l_x \text{, para espaçamento de 100 cm entre nervuras}
\tag{6}
$$

$$
h = 3\%\cdot l_x \text{, para espaçamento de 50 cm entre nervuras}
\tag{7}
$$

$$
b_w = \frac{1}{4}h \text{ a } \frac{1}{3}h
\tag{8}
$$

Segundo [Rebello [2]](#ref-2), para estruturas usuais em concreto armado a altura da capa ($h_f$) esse pode variar de 4 a 7 cm.

Já as distâncias intereixos em lajes nervuradas moldadas *in loco* não decorrem de uma formulação de pré-dimensionamento, mas sim do elemento de enchimento (EPS, cerâmica etc.) adotado pelo projetista, cujas dimensões comerciais definem a largura da nervura e o vão entre eixos.

b) Lajes bidirecionais (em grelha):

$$
h = 4\%\cdot\frac{l_y+l_x}{2}
\tag{9}
$$

$$
b_w = \frac{1}{4}h \text{ a } \frac{1}{3}h
\tag{10}
$$

Segundo [Rebello [2]](#ref-2), o espaçamento $a$ entre nervuras dessas lajes bidirecionais varia de $1{,}5\,h$ a $2{,}0\,h$.

### Dimensões mínimas de lajes

As alturas estimadas pelas relações anteriores devem ser confrontadas com os limites geométricos da [ABNT NBR 6118 [1]](#ref-1), itens 13.2.4.1 e 13.2.4.2. Para as lajes maciças de concreto armado tratadas nesta aula:

| Situação | Espessura mínima |
|---|---:|
| Cobertura, sem balanço | 7 cm |
| Piso, sem balanço | 8 cm |
| Balanço | 10 cm |
| Suporte de veículos com peso total até 30 kN | 10 cm |
| Suporte de veículos com peso total acima de 30 kN | 12 cm |
| Laje lisa | 16 cm |
| Laje-cogumelo, fora do capitel | 14 cm |

Para lajes nervuradas, a geometria envolve também a mesa e as nervuras. Sem tubulações horizontais embutidas, a mesa deve ter espessura de pelo menos 4 cm e não inferior a $1/15$ da distância livre entre as faces das nervuras. Essa distância livre não é o espaçamento entre eixos.

Com tubulações embutidas de diâmetro até 10 mm, o mínimo absoluto da mesa é 5 cm. Acima desse diâmetro, considera-se 4 cm mais o diâmetro da tubulação, ou 4 cm mais duas vezes esse diâmetro quando houver cruzamento, mantendo-se também a condição relativa à distância entre nervuras. As nervuras devem ter largura mínima de 5 cm; larguras inferiores a 8 cm não admitem armadura de compressão.

A escolha final deve satisfazer simultaneamente as condições aplicáveis. Por exemplo, uma estimativa de 7 cm para uma laje de piso sem balanço precisa ser elevada a pelo menos 8 cm, e ainda depende das verificações de resistência e de serviço. Os valores práticos atribuídos a Rebello não dispensam essas verificações.

### Coeficiente adicional de segurança para lajes em balanço

Além dos critérios de pré-dimensionamento apresentados, as lajes em balanço estão sujeitas a um coeficiente adicional de segurança $\gamma_n$, prescrito pela [ABNT NBR 6118 [1]](#ref-1) em função da altura da laje, conforme o [Quadro 1](#quadro1).

(quadro1)=
**Quadro 1 — Valores do coeficiente adicional $\gamma_n$ para lajes em balanço.**

| $h$ (cm) | ≥ 19 | 18 | 17 | 16 | 15 | 14 | 13 | 12 | 11 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $\gamma_n$ | 1,00 | 1,05 | 1,10 | 1,15 | 1,20 | 1,25 | 1,30 | 1,35 | 1,40 | 1,45 |


O [Quadro 1](#quadro1) pode ser expresso pela Equação (11), em que $h$ é a altura da laje em centímetros:

$$
\gamma_n = 1{,}95 - 0{,}05\,h
\tag{11}
$$

O coeficiente $\gamma_n$ deve majorar os esforços solicitantes finais de cálculo nas lajes em balanço, quando de seu dimensionamento.

A Equação (11) aplica-se ao intervalo $10\leq h<19\text{ cm}$; para $h\geq19\text{ cm}$, adota-se $\gamma_n=1{,}00$, conforme o quadro.

## Pré-dimensionamento de pilares

### Área de influência

[Bacarji  [3]](#ref-3) orienta a divisão da área de influência dos pilares em faixas proporcionais ao vão, de acordo com a posição do pilar na planta:

- $0{,}45\cdot l$: pilar de extremidade ou de canto, na direção da menor dimensão do pilar ($b$);
- $0{,}50\cdot l$: pilar de extremidade ou de canto, na direção da maior dimensão do pilar ($h$);
- $0{,}55\cdot l$: complemento dos casos anteriores (demais faixas, incluindo pilares intermediários).

(figura2)=
**Figura 2.** Planta de estimativa da área de influência de um pilar de concreto armado.
```{figure} ../_static/aulas/pre-dimensionamento/planta-carga-pilar.png
:alt: planta de cargas
:width: 75%
:align: center
```

### Carga estimada e seção transversal do pilar

Após a determinação da área de influência e do carregamento estimado no pavimento, a seção transversal do pilar pode ser obtida pela Equação (12):

$$
A_c = \frac{N_d^{*}}{0{,}85\,f_{cd} + \rho\,\sigma_{s,\varepsilon=0,2\%}}
\tag{12}
$$

em que:

- $A_c$ é a área da seção transversal do pilar, em $\mathrm{cm^2}$;
- $N_d^{*}$ é a força normal de cálculo para pré-dimensionamento, em $\mathrm{kN}$;
- $f_{cd} = f_{ck}/1{,}40$ é a resistência à compressão de cálculo do concreto, em $\mathrm{kN/cm^2}$;
- $\sigma_{s,\varepsilon=0,2\%}$ é a tensão no aço correspondente a uma deformação de $0{,}20\%$, que para o aço CA-50 vale $420\ \mathrm{MPa}$;
- $\rho$ é a taxa de armadura do pilar; da [Costa [4]](#ref-4) recomenda, como valor intermediário, $\rho = 2\%$ (inserido na Equação (12) como $\rho = 2/100$, e não em taxa percentual).

Para determinar a carga atuante de pré-dimensionamento, utilizam-se as Equações (13) a (16):

$$
N_k^{*} = Q_{tot}\cdot A_i
\tag{13}
$$

$$
N_k^{*} = n_{tipo}\cdot N_k^{tipo} + n_{cob}\cdot N_k^{cob}
\tag{14}
$$

$$
N_d^{*} = \alpha\cdot N_k^{*}
\tag{15}
$$

$$
\alpha =
\begin{cases}
1{,}8, & \text{pilares intermediários} \\
2{,}2, & \text{pilares de extremidade} \\
2{,}5, & \text{pilares de canto}
\end{cases}
\tag{16}
$$

em que $N_k^{*}$ é a carga característica para pré-dimensionamento; $Q_{tot}$ é a carga total no pavimento; $A_i$ é a área de influência do pilar $i$ analisado; $N_k^{tipo}$ é a carga em um pilar do pavimento tipo; $n_{tipo}$ é o número de pavimentos tipo acima do nível calculado; $N_k^{cob}$ é a carga em um pilar do pavimento de cobertura; $n_{cob}$ é o número de pavimentos de cobertura acima do nível calculado; e $\alpha$ é um coeficiente de majoração da carga de pré-dimensionamento, que leva em conta os esforços de flexão não considerados nessa etapa.

### Dimensão mínima da seção do pilar

O item 13.2.3 da [ABNT NBR 6118 [1]](#ref-1) estabelece 19 cm como menor dimensão usual. Em casos especiais, permite dimensões entre 14 e 19 cm com a majoração adicional indicada abaixo. A área da seção deve ser de pelo menos $360\text{ cm}^2$.

Além dos critérios de pré-dimensionamento apresentados, os pilares com menor dimensão da seção transversal ($b$) inferior a $19\text{ cm}$ também estão sujeitos ao coeficiente adicional de segurança $\gamma_n$ prescrito pela [ABNT NBR 6118 [1]](#ref-1), agora em função da menor dimensão da seção, conforme da [Costa [4]](#ref-4) e o [Quadro 2](#quadro2).

(quadro2)=
**Quadro 2.** Coeficiente adicional $\gamma_n$ em função da menor dimensão da seção do pilar ($b$).

| $b$ (cm) | ≥ 19 | 18 | 17 | 16 | 15 | 14 |
| --- | --- | --- | --- | --- | --- | --- |
| $\gamma_n$ | 1,00 | 1,05 | 1,10 | 1,15 | 1,20 | 1,25 |

O [Quadro 2](#quadro2) pode ser expresso pela Equação (17), em que $b$ é a menor dimensão da seção do pilar em centímetros:

$$
\gamma_n = 1{,}95 - 0{,}05\,b
\tag{17}
$$

O coeficiente $\gamma_n$ deve majorar os esforços solicitantes finais de cálculo nos pilares, quando de seu dimensionamento.

A Equação (17) aplica-se a $14\leq b<19\text{ cm}$; para $b\geq19\text{ cm}$, adota-se $\gamma_n=1{,}00$. Sua extrapolação não autoriza seções com dimensão inferior a 14 cm.

## Síntese

```{admonition} Do lançamento às dimensões iniciais
:class: destaque-azul

Antes dos cálculos, definir o sistema estrutural, acompanhar o caminho das cargas até as fundações e compatibilizar lajes, vigas e pilares com os pavimentos e as instalações. Com esse arranjo inicial:

1. Verificar, para vigas sem travamento lateral por lajes, a largura mínima dada pelas Equações (1) e (2).
2. Estimar a altura das lajes maciças ou nervuradas com base nos vãos $l_x$ e $l_y$ do painel e conferir as dimensões mínimas aplicáveis.
3. Majorar os esforços de lajes em balanço pelo coeficiente $\gamma_n$, conforme o [Quadro 1](#quadro1).
4. Definir a área de influência de cada pilar a partir das faixas de Bacarji.
5. Estimar a carga característica e de cálculo do pilar e obter a área da seção transversal pela Equação (12).
6. Conferir a área e a menor dimensão da seção do pilar; nos casos especiais entre 14 e 19 cm, majorar os esforços pelo coeficiente $\gamma_n$ do [Quadro 2](#quadro2).

Após a análise estrutural, revisar as dimensões e o lançamento conforme os esforços, os deslocamentos e a estabilidade do conjunto.
```

## Referências

(ref-1)=
**[1]** ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **ABNT NBR 6118**: Projeto de estruturas de concreto. 4. ed. Rio de Janeiro: ABNT, 2023. Itens 13.2.2 a 13.2.4 e 15.10.

(ref-2)=
**[2]** REBELLO, Yopanan Conrado Pereira. **Bases para projeto estrutural na arquitetura**. 2. ed. São Paulo: Zigurate Editora, 2007.

(ref-3)=
**[3]** BACARJI, Edgar. **Análise de estruturas de edifícios: projeto de pilares**. 1993. Dissertação (Mestrado em Engenharia de Estruturas) — Escola de Engenharia de São Carlos, Universidade de São Paulo, São Carlos, 1993.

(ref-4)=
**[4]** COSTA, João Bosco da. **Estruturas de concreto armado II**. Goiânia: [s.n.], [s.d.]. E-book.

(ref-5)=
**[5]** PEREIRA JUNIOR, Wanderlei Malaquias. **Análise e concepção do sistema estrutural**. Capítulo de livro do professor, arquivo `lanc-pre-dim.htm` do repositório. Material-base desta introdução.

(ref-6)=
**[6]** ALVA, Gerson Moacyr Sisniegas. **Concepção estrutural de edifícios em concreto armado**. Santa Maria: Universidade Federal de Santa Maria,
2007. Exemplo de lançamento reproduzido no material-base [5].

(ref-7)=
**[7]** WIGHT, James K.; MACGREGOR, James G. **Reinforced concrete: mechanics and design**. 6. ed. Upper Saddle River: Pearson Prentice Hall,
2012. Figura dos elementos estruturais reproduzida no material-base [5].
