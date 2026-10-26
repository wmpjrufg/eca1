# Aula 02: Lançamento e pré-dimensionamento estrutural

O projeto de uma estrutura começa pela definição de como a edificação será sustentada. Antes de calcular armaduras, é necessário escolher o sistema estrutural, posicionar seus elementos e compreender como as ações chegarão às fundações. Essas decisões constituem a **concepção estrutural** e orientam o lançamento de lajes, vigas e pilares na planta de arquitetura.

Nesta aula, a discussão parte do sistema estrutural e do caminho das cargas, passa pelas observações de lançamento, introduz o projeto de lajes (vão efetivo e relação entre vãos) e chega às estimativas iniciais das seções e às dimensões mínimas. A introdução foi adaptada do capítulo *Análise e concepção do sistema estrutural*, do material do professor [Pereira Junior [5]](#ref-5).

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

```{list-table}
:class: eq-table
:widths: 90 10

* - $\displaystyle b \geq \frac{l_0}{50}$
  - (1)
```

```{list-table}
:class: eq-table
:widths: 90 10

* - $\displaystyle b \geq \beta_{fl}\,h$
  - (2)
```

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

## Introdução ao projeto de lajes

### Aplicações

A [Figura 2](#figura2) mostra três tipos de laje usuais em edifícios de múltiplos pavimentos: maciça, lisa e nervurada.

(figura2)=
**Figura 2.** Aplicações do conceito de lajes em edifícios de múltiplos pavimentos.
```{figure} ../_static/aulas/introducao-lajes/exemplos-lajes-abc.png
:alt: Exemplos de laje maciça, laje lisa e laje nervurada
:width: 90%
:align: center
```

### Vão livre, distância entre eixos e vão efetivo

A análise de uma laje começa pela determinação do **vão efetivo**. Para cada direção do painel, identifique primeiro a distância livre entre as faces dos apoios. A [Figura 3](#figura3) apresenta a idealização do vão efetivo de uma laje, análoga à de uma viga. O procedimento segue o item 14.6.2.4 da [ABNT NBR 6118 [1]](#ref-1).

(figura3)=
**Figura 3.** Geometria para determinação do vão efetivo.
```{figure} ../_static/aulas/introducao-lajes/vao-efetivo.png
:alt: Vão livre de uma laje e parcelas de apoio utilizadas para obter seu vão efetivo
:width: 70%
:align: center
```

A Equação (3) apresenta o cálculo do vão efetivo:

```{list-table}
:class: eq-table
:widths: 90 10

* - $\displaystyle l_{ef}=l_0+a_1+a_2, \qquad a_i=\min\left(\frac{t_i}{2};\,0{,}3h\right)$
  - (3)
```

$l_0$ é o vão livre, medido entre as faces dos apoios; $t_i$ é a largura do apoio $i$, medida na direção estudada; e $h$ é a espessura da laje. Calcula-se uma parcela $a_i$ para cada extremidade do vão, usando a largura do respectivo apoio. Todas as dimensões devem estar na mesma unidade.

```{admonition} Exemplo 1
:class: destaque-verde

**Enunciado:** considere um painel com distâncias entre eixos de $4{,}00\times5{,}00\,\mathrm{m}$, vigas de $20\,\mathrm{cm}$ em todo o contorno e espessura inicial de $10\,\mathrm{cm}$. Determine os vãos efetivos $l_x$ e $l_y$.

**Resolução:** como as vigas têm a mesma largura nos dois lados de cada direção, o vão livre é a distância entre eixos menos $20\,\mathrm{cm}$:

$$
l_{0x}=4{,}00-0{,}20=3{,}80\,\mathrm{m},
\qquad
l_{0y}=5{,}00-0{,}20=4{,}80\,\mathrm{m}.
$$

Em cada apoio, $t_i=0{,}20\,\mathrm{m}$; portanto, metade da largura do apoio é $t_i/2=0{,}10\,\mathrm{m}$. O outro valor do mínimo vem da espessura da laje: $0{,}3h=0{,}3\times0{,}10=0{,}03\,\mathrm{m}$. Logo, em cada extremidade:

$$
a_i=\min\left(\frac{0{,}20}{2};\,0{,}3\times0{,}10\right)
=\min(0{,}10;\,0{,}03)=0{,}03\,\mathrm{m}.
$$

Somando ao vão livre as parcelas dos dois apoios:

$$
l_x=l_{0x}+2a_i=3{,}80+2(0{,}03)=3{,}86\,\mathrm{m},
$$

$$
l_y=l_{0y}+2a_i=4{,}80+2(0{,}03)=4{,}86\,\mathrm{m}.
$$

Neste exemplo, $l_x$ é o menor vão efetivo e $l_y$, o maior. Se a espessura adotada mudar, as parcelas $a_i$ devem ser recalculadas.
```

### Uma ou duas direções principais?

Para um painel retangular apoiado nos quatro lados, a relação entre os vãos ajuda a escolher a aproximação de cálculo, conforme a Equação (4):

```{list-table}
:class: eq-table
:widths: 90 10

* - $\displaystyle \lambda=\frac{l_y}{l_x},\qquad l_x\leq l_y$
  - (4)
```

Se $\lambda\leq2$, a laje tem comportamento bidirecional, e os momentos devem ser determinados nas duas direções. Se $\lambda>2$, o comportamento é predominantemente unidirecional, e a análise é feita em faixas na direção do menor vão.

No painel do Exemplo 1, $\lambda=4{,}86/3{,}86\approx1{,}26$, conduzindo ao estudo em duas direções.

## Pré-dimensionamento de lajes

Diversos autores apresentam procedimentos para a determinação da geometria da forma em lajes maciças e nervuradas. Nesta aula, o foco adotado é o trabalho de [Rebello [2]](#ref-2). Os vãos $l_x$ e $l_y$ das equações a seguir são os vãos efetivos da Equação (3), com $l_x\leq l_y$. O pré-dimensionamento fornece uma seção para iniciar a análise; depois, resistência, deformações, fissuração e disposição das armaduras podem exigir sua revisão.

### Lajes maciças

a) Laje armada em duas direções:

```{list-table}
:class: eq-table
:widths: 90 10

* - $\displaystyle h = 2\%\cdot\frac{l_y+l_x}{2}$
  - (5)
```

b) Laje armada em uma direção:

```{list-table}
:class: eq-table
:widths: 90 10

* - $\displaystyle h = 2\%\cdot l_x$
  - (6)
```

c) Lajes em balanço:

```{list-table}
:class: eq-table
:widths: 90 10

* - $\displaystyle h = 4\%\cdot l_x$
  - (7)
```

Nas Equações (5) a (7), use a mesma unidade para os vãos e para $h$; em (7), $l_x$ é o comprimento do balanço.

```{admonition} Exemplo 2
:class: destaque-verde

**Enunciado:** estime a espessura da laje maciça do Exemplo 1, armada em duas direções, e compare com o mínimo da NBR 6118 para piso sem balanço.

**Resolução:** com $l_x=3{,}86\,\mathrm{m}$ e $l_y=4{,}86\,\mathrm{m}$, a Equação (5) fornece:

$$
h_{est}=0{,}02\cdot\frac{3{,}86+4{,}86}{2}
=0{,}0872\,\mathrm{m}=8{,}72\,\mathrm{cm}.
$$

Esse valor atende ao mínimo de $8\,\mathrm{cm}$ para piso sem balanço. Pode-se manter $h=10\,\mathrm{cm}$ como escolha inicial para organizar o pavimento e prosseguir com as verificações; a estimativa de $8{,}72\,\mathrm{cm}$ não justifica, sozinha, reduzir a espessura.
```

### Lajes nervuradas moldadas

Como as lajes nervuradas se dividem em diversos grupos, adotam-se critérios distintos para as lajes unidirecionais e para as lajes bidirecionais.

a) Laje armada em uma direção:

