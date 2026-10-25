# Aula 10: Detalhamento de lajes maciças

As aulas anteriores levaram cada laje do pavimento até a área de aço por metro, em cada direção e em cada região: os esforços vieram da [Aula 06](006-esforcos-lajes.md), as verificações preliminares da [Aula 07](007-verificacoes-preliminares-lajes.md), o dimensionamento da [Aula 08](008-armadura-simples.md) e as regras de ancoragem da [Aula 09](009-detalhamento-secoes.md). Falta a etapa que chega à obra: **quais barras, com que espaçamento, com que comprimento, quantas e em que posição?**

A aula segue a ordem do trabalho do projetista: escolher bitola e espaçamento, conferir as armaduras mínimas e os limites construtivos, definir o comprimento das barras positivas e negativas, contar as barras, prever as armaduras de borda e de canto e, por fim, desenhar as plantas de armação e montar a tabela de aço. Um exemplo com duas lajes vizinhas, no padrão do trabalho prático, acompanha todas as etapas.

```{admonition} Objetivos da aula
:class: destaque-azul

- Converter a área de aço por metro em bitola e espaçamento.
- Verificar as armaduras mínimas, a armadura de distribuição, o espaçamento máximo e o diâmetro máximo das barras de laje.
- Determinar o comprimento e o número das barras positivas.
- Determinar o comprimento das barras negativas sobre os apoios pelas três alternativas usuais.
- Prever a armadura negativa de borda, as barras de distribuição e a armadura de canto.
- Desenhar as plantas de armação positiva e negativa e montar a tabela de aço.
```

## A sequência do detalhamento

1. **Áreas de aço** por metro ($\text{cm}^2/\text{m}$), em cada direção e região: positivas (vão) e negativas (apoios).
2. **Bitola e espaçamento** de cada armadura.
3. **Verificações**: armadura mínima, armadura de distribuição, espaçamento máximo e diâmetro máximo.
4. **Comprimentos**: barras positivas, negativas sobre apoios, negativas de borda e de canto.
5. **Quantidades**: número de barras em cada posição.
6. **Desenho**: planta de armação positiva, planta de armação negativa e cortes.
7. **Tabela de aço**: comprimento total e massa por bitola.

## Bitola e espaçamento

Para uma área necessária $A_s$ (cm²/m) e uma barra de área $A_{s\phi}$ (cm²), o número de barras por metro e o espaçamento são:

$$n=\frac{A_s}{A_{s\phi}}\qquad\qquad s=\frac{1\text{ m}}{n}=\frac{A_{s\phi}}{A_s}\ (\text{m})$$

Arredonda-se $s$ **para baixo** (em geral, a centímetro inteiro). A área efetiva é $A_{s,ef}=A_{s\phi}/s$. A tabela abaixo dá a área por metro de algumas combinações usuais:

| $\phi$ (mm) | $s=10$ cm | $s=12$ cm | $s=15$ cm | $s=17$ cm | $s=20$ cm |
|---|---:|---:|---:|---:|---:|
| 5,0 | 1,96 | 1,64 | 1,31 | 1,15 | 0,98 |
| 6,3 | 3,12 | 2,60 | 2,08 | 1,84 | 1,56 |
| 8,0 | 5,03 | 4,19 | 3,35 | 2,96 | 2,52 |
| 10,0 | 7,85 | 6,54 | 5,24 | 4,62 | 3,93 |

Valores em $\text{cm}^2/\text{m}$. Na prática, evitam-se espaçamentos menores que 7 a 8 cm, que dificultam a concretagem e a montagem, e procura-se repetir as mesmas bitolas em todo o pavimento.

## Limites da NBR 6118 para as armaduras de lajes

### Armaduras mínimas

Segundo o item 19.3.3.2 da NBR 6118, a armadura mínima melhora o desempenho e a ductilidade à flexão e à punção e controla a fissuração. Deve ser feita, de preferência, com barras de alta aderência ou telas soldadas. Com $\rho_s=A_s/(b_wh)$ e $\rho_{min}$ da Tabela 17.3 (para C20 a C30, $\rho_{min}=0{,}150\%$; ver a Aula 07):

