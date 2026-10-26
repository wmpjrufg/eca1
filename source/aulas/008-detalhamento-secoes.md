# Aula 08: Detalhamento de seções retangulares

Na [Aula 07](007-armadura-simples.md), o dimensionamento forneceu uma **área de aço** $A_s$. Uma área, porém, não se constrói: o que vai para a obra são **barras** de diâmetros comerciais, dispostas em camadas, envolvidas por estribos, com cobrimento suficiente e espaço para o concreto passar. A pergunta desta aula é: **como transformar $A_s$ em um arranjo de barras que possa ser executado e que não invalide as hipóteses usadas no cálculo?**

O detalhamento não é uma etapa "de desenho" separada do cálculo. Ao escolher as barras, o projetista define a posição real do centroide da armadura e, portanto, a altura útil $d$ efetiva da seção. Se o arranjo ficar diferente do previsto, o cálculo precisa ser refeito. A aula percorre essa sequência e termina com o exemplo da viga de seção $25\times90$ cm, uma atividade em sala e uma introdução à ancoragem, que será usada no detalhamento das lajes na [Aula 9](009-detalhamento-lajes.md).

```{admonition} Objetivos da aula
:class: destaque-azul

- Escolher bitolas comerciais e o número de barras para uma área de aço calculada.
- Determinar o cobrimento nominal e os espaçamentos livres mínimos entre barras.
- Calcular quantas barras cabem em uma camada e organizar as camadas.
- Calcular o centroide da armadura, a altura útil real e conferir o $d$ adotado no dimensionamento.
- Verificar se a armadura pode ser considerada concentrada no seu centroide.
- Prever as armaduras complementares: porta-estribos e armadura de pele.
- Calcular o comprimento de ancoragem básico e reconhecer as zonas de boa e de má aderência.
```

## O que o detalhamento precisa garantir

| Exigência | Por quê | Onde aparece |
|---|---|---|
| Cobrimento nominal | Durabilidade (proteção contra corrosão), aderência e proteção ao fogo | Distância da face do concreto à face da barra mais externa (o estribo) |
| Espaçamento livre entre barras | Permitir que o concreto envolva cada barra e que a agulha do vibrador passe | Distâncias $a_h$ e $a_v$ |
| Altura útil real $\geq$ altura útil adotada | O momento resistente é proporcional a $d$; um $d$ menor reduz a capacidade | Centroide da armadura |
| Armadura concentrada | O cálculo admite toda a armadura no centroide, com uma só deformação | Critério de $10\%h$ |
| Armaduras complementares | Controlar fissuras na alma, montar a armação e manter os estribos na posição | Pele e porta-estribos |
| Ancoragem | A barra só desenvolve a tensão de cálculo se tiver comprimento de aderência suficiente | Comprimento de ancoragem $\ell_b$ |

## Barras comerciais e número de barras

As barras de aço CA-50 são fornecidas nos diâmetros abaixo. Para estribos e armaduras de lajes, também se usa o CA-60 de $5{,}0$ mm.

| $\phi$ (mm) | 5,0 (CA-60) | 6,3 | 8,0 | 10,0 | 12,5 | 16,0 | 20,0 | 25,0 | 32,0 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Área $A_\phi$ (cm²) | 0,196 | 0,312 | 0,503 | 0,785 | 1,227 | 2,011 | 3,142 | 4,909 | 8,042 |
| Massa (kg/m) | 0,154 | 0,245 | 0,395 | 0,617 | 0,963 | 1,578 | 2,466 | 3,853 | 6,313 |

O número de barras é o menor inteiro que fornece a área necessária:

$$n=\left\lceil\frac{A_{s,nec}}{A_\phi}\right\rceil,\qquad A_{s,ef}=n\,A_\phi\geq A_{s,nec}$$

