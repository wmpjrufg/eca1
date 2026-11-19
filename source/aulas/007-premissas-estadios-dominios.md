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

Figura 1. Ensaio de flexão em quatro pontos. Entre as duas cargas o cortante é nulo e o momento é constante. O diagrama de momento é desenhado do lado tracionado da viga. A viga é instrumentada com extensômetros no concreto e na armadura e com medição da flecha no meio do vão. Esquema sem escala.
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

com $\varepsilon_{c2}=2{,}0\text{‰}$ e $\varepsilon_{cu}=3{,}5\text{‰}$. O fator $0{,}85$ considera a perda de resistência do concreto submetido a tensões constantes ao longo do tempo. Para o aço, $\varepsilon_{yd}=f_{yd}/E_s$, que vale $2{,}07\text{‰}$ para o CA-50 com $\gamma_s=1{,}15$ e $E_s=210000\text{ MPa}$.

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
- **Domínio 4.** Armadura em excesso. O concreto esmaga antes de o aço escoar. A ruína é frágil e sem aviso, e o aço fica subaproveitado. A NBR 6118 não admite dimensionar vigas nesse domínio. Quando a seção cai nele, aumenta-se a altura ou usa-se armadura na zona comprimida (item 17.2.3), tema de outra aula.

### Limites entre os domínios

Pela semelhança de triângulos no diagrama linear, com os módulos das deformações,

$$
\xi=\frac{x}{d}=\frac{\varepsilon_c}{\varepsilon_c+\varepsilon_s}.
$$

As fronteiras entre domínios saem dessa expressão com as deformações dos pivôs, todas na mesma unidade (aqui, $0{,}010=10\text{‰}$):

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

### Limites em função do momento adimensional

Antes de calcular a armadura, o enquadramento costuma ser feito pelo **momento fletor adimensional**

$$
\mu=\frac{M_d}{b_wd^2f_{cd}},
$$

que depende só dos dados do projeto: $M_d$, $b_w$, $d$ e $f_{ck}$. Para a seção retangular, o equilíbrio (deduzido na [Aula 08](008-armadura-simples.md)) relaciona $\mu$ e $\xi$:

$$
\mu=\alpha_c\eta_c\lambda\xi\left(1-\frac{\lambda\xi}{2}\right),
$$

com $\lambda=0{,}8$ e $\alpha_c=0{,}85$ para $f_{ck}\leq50$ MPa, e com $\eta_c=1$ para $f_{ck}\leq40$ MPa e $\eta_c=(40/f_{ck})^{1/3}$ para $40<f_{ck}\leq90$ MPa. Substituindo os $\xi$ das fronteiras, obtêm-se os limites $\mu_L$. Entre C20 e C50 os $\xi_L$ não mudam, mas os $\mu_L$ diminuem acima de C40, por causa de $\eta_c$:

| Limite | $\xi_L$ | $\mu_L$ até C40 | $\mu_L$ C45 | $\mu_L$ C50 |
|---|---:|---:|---:|---:|
| 2a / 2b | 0,167 | 0,106 | 0,102 | 0,098 |
| 2 / 3 | 0,259 | 0,158 | 0,152 | 0,147 |
| 3 / 4, CA-50 | 0,628 | 0,320 | 0,308 | 0,297 |
| Ductilidade | 0,45 | 0,251 | 0,241 | 0,233 |

Esses valores coincidem com os Quadros 4.1 a 4.4 do capítulo 4 do material do professor, que também traz C55 a C90. Para C60 e CA-50, por exemplo, $\xi_L=0{,}186$, $0{,}224$ e $0{,}582$, com $\mu_L=0{,}094$, $0{,}112$ e $0{,}246$.

O domínio da seção é então:

| Condição | Domínio |
|---|---|
| $\mu<\mu_{L(2a/2b)}$ | 2a |
| $\mu_{L(2a/2b)}\leq\mu<\mu_{L(2/3)}$ | 2b |
| $\mu_{L(2/3)}\leq\mu\leq\mu_{L(3/4)}$ | 3 |
| $\mu>\mu_{L(3/4)}$ | 4 |

Se a seção cai no domínio 4, a altura útil mínima para que ela passe ao domínio 3, mantidos $M_d$, $b_w$ e o concreto, é

$$
d_{min}=\sqrt{\frac{M_d}{\mu_{L(3/4)}\,b_wf_{cd}}}.
$$

### Ductilidade