| Armadura | Taxa mínima |
|---|---|
| Negativa | $\rho_s\geq\rho_{min}$ |
| Positiva de laje armada em duas direções (cada direção) | $\rho_s\geq0{,}67\,\rho_{min}$ |
| Positiva principal de laje armada em uma direção | $\rho_s\geq\rho_{min}$ |
| Positiva secundária (distribuição) de laje armada em uma direção | $A_s/s\geq20\%$ da principal, $\geq0{,}9\ \text{cm}^2/\text{m}$ e $\rho_s\geq0{,}5\,\rho_{min}$ |

### Armadura máxima

A soma das armaduras de tração e de compressão não pode ultrapassar $4\%\,A_c$ (itens 19.3.3.3 e 17.3.5.2.4). Em lajes usuais, esse limite raramente governa.

### Armadura secundária de flexão

Em lajes armadas em duas direções, a armadura secundária de flexão, por metro de largura, deve ter área de pelo menos $20\%$ da armadura principal, com espaçamento de no máximo $33$ cm (item 20.1). A emenda dessas barras segue os critérios da armadura principal.

### Espaçamento e diâmetro máximos

Na região dos maiores momentos fletores, a armadura principal de flexão deve respeitar (item 20.1):

$$s\leq\begin{cases}20\text{ cm}\\ 2h\end{cases}\qquad\qquad\phi\leq\frac{h}{8}$$

Em lajes armadas em duas direções, as duas direções são calculadas e tratadas como principais; nesta disciplina, aplicamos o limite de $20$ cm (ou $2h$, se menor) às duas.

## Barras positivas: comprimento e distribuição

### Comprimento

As barras inferiores estão adequadamente ancoradas se avançarem, pelo menos, $10\phi$ além da face dos apoios. Nas extremidades do edifício, costumam ser estendidas até junto à face externa da viga, respeitando o cobrimento. Uma regra prática para o comprimento reto é

$$C=l_0+2\,\ell_{ext},\qquad \ell_{ext}\geq10\phi,\quad\ell_{ext}\leq t-c_{nom}$$

em que $l_0$ é o vão livre (entre faces das vigas) e $t$ a largura da viga de apoio. Arredonda-se $C$ para baixo, para múltiplo de $5$ cm, conferindo que $\ell_{ext}\geq10\phi$ continue atendido.

```{admonition} Barras alternadas
:class: destaque-azul

Para economizar aço, metade das barras pode ser interrompida antes dos apoios, com os comprimentos aproximados abaixo (Pinheiro, Muzardo e Santos), centrados no vão. As demais vão de apoio a apoio. Nesta disciplina, usamos barras corridas, que são mais simples de desenhar e de montar.

| Vínculos nas extremidades da barra | Comprimento da barra mais curta |
|---|---|
| Dois lados apoiados | $0{,}85\,l$ |
| Um lado apoiado e outro engastado | $0{,}85\,l$ |
| Dois lados engastados | $0{,}70\,l$ |
```

### Número de barras

As barras de uma direção são distribuídas ao longo do vão livre da **outra** direção. Deixando a primeira e a última barra a no máximo $s/2$ da face das vigas:

$$n=\left\lceil\frac{l_0}{s}\right\rceil$$

em que $l_0$ é o comprimento livre da faixa em que as barras se distribuem. Com esse número, o espaçamento real ($l_0/n$) é igual ou menor que $s$.

## Barras negativas sobre os apoios

### Extensão a partir do eixo do apoio

O comprimento das barras negativas deve vir do diagrama de momentos fletores na região do apoio. Em edifícios usuais, para apoios de lajes retangulares sem bordas livres, pode-se usar um **diagrama trapezoidal aproximado**, com base de $0{,}25\,\ell$ de cada lado do eixo do apoio, deslocado de $a_\ell$. O valor de $\ell$ é:

- o **maior dos menores vãos** das lajes adjacentes, quando as duas foram consideradas engastadas nesse apoio;
- o **menor vão da laje admitida engastada**, quando a outra foi suposta simplesmente apoiada nesse vínculo.