Não existe uma única resposta correta. Bitolas finas distribuem melhor as fissuras e ancoram em comprimentos menores, mas exigem mais barras, mais camadas e mais mão de obra. Bitolas grossas ocupam menos espaço, mas aumentam o comprimento de ancoragem e a abertura de fissuras. Na prática, procuram-se arranjos com **poucas camadas** (de preferência uma ou duas), **poucas bitolas diferentes** na mesma peça e, no mínimo, **duas barras** por face tracionada, uma em cada canto do estribo.

Para definir $c_{nom}$, consulte [Cobrimento nominal na Aula 01](001-hist-prop.md#cobrimento-nominal). Nas vigas, o cobrimento é medido até a face do **estribo**, que é a barra mais próxima da superfície.

## Espaçamento livre entre barras

O concreto precisa envolver cada barra. A NBR 6118 (item 18.3.2.2) fixa os espaçamentos **livres** mínimos (entre as faces das barras):

$$a_h\geq\begin{cases}20\text{ mm}\\ \phi\\ 1{,}2\,d_{máx}\end{cases}\qquad\qquad a_v\geq\begin{cases}20\text{ mm}\\ \phi\\ 0{,}5\,d_{máx}\end{cases}$$

em que $a_h$ é o espaçamento horizontal (na mesma camada), $a_v$ o vertical (entre camadas) e $d_{máx}$ a dimensão máxima característica do agregado (brita 1: $19$ mm; brita 2: $25$ mm). Esses valores são mínimos: é boa prática deixar, em alguma posição da seção, um espaço maior para a **agulha do vibrador** e alinhar verticalmente as barras das camadas.

```{figure} ../_static/aulas/detalhamento-secoes/secao-espacamentos.png
:alt: Seção retangular de viga com estribo, duas camadas de barras tracionadas e as cotas de cobrimento, diâmetro do estribo, largura disponível, espaçamentos horizontal e vertical, centroide e altura útil
:width: 75%
:align: center

Grandezas do detalhamento transversal de uma seção retangular.
```

### Quantas barras cabem em uma camada?

A largura disponível para as barras longitudinais, entre as faces internas do estribo, é

$$b_{disp}=b_w-2\,(c_{nom}+\phi_t)$$

Com $n$ barras de diâmetro $\phi$ e $n-1$ espaços $a_h$, é preciso que $n\,\phi+(n-1)\,a_h\leq b_{disp}$, ou seja,

$$n_{camada}\leq\frac{b_{disp}+a_h}{\phi+a_h}\qquad(\text{arredondar para baixo})$$

## Várias camadas: centroide e altura útil real

Quando as barras não cabem em uma camada, distribuem-se em várias. As camadas devem ficar alinhadas verticalmente, com as camadas mais cheias junto à face tracionada. Medindo as distâncias $y_i$ do centro de cada camada à **face tracionada**:

$$y_1=c_{nom}+\phi_t+\frac{\phi}{2},\qquad y_{i+1}=y_i+\phi+a_v$$

$$y_{cg}=\frac{\sum A_i\,y_i}{\sum A_i},\qquad d_{real}=h-y_{cg}$$

```{admonition} Confira sempre o d
:class: destaque-vermelho

O dimensionamento da Aula 07 partiu de um $d$ estimado (em geral $d\approx0{,}9h$ ou $h$ menos 5 a 10 cm). Depois do arranjo:

- se $d_{real}\geq d_{adotado}$, o cálculo está do lado da segurança;
- se $d_{real}<d_{adotado}$, **recalcule $A_s$ com $d_{real}$** e refaça o arranjo. Uma ou duas iterações bastam.
```

### Quando a armadura pode ser considerada concentrada?

O dimensionamento admite toda a armadura no seu centroide, com uma única deformação. A NBR 6118 (item 17.2.4.1) aceita essa simplificação se a distância do centroide da armadura à barra **mais afastada da linha neutra** não ultrapassar $10\%$ da altura da seção:

$$a=y_{cg}-y_1\leq0{,}10\,h$$

Se o critério não for atendido, as camadas mais próximas da linha neutra têm deformação bem menor que as externas e o cálculo precisa considerar cada camada separadamente.

## Armaduras complementares

**Porta-estribos.** São barras longitudinais construtivas, colocadas nos cantos do estribo, na zona comprimida, para montar a armação e manter os estribos na posição. Em geral usam-se duas barras de $8$ a $10$ mm (prática corrente; podem ser aproveitadas como armadura de compressão quando houver).

**Armadura de pele.** Em vigas com $h>60$ cm, a NBR 6118 (item 17.3.5.2.3) exige uma armadura lateral para controlar a fissuração da alma: em **cada face**, $A_{s,pele}=0{,}10\%\,A_{c,alma}$, com barras de alta aderência espaçadas de no máximo $20$ cm, não sendo necessário ultrapassar $5$ cm²/m por face. Para $h\leq60$ cm, pode ser dispensada.

**Estribos e ramos.** O dimensionamento dos estribos é assunto da verificação ao cisalhamento. Para o detalhamento transversal, importa saber que o estribo envolve as barras longitudinais e que, em seções largas ou com muitas barras por camada, usam-se estribos com mais de dois ramos verticais, porque a norma limita o espaçamento transversal entre ramos (item 18.3.3.2).

**Armadura máxima.** A soma das armaduras de tração e de compressão não pode ultrapassar $4\%\,A_c$, calculada fora das regiões de emenda (item 17.3.5.2.4).

## Ancoragem: quanto a barra precisa avançar

Uma barra só desenvolve a tensão $f_{yd}$ se estiver **ancorada**, isto é, se tiver um comprimento suficiente para transferir a força ao concreto por aderência. Esse conceito define os comprimentos das barras nos desenhos, e será usado na Aula 9.

### Zonas de boa e de má aderência

A aderência é melhor nas barras da parte inferior das peças, porque o concreto em volta delas fica mais compacto. A NBR 6118 (item 9.3.1) considera em **boa aderência** as barras com inclinação de pelo menos $45°$ com a horizontal e as barras horizontais que estejam: em peças com $h<60$ cm, até $30$ cm acima da face inferior (ou da junta de concretagem mais próxima); em peças com $h\geq60$ cm, a mais de $30$ cm abaixo da face superior. As demais estão em **má aderência**.

```{figure} ../_static/aulas/detalhamento-secoes/zonas-aderencia.png
:alt: Duas seções de viga mostrando, em verde, a zona de boa aderência e, em vermelho, a zona de má aderência, para altura menor que 60 cm e maior ou igual a 60 cm
:width: 70%
:align: center

Zonas de boa e de má aderência para barras horizontais.
```

### Comprimento de ancoragem básico

A resistência de aderência de cálculo é

$$f_{bd}=\eta_1\,\eta_2\,\eta_3\,f_{ctd},\qquad f_{ctd}=\frac{0{,}7\cdot0{,}3\,f_{ck}^{2/3}}{\gamma_c}$$

com $\eta_1=2{,}25$ para barras nervuradas (CA-50), $\eta_2=1{,}0$ em boa aderência e $0{,}7$ em má aderência, e $\eta_3=1{,}0$ para $\phi<32$ mm. Igualando a força na barra, $A_\phi f_{yd}$, à força de aderência ao longo do comprimento, $\pi\phi\,\ell_b\,f_{bd}$:

$$\ell_b=\frac{\phi}{4}\,\frac{f_{yd}}{f_{bd}}\geq25\,\phi$$

| Concreto | C20 | C25 | C30 | C35 | C40 |
|---|---:|---:|---:|---:|---:|
| $\ell_b/\phi$, boa aderência | 44 | 38 | 34 | 31 | 28 |
| $\ell_b/\phi$, má aderência | 63 | 54 | 48 | 43 | 40 |

(CA-50, $\gamma_c=1{,}4$, $\gamma_s=1{,}15$; valores arredondados para cima.)

O comprimento necessário pode ser reduzido quando a barra tem gancho ou quando há armadura em excesso:

$$\ell_{b,nec}=\alpha\,\ell_b\,\frac{A_{s,calc}}{A_{s,ef}}\geq\ell_{b,min}=\max(0{,}3\,\ell_b;\ 10\,\phi;\ 100\text{ mm})$$

com $\alpha=1{,}0$ para barras sem gancho e $\alpha=0{,}7$ para barras tracionadas com gancho, desde que o cobrimento no plano normal ao do gancho seja de pelo menos $3\phi$ (item 9.4.2.5).

### Ganchos

Os ganchos das extremidades das barras tracionadas podem ser semicirculares, em ângulo de $45°$ interno ou em ângulo reto, com as pontas retas mínimas da figura. O diâmetro interno de dobramento (pino) do CA-50 é $5\phi$ para $\phi<20$ mm e $8\phi$ para $\phi\geq20$ mm (Tabela 9.1).

```{figure} ../_static/aulas/detalhamento-secoes/ganchos.png
:alt: Três tipos de gancho de extremidade de barra: semicircular com ponta reta de 2 diâmetros, a 135 graus com ponta reta de 4 diâmetros e a 90 graus com ponta reta de 8 diâmetros
:width: 85%
:align: center

Tipos de gancho e pontas retas mínimas.
```

````{admonition} Exemplo resolvido: seção de apoio de uma viga contínua
:class: destaque-verde

**Dados.** Viga contínua de dois vãos de $8$ m, carga $p=48{,}3$ kN/m, seção $25\times90$ cm, $d=80$ cm adotado no dimensionamento. Na seção do apoio central, $A_{s,nec}=19{,}51$ cm² (já verificada quanto às armaduras mínima e máxima) e $x=35{,}83$ cm. Concreto com brita 2 ($d_{máx}=25$ mm), cobrimento de $3$ cm, estribo de $6{,}3$ mm. No apoio central o momento é negativo: a **face tracionada é a superior**.

**1. Número de barras.** Com $\phi12{,}5$ ($A_\phi=1{,}227$ cm²):

$$n=\left\lceil\frac{19{,}51}{1{,}227}\right\rceil=\lceil15{,}9\rceil=16\text{ barras}\qquad A_{s,ef}=19{,}63\text{ cm}^2$$

**2. Espaçamentos livres mínimos.**

$$a_h\geq\max(2{,}0;\ 1{,}25;\ 1{,}2\cdot2{,}5)=3{,}0\text{ cm}\qquad a_v\geq\max(2{,}0;\ 1{,}25;\ 0{,}5\cdot2{,}5)=2{,}0\text{ cm}$$

**3. Barras por camada.**

$$b_{disp}=25-2\,(3+0{,}63)=17{,}74\text{ cm}\qquad n_{camada}\leq\frac{17{,}74+3{,}0}{1{,}25+3{,}0}=4{,}9\ \Rightarrow\ 4\text{ barras}$$

Nos slides da disciplina, adotou-se $a_h=4$ cm, deixando folga para o vibrador: $(17{,}74+4)/(1{,}25+4)=4{,}1$, também 4 barras. Com 4 barras, o espaço livre real é $(17{,}74-4\cdot1{,}25)/3=4{,}25$ cm. São necessárias **4 camadas de 4 barras**.

**4. Posição das camadas** (a partir da face superior). A primeira camada fica a $y_1=3+0{,}63+1{,}25/2\approx4{,}28$ cm (os slides arredondam $\phi$ para $1{,}3$ cm). Adotando $3{,}5$ cm entre eixos de camadas (espaço livre de $3{,}5-1{,}25=2{,}25$ cm $\geq a_v$):

$$y_1=4{,}28;\quad y_2=7{,}78;\quad y_3=11{,}28;\quad y_4=14{,}78\text{ cm}$$

**5. Centroide e altura útil real.** Como todas as camadas têm a mesma área,

$$y_{cg}=\frac{4A_\phi\,(4{,}28+7{,}78+11{,}28+14{,}78)}{16\,A_\phi}=\frac{38{,}12}{4}=9{,}53\text{ cm}$$

$$d_{real}=90-9{,}53=80{,}47\text{ cm}\geq d_{adotado}=80\text{ cm}\quad\Rightarrow\quad\text{OK}$$

**6. Armadura concentrada.**

$$a=y_{cg}-y_1=9{,}53-4{,}28=5{,}25\text{ cm}\leq0{,}10\cdot90=9{,}0\text{ cm}\quad\Rightarrow\quad\text{OK}$$

**7. Armadura de pele** ($h=90>60$ cm):

$$A_{s,pele}=0{,}10\%\cdot25\cdot90=2{,}25\text{ cm}^2\text{ por face}\ (2{,}5\text{ cm}^2/\text{m}<5\text{ cm}^2/\text{m})$$

Com $\phi6{,}3$: $2{,}25/0{,}312=7{,}2$, ou seja, **8 barras de $\phi6{,}3$ por face** ($2{,}50$ cm²); com $\phi8$, 5 barras por face ($2{,}51$ cm²). O espaçamento não pode passar de $20$ cm. Nos slides, as barras de pele foram concentradas na região tracionada, entre a última camada e a linha neutra, onde as fissuras se formam. Como em uma viga contínua a zona tracionada muda de lado entre o apoio e o vão, é comum distribuir a pele ao longo de toda a altura da alma, respeitando o espaçamento máximo.

**8. Complementos.** Duas barras porta-estribos nos cantos inferiores (zona comprimida) e estribos de $\phi6{,}3$ com 4 ramos, que envolvem e travam as barras das camadas.

**9. Armadura máxima.** $A_{s,ef}=19{,}63$ cm² $\leq4\%\cdot25\cdot90=90$ cm². OK.
````

```{figure} ../_static/aulas/detalhamento-secoes/exemplo-secao-apoio.png
:alt: Seção de apoio da viga 25 por 90 centímetros com quatro camadas de quatro barras de 12,5 milímetros no topo, barras de pele nas laterais até a linha neutra, porta-estribos na base e estribo de quatro ramos
:width: 75%
:align: center

Detalhamento final da seção de apoio do exemplo.
```

```{admonition} Leitura crítica do exemplo
:class: destaque-azul

Dezesseis barras em quatro camadas funcionam, mas tornam a concretagem difícil em uma seção de $25$ cm. A Atividade em sala compara esse arranjo com bitolas maiores. Repare também que as barras superiores de uma viga com $h=90$ cm estão na **zona de má aderência**: os comprimentos de ancoragem dessas barras serão cerca de $40\%$ maiores que os das barras inferiores.
```

## Atividade em sala

### Exercício 1: outras bitolas para a mesma seção

Para a seção de apoio do exemplo ($A_{s,nec}=19{,}51$ cm², $d_{adotado}=80$ cm), refaça o detalhamento com $\phi16$ e com $\phi20$, usando os espaçamentos mínimos ($a_h=3{,}0$ cm, $a_v=2{,}0$ cm). Para cada bitola, determine: número de barras, $A_{s,ef}$, barras por camada, número de camadas, $y_{cg}$, $d_{real}$ e o critério de armadura concentrada. Compare com o arranjo de $\phi12{,}5$ e escolha um, justificando.

| Bitola | $n$ | $A_{s,ef}$ (cm²) | Barras por camada | Camadas | $y_{cg}$ (cm) | $d_{real}$ (cm) | $a\leq0{,}1h$? |
|---|---:|---:|---:|---:|---:|---:|---|
| $\phi12{,}5$ | 16 | 19,63 | 4 | 4 | 9,53 | 80,47 | Sim |
| $\phi16$ | | | | | | | |
| $\phi20$ | | | | | | | |

### Exercício 2: seção de vão da mesma viga

Na seção de máximo momento positivo da mesma viga, a área necessária é $A_{s,nec}=11{,}0$ cm² (tração embaixo). Detalhe a seção com $\phi16$: número de barras, camadas, $d_{real}$, verificação de armadura concentrada, armadura de pele e porta-estribos. Desenhe a seção.

### Exercício 3: viga estreita

Uma viga $14\times50$ cm em CAA II (cobrimento de $3{,}0$ cm), concretada com brita 1 ($d_{máx}=19$ mm), com estribo de $\phi5{,}0$, foi dimensionada com $d=44$ cm e precisa de $A_{s,nec}=4{,}20$ cm². Compare os arranjos com $\phi10$, $\phi12{,}5$ e $\phi16$. Em qual deles o $d_{real}$ é menor que o $d$ adotado? O que fazer nesse caso?

### Exercício 4: ancoragem

Considere concreto C25 e barras de $\phi12{,}5$.

1. Calcule $f_{ctd}$, $f_{bd}$ e $\ell_b$ em boa e em má aderência.
2. As barras superiores da seção de apoio do exemplo ($h=90$ cm) estão em boa ou em má aderência? E as barras inferiores?
3. Calcule $\ell_{b,nec}$ das barras superiores supondo ganchos nas extremidades ($\alpha=0{,}7$) e $A_{s,calc}/A_{s,ef}=19{,}51/19{,}63$. Confira $\ell_{b,min}$.

## Roteiro do detalhamento transversal

1. Escolher a bitola e calcular $n=\lceil A_{s,nec}/A_\phi\rceil$.
2. Definir $c_{nom}$ (CAA) e conferir $d_{máx}\leq1{,}2c_{nom}$.
3. Calcular $a_h$, $a_v$, $b_{disp}$ e o número de barras por camada.
4. Distribuir as barras em camadas alinhadas e calcular $y_{cg}$ e $d_{real}$.
5. Se $d_{real}<d_{adotado}$, recalcular $A_s$ e voltar ao passo 1.
6. Verificar a armadura concentrada ($a\leq0{,}10h$) e a armadura máxima.
7. Prever porta-estribos e, se $h>60$ cm, armadura de pele.
8. Desenhar a seção com a identificação das barras (posição, quantidade, bitola).

## Síntese

```{admonition} O que levar desta aula
:class: destaque-azul

1. O detalhamento transforma a área calculada em barras comerciais e define o $d$ real da seção.
2. O cobrimento nominal depende da CAA e é medido até o estribo. Os espaçamentos livres mínimos dependem do diâmetro da barra e do agregado.
3. O número de barras por camada é $n\leq(b_{disp}+a_h)/(\phi+a_h)$.
4. Com várias camadas, $d_{real}=h-y_{cg}$ deve ser maior ou igual ao $d$ do dimensionamento; caso contrário, recalcula-se $A_s$.
5. A armadura pode ser tratada como concentrada se $y_{cg}-y_1\leq0{,}10h$.
6. Vigas com $h>60$ cm exigem armadura de pele de $0{,}10\%A_{c,alma}$ por face, com espaçamento de até $20$ cm.
7. O comprimento de ancoragem depende da aderência: barras em má aderência precisam de comprimentos cerca de $40\%$ maiores.
```

## Referências

- PEREIRA JUNIOR, Wanderlei Malaquias. *Exemplo 02: detalhamento e verificação do centroide da armadura*. Material do professor (Estruturas de Concreto Armado 1, aula 35). Base para o exemplo resolvido.
- ABNT. *NBR 6118: Projeto de estruturas de concreto*. Rio de Janeiro, 2023. Itens 7.4 (cobrimento, Tabela 7.2), 9.3 e 9.4 (aderência e ancoragem, Tabela 9.1), 17.2.4.1 (armadura concentrada), 17.3.5.2 (armaduras mínima, de pele e máxima) e 18.3 (disposições construtivas de vigas).
- CARVALHO, Roberto Chust; FIGUEIREDO FILHO, Jasson Rodrigues de. *Cálculo e detalhamento de estruturas usuais de concreto armado*. São Carlos: EdUFSCar.
