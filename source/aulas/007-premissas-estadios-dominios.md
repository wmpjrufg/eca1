# Aula 07: Premissas básicas, ensaio de Stuttgart, estádios e domínios de deformação

Na [Aula 06](006-verificacoes-preliminares-lajes.md), a verificação da flecha já pediu o momento de fissuração e a inércia da seção fissurada, isto é, o **Estádio II**. Esta aula explica de onde vêm esses conceitos e prepara o dimensionamento da [Aula 08](008-armadura-simples.md). A sequência é a da própria história do método: observar uma viga até a ruína, identificar as fases do seu comportamento, fixar as premissas que permitem calcular o estado-limite último e, por fim, classificar os possíveis diagramas de deformação em domínios.

```{admonition} Objetivos da aula
:class: destaque-azul

- Descrever o ensaio de flexão em quatro pontos (ensaio de Stuttgart) e o que ele revela sobre o comportamento de uma viga de concreto armado.
- Distinguir os Estádios I, II e III e associar cada um a uma verificação de projeto.
- Enunciar as premissas básicas do dimensionamento no estado-limite último.
- Identificar os domínios de deformação, seus pivôs e os limites de $\xi=x/d$.
- Enquadrar uma seção em flexão simples no domínio correspondente.
```

## Do comportamento real ao modelo de cálculo

Um modelo de cálculo só é confiável se reproduzir o que a estrutura faz. O concreto armado é um material composto, que fissura e cuja rigidez muda com a carga. Por isso, antes de equacionar o equilíbrio de uma seção, convém observar uma viga sendo carregada até a ruína e anotar o que acontece com as deformações, com as fissuras e com a flecha.

| Etapa | Pergunta | Onde é tratada |
|---|---|---|
| Ensaio | O que se observa quando a carga cresce até a ruína? | Esta aula |
| Estádios | Quais fases de comportamento existem e o que as separa? | Esta aula |
| Premissas | O que se admite para calcular o estado-limite último? | Esta aula |
| Domínios | Quais diagramas de deformação a norma admite na ruína? | Esta aula |
| Equilíbrio e $A_s$ | Quanta armadura equilibra o momento de cálculo? | [Aula 08](008-armadura-simples.md) |

## O ensaio de Stuttgart