Para lajes armadas em uma direção, com borda engastada, a extensão é $0{,}25$ do vão. O deslocamento do diagrama, em lajes sem armadura transversal, é $a_\ell=1{,}5\,d$, e $\ell_b$ é o comprimento de ancoragem da Aula 09 (com gancho, $0{,}7\,\ell_b$).

```{figure} ../_static/aulas/detalhamento-lajes/negativas-alternativas.png
:alt: Diagrama trapezoidal de momento negativo sobre o apoio, com base de 0,25 do vão de cada lado, e três arranjos de barras negativas: um só tipo, dois comprimentos e barras alternadas de mesmo comprimento
:width: 80%
:align: center

Diagrama aproximado de momentos negativos e alternativas para as barras (adaptado de Pinheiro, Muzardo e Santos).
```

### Três alternativas

**a) Um só tipo de barra.** Cada barra se estende $a_1$ de cada lado do eixo do apoio, com

$$a_1\geq\begin{cases}a_\ell+\ell_b\\ 0{,}25\,\ell+10\phi\end{cases}\qquad(\text{em geral, prevalece o segundo})$$

**b) Dois comprimentos.** Metade das barras é longa ($a_{21}$) e metade é curta ($a_{22}$):

$$a_{21}\geq\begin{cases}\dfrac{0{,}25\,\ell+a_\ell}{2}+\ell_b\\[2mm] 0{,}25\,\ell+10\phi\end{cases}\qquad a_{22}\geq\begin{cases}a_\ell+\ell_b\\[1mm] \dfrac{0{,}25\,\ell+a_\ell}{2}+10\phi\end{cases}$$

(em geral, prevalece o segundo valor de $a_{21}$ e o segundo de $a_{22}$).

**c) Barras alternadas de mesmo comprimento.** Todas as barras têm o mesmo comprimento $a=a_{21}+a_{22}$, e são colocadas de forma alternada: uma avança $a_{21}$ para um lado e $a_{22}$ para o outro; a seguinte, o contrário. Com os valores que em geral prevalecem:

$$a=0{,}25\,\ell+10\phi+\frac{0{,}25\,\ell+a_\ell}{2}+10\phi=\frac{3}{8}\,\ell+20\phi+0{,}75\,d$$

Em uma primeira estimativa, pode-se posicioná-las com $a_{21}\approx\frac{2}{3}a$ e $a_{22}\approx\frac{1}{3}a$, conferindo depois os mínimos de cada lado. Os comprimentos são arredondados para múltiplos de $5$ cm.

A alternativa (c) é a mais econômica e tem uma só posição de barra no desenho; a (a) é a mais simples de montar.

### Ganchos e posicionamento

As barras negativas terminam, em geral, com ganchos em ângulo reto voltados para baixo, cuja perna mede cerca de $h-2c_{nom}$. Como a ponta reta mínima do gancho de $90°$ é $8\phi$, em lajes finas isso limita a bitola: com $h=12$ cm e $c_{nom}=2{,}5$ cm, a perna é $7$ cm e cabe $\phi8$ ($8\phi=6{,}4$ cm), mas não $\phi10$ ($8$ cm).

Para garantir a posição das barras negativas durante a concretagem, colocam-se, perpendicularmente a elas, **barras de distribuição** com as mesmas áreas e espaçamentos da armadura positiva secundária ($\geq20\%$ da principal, $\geq0{,}9\ \text{cm}^2/\text{m}$, $\rho_s\geq0{,}5\rho_{min}$, $s\leq33$ cm), e apoia-se o conjunto em **caranguejos** (barras dobradas que se apoiam na armadura inferior) ou em espaçadores próprios.

## Armadura negativa de borda

Nos apoios de lajes **sem continuidade** com lajes adjacentes e ligados às vigas de borda, a laje é calculada como simplesmente apoiada, mas a ligação monolítica com a viga produz momentos negativos que fissuram a face superior. Por isso, dispõe-se uma **armadura negativa de borda**.