A seção pode estar no domínio 3 e, ainda assim, ter pouca ductilidade quando $\xi$ é grande. Por isso a NBR 6118 (item 14.6.4.3) limita a posição da linha neutra em $\xi\leq0{,}45$ para $f_{ck}\leq50$ MPa e em $\xi\leq0{,}35$ para $50<f_{ck}\leq90$ MPa. O capítulo 4 do material do professor verifica esse critério nas seções sobre apoios, com momento negativo, onde se espera a formação de rótulas plásticas. Nesta disciplina, ele é aplicado em todas as seções dos exercícios, como se verá na [Aula 08](008-armadura-simples.md). Em termos de $\mu$, o limite $\xi\leq0{,}45$ equivale a $\mu\leq0{,}251$ (até C40) e é mais restritivo que a fronteira entre os domínios 3 e 4. Assim, uma seção do domínio 3 pode não atender ao critério de ductilidade.

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

Os exercícios a seguir são variações dos exemplos da aula.

```{admonition} Exercício 5: cargas do ensaio de outra viga (variação do Exemplo 1)
:class: destaque-verde

Uma viga C35 tem $b_w=25\text{ cm}$ e $h=60\text{ cm}$ e é ensaiada com $L=6{,}00\text{ m}$ e cargas a $L/3$ dos apoios. Seu momento resistente de cálculo é $M_{Rd}=310\text{ kN m}$. Desprezando o peso próprio, determine a carga total $P$ que inicia a fissuração, a carga total que leva à ruína e a razão entre elas.
```

**Conferência:** $f_{ctm}=3{,}210\text{ MPa}$, $I_c=4{,}5\times10^9\text{ mm}^4$ e $M_r\approx72{,}2\text{ kN m}$. Com $a=2{,}00\text{ m}$, $P/2\approx36{,}1\text{ kN}$ e $P\approx72{,}2\text{ kN}$ na fissuração; na ruína, $P/2=155\text{ kN}$ e $P=310\text{ kN}$. A razão é $\approx0{,}23$.

```{admonition} Exercício 6: estádios de outra seção (variação do Exemplo 2)
:class: destaque-verde

Uma viga de $b_w=15\text{ cm}$, $h=40\text{ cm}$ e $d=36\text{ cm}$, em C30 e CA-50, tem armadura de $2\phi20$ ($A_s=6{,}28\text{ cm}^2$). Use $E_s=210\,000\text{ MPa}$ e $E_{cs}=26\,838\text{ MPa}$.

1. Calcule o momento de fissuração $M_r$.
2. Para um momento de serviço $M=40\text{ kN m}$, verifique se a seção está fissurada e determine $x_{II}$, $I_{II}$, $\sigma_c$ e $\sigma_s$.
3. No ELU, o equilíbrio da seção (Aula 08) fornece $\xi=0{,}347$. Calcule $\varepsilon_s$, identifique o domínio e diga se o aço escoa.
```

**Conferência:** (1) $M_r\approx17{,}4\text{ kN m}$. (2) $40>17{,}4$, então a seção está fissurada. Com $\alpha_e=7{,}82$, $x_{II}\approx124{,}3\text{ mm}$, $I_{II}\approx3{,}69\times10^8\text{ mm}^4$ ($0{,}46I_c$), $\sigma_c\approx13{,}5\text{ MPa}$ e $\sigma_s\approx200\text{ MPa}$. (3) $\varepsilon_s=3{,}5(1-0{,}347)/0{,}347\approx6{,}59\text{‰}>2{,}07\text{‰}$: domínio 3, com o aço escoando.

```{admonition} Exercício 7: domínios em concreto de alta resistência (variação do Exemplo 3)
:class: destaque-verde

Para C60 e CA-50, determine: (a) $\varepsilon_{c2}$ e $\varepsilon_{cu}$ pelas expressões do item de premissas; (b) os valores de $\xi$ nas fronteiras 2a/2b, 2/3 e 3/4; (c) o domínio de cada par $(\varepsilon_c;\varepsilon_s)$, em ‰: $(2{,}0;\,10)$, $(2{,}8;\,10)$, $(\varepsilon_{cu};\,5{,}0)$ e $(\varepsilon_{cu};\,1{,}5)$.
```

**Conferência:** (a) $\varepsilon_{c2}=2{,}288\text{‰}$ e $\varepsilon_{cu}=2{,}884\text{‰}$. (b) $\xi=0{,}186$, $0{,}224$ e $0{,}582$. (c) $\xi=0{,}167$, domínio 2a; $\xi=0{,}219$, domínio 2b; $\xi=0{,}366$, domínio 3; $\xi=0{,}658$, domínio 4.

```{admonition} Exercício 8: domínio pelo momento adimensional
:class: destaque-verde

Uma seção em vão de viga de edifício residencial tem $b_w=20\text{ cm}$ e $d=46\text{ cm}$, com aço CA-50 e $\gamma_g=\gamma_q=1{,}4$. Para cada caso, calcule $M_d$, $f_{cd}$ e $\mu$ e identifique o domínio, usando a tabela de $\mu_L$:

(a) C25, $M_{gk}=45\text{ kN m}$ e $M_{qk}=30\text{ kN m}$;
(b) C25, $M_{gk}=50\text{ kN m}$ e $M_{qk}=45\text{ kN m}$;
(c) o caso (b) com C50.
```