Costuma-se chamar de **ensaio de Stuttgart** o ensaio clássico de uma viga de concreto armado biapoiada, carregada por **duas forças iguais** e simétricas, com a carga crescendo desde zero até a ruína ([Figura 1](#fig-ensaio)). Ele está associado à escola alemã de Stuttgart (Mörsch, Leonhardt e colaboradores), citada na [Aula 01](001-hist-prop.md), e aparece nos livros de concreto armado como a ilustração padrão das fases do comportamento à flexão.

(fig-ensaio)=
```{figure} ../_static/aulas/estadios-dominios/ensaio-quatro-pontos.png
:alt: Viga biapoiada com duas cargas P/2 a um terço do vão de cada apoio, diagrama de cortante com valor nulo no trecho central e diagrama de momento constante nesse trecho
:width: 85%
:align: center

Figura 1. Ensaio de flexão em quatro pontos. Entre as duas cargas o cortante é nulo e o momento é constante. A viga é instrumentada com extensômetros no concreto e na armadura e com medição da flecha no meio do vão. Esquema sem escala.
```

Com as cargas a uma distância $a=L/3$ de cada apoio, o trecho central fica em **flexão pura**: $V=0$ e

$$
M=\frac{P}{2}\,a=\frac{PL}{6}.
$$

Nesse trecho aparecem apenas as fissuras de flexão, verticais, sem a interferência do cortante. Os trechos laterais, com $V=P/2$, servem para o estudo do cisalhamento, tratado em outra etapa.

### O que se observa

Aumentando a carga de zero até a ruína, o ensaio mostra quatro fases:

1. **Carga pequena.** Não há fissuras. Concreto e aço deformam juntos, e as deformações medidas ao longo da altura variam linearmente.
2. **Primeiras fissuras.** Quando a tração no concreto alcança sua resistência, surgem fissuras verticais no trecho de momento máximo. Em cada fissura, a força de tração passa a ser carregada só pela armadura.
3. **Fissuração estabilizada.** Novas fissuras aparecem e as existentes sobem em direção à face comprimida. A linha neutra sobe, a tensão na armadura cresce e a flecha aumenta mais depressa que a carga.
4. **Ruína.** Ou a armadura escoa e as fissuras se abrem muito, ou o concreto comprimido se esmaga. Numa viga com quantidade adequada de armadura, a ruína ocorre depois do escoamento do aço, com aviso visível.

Dois resultados do ensaio sustentam o modelo de cálculo. O primeiro é que as deformações medidas ao longo da altura continuam lineares, em média, mesmo depois da fissuração. O segundo é que o comportamento muda de natureza em dois momentos, a fissuração e o escoamento, o que leva à divisão em estádios.

## Os estádios

Os **estádios** são as fases de comportamento de uma seção sob momento crescente. A [Figura 2](#fig-curva-m-chi) mostra a relação entre momento e curvatura de forma esquemática, e a [Figura 3](#fig-estadios) mostra a seção, as deformações e as tensões em cada fase.

(fig-curva-m-chi)=
```{figure} ../_static/aulas/estadios-dominios/curva-momento-curvatura.png
:alt: Curva de momento fletor contra curvatura com três trechos, estádio I até o momento de fissuração, estádio II até o escoamento da armadura e estádio III até a ruína
:width: 85%
:align: center

Figura 2. Curva momento–curvatura esquemática. A fissuração reduz a rigidez e o escoamento da armadura a reduz de novo. Esquema sem escala.
```

(fig-estadios)=
```{figure} ../_static/aulas/estadios-dominios/estadios-secao.png
:alt: Seção retangular com armadura inferior, diagramas de deformação e diagramas de tensão nos estádios I, II e III
:width: 100%
:align: center

Figura 3. Seção, deformações e tensões nos três estádios. Esquema sem escala.
```

### Estádio I: seção não fissurada

O concreto tracionado ainda resiste. O material se comporta de modo aproximadamente elástico, com diagrama linear de tensões, tanto na compressão quanto na tração. A linha neutra passa perto do centro de gravidade da seção.

O estádio termina quando a tração na fibra inferior atinge a resistência do concreto à tração. O momento correspondente é o **momento de fissuração**, já usado na Aula 06,

$$
M_r=\alpha\frac{f_{ctm}I_c}{y_t},
\qquad\alpha=1{,}5\text{ para seção retangular.}
$$

Costuma-se subdividir o estádio em Ia (concreto tracionado ainda elástico) e Ib (concreto tracionado já em plastificação, no instante que antecede a fissura). Para o projeto, basta o valor de $M_r$.

### Estádio II: seção fissurada

Abaixo da linha neutra, o concreto está fissurado e sua resistência à tração é desprezada. A tração fica só na armadura. A compressão no concreto ainda é linear, e o aço ainda é elástico. A linha neutra sobe em relação ao Estádio I, e a rigidez da seção cai.

Para uma seção retangular com armadura simples, a posição $x_{II}$ da linha neutra e a inércia $I_{II}$ saem do equilíbrio da seção homogeneizada, com $\alpha_e=E_s/E_{cs}$:

$$
\frac{b_wx_{II}^2}{2}=\alpha_eA_s(d-x_{II}),
\qquad
I_{II}=\frac{b_wx_{II}^3}{3}+\alpha_eA_s(d-x_{II})^2.
$$

Para um momento $M$ nesse estádio, as tensões extremas valem

$$
\sigma_c=\frac{M\,x_{II}}{I_{II}},
\qquad
\sigma_s=\alpha_e\frac{M\,(d-x_{II})}{I_{II}}.
$$

O Estádio II é o estado da estrutura sob **cargas de serviço**. É nele que se calculam a abertura das fissuras e as flechas, como se viu na Aula 06 com a inércia equivalente de Branson. Em vigas com armadura usual, o estádio termina quando a armadura começa a escoar.

### Estádio III: ruína

O concreto comprimido deixa de ser linear: o diagrama de tensões se curva e, na ruína, o concreto está plastificado na parte mais comprimida. A armadura tracionada escoa. A linha neutra sobe ainda mais, e a seção chega ao **estado-limite último**.

O diagrama de tensões curvo é substituído, no cálculo, pelos diagramas de projeto das premissas da próxima seção. É no Estádio III que se faz o **dimensionamento** da Aula 08.

### Resumo dos estádios

| Estádio | Intervalo | Concreto tracionado | Diagrama de compressão | Uso no projeto |
|---|---|---|---|---|
| I | $0$ a $M_r$ | Resiste | Linear | $M_r$; rigidez bruta $I_c$ |
| II | $M_r$ até o escoamento da armadura | Fissurado, desprezado | Linear | Estados-limite de serviço: fissuração e flecha |
| III | Até a ruína | Desprezado | Curvo (plastificado) | Estado-limite último: dimensionamento |

## Premissas básicas do dimensionamento no ELU

O dimensionamento no estado-limite último parte das hipóteses do item 17.2.2 da NBR 6118. Cada uma delas pode ser lida como uma consequência do que o ensaio mostrou.

1. **Seções planas permanecem planas.** As deformações variam linearmente com a distância à linha neutra. O ensaio confirma isso em média, mesmo com fissuras.
2. **Aderência perfeita.** A deformação de uma barra aderente é igual à do concreto que a envolve, $\varepsilon_s=\varepsilon_c$ na mesma fibra.
3. **Resistência à tração do concreto desprezada.** No ELU, toda a tração é resistida pela armadura.
4. **Diagrama tensão–deformação de cálculo do concreto na compressão.** Parábola-retângulo, com tensão máxima $0{,}85f_{cd}$, ou o bloco retangular equivalente da Aula 08.
5. **Diagrama tensão–deformação de cálculo do aço.** Elastoplástico perfeito, com $\sigma_s=E_s\varepsilon_s$ até $\varepsilon_{yd}$ e $\sigma_s=f_{yd}$ depois.
6. **Estado-limite último.** Fica caracterizado quando o diagrama de deformações coincide com um dos domínios da seção seguinte, isto é, quando o aço atinge o alongamento máximo de $10\text{‰}$ ou o concreto atinge o encurtamento último $\varepsilon_{cu}$.
7. **Equilíbrio.** As resultantes das tensões equilibram os esforços solicitantes de cálculo.

(fig-sigma-eps)=
```{figure} ../_static/aulas/estadios-dominios/diagramas-tensao-deformacao.png
:alt: À esquerda, diagrama parábola-retângulo do concreto; à direita, diagrama elastoplástico perfeito do aço CA-50
:width: 100%
:align: center

Figura 4. Diagramas tensão–deformação de cálculo, para concreto até C50 e aço CA-50.
```

A [Figura 4](#fig-sigma-eps) mostra os dois diagramas. Para concretos até C50, o diagrama parábola-retângulo é

$$
\sigma_c=0{,}85f_{cd}\left[1-\left(1-\frac{\varepsilon_c}{\varepsilon_{c2}}\right)^2\right]
\quad(\varepsilon_c\leq\varepsilon_{c2}),
\qquad
\sigma_c=0{,}85f_{cd}\quad(\varepsilon_{c2}\leq\varepsilon_c\leq\varepsilon_{cu}),
$$

com $\varepsilon_{c2}=2{,}0\text{‰}$ e $\varepsilon_{cu}=3{,}5\text{‰}$. O fator $0{,}85$ reúne, entre outros efeitos, a ação de longa duração da carga. Para o aço, $\varepsilon_{yd}=f_{yd}/E_s$, que vale $2{,}07\text{‰}$ para o CA-50 com $\gamma_s=1{,}15$ e $E_s=210000\text{ MPa}$.

Para C55 a C90, os valores de $\varepsilon_{c2}$ e $\varepsilon_{cu}$ mudam:

$$
\varepsilon_{c2}=\left[2+0{,}085(f_{ck}-50)^{0{,}53}\right]\text{‰},
\qquad
\varepsilon_{cu}=\left[2{,}6+35\left(\frac{90-f_{ck}}{100}\right)^4\right]\text{‰},
$$

com $f_{ck}$ em MPa.

## Domínios de deformação

Os **domínios** reúnem todos os diagramas lineares de deformação que a norma admite na ruína de uma seção. Cada diagrama é definido por duas deformações, e as retas limite giram em torno de três pontos fixos, os **pivôs**:

| Pivô | Posição | Deformação fixada |
|---|---|---|
| A | Altura da armadura tracionada | $\varepsilon_s=10\text{‰}$ (alongamento máximo) |
| B | Fibra mais comprimida | $\varepsilon_c=\varepsilon_{cu}=3{,}5\text{‰}$ |
| C | A $3h/7$ da fibra mais comprimida | $\varepsilon_c=\varepsilon_{c2}=2{,}0\text{‰}$ |

A [Figura 5](#fig-dominios) mostra as retas limite que partem de cada pivô e as regiões entre elas.

(fig-dominios)=
```{figure} ../_static/aulas/estadios-dominios/dominios-deformacao.png
:alt: Retas e domínios de deformação, com os pivôs A, B e C e as retas a e b
:width: 95%
:align: center

Figura 5. Domínios de deformação no estado-limite último, para $f_{ck}\leq50$ MPa. Esquema sem escala.
```

| Região | Pivô | Solicitação típica | Característica |
|---|---|---|---|
| Reta a | | Tração uniforme | $\varepsilon_s=10\text{‰}$ em toda a seção |
| Domínio 1 | A | Tração não uniforme | Seção inteira tracionada, sem compressão |
| Domínio 2 | A | Flexão simples ou composta | Aço no limite de $10\text{‰}$; concreto com $\varepsilon_c<\varepsilon_{cu}$ |
| Domínio 3 | B | Flexão simples ou composta | Concreto em $\varepsilon_{cu}$; aço escoando, $\varepsilon_{yd}\leq\varepsilon_s\leq10\text{‰}$ |
| Domínio 4 | B | Flexão simples ou composta | Concreto em $\varepsilon_{cu}$; aço sem escoar, $\varepsilon_s<\varepsilon_{yd}$ |
| Domínio 4a | B | Flexão composta | Linha neutra no cobrimento da armadura inferior |
| Domínio 5 | C | Compressão não uniforme | Seção inteira comprimida |
| Reta b | | Compressão uniforme | $\varepsilon_c=\varepsilon_{c2}$ em toda a seção |

Na **flexão simples**, a seção só pode estar nos domínios 2, 3 ou 4. O domínio em que a seção cai depende da quantidade de armadura:

- **Domínio 2.** Pouca armadura em relação à seção. O aço chega ao limite de $10\text{‰}$ sem que o concreto esteja esgotado. É o caso usual das lajes.
- **Domínio 3.** Armadura adequada. O aço escoa e o concreto atinge $\varepsilon_{cu}$ ao mesmo tempo. A ruína é dúctil, com fissuras abertas e flecha grande antes do colapso.
- **Domínio 4.** Armadura em excesso. O concreto esmaga antes de o aço escoar. A ruína é frágil e sem aviso, e o aço fica subaproveitado. Deve ser evitado.

### Limites entre os domínios

Pela semelhança de triângulos no diagrama linear, com os módulos das deformações,

$$
\xi=\frac{x}{d}=\frac{\varepsilon_c}{\varepsilon_c+\varepsilon_s}.
$$

As fronteiras entre domínios saem dessa expressão com as deformações dos pivôs:

$$
\xi_{2a/2b}=\frac{\varepsilon_{c2}}{\varepsilon_{c2}+0{,}010},\qquad
\xi_{2/3}=\frac{\varepsilon_{cu}}{\varepsilon_{cu}+0{,}010},\qquad
\xi_{3/4}=\frac{\varepsilon_{cu}}{\varepsilon_{cu}+\varepsilon_{yd}}.
$$

O domínio 2 é subdividido em 2a, em que o concreto ainda está na parte parabólica do diagrama ($\varepsilon_c<\varepsilon_{c2}$), e 2b, em que já atingiu o trecho constante. Para C20 a C50 e CA-50:

| Região | Intervalo de $\xi$ | Condição no ELU |
|---|---|---|
| Domínio 2a | $0<\xi<0{,}167$ | Aço a $10\text{‰}$ e concreto abaixo de $\varepsilon_{c2}$ |
| Domínio 2b | $0{,}167\leq\xi<0{,}259$ | Aço a $10\text{‰}$ e concreto entre $\varepsilon_{c2}$ e $\varepsilon_{cu}$ |
| Domínio 3 | $0{,}259\leq\xi\leq0{,}628$ | Concreto a $\varepsilon_{cu}$, com escoamento da armadura tracionada |
| Domínio 4 | $0{,}628<\xi<1$ | Concreto atinge $\varepsilon_{cu}$ antes do escoamento da armadura |

A seção pode estar no domínio 3 e, ainda assim, ter pouca ductilidade quando $\xi$ é grande. Por isso a NBR 6118 limita a posição da linha neutra em $\xi\leq0{,}45$ para $f_{ck}\leq50$ MPa (item 14.6.4.3). Esse limite é usado no dimensionamento da [Aula 08](008-armadura-simples.md).

### Estádios e domínios

Os estádios descrevem a **evolução** da seção com a carga. Os domínios descrevem os **estados finais** possíveis. O Estádio III é o estado de ruína, e cada diagrama de deformação dos domínios 2, 3 e 4 é uma ruína possível. Numa viga bem armada, a trajetória da seção passa pelos Estádios I e II e termina no domínio 3.

## Exemplos para desenvolver em sala

### Exemplo 1: cargas do ensaio de quatro pontos

Uma viga de concreto armado C30 tem $b_w=20\text{ cm}$, $h=50\text{ cm}$, $d=45\text{ cm}$ e armadura $A_s=10{,}73\text{ cm}^2$, a mesma do Exemplo 1 da Aula 08. Ela é ensaiada com $L=4{,}50\text{ m}$ e cargas a $a=L/3=1{,}50\text{ m}$ de cada apoio. Despreze o peso próprio. Determine a carga total $P$ que provoca a fissuração e a carga que provoca a ruína.

O momento de fissuração, com $f_{ctm}=0{,}3\times30^{2/3}=2{,}896\text{ MPa}$, $I_c=200\times500^3/12=2{,}083\times10^9\text{ mm}^4$ e $y_t=250\text{ mm}$, é

$$
M_r=1{,}5\,\frac{2{,}896\times2{,}083\times10^9}{250}
=36{,}2\times10^6\text{ N mm}=36{,}2\text{ kN m}.
$$

Como $M=(P/2)\,a$, a fissuração ocorre com

$$
\frac{P}{2}=\frac{36{,}2}{1{,}50}=24{,}1\text{ kN},
\qquad P=48{,}3\text{ kN}.
$$

Com a resistência de cálculo, o momento resistente dessa armadura é o momento de cálculo da Aula 08, $M_{Rd}=180\text{ kN m}$. A ruína ocorre com

$$
\frac{P}{2}=\frac{180}{1{,}50}=120\text{ kN},
\qquad P=240\text{ kN}.
$$

A fissuração ocorre com cerca de $20\%$ da carga de ruína. Isso mostra que uma viga de concreto armado trabalha **fissurada** sob as cargas de serviço. Num ensaio real, as resistências médias dos materiais, maiores que as de cálculo, conduziriam a cargas maiores.

### Exemplo 2: a mesma seção nos três estádios

Considere a seção do Exemplo 1, com $E_{cs}=26\,838\text{ MPa}$ e $E_s=210\,000\text{ MPa}$, de modo que $\alpha_e=7{,}82$.

**Estádio I.** A seção fissura em $M_r=36{,}2\text{ kN m}$, calculado no Exemplo 1.

**Estádio II**, para um momento de serviço $M=60\text{ kN m}$. Como $60>36{,}2$, a seção está fissurada. Com $\alpha_eA_s=7{,}82\times1073=8393\text{ mm}^2$,

$$
100x_{II}^2+8393\,x_{II}-8393\times450=0
\quad\Rightarrow\quad x_{II}=156{,}9\text{ mm},
$$

$$
I_{II}=\frac{200\times156{,}9^3}{3}+8393\,(450-156{,}9)^2
=9{,}78\times10^8\text{ mm}^4=0{,}47\,I_c.
$$

As tensões são

$$
\sigma_c=\frac{60\times10^6\times156{,}9}{9{,}78\times10^8}=9{,}6\text{ MPa},
\qquad
\sigma_s=7{,}82\,\frac{60\times10^6\times(450-156{,}9)}{9{,}78\times10^8}=140{,}7\text{ MPa}.
$$

A armadura trabalha a cerca de um terço de $f_{yd}=434{,}8\text{ MPa}$, e a rigidez da seção fissurada é menos da metade da bruta.

**Estádio III**, no ELU, com $M_d=180\text{ kN m}$, como na Aula 08: $\xi=0{,}356$, $x=160\text{ mm}$, $\varepsilon_s=6{,}34\text{‰}>\varepsilon_{yd}=2{,}07\text{‰}$. O aço escoa, $\sigma_s=f_{yd}$, e a seção está no domínio 3.

Embora $x_{II}\approx x$ neste exemplo, as duas posições da linha neutra correspondem a hipóteses diferentes: elástica no Estádio II e plastificada no Estádio III.

### Exemplo 3: enquadrar pares de deformações nos domínios

Para cada par de deformações no ELU, calcula-se $\xi=\varepsilon_c/(\varepsilon_c+\varepsilon_s)$ e compara-se com as fronteiras, para C30 e CA-50.

| $\varepsilon_c$ (‰) | $\varepsilon_s$ (‰) | $\xi$ | Domínio | Comentário |
|---:|---:|---:|---|---|
| 1,5 | 10,0 | 0,130 | 2a | Aço no limite; concreto abaixo de $\varepsilon_{c2}$ |
| 3,0 | 10,0 | 0,231 | 2b | Aço no limite; concreto no trecho constante |
| 3,5 | 6,34 | 0,356 | 3 | Seção do Exemplo 2 |
| 3,5 | 1,5 | 0,700 | 4 | Aço abaixo de $\varepsilon_{yd}$; ruína frágil |

## Exercícios para resolver em sala

```{admonition} Exercício 1: domínio a partir das deformações
:class: destaque-verde

Para C30 e CA-50, determine $\xi$ e o domínio de cada par $(\varepsilon_c;\varepsilon_s)$, em ‰: (a) $(1{,}0;\,10{,}0)$; (b) $(2{,}5;\,10{,}0)$; (c) $(3{,}5;\,4{,}0)$; (d) $(3{,}5;\,1{,}0)$. Diga se o limite $\xi\leq0{,}45$ é atendido.
```

**Conferência:** (a) $\xi=0{,}091$, domínio 2a; (b) $\xi=0{,}200$, domínio 2b; (c) $\xi=0{,}467$, domínio 3, mas acima de $0{,}45$; (d) $\xi=0{,}778$, domínio 4.

```{admonition} Exercício 2: ensaio de uma viga
:class: destaque-verde

Uma viga C30 de $b_w=15\text{ cm}$ e $h=40\text{ cm}$ é ensaiada com vão $L=3{,}60\text{ m}$ e cargas a $L/3$ dos apoios. Calcule o momento de fissuração e a carga total $P$ que inicia a fissuração, desprezando o peso próprio.
```

**Conferência:** $f_{ctm}=2{,}896\text{ MPa}$, $I_c=8{,}0\times10^8\text{ mm}^4$, $M_r\approx17{,}4\text{ kN m}$, $a=1{,}20\text{ m}$, $P/2\approx14{,}5\text{ kN}$ e $P\approx29{,}0\text{ kN}$.

```{admonition} Exercício 3: deformações a partir de $\xi$
:class: destaque-verde

Para C30 e CA-50, determine o domínio e as deformações $\varepsilon_c$ e $\varepsilon_s$ para (a) $\xi=0{,}10$, (b) $\xi=0{,}30$ e (c) $\xi=0{,}70$.
```

**Conferência:** (a) domínio 2a, $\varepsilon_s=10\text{‰}$ e $\varepsilon_c=1{,}11\text{‰}$; (b) domínio 3, $\varepsilon_c=3{,}5\text{‰}$ e $\varepsilon_s=8{,}17\text{‰}$; (c) domínio 4, $\varepsilon_c=3{,}5\text{‰}$ e $\varepsilon_s=1{,}5\text{‰}$.

```{admonition} Exercício 4: estádio de cada verificação
:class: destaque-verde

Indique o estádio associado a cada item: (a) cálculo de $M_r$; (b) abertura de fissuras sob cargas de serviço; (c) área de aço no ELU; (d) flecha pela inércia equivalente de Branson.
```

**Conferência:** (a) Estádio I; (b) Estádio II; (c) Estádio III; (d) o Estádio I, por $I_c$, e o Estádio II, por $I_{II}$, combinados pela expressão de Branson.

## O que levar para a Aula 08

| Conceito | Papel no dimensionamento |
|---|---|
| Estádio III | É o estado em que se equilibra o momento de cálculo |
| Premissas 1 a 7 | Permitem a compatibilidade de deformações e o equilíbrio da seção |
| $\xi=\varepsilon_c/(\varepsilon_c+\varepsilon_s)$ | Liga a posição da linha neutra às deformações |
| Fronteiras $0{,}167$, $0{,}259$ e $0{,}628$ | Classificam a seção após o cálculo de $\xi$ |
| Limite $\xi\leq0{,}45$ | Garante ductilidade sem redistribuição de momentos |

## Referências

- ABNT — ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. *NBR 6118: Projeto de estruturas de concreto*. Rio de Janeiro, 2023, versão corrigida de 2024. Itens 14.6.4.3 e 17.2.2.
- *Dimensionamento de seções retangulares com armadura simples*. Capítulo 4 do material fornecido pelo professor, arquivo `ECA_Livro_2025-02_-_cap4_-_revisado`. Base da definição dos domínios e das expressões de $\varepsilon_{c2}$ e $\varepsilon_{cu}$.
- LEONHARDT, F.; MÖNNIG, E. *Construções de concreto*, v. 1: Princípios básicos do dimensionamento de estruturas de concreto armado. Rio de Janeiro: Interciência. Comportamento à flexão e estádios.
- CARVALHO, R. C.; FIGUEIREDO FILHO, J. R. *Cálculo e detalhamento de estruturas usuais de concreto armado*. São Carlos: EdUFSCar. Estádios e domínios de deformação.