```{admonition} Critério a adotar
:class: destaque-vermelho

Carvalho e Figueiredo Filho observam que a recomendação explícita de armadura negativa de borda não foi mantida na versão final da NBR 6118:2023 e registram o critério da NBR 6118:1980 para as barras sobre os apoios. Na prática de projeto, usa-se uma armadura de área mínima $\rho_s\geq0{,}67\rho_{min}$ (valor que constava da Tabela 19.1 da edição de 2014), estendida a partir da face do apoio por um comprimento da ordem de $0{,}15\,l_x$, com gancho na extremidade. **Nesta disciplina, adote esse critério**, ou outro indicado pelo professor, e registre-o na memória de cálculo.
```

## Armadura de canto

Nos cantos de lajes retangulares formados por **duas bordas simplesmente apoiadas**, os momentos volventes (momentos torçores) tendem a levantar o canto. Quando não se calcula uma armadura específica para esses momentos, deve-se dispor uma **armadura de canto**:

- **superior**: barras paralelas à bissetriz do ângulo do canto;
- **inferior**: barras perpendiculares à bissetriz, ou, em substituição, uma malha de duas armaduras perpendiculares;
- **área**: tanto a superior quanto a inferior com, pelo menos, **metade da armadura no centro da laje, na direção mais armada** ($a_{sc}\geq\frac12a_{sx}$);
- **extensão**: até $1/5$ do menor vão da laje ($l_x/5$), medida a partir das faces dos apoios.

```{figure} ../_static/aulas/detalhamento-lajes/armadura-canto.png
:alt: Planta de uma laje com duas bordas engastadas e duas apoiadas; no canto entre as bordas apoiadas, um quadrado de lado lx sobre 5 com barras superiores paralelas à bissetriz e, ao lado, barras inferiores perpendiculares à bissetriz
:width: 85%
:align: center

Armadura de canto em um canto formado por duas bordas simplesmente apoiadas (adaptado de Pinheiro, Muzardo e Santos).
```

Na prática, a armadura negativa de borda das duas vigas que formam o canto já forma uma malha superior. Se essa malha tiver, em cada direção, área de pelo menos $a_{sc}$ e se estender até $l_x/5$, ela pode substituir a armadura superior de canto.

## Desenho e tabela de aço

As lajes são representadas em **plantas de armação**: uma para a armadura positiva (inferior) e outra para a negativa (superior). Em cada posição desenha-se **uma barra representativa** e uma **linha de distribuição** que indica a faixa em que as barras se repetem. A barra é identificada por:

$$\underbrace{33}_{\text{quantidade}}\ \underbrace{\text{N1}}_{\text{posição}}\ \underbrace{\phi6{,}3}_{\text{bitola}}\ \underbrace{\text{c/15}}_{\text{espaçamento}}\ \underbrace{C=405}_{\text{comprimento (cm)}}$$

A **tabela de aço** reúne, para cada posição, a bitola, a quantidade, o comprimento unitário e o comprimento total; e, para cada bitola, a massa total, com a massa linear da Aula 09.

````{admonition} Exemplo resolvido: lajes L1 e L2
:class: destaque-verde

**Dados.** Duas lajes vizinhas, apoiadas em vigas de $14$ cm de largura: L1 com $4{,}00\times5{,}00$ m e L2 com $3{,}60\times5{,}00$ m (medidas entre eixos), separadas pela viga V2. Concreto C30, aço CA-50, CAA II ($c_{nom}=2{,}5$ cm), brita 1, $h=12$ cm. As bordas sobre as vigas externas (V1, V3, V4 e V5) foram consideradas simplesmente apoiadas e a borda comum (V2), engastada nas duas lajes. Os momentos de cálculo, já compatibilizados na borda comum (Aula 06), são:

| Região | L1 | L2 |
|---|---:|---:|
| Positivo na direção x (vão menor) | $7{,}2$ | $5{,}9$ |
| Positivo na direção y | $3{,}6$ | $2{,}7$ |
| Negativo sobre V2 (direção x) | $-13{,}7$ | $-13{,}7$ |

Valores em kN·m/m.

```{figure} ../_static/aulas/detalhamento-lajes/planta-positivas.png
:alt: Planta das lajes L1 e L2 com as vigas V1 a V5 e as quatro posições de barras positivas N1 a N4 com quantidades, bitolas, espaçamentos e comprimentos
:width: 90%
:align: center

Planta de armação positiva do exemplo.
```