**Conferência:** (a) $M_d=105\text{ kN m}$, $f_{cd}=17{,}86\text{ MPa}$, $\mu=0{,}139$, domínio 2b ($0{,}106\leq\mu<0{,}158$). (b) $M_d=133\text{ kN m}$, $\mu=0{,}176$, domínio 3. (c) $f_{cd}=35{,}71\text{ MPa}$, $\mu=0{,}088<0{,}098$, domínio 2a. O mesmo momento, com concreto mais resistente, cai num domínio de menor aproveitamento do concreto.

```{admonition} Exercício 9: seção sobre apoio e altura mínima
:class: destaque-verde

A seção do Exercício 8, em C25, está sobre um apoio interno de viga contínua com momento negativo $M_d=250\text{ kN m}$. Calcule $\mu$, identifique o domínio e diga se a seção atende ao critério de ductilidade. Em seguida, determine a altura útil mínima (a) para ficar no domínio 3 e (b) para atender à ductilidade.
```

**Conferência:** $\mu=0{,}331>0{,}320$, domínio 4, que a norma não admite para vigas, e também $\mu>0{,}251$, logo a ductilidade não é atendida. (a) $d_{min}=\sqrt{250\times10^6/(0{,}320\times200\times17{,}86)}\approx468\text{ mm}$. (b) $d_{min}=\sqrt{250\times10^6/(0{,}251\times200\times17{,}86)}\approx528\text{ mm}$. Adotando $d\approx53\text{ cm}$, atendem-se os dois critérios.

```{admonition} Exercício 10: faixa de laje (variação do Exemplo 3)
:class: destaque-verde

Uma faixa de laje de $1{,}00\text{ m}$ tem $h=14\text{ cm}$ e $d=11\text{ cm}$, em C25 e CA-50, com $m_d=9\text{ kN m/m}$. Calcule $\mu$ e identifique o domínio. Estime $\xi=1{,}25\left(1-\sqrt{1-2\mu/0{,}85}\right)$ (expressão da Aula 08) e a deformação do concreto $\varepsilon_c=10\,\xi/(1-\xi)$, em ‰. Explique por que as lajes costumam ficar no domínio 2.
```

**Conferência:** $f_{cd}=17{,}86\text{ MPa}$ e $\mu=9\times10^6/(1000\times110^2\times17{,}86)=0{,}042<0{,}106$, domínio 2a. $\xi\approx0{,}063$ e $\varepsilon_c\approx0{,}67\text{‰}<\varepsilon_{c2}$. A espessura da laje é grande em relação ao momento por metro, então a armadura necessária é pequena: o aço chega a $10\text{‰}$ muito antes de o concreto se esgotar.

## O que levar para a Aula 08

| Conceito | Papel no dimensionamento |
|---|---|
| Estádio III | É o estado em que se equilibra o momento de cálculo |
| Premissas 1 a 7 | Permitem a compatibilidade de deformações e o equilíbrio da seção |
| $\xi=\varepsilon_c/(\varepsilon_c+\varepsilon_s)$ | Liga a posição da linha neutra às deformações |
| Fronteiras $0{,}167$, $0{,}259$ e $0{,}628$ | Classificam a seção após o cálculo de $\xi$ |
| $\mu=M_d/(b_wd^2f_{cd})$ e $\mu_L$ | Permitem enquadrar a seção antes de calcular a armadura |
| $d_{min}$ para o domínio 3 | Dá a altura útil mínima quando a seção cai no domínio 4 |
| Limite $\xi\leq0{,}45$ ($\mu\leq0{,}251$) | Garante ductilidade sem redistribuição de momentos |

## Referências

- ABNT — ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. *NBR 6118: Projeto de estruturas de concreto*. Rio de Janeiro, 2023, versão corrigida de 2024. Itens 14.6.4.3 e 17.2.2.
- *Dimensionamento de seções retangulares com armadura simples*. Capítulo 4 do material fornecido pelo professor, arquivo `ECA_Livro_2025-02_-_cap4_-_revisado`. Base da definição dos domínios, das expressões de $\varepsilon_{c2}$ e $\varepsilon_{cu}$ e dos limites $\xi_L$ e $\mu_L$ (Quadros 4.1 a 4.4).
- LEONHARDT, F.; MÖNNIG, E. *Construções de concreto*, v. 1: Princípios básicos do dimensionamento de estruturas de concreto armado. Rio de Janeiro: Interciência. Comportamento à flexão e estádios.
- CARVALHO, R. C.; FIGUEIREDO FILHO, J. R. *Cálculo e detalhamento de estruturas usuais de concreto armado*. São Carlos: EdUFSCar. Estádios e domínios de deformação.