```{list-table}
:class: eq-table
:widths: 90 10

* - $\displaystyle h = 4\%\cdot l_x \text{, para espaçamento de 100 cm entre nervuras}$
  - (8)
```

```{list-table}
:class: eq-table
:widths: 90 10

* - $\displaystyle h = 3\%\cdot l_x \text{, para espaçamento de 50 cm entre nervuras}$
  - (9)
```

```{list-table}
:class: eq-table
:widths: 90 10

* - $\displaystyle b_w = \frac{1}{4}h \text{ a } \frac{1}{3}h$
  - (10)
```

Segundo [Rebello [2]](#ref-2), para estruturas usuais em concreto armado a altura da capa ($h_f$) esse pode variar de 4 a 7 cm.

Já as distâncias intereixos em lajes nervuradas moldadas *in loco* não decorrem de uma formulação de pré-dimensionamento, mas sim do elemento de enchimento (EPS, cerâmica etc.) adotado pelo projetista, cujas dimensões comerciais definem a largura da nervura e o vão entre eixos.

b) Lajes bidirecionais (em grelha):

```{list-table}
:class: eq-table
:widths: 90 10

* - $\displaystyle h = 4\%\cdot\frac{l_y+l_x}{2}$
  - (11)
```

```{list-table}
:class: eq-table
:widths: 90 10

* - $\displaystyle b_w = \frac{1}{4}h \text{ a } \frac{1}{3}h$
  - (12)
```

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