**1. Armaduras mínimas.** $A_{s,min}^{+}=0{,}67\cdot0{,}150\%\cdot100\cdot12=1{,}21\ \text{cm}^2/\text{m}$ (positiva, duas direções) e $A_{s,min}^{-}=0{,}150\%\cdot100\cdot12=1{,}80\ \text{cm}^2/\text{m}$ (negativa).

**2. Áreas, bitolas e espaçamentos** (procedimento da Aula 08; todas as seções no domínio 2, $\varphi_{adot}=0{,}931$). A direção x, mais solicitada, fica na camada inferior; a direção y, sobre ela.

| Armadura | $d$ (cm) | $A_{s,calc}$ | $A_{s,nec}$ | $s_{max}$ pela área | Adotado | $A_{s,ef}$ |
|---|---:|---:|---:|---:|---|---:|
| L1, x (+) | 9,19 | 1,94 | 1,94 | 16,1 cm | $\phi6{,}3$ c/15 | 2,08 |
| L1, y (+) | 8,56 | 1,04 | 1,21 | 25,8 cm | $\phi6{,}3$ c/20 | 1,56 |
| L2, x (+) | 9,19 | 1,59 | 1,59 | 19,6 cm | $\phi6{,}3$ c/19 | 1,64 |
| L2, y (+) | 8,56 | 0,78 | 1,21 | 25,8 cm | $\phi6{,}3$ c/20 | 1,56 |
| V2 (−) | 9,10 | 3,72 | 3,72 | 13,5 cm | $\phi8$ c/13 | 3,87 |

Áreas em $\text{cm}^2/\text{m}$. Verificações: $s\leq\min(20;\,2\cdot12)=20$ cm em todas as posições; $\phi\leq h/8=15$ mm; armadura máxima atendida com folga. Na negativa, $\phi8$ foi escolhido em vez de $\phi10$ por causa da perna do gancho.

**3. Comprimento e número das barras positivas.** Vãos livres: L1, $l_{0x}=400-14=386$ cm; L2, $l_{0x}=360-14=346$ cm; ambas, $l_{0y}=500-14=486$ cm. Extensão nas vigas: até $t-c_{nom}=14-2{,}5=11{,}5$ cm, maior que $10\phi=6{,}3$ cm.

| Posição | Barras | $C=l_0+2\cdot11{,}5$ | Adotado | Distribuição | Quantidade |
|---|---|---:|---:|---|---:|
| N1 | L1, x | 409 | 405 | ao longo de $486$ cm, c/15 | $\lceil486/15\rceil=33$ |
| N2 | L1, y | 509 | 505 | ao longo de $386$ cm, c/20 | $\lceil386/20\rceil=20$ |
| N3 | L2, x | 369 | 365 | ao longo de $486$ cm, c/19 | $\lceil486/19\rceil=26$ |
| N4 | L2, y | 509 | 505 | ao longo de $346$ cm, c/20 | $\lceil346/20\rceil=18$ |

Com $C$ arredondado para baixo, cada barra entra $9{,}5$ cm em cada viga, ainda maior que $10\phi$.

**4. Barras negativas sobre V2.** As duas lajes são engastadas em V2: $\ell=\max(4{,}00;\ 3{,}60)=4{,}00$ m. Para $\phi8$ e $d=9{,}1$ cm:

$$a_\ell=1{,}5\cdot9{,}1=13{,}7\text{ cm}\qquad\ell_b=33{,}4\phi=26{,}7\text{ cm (C30, boa aderência)}\qquad\ell_{b,gancho}=0{,}7\cdot26{,}7=18{,}7\text{ cm}$$

*Alternativa (a):*

$$a_1\geq\max(13{,}7+18{,}7;\ 0{,}25\cdot400+10\cdot0{,}8)=\max(32{,}4;\ 108)=108\ \Rightarrow\ 110\text{ cm}$$

Cada barra: $2\cdot110=220$ cm retos e dois ganchos de $7$ cm, $C=234$ cm.

*Alternativa (c):*

