# Aula 01: Histórico e propriedades

Esta aula apresenta um panorama sobre o concreto armado: um breve histórico de sua evolução, desde as primeiras construções em pedra e argamassa até a normalização moderna, e uma síntese das propriedades dos materiais (concreto e aço) que serão utilizadas ao longo da disciplina.

## Breve histórico do concreto armado

### Da pedra ao concreto romano

A humanidade recorreu, inicialmente, a blocos de pedra sobrepostos para erguer suas construções mais duráveis, como templos, câmaras funerárias e abrigos. Onde pedra e madeira eram escassas, no entanto, os povos antigos passaram a queimar barro para fabricar tijolos, técnica já presente na Mesopotâmia por volta de 3.500 a.C. e nas pirâmides egípcias, que empregavam argamassas à base de gipsita e cal.

O concreto, tal como o conhecemos, tem origem na pozolana: uma cinza de origem vulcânica, característica da região italiana de Pozzuoli, que, combinada com cal hidratada, dá origem a um aglomerante resistente e capaz de endurecer em contato com a água. Ao longo de quase cinco séculos (4 a.C. a 476 d.C.), os romanos empregaram esse material em obras emblemáticas, como a Via Ápia, termas, aquedutos e, sobretudo, o Coliseu (ver [Figura 1](#fig-1)) e o Pantheon.

(fig-1)=
**Figura 1.** O Coliseu romano e sua fundação.
```{figure} ../_static/aulas/historico_props/coliseu.png
:alt: Coliseu Romano
:width: 90%
:align: center
```

### O surgimento do concreto armado

Registros arqueológicos das termas de Caracalla, em Roma, revelam o caso mais antigo conhecido de reforço metálico em construções: barras de bronze embutidas em argamassa de pozolana, encontradas justamente nos trechos de vão mais largo. Esse conhecimento praticamente se perdeu durante a Idade Média, e só foi retomado com força no século XVIII, quando Smeaton e Vicat conduziram os primeiros estudos sistemáticos sobre aglomerantes hidráulicos, trabalho que culminou, em 1824, na patente do cimento Portland por Joseph Aspdin.

Foi [Thaddeus Hyatt](#nota-1), em 1877, quem sistematizou pela primeira vez as razões que tornam o aço e o concreto compatíveis como material composto: o concreto protege as armaduras da ação do fogo, a aderência entre os dois é suficiente para que atuem solidariamente, e seus coeficientes de dilatação térmica praticamente coincidem. Coube à França, nas décadas seguintes, uma série de aplicações pioneiras: um barco em argamassa armada por Lambot (1855), vasos de concreto reforçados com arame por Monier (1861) e, por Coignet, vigas e tubos de concreto armado apresentados na Exposição de Paris de 1867. Já nos Estados Unidos, a Ward House (1873–1876) permanece como a mais antiga edificação em concreto armado ainda de pé, e o Edifício Ingalls (Cincinnati, 1902–1903) inaugurou a era dos arranha-céus construídos nesse material.

Coube ao engenheiro alemão [Emil Mörsch](#nota-2), da Universidade de Stuttgart, formular em 1908 a primeira teoria consistente para o dimensionamento de peças de concreto armado, cujos princípios básicos seguem válidos até os dias de hoje.

### O concreto armado no Brasil

No Brasil, os primeiros registros do uso do então chamado "cimento armado" remontam a 1904, em residências de Copacabana, no Rio de Janeiro. Sua disseminação, contudo, está diretamente ligada à imigração alemã do início do século XX, episódio que trouxe ao país o engenheiro Lambert Riedlinger e a empresa Wayss & Freytag. Foi nesse contexto que Emilio Baumgart despontou como um dos grandes nomes da engenharia nacional, assinando obras como o edifício do Jornal A Noite (1930), com seu recorde de 104,75 m de altura, e a ponte sobre o Rio do Peixe (SC, 1930), então a maior ponte em viga reta construída em balanços sucessivos no mundo [Vasconcelos [3]](#ref-3).

### Ensino e normalização

O ensino sistemático do dimensionamento em concreto armado só ganhou espaço nos currículos de engenharia em 1897. A regulamentação técnica seguiu ritmo semelhante: a Alemanha abriu caminho em 1904, seguida de perto pela França (1906), pela Inglaterra (1915) e pelos Estados Unidos (1917). O Brasil chegaria à sua primeira norma apenas em 1940, batizada de NB-1; passou por revisões em 1960 e 1978 até assumir, em 1980, o nome que mantém até hoje, [ABNT NBR 6118 [1]](#ref-1), atualmente em sua edição de 2023.

## Propriedades do concreto armado

### Viabilidade do compósito concreto-aço

Em sua forma simples, o concreto reúne cimento, água e agregados miúdos e graúdos, resultando em um material com ótimo desempenho à compressão, mas capaz de resistir a apenas cerca de 10% desse valor quando tracionado. É justamente para suprir essa fragilidade que se posicionam barras de aço na região tracionada da peça: o concreto passa a responder pela compressão, enquanto o aço assume, depois que essa região fissura, a função de equilibrar os esforços de tração.

A [Figura 2](#fig-2) compara os esquemas de vigas de concreto com e sem armaduras longitudinais.

(fig-2)=
**Figura 2.** Influência da armadura no comportamento de vigas de concreto: (a) viga; (b) comportamento de viga de concreto simples; (c) comportamento de viga de concreto armado.
```{figure} ../_static/aulas/historico_props/vigas-concreto-armaduras-abc.png
:alt: Três vigas sob duas cargas concentradas: (a) concreto simples com fissura central; (b) armadura longitudinal e fissuras inclinadas próximas aos apoios; (c) armadura longitudinal e estribos.
:width: 100%
:align: center
```

Segundo [Hyatt](#nota-1), o concreto armado só é viável devido a três fatores:

- **Aderência:** garante que concreto e aço trabalhem em conjunto, com a mesma deformação na interface entre os materiais;
- **Coeficientes de dilatação térmica compatíveis:** ambos os materiais têm coeficiente da ordem de $1{,}0\times10^{-5}\text{/°C}$, evitando variações volumétricas diferenciais para níveis usuais de temperatura;
- **Proteção contra a oxidação da armadura:** o concreto é um material alcalino, devido ao hidróxido de cálcio formado na hidratação do cimento, que cria um ambiente desfavorável à corrosão do aço.

A [Figura 3](#fig-3) apresenta uma viga de concreto armado em perspectiva, com trechos de concreto omitidos para visualizar as barras longitudinais e os estribos que compõem a armadura.

(fig-3)=
**Figura 3.** Armaduras típicas de uma viga de concreto armado, em perspectiva.
```{figure} ../_static/aulas/historico_props/viga-armaduras-perspectiva.png
:alt: Viga de concreto armado em perspectiva, com trechos nas extremidades revelando as barras longitudinais e os estribos.
:width: 100%
:align: center
```

### Fissuração, vantagens e desvantagens

Fissuras são, na prática, inseparáveis do concreto armado: bastam pequenas deformações de tração para que o material fissure. Evitá-las por completo exigiria armaduras tão conservadoras que o custo da estrutura se tornaria proibitivo. Por isso, a estratégia de projeto não é impedir a fissuração, e sim manter a abertura das fissuras dentro de limites que preservem a durabilidade da peça em serviço.

Entre as principais vantagens do concreto armado estão:

- menor custo em relação a outros materiais estruturais;
- grande variedade de formas possíveis;
- facilidade de execução;
- boa resistência a efeitos térmicos, atmosféricos e a desgastes mecânicos;
- possibilidade de obter estruturas monolíticas e contínuas quando moldadas no local.

Como principais desvantagens, destacam-se:

- peso próprio elevado;
- dificuldades para reformas e demolições futuras;
- baixo grau de proteção térmica que a estrutura oferece.

### Resistência à compressão

Entre as propriedades mecânicas do concreto, a resistência à compressão é a mais relevante para o projeto estrutural, sendo obtida por ensaios padronizados em corpos de prova cilíndricos. Por se tratar de uma grandeza sujeita a dispersão estatística, adota-se em projeto não a média dos resultados, mas a resistência característica ($f_{ck}$): o valor abaixo do qual ficam apenas 5% dos ensaios de um lote, o que equivale a uma garantia de 95% de que a resistência real supere a de projeto.

Como a hidratação do cimento é um processo contínuo, a resistência do concreto continua a evoluir muito além do momento da concretagem. O item 12.3.3 da [ABNT NBR 6118 [1]](#ref-1) permite estimar essa resistência em qualquer idade $t$ (em dias) a partir do valor de referência aos 28 dias, por meio de

$$
f_{ck,j} = \beta_t(t)\cdot f_{ck}
\tag{1}
$$

$$
\beta_t(t) = e^{\,s\left(1-\sqrt{28/t}\right)}
\tag{2}
$$

com:

- $s = 0{,}38$ para cimentos de endurecimento lento (CPIII e IV);
- $s = 0{,}25$ para cimentos de endurecimento normal (CPI e II);
- $s = 0{,}20$ para cimentos de endurecimento rápido (CPV-ARI). A norma determina o uso desse mesmo valor também para concretos de classe C60 ou superior, independentemente do cimento empregado.

```{admonition} Exemplo 1
:class: destaque-verde

Uma fábrica de pré-moldados utiliza cimento CPV-ARI na produção de suas peças. Para liberar o transporte dos elementos, é necessário garantir $f_{ck}$ superior a $21\text{ MPa}$ já aos 2 dias de idade. Qual classe de resistência do concreto deve ser especificada para atender a essa exigência?
```

### Módulo de elasticidade

A rigidez do concreto também é estimada a partir de $f_{ck}$, distinguindo-se dois módulos de elasticidade: o módulo tangente na origem ($E_{ci}$) e o módulo secante ($E_{cs}$), este mais próximo do comportamento real da estrutura em serviço e, por isso, mais utilizado na análise estrutural. O item 8.2.8 da [ABNT NBR 6118 [1]](#ref-1) fornece, para a idade de 28 dias, as seguintes estimativas:

$$
E_{ci} = \alpha_E\cdot 5600\cdot\sqrt{f_{ck}} \quad \text{, para concretos de classe C20 a C50}
\tag{3a}
$$

$$
E_{ci} = 21{,}5\times10^{3}\cdot\alpha_E\cdot\left(\frac{f_{ck}}{10}+1{,}25\right)^{1/3} \quad \text{, para concretos de classe C55 a C90}
\tag{3b}
$$

$$
E_{cs} = \alpha_i\cdot E_{ci}
\tag{4}
$$

$$
\alpha_i = 0{,}8+0{,}2\cdot\frac{f_{ck}}{80}\leq 1{,}0
\tag{5}
$$

em que $f_{ck}$ é dado em MPa e $\alpha_E$ é um coeficiente que depende do agregado graúdo utilizado: $\alpha_E=1{,}2$ para basalto e diabásio; $\alpha_E=1{,}0$ para granito e gnaisse; $\alpha_E=0{,}9$ para calcário; e $\alpha_E=0{,}7$ para arenito. A [Tabela 1](#tab-1) apresenta valores estimados e arredondados desses módulos para as classes usuais de resistência.

(tab-1)=
**Tabela 1.** Valores estimados do módulo de elasticidade em função da classe de resistência à compressão do concreto (considerando agregado graúdo de granito, $\alpha_E=1{,}0$).

| Classe | C20 | C25 | C30 | C35 | C40 | C45 | C50 | C60 | C70 | C80 | C90 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| $E_{ci}$ (GPa) | 25 | 28 | 31 | 33 | 35 | 38 | 40 | 42 | 43 | 45 | 47 |
| $E_{cs}$ (GPa) | 21 | 24 | 27 | 29 | 32 | 34 | 37 | 40 | 42 | 45 | 47 |
| $\alpha_i$ | 0,85 | 0,86 | 0,88 | 0,89 | 0,90 | 0,91 | 0,93 | 0,95 | 0,98 | 1,00 | 1,00 |

O módulo de elasticidade acompanha a mesma lógica de evolução no tempo já vista para a resistência. Entre 7 e 28 dias, na ausência de ensaios específicos, seu valor pode ser projetado a partir do módulo obtido aos 28 dias, por meio de

$$
E_{ci}(t) = E_{ci}\cdot\left(\frac{f_{ckj}}{f_{ck}}\right)^{0{,}5} \quad \text{, para concretos até a classe C50}
\tag{6a}
$$

$$
E_{ci}(t) = E_{ci}\cdot\left(\frac{f_{ckj}}{f_{ck}}\right)^{0{,}3} \quad \text{, para concretos de classe C55 a C90}
\tag{6b}
$$

em que $E_{ci}(t)$ é a estimativa do módulo de elasticidade na idade $t$ e $f_{ckj}$ é a resistência característica à compressão na idade $j$ em que se deseja estimar o módulo.

```{admonition} Exemplo 2
:class: destaque-verde

Durante a troca dos aparelhos de apoio de uma ponte de concreto armado, a superestrutura é temporariamente levantada por atuadores hidráulicos, e um bloco de concreto é posicionado entre a superestrutura e a mesoestrutura para mantê-las afastadas com segurança, sem fissurar por compressão. Esse bloco tem classe de resistência C30, seção $14\times30\text{ cm}$, altura de $100\text{ cm}$ e é armado com 4 barras longitudinais de $10\text{ mm}$ (aço com $E_s=210\text{ GPa}$). O manômetro dos atuadores indica uma força de $1600\text{ kN}$, correspondente ao peso da superestrutura apoiado sobre o bloco. Esse elemento atende ao limite de encurtamento de $2\text{ mm}$ exigido pela empresa responsável pela obra?
```

### Diagrama tensão-deformação

Sob compressão, o concreto se comporta de maneira não linear, mantendo-se praticamente constante apenas o coeficiente de Poisson, com valor médio $\nu=0{,}2$ prescrito pela norma. Para simplificar o dimensionamento, o item 8.2.10.1 da [ABNT NBR 6118 [1]](#ref-1) substitui essa curva real por um diagrama idealizado, do tipo parábola-retângulo:

$$
\sigma_c =
\begin{cases}
0{,}85\,\eta_c\,f_{cd}\left[1-\left(1-\dfrac{\varepsilon_c}{\varepsilon_{c2}}\right)^{n}\right], & 0\leq\varepsilon_c\leq\varepsilon_{c2} \\[8pt]
0{,}85\,\eta_c\,f_{cd}, & \varepsilon_{c2}\leq\varepsilon_c\leq\varepsilon_{cu}
\end{cases}
\tag{7}
$$

em que $f_{cd}$ é a resistência de cálculo à compressão do concreto e $\eta_c$ é um redutor da resistência à compressão para concretos de classes mais elevadas, definido pela [Tabela 2](#tab-2). Já $\varepsilon_{c2}$, a deformação específica no início do patamar plástico, $\varepsilon_{cu}$, a deformação específica de ruptura do concreto, e o expoente $n$ dependem da classe de resistência, conforme a [Tabela 3](#tab-3).

(tab-2)=
**Tabela 2.** Valores do coeficiente $\eta_c$ em função da classe de resistência do concreto.

| Classe de resistência | $\eta_c$ |
|---|---|
| $f_{ck}\leq 40\text{ MPa}$ | $1{,}0$ |
| $f_{ck} > 40\text{ MPa}$ | $(40/f_{ck})^{1/3}$ |

(tab-3)=
**Tabela 3.** Valores de $\varepsilon_{c2}$, $\varepsilon_{cu}$ e $n$ em função da classe de resistência do concreto.

| | Concreto até a classe C50 | Concreto de classe C55 a C90 |
|---|---|---|
| $\varepsilon_{c2}$ | $2{,}0\text{‰}$ | $2{,}0\text{‰}+0{,}085\text{‰}\,(f_{ck}-50)^{0{,}53}$ |
| $\varepsilon_{cu}$ | $3{,}5\text{‰}$ | $2{,}6\text{‰}+35\text{‰}\left[\dfrac{90-f_{ck}}{100}\right]^{4}$ |
| $n$ | $2$ | $1{,}4+23{,}4\left[\dfrac{90-f_{ck}}{100}\right]^{4}$ |

A [Figura 4](#fig-4) apresenta detalhes do diagrama tensão-deformação do concreto.

(fig-4)=
**Figura 4.** Diagrama idealizado para tensão-deformação do concreto.
```{figure} ../_static/aulas/historico_props/tensao-def.png
:alt: Diagrama Tensão - deformação
:width: 90%
:align: center
```

### Comportamento em tração

Em ordem de grandeza bem menor que a compressão, a resistência à tração do concreto também pode ser estimada em função de $f_{ck}$, na falta de ensaios diretos. É o que permite o item 8.2.5 da [ABNT NBR 6118 [1]](#ref-1), ao definir a resistência à tração direta média ($f_{ct,m}$) por

$$
f_{ct,m} = 0{,}3\cdot f_{ck}^{2/3} \quad \text{, para concretos de classe até C50}
\tag{8a}
$$

$$
f_{ct,m} = 2{,}12\cdot\ln\left(1+0{,}11\,f_{ck}\right) \quad \text{, para concretos de classe C55 a C90}
\tag{8b}
$$

com $f_{ck}$ e $f_{ct,m}$ em MPa. Os valores característicos inferior e superior da resistência à tração são dados por

$$
f_{ctk,inf} = 0{,}7\cdot f_{ct,m}
\tag{9}
$$

$$
f_{ctk,sup} = 1{,}3\cdot f_{ct,m}
\tag{10}
$$

Enquanto a peça permanece sem fissuras, seu comportamento à tração é representado por um diagrama bilinear simplificado, adotando-se o mesmo módulo de deformação inicial já estimado para a compressão.

```{admonition} Exemplo 3
:class: destaque-verde

Um prisma de concreto com seção $15\times15\text{ cm}$ e vão de $45\text{ cm}$ será submetido a um ensaio de flexão em três pontos. Admitindo comportamento elástico linear e que a tensão na face inferior do prisma não deve superar a resistência à tração direta do concreto (com $f_{ck}=40\text{ MPa}$), qual é a força máxima que a peça suporta antes de fissurar?
```

### Propriedades reológicas do concreto

Além das deformações imediatas, o concreto acumula, ao longo do tempo, dois outros tipos de deformação:

- **Retração:** o concreto perde volume à medida que a água livre em seu interior migra para o ambiente, fenômeno mais intenso quanto mais seco for o ar ao redor e que se estabiliza, tipicamente, entre 2 e 3 anos após a cura;
- **Fluência (ou deformação lenta):** sob carga constante e de longa duração, o concreto continua a se deformar lentamente com o passar do tempo, podendo essa deformação adicional atingir até quatro vezes o valor da deformação elástica inicial.

Na prática, esses efeitos se traduzem em flechas maiores em vigas e lajes e em esforços adicionais que surgem quando a estrutura é hiperestática. A variação uniforme de temperatura segue lógica parecida: em estruturas isostáticas, provoca apenas deslocamentos; em hiperestáticas, gera esforços que também precisam ser considerados no projeto.

## Aço para concreto armado

A nomenclatura do aço para concreto armado combina as letras CA com o valor característico da tensão de escoamento em MPa; um CA-50, por exemplo, escoa a $f_{yk}=500\text{ MPa}$. A [ABNT NBR 7480 [2]](#ref-2) reconhece três categorias: as barras CA-25 e CA-50, laminadas a quente, e os fios CA-60, obtidos por trefilação ou laminação a frio.

As barras de aço CA-50 são fornecidas em diâmetros nominais padronizados, com massa linear e área de aço tabeladas em função do diâmetro e da quantidade de barras ([Tabela 4](#tab-4)). Os fios de aço CA-60 seguem a mesma lógica, em diâmetros usualmente menores ([Tabela 5](#tab-5)).

(tab-4)=
**Tabela 4.** Massa linear e área de aço das barras CA-50 em função do diâmetro nominal e da quantidade de barras.

| $\phi$ (mm) | Massa linear (kg/m) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 6,3 | 0,245 | 0,312 | 0,624 | 0,936 | 1,248 | 1,560 | 1,872 | 2,184 | 2,496 | 2,808 | 3,120 |
| 8,0 | 0,395 | 0,503 | 1,006 | 1,509 | 2,012 | 2,515 | 3,018 | 3,521 | 4,024 | 4,527 | 5,030 |
| 10,0 | 0,617 | 0,785 | 1,570 | 2,355 | 3,140 | 3,925 | 4,710 | 5,495 | 6,280 | 7,065 | 7,850 |
| 12,5 | 0,963 | 1,227 | 2,454 | 3,681 | 4,908 | 6,135 | 7,362 | 8,589 | 9,816 | 11,043 | 12,270 |
| 16,0 | 1,578 | 2,011 | 4,022 | 6,033 | 8,044 | 10,055 | 12,066 | 14,077 | 16,088 | 18,099 | 20,110 |
| 20,0 | 2,466 | 3,142 | 6,284 | 9,426 | 12,568 | 15,710 | 18,852 | 21,994 | 25,136 | 28,278 | 31,420 |
| 25,0 | 3,853 | 4,909 | 9,818 | 14,727 | 19,636 | 24,545 | 29,454 | 34,363 | 39,272 | 44,181 | 49,090 |
| 32,0 | 6,313 | 8,042 | 16,084 | 24,126 | 32,168 | 40,210 | 48,252 | 56,294 | 64,336 | 72,378 | 80,420 |

**Nota:** as colunas numeradas de 1 a 10 indicam a área de aço total (cm²) correspondente à quantidade de barras do diâmetro indicado.

(tab-5)=
**Tabela 5.** Massa linear e área de aço dos fios CA-60 em função do diâmetro nominal e da quantidade de fios.

| $\phi$ (mm) | Massa linear (kg/m) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4,2 | 0,109 | 0,139 | 0,278 | 0,417 | 0,556 | 0,695 | 0,834 | 0,973 | 1,112 | 1,251 | 1,390 |
| 5,0 | 0,154 | 0,196 | 0,392 | 0,588 | 0,784 | 0,980 | 1,176 | 1,372 | 1,568 | 1,764 | 1,960 |
| 5,5 | 0,187 | 0,238 | 0,476 | 0,714 | 0,952 | 1,190 | 1,428 | 1,666 | 1,904 | 2,142 | 2,380 |
| 6,0 | 0,222 | 0,283 | 0,566 | 0,849 | 1,132 | 1,415 | 1,698 | 1,981 | 2,264 | 2,547 | 2,830 |
| 7,0 | 0,302 | 0,385 | 0,770 | 1,155 | 1,540 | 1,925 | 2,310 | 2,695 | 3,080 | 3,465 | 3,850 |
| 8,0 | 0,395 | 0,503 | 1,006 | 1,509 | 2,012 | 2,515 | 3,018 | 3,521 | 4,024 | 4,527 | 5,030 |
| 9,5 | 0,558 | 0,709 | 1,418 | 2,127 | 2,836 | 3,545 | 4,254 | 4,963 | 5,672 | 6,381 | 7,090 |
| 10,0 | 0,617 | 0,785 | 1,570 | 2,355 | 3,140 | 3,925 | 4,710 | 5,495 | 6,280 | 7,065 | 7,850 |

**Nota:** as colunas numeradas de 1 a 10 indicam a área de aço total (cm²) correspondente à quantidade de fios do diâmetro indicado.

O aço também é representado, em projeto, por um diagrama tensão–deformação simplificado: um trecho inicial elástico linear, seguido de um patamar de escoamento a tensão constante. Na ausência de ensaios, adota-se $E_s = 210\text{ GPa}$ para o módulo de elasticidade, e a deformação máxima considerada nas estruturas de concreto armado é limitada a $10\text{‰}$.

A [Figura 5](#fig-5) apresenta detalhes do diagrama tensão-deformação do aço.

(fig-5)=
**Figura 5.** Diagrama idealizado para tensão-deformação do aço.
```{figure} ../_static/aulas/historico_props/tensao-def-aco.png
:alt: Diagrama Tensão - deformação
:width: 90%
:align: center
```


## Notas

(nota-1)=
**Nota 1.** Thaddeus Hyatt (1816–1901), advogado norte-americano, tornou-se um dos pioneiros do concreto armado ao publicar, em 1877, os ensaios que comprovaram a compatibilidade entre aço e concreto.

(nota-2)=
**Nota 2.** O engenheiro alemão Emil Mörsch (1872–1950), professor em Stuttgart, é autor da primeira teoria consistente sobre o dimensionamento de elementos de concreto armado, publicada em 1908.

## Referências

(ref-1)=
[1] ABNT — ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. *NBR 6118: Projeto de estruturas de concreto*. 4. ed. Rio de Janeiro, 2023.

(ref-2)=
[2] ABNT — ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. *NBR 7480: aço destinado a armaduras para estruturas de concreto armado - Requisitos*. 4. ed. Rio de Janeiro, 2024.

(ref-3)=
[3] VASCONCELOS, Augusto Carlos. *O concreto no Brasil: pré-fabricação, monumentos, fundações*. São Paulo: Studio Nobel, 2002.