### Espessura total e altura útil

```{figure} ../_static/aulas/introducao-lajes/secao-trans-laje.png
:alt: Seção de laje maciça indicando espessura total, altura útil, cobrimento e posição da armadura
:width: 70%
:align: center

Posição da armadura na seção. Figura do material do professor.
```

A altura útil $d$ é medida da face comprimida até o centro da armadura tracionada. Para uma camada junto à face oposta, vale a Equação (13):

```{list-table}
:class: eq-table
:widths: 90 10

* - $\displaystyle d=h-c-\frac{\phi}{2}$
  - (13)
```

em que $c$ é o cobrimento e $\phi$ é o diâmetro da barra. Com $h=10\,\mathrm{cm}$, cobrimento adotado no exemplo de $2{,}5\,\mathrm{cm}$ e barra de $8\,\mathrm{mm}$, obtém-se $d=10-2{,}5-0{,}8/2=7{,}1\,\mathrm{cm}$. O cobrimento deste exemplo é um dado, cuja escolha no projeto depende das condições de exposição e execução.

Em uma laje bidirecional, as barras se cruzam em alturas diferentes. Por isso, as duas direções podem apresentar alturas úteis distintas, mesmo com uma única espessura de laje.

### Coeficiente adicional de segurança para lajes em balanço