$$a_{21}\geq\max\left(\frac{100+13{,}7}{2}+18{,}7;\ 108\right)=108\Rightarrow110\text{ cm}\qquad a_{22}\geq\max\left(32{,}4;\ \frac{100+13{,}7}{2}+8\right)=64{,}9\Rightarrow65\text{ cm}$$

$a=110+65=175$ cm (a expressão aproximada dá $\frac38\cdot400+20\cdot0{,}8+0{,}75\cdot9{,}1=172{,}8$ cm). Cada barra: $175$ cm retos e dois ganchos de $7$ cm, $C=189$ cm, colocadas alternadamente. Quantidade: $\lceil486/13\rceil=38$ barras. **Adota-se a alternativa (c): $38$ N5 $\phi8$ c/13, $C=189$ cm**, que gasta $19\%$ menos aço que a (a) nessa posição.

**5. Barras de distribuição sob as negativas.** $A_s\geq\max(0{,}20\cdot3{,}72;\ 0{,}9;\ 0{,}5\cdot1{,}80)=0{,}90\ \text{cm}^2/\text{m}$: $\phi6{,}3$ c/30 ($1{,}04\ \text{cm}^2/\text{m}$, $s\leq33$ cm). As negativas ocupam uma faixa de $2\cdot110=220$ cm: $\lceil220/30\rceil=8$ barras N6 de $C=505$ cm, paralelas a V2.

```{figure} ../_static/aulas/detalhamento-lajes/planta-negativas.png
:alt: Planta das lajes L1 e L2 com as barras negativas alternadas N5 sobre a viga V2 e as barras de distribuição N6
:width: 90%
:align: center

Planta de armação negativa sobre V2.
```

```{figure} ../_static/aulas/detalhamento-lajes/corte-sobre-v2.png
:alt: Corte transversal da laje sobre a viga V2 mostrando as barras positivas das duas lajes, a barra negativa com ganchos, as barras de distribuição, o caranguejo e os espaçadores
:width: 95%
:align: center

Corte sobre V2: posição relativa das armaduras.
```

**6. Tabela de aço** (sem as armaduras de borda e de canto, que ficam para a atividade):

| Posição | $\phi$ (mm) | Quantidade | $C$ unitário (m) | $C$ total (m) |
|---|---:|---:|---:|---:|
| N1 | 6,3 | 33 | 4,05 | 133,65 |
| N2 | 6,3 | 20 | 5,05 | 101,00 |
| N3 | 6,3 | 26 | 3,65 | 94,90 |
| N4 | 6,3 | 18 | 5,05 | 90,90 |
| N5 | 8,0 | 38 | 1,89 | 71,82 |
| N6 | 6,3 | 8 | 5,05 | 40,40 |

| Bitola | Comprimento total (m) | Massa linear (kg/m) | Massa (kg) |
|---|---:|---:|---:|
| $\phi6{,}3$ | 460,85 | 0,245 | 112,9 |
| $\phi8$ | 71,82 | 0,395 | 28,4 |
| **Total** | | | **141,3** |

Na encomenda real, acrescentam-se as perdas de corte (em geral, alguns por cento), conforme a prática da obra.
````

## Atividade em sala

### Exercício 1: completar o exemplo

1. **Negativas de borda.** Dimensione a armadura negativa de borda sobre V1, V3, V4 e V5 ($\rho_s\geq0{,}67\rho_{min}$; extensão de $0{,}15\,l_x$ a partir da face do apoio; ganchos de $7$ cm). Defina bitola, espaçamento, comprimento e quantidade em cada borda.
2. **Cantos.** Identifique os cantos com duas bordas simplesmente apoiadas e calcule a armadura de canto ($a_{sc}\geq\frac12a_{sx}$, extensão $l_x/5$). A malha formada pelas negativas de borda atende à armadura superior de canto? Se não, o que falta?
3. **Atualize a tabela de aço** e calcule o acréscimo de massa.
4. Desenhe à mão as duas plantas de armação completas.

### Exercício 2: laje armada em uma direção

A laje L3 tem $3{,}00\times7{,}50$ m entre eixos, apoiada em vigas de $14$ cm nas quatro bordas, $h=10$ cm, C30, CA-50, CAA II. O momento positivo de cálculo na direção do vão menor é $m_d=6{,}0$ kN·m/m.