Além dos critérios de pré-dimensionamento apresentados, as lajes em balanço estão sujeitas a um coeficiente adicional de segurança $\gamma_n$, prescrito pela [ABNT NBR 6118 [1]](#ref-1) em função da altura da laje, conforme o [Quadro 1](#quadro1).

(quadro1)=
**Quadro 1 — Valores do coeficiente adicional $\gamma_n$ para lajes em balanço.**

| $h$ (cm) | ≥ 19 | 18 | 17 | 16 | 15 | 14 | 13 | 12 | 11 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $\gamma_n$ | 1,00 | 1,05 | 1,10 | 1,15 | 1,20 | 1,25 | 1,30 | 1,35 | 1,40 | 1,45 |


O [Quadro 1](#quadro1) pode ser expresso pela Equação (14), em que $h$ é a altura da laje em centímetros:

```{list-table}
:class: eq-table
:widths: 90 10

* - $\displaystyle \gamma_n = 1{,}95 - 0{,}05\,h$
  - (14)
```

O coeficiente $\gamma_n$ deve majorar os esforços solicitantes finais de cálculo nas lajes em balanço, quando de seu dimensionamento.

A Equação (14) aplica-se ao intervalo $10\leq h<19\text{ cm}$; para $h\geq19\text{ cm}$, adota-se $\gamma_n=1{,}00$, conforme o quadro.

### Atividade: preparar o painel para a análise

Considere uma laje de piso maciça, com quatro bordos apoiados em vigas de $20\,\mathrm{cm}$, dimensões entre eixos de $4{,}20\times5{,}40\,\mathrm{m}$ e espessura inicial de $12\,\mathrm{cm}$. Há continuidade monolítica com um painel semelhante ao longo de um dos bordos de maior comprimento; os demais bordos são externos e serão idealizados como simplesmente apoiados.

1. Desenhe os vínculos e indique a hipótese adotada para o bordo interno.
2. Calcule os dois vãos efetivos e a relação $\lambda$.
3. Escolha a aproximação de uma ou duas direções.
4. Estime a espessura e compare-a com o mínimo de piso da NBR 6118.
5. Registre quais verificações ainda faltam para confirmar a espessura.

**Conferência:** com $a_i=3{,}6\,\mathrm{cm}$, os vãos são $4{,}072\,\mathrm{m}$ e $5{,}272\,\mathrm{m}$; $\lambda\approx1{,}295$ e $h_{est}\approx9{,}34\,\mathrm{cm}$. O painel será estudado em duas direções. A espessura de $12\,\mathrm{cm}$ permanece como hipótese inicial até as verificações posteriores.

Para cada laje do trabalho, entregue uma linha com identificação, tipo, vãos, vínculos, relação $\lambda$ e espessura adotada, acompanhada de um croqui. Esses dados serão a entrada do cálculo dos esforços da [Aula 05](005-esforcos-lajes.md).

## Pré-dimensionamento de pilares

### Área de influência

[Bacarji  [3]](#ref-3) orienta a divisão da área de influência dos pilares em faixas proporcionais ao vão, de acordo com a posição do pilar na planta:

- $0{,}45\cdot l$: pilar de extremidade ou de canto, na direção da menor dimensão do pilar ($b$);
- $0{,}50\cdot l$: pilar de extremidade ou de canto, na direção da maior dimensão do pilar ($h$);
- $0{,}55\cdot l$: complemento dos casos anteriores (demais faixas, incluindo pilares intermediários).

(figura4)=
**Figura 4.** Planta de estimativa da área de influência de um pilar de concreto armado.
```{figure} ../_static/aulas/pre-dimensionamento/planta-carga-pilar.png
:alt: planta de cargas
:width: 75%
:align: center
```

### Carga estimada e seção transversal do pilar

Após a determinação da área de influência e do carregamento estimado no pavimento, a seção transversal do pilar pode ser obtida pela Equação (15):

```{list-table}
:class: eq-table
:widths: 90 10

* - $\displaystyle A_c = \frac{N_d^{*}}{0{,}85\,f_{cd} + \rho\,\sigma_{s,\varepsilon=0,2\%}}$
  - (15)
```

em que:

- $A_c$ é a área da seção transversal do pilar, em $\mathrm{cm^2}$;
- $N_d^{*}$ é a força normal de cálculo para pré-dimensionamento, em $\mathrm{kN}$;
- $f_{cd} = f_{ck}/1{,}40$ é a resistência à compressão de cálculo do concreto, em $\mathrm{kN/cm^2}$;
- $\sigma_{s,\varepsilon=0,2\%}$ é a tensão no aço correspondente a uma deformação de $0{,}20\%$, que para o aço CA-50 vale $420\ \mathrm{MPa}$;
- $\rho$ é a taxa de armadura do pilar; da [Costa [4]](#ref-4) recomenda, como valor intermediário, $\rho = 2\%$ (inserido na Equação (15) como $\rho = 2/100$, e não em taxa percentual).

Para determinar a carga atuante de pré-dimensionamento, utilizam-se as Equações (16) a (19):

```{list-table}
:class: eq-table
:widths: 90 10

* - $\displaystyle N_k^{*} = Q_{tot}\cdot A_i$
  - (16)
```

```{list-table}
:class: eq-table
:widths: 90 10

* - $\displaystyle N_k^{*} = n_{tipo}\cdot N_k^{tipo} + n_{cob}\cdot N_k^{cob}$
  - (17)
```

```{list-table}
:class: eq-table
:widths: 90 10

* - $\displaystyle N_d^{*} = \alpha\cdot N_k^{*}$
  - (18)
```

```{list-table}
:class: eq-table
:widths: 90 10

* - $\displaystyle \alpha = \begin{cases} 1{,}8, & \text{pilares intermediários} \\ 2{,}2, & \text{pilares de extremidade} \\ 2{,}5, & \text{pilares de canto} \end{cases}$
  - (19)
```

em que $N_k^{*}$ é a carga característica para pré-dimensionamento; $Q_{tot}$ é a carga total no pavimento; $A_i$ é a área de influência do pilar $i$ analisado; $N_k^{tipo}$ é a carga em um pilar do pavimento tipo; $n_{tipo}$ é o número de pavimentos tipo acima do nível calculado; $N_k^{cob}$ é a carga em um pilar do pavimento de cobertura; $n_{cob}$ é o número de pavimentos de cobertura acima do nível calculado; e $\alpha$ é um coeficiente de majoração da carga de pré-dimensionamento, que leva em conta os esforços de flexão não considerados nessa etapa.

### Dimensão mínima da seção do pilar

O item 13.2.3 da [ABNT NBR 6118 [1]](#ref-1) estabelece 19 cm como menor dimensão usual. Em casos especiais, permite dimensões entre 14 e 19 cm com a majoração adicional indicada abaixo. A área da seção deve ser de pelo menos $360\text{ cm}^2$.

Além dos critérios de pré-dimensionamento apresentados, os pilares com menor dimensão da seção transversal ($b$) inferior a $19\text{ cm}$ também estão sujeitos ao coeficiente adicional de segurança $\gamma_n$ prescrito pela [ABNT NBR 6118 [1]](#ref-1), agora em função da menor dimensão da seção, conforme da [Costa [4]](#ref-4) e o [Quadro 2](#quadro2).

(quadro2)=
**Quadro 2.** Coeficiente adicional $\gamma_n$ em função da menor dimensão da seção do pilar ($b$).

| $b$ (cm) | ≥ 19 | 18 | 17 | 16 | 15 | 14 |
| --- | --- | --- | --- | --- | --- | --- |
| $\gamma_n$ | 1,00 | 1,05 | 1,10 | 1,15 | 1,20 | 1,25 |

O [Quadro 2](#quadro2) pode ser expresso pela Equação (20), em que $b$ é a menor dimensão da seção do pilar em centímetros:

```{list-table}
:class: eq-table
:widths: 90 10

* - $\displaystyle \gamma_n = 1{,}95 - 0{,}05\,b$
  - (20)
```

O coeficiente $\gamma_n$ deve majorar os esforços solicitantes finais de cálculo nos pilares, quando de seu dimensionamento.

A Equação (20) aplica-se a $14\leq b<19\text{ cm}$; para $b\geq19\text{ cm}$, adota-se $\gamma_n=1{,}00$. Sua extrapolação não autoriza seções com dimensão inferior a 14 cm.

## Síntese

```{admonition} Do lançamento às dimensões iniciais
:class: destaque-azul

Antes dos cálculos, definir o sistema estrutural, acompanhar o caminho das cargas até as fundações e compatibilizar lajes, vigas e pilares com os pavimentos e as instalações. Com esse arranjo inicial:

1. Verificar, para vigas sem travamento lateral por lajes, a largura mínima dada pelas Equações (1) e (2).
2. Determinar os vãos efetivos $l_x$ e $l_y$ pela Equação (3), classificar o painel pela relação $\lambda$ (Equação 4), estimar a altura das lajes maciças ou nervuradas e conferir as dimensões mínimas aplicáveis.
3. Majorar os esforços de lajes em balanço pelo coeficiente $\gamma_n$, conforme o [Quadro 1](#quadro1).
4. Definir a área de influência de cada pilar a partir das faixas de Bacarji.
5. Estimar a carga característica e de cálculo do pilar e obter a área da seção transversal pela Equação (15).
6. Conferir a área e a menor dimensão da seção do pilar; nos casos especiais entre 14 e 19 cm, majorar os esforços pelo coeficiente $\gamma_n$ do [Quadro 2](#quadro2).

Após a análise estrutural, revisar as dimensões e o lançamento conforme os esforços, os deslocamentos e a estabilidade do conjunto.
```

## Referências

(ref-1)=
**[1]** ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **ABNT NBR 6118**: Projeto de estruturas de concreto. 4. ed. Rio de Janeiro: ABNT, 2023. Itens 13.2.2 a 13.2.4, 14.6.2.4 e 15.10.

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