1. Classifique a laje e calcule a armadura principal (compare $\phi6{,}3$ e $\phi8$).
2. Calcule a armadura de distribuição (secundária) e o seu espaçamento máximo.
3. Determine os comprimentos e as quantidades das barras principais e de distribuição.
4. Por que a armadura de distribuição de uma laje armada em uma direção não pode ser "só a mínima de $0{,}9\ \text{cm}^2/\text{m}$" em qualquer caso?

### Exercício 3: trabalho prático

Aplique o roteiro desta aula às lajes do pavimento-tipo do trabalho prático, usando as áreas de aço obtidas na Entrega 4. Monte a planta de armação positiva, a planta de armação negativa e a tabela de aço do pavimento.

## Roteiro do detalhamento de lajes

1. Para cada laje, direção e região, calcular $A_s$ e conferir $A_{s,min}$ (Tabela 19.1).
2. Escolher $\phi$ e $s$ (arredondar $s$ para baixo); verificar $s\leq\min(20;2h)$ e $\phi\leq h/8$.
3. Barras positivas: $C=l_0+2\ell_{ext}$, com $\ell_{ext}\geq10\phi$; $n=\lceil l_0/s\rceil$.
4. Barras negativas: definir $\ell$, $a_\ell=1{,}5d$ e $\ell_b$; escolher a alternativa (a), (b) ou (c); conferir a perna do gancho.
5. Barras de distribuição sob as negativas e armadura secundária.
6. Negativas de borda e armadura de canto.
7. Plantas de armação, cortes e tabela de aço.

## Síntese

```{admonition} O que levar desta aula
:class: destaque-azul

1. O espaçamento sai de $s=A_{s\phi}/A_s$ e é arredondado para baixo; a área efetiva deve ser maior que a necessária e que a mínima.
2. Em lajes, $s\leq\min(20\text{ cm};2h)$ e $\phi\leq h/8$; a armadura secundária tem pelo menos $20\%$ da principal, $0{,}9\ \text{cm}^2/\text{m}$ e $s\leq33$ cm.
3. As barras positivas entram pelo menos $10\phi$ além da face do apoio; seu número é $\lceil l_0/s\rceil$.
4. As barras negativas cobrem um diagrama trapezoidal de base $0{,}25\ell$ de cada lado do apoio, deslocado de $a_\ell=1{,}5d$, mais ancoragem: $a_1\geq\max(a_\ell+\ell_b;\ 0{,}25\ell+10\phi)$. Barras alternadas de mesmo comprimento economizam aço.
5. A bitola das negativas é limitada pela perna do gancho em lajes finas.
6. Bordas sem continuidade recebem armadura negativa de borda e cantos entre bordas apoiadas recebem armadura de canto ($a_{sc}\geq a_{sx}/2$, até $l_x/5$).
7. O produto final são as plantas de armação positiva e negativa e a tabela de aço.
```

## Referências

- CARVALHO, Roberto Chust; FIGUEIREDO FILHO, Jasson Rodrigues de. *Cálculo e detalhamento de estruturas usuais de concreto armado*. São Carlos: EdUFSCar. Capítulo de lajes maciças, item 7.4.11 (detalhamento das armaduras: espaçamento, armaduras mínimas e máximas, armadura secundária, espaçamento e diâmetro máximos e armadura sobre os apoios).
- PINHEIRO, Libânio Miranda; MUZARDO, Cassiane D.; SANTOS, Sandro P. *Fundamentos do concreto e projeto de edifícios*. São Carlos: EESC-USP. Capítulo 11, *Lajes maciças*, itens 11.8 (barras sobre os apoios), 11.9 (barras inferiores) e 11.10 (armadura de canto).
- ABNT. *NBR 6118: Projeto de estruturas de concreto*. Rio de Janeiro, 2023. Itens 9.4 (ancoragem), 17.3.5 (armaduras mínima e máxima), 19.3.3 (armaduras longitudinais de lajes) e 20.1 (detalhamento de lajes); Tabelas 17.3 e 19.1.
