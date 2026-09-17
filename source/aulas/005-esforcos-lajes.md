# Aula 05: Esforços em lajes

Na [Aula 04](004-introducao-lajes.md), cada painel recebeu uma geometria, uma espessura inicial e uma representação de seus apoios. Agora vamos transformar esses dados em momentos fletores. A pergunta central é: **quais esforços precisam ser resistidos no vão e junto às bordas de cada laje?**

A aula começa com a interpretação dos esforços e uma apresentação da analogia de grelha. Em seguida, o trabalho se concentra nas tabelas de lajes: escolher o caso, localizar os coeficientes, calcular os momentos e tratar a continuidade entre painéis. A carga por área será um dado dos exemplos; sua composição foi estudada na [Aula 03](003-carregamentos.md).

```{admonition} Objetivos da aula
:class: destaque-azul

- Distinguir esforços de uma barra e esforços por unidade de largura de uma laje.
- Compreender o que uma grelha representa no pavimento.
- Usar uma tabela de momentos com eixos, vínculos e unidades coerentes.
- Compatibilizar os momentos de painéis vizinhos no cálculo simplificado.
```

## O que vamos calcular?

Adotaremos $x$ na direção do menor vão efetivo e $y$ na do maior, com $\lambda=l_y/l_x$. O momento $m_x$ solicita faixas paralelas a $x$ e está associado à armadura nessa direção. A interpretação de $m_y$ é equivalente para a direção $y$.

| Grandeza | Significado | Unidade usual |
|---|---|---|
| $m_x$, $m_y$ | Momentos fletores por unidade de largura da placa | $\mathrm{kN\,m/m}$ |
| $m_{xy}$ | Momento volvente, associado à torção da placa | $\mathrm{kN\,m/m}$ |
| $v_x$, $v_y$ | Esforços cortantes por unidade de largura | $\mathrm{kN/m}$ |
| $M$, $V$ | Momento e cortante de uma barra ou faixa de largura definida | $\mathrm{kN\,m}$ e $\mathrm{kN}$ |

Nas situações de flexão aqui estudadas, o momento positivo traciona a face inferior e o negativo, a superior. Usaremos $X$ para o **módulo** do momento negativo: se $X=8\,\mathrm{kN\,m/m}$, o momento com sinal será $-8\,\mathrm{kN\,m/m}$.

Uma faixa de $1\,\mathrm{m}$ submetida a $m=5\,\mathrm{kN\,m/m}$ tem momento total $M=5\,\mathrm{kN\,m}$. Os números coincidem por causa da largura escolhida; as grandezas continuam diferentes.

## Modelos para obter os esforços

| Modelo | Como representa a laje | Uso nesta sequência |
|---|---|---|
| Faixas | Barras paralelas na direção resistente principal. | Aproximação para lajes unidirecionais. |
| Analogia de grelha | Rede de barras conectadas, com flexão e torção. | Entender a interação entre lajes e vigas. |
| Tabelas de placas | Painel isolado com geometria e vínculos padronizados. | Cálculo manual de lajes retangulares bidirecionais. |
| Elementos finitos | Superfície subdividida em elementos de placa ou casca. | Análises de geometrias e condições mais gerais. |

### Analogia de grelha

Imagine dividir a superfície do piso em faixas que se cruzam. Cada faixa é representada por barras, e os cruzamentos tornam-se nós. Nesses nós, as barras compartilham deslocamentos e rotações: o esforço aplicado em uma região pode mobilizar as duas direções da malha.

```{figure} ../_static/aulas/esforcos-lajes/grelha.svg
:alt: Rede de barras em duas direções conectadas nos cruzamentos, com vigas no contorno e pilares nos cantos
:width: 80%
:align: center

Esquema de uma grelha de pavimento. As barras internas representam faixas de laje; o contorno representa as vigas. Desenho didático, sem escala.
```

Na montagem do modelo, definem-se a posição das barras, suas larguras de influência, as rigidezes à flexão e à torção e as ligações com vigas e pilares. A malha deve representar aberturas, mudanças de espessura e apoios relevantes. A distribuição das ações entre as barras precisa preservar a carga total do pavimento.

Uma barra associada a uma faixa de largura $b$ e espessura $h$ tem, como referência geométrica para a flexão, $I=bh^3/12$. A equivalência com uma placa exige também tratar a torção e a participação das barras nas duas direções. A escolha dessas rigidezes interfere na distribuição dos esforços e nos deslocamentos.

A fissuração modifica a rigidez do concreto armado. Por isso, os parâmetros de uma análise elástica inicial precisam ser distinguidos daqueles usados para estudar a estrutura fissurada. Coeficientes destinados a outras análises não devem ser transferidos automaticamente para todas as barras da grelha.

**O que a grelha acrescenta?** As vigas podem se deformar junto com as lajes, e os painéis interagem pelo mesmo modelo. Nas tabelas, essa interação é substituída por vínculos idealizados em cada painel. Assim, diferenças entre os resultados podem vir das hipóteses de apoio e rigidez.

Para uma comparação, iguale vãos, vínculos e ações e converta as unidades. Se uma barra representa uma faixa de $0{,}50\,\mathrm{m}$ e apresenta $M=3{,}0\,\mathrm{kN\,m}$, o momento médio equivalente nessa faixa é:

$$
m\approx\frac{M}{b}=\frac{3{,}0}{0{,}50}=6{,}0\,\mathrm{kN\,m/m}.
$$

Essa conversão exige conhecer a largura efetivamente representada pela barra e a convenção do programa. Refinar a malha ajuda a estudar a convergência, mas não corrige um vínculo escolhido incorretamente.

### Quando basta uma faixa?

Para uma laje predominantemente unidirecional, podemos analisar uma faixa de largura $b=1\,\mathrm{m}$, com carga linear $q=pb$. A direção da faixa acompanha o vão resistente.

| Faixa sob carga uniforme | Momento positivo máximo | Módulo do negativo |
|---|---|---|
| Simplesmente apoiada nas extremidades | $ql^2/8$ | Zero nos apoios ideais |
| Engastada nas duas extremidades | $ql^2/24$ | $ql^2/12$ em cada extremidade |
| Balanço | Zero | $ql^2/2$ na raiz |

São resultados de barras com os vínculos indicados. Uma faixa contínua com vários tramos precisa ser analisada com sua continuidade; não basta separar todos os vãos como se fossem independentes. Para o painel bidirecional, passaremos às tabelas de placas.

## Como funciona uma tabela de lajes?

O comportamento de uma placa depende de sua forma, dos apoios e da distribuição das ações. As tabelas reúnem soluções desse problema em **coeficientes adimensionais**. Ao escolher uma coluna e uma linha, estamos escolhendo também as hipóteses de uma solução estrutural.

No procedimento desta aula, consideram-se painéis retangulares, espessura constante, comportamento elástico linear e carga uniforme por área. A validade do caso depende ainda dos vínculos e da condição dos cantos prevista na referência.

A família adotada no material do professor é a de **Bares, adaptada por Libânio Pinheiro**. Para consulta, utilizaremos as tabelas A-8 a A-10 do material de [Bastos, *Lajes de concreto armado*](https://wwwp.feb.unesp.br/pbastos/concreto1/Lajes.pdf#page=94), nas páginas impressas 90 a 92. O pequeno recorte numérico usado adiante corresponde à tabela A-8.

### Primeiro: desenhar e orientar o painel

Antes de procurar números, registre os vínculos em um croqui. Uma borda paralela a $y$ está em uma extremidade de uma faixa que vence o vão $l_x$; um engaste nessa borda está associado a um momento negativo da direção $x$.

```{admonition} A posição do engaste faz parte do caso
:class: destaque-azul

Duas lajes podem ter uma borda engastada e três apoiadas, mas exigir colunas diferentes. Engastar uma borda de comprimento $l_x$ ou uma de comprimento $l_y$ altera o problema. Compare o desenho completo da tabela com o croqui do painel.
```

Ao girar um desenho, mantenha a correspondência dos eixos e dos coeficientes. A quantidade de bordas engastadas, isoladamente, não identifica o caso.

### Segundo: calcular a relação entre os vãos

$$
\lambda=\frac{l_y}{l_x},\qquad l_y\geq l_x.
$$

Use os vãos efetivos obtidos na Aula 04. A linha de $\lambda$ pertence ao caso de apoio escolhido; não se deve misturar coeficientes de casos diferentes.

### Terceiro: identificar as colunas e a expressão do cabeçalho

Na convenção usada aqui:

$$
m_x=\mu_x\frac{pl_x^2}{100},\qquad
m_y=\mu_y\frac{pl_x^2}{100},
$$

$$
X_x=\mu'_x\frac{pl_x^2}{100},\qquad
X_y=\mu'_y\frac{pl_x^2}{100}.
$$

| Coeficiente | Resultado | Região associada |
|---|---|---|
| $\mu_x$ | $m_x$ positivo | Vão, direção $x$ |
| $\mu_y$ | $m_y$ positivo | Vão, direção $y$ |
| $\mu'_x$ | Módulo $X_x$ | Bordo engastado normal a $x$ |
| $\mu'_y$ | Módulo $X_y$ | Bordo engastado normal a $y$ |

**As quatro expressões usam $l_x^2$.** A participação do maior vão já está incorporada no coeficiente por meio de $\lambda$. Também é preciso conferir o divisor 100: outra publicação pode apresentar a mesma solução com uma normalização diferente.

Com $p$ em $\mathrm{kN/m^2}$ e os vãos em metros, o resultado é expresso como momento por unidade de largura, em $\mathrm{kN\,m/m}$. O símbolo $p$ representa o caso de carga analisado. Se forem usadas ações de cálculo, obtêm-se esforços de cálculo; não se aplica novamente a mesma ponderação ao final.

## Exemplo resolvido: consulta e interpolação

Considere um painel com os **quatro bordos simplesmente apoiados**, vãos efetivos $l_x=4{,}00\,\mathrm{m}$ e $l_y=5{,}30\,\mathrm{m}$ e carga uniforme dada de $p=6{,}00\,\mathrm{kN/m^2}$. Admitem-se as condições de contorno do caso tabelado, incluindo a restrição de levantamento dos cantos.

Na tabela A-8, esse esquema corresponde ao **tipo 1**. Para os exemplos desta aula, o recorte de consulta é:

| $\lambda$ | Tipo 1: $\mu_x$ | Tipo 1: $\mu_y$ | Tipo 2B: $\mu_x$ | Tipo 2B: $\mu'_x$ | Tipo 2B: $\mu_y$ |
|---:|---:|---:|---:|---:|---:|
| 1,30 | 6,44 | 4,12 | 4,71 | 10,32 | 2,42 |
| 1,35 | 6,77 | 4,06 | 4,86 | 10,54 | 2,34 |

Fonte dos coeficientes: [Bastos, tabela A-8, p. 90](https://wwwp.feb.unesp.br/pbastos/concreto1/Lajes.pdf#page=94), que os atribui a Bares e à adaptação de Pinheiro (1994). O tipo 2B possui uma borda de comprimento $l_y$ engastada e as outras três simplesmente apoiadas. O recorte serve somente ao intervalo e aos casos indicados; os demais casos devem ser consultados no documento.

### Localizar o valor intermediário

$$
\lambda=\frac{5{,}30}{4{,}00}=1{,}325.
$$

O valor está entre 1,30 e 1,35. Dentro do mesmo caso, interpolamos cada coeficiente por:

$$
\mu=\mu_a+\frac{\lambda-\lambda_a}{\lambda_b-\lambda_a}(\mu_b-\mu_a).
$$

A fração do intervalo é $(1{,}325-1{,}30)/(1{,}35-1{,}30)=0{,}5$. Para o tipo 1:

$$
\mu_x=6{,}44+0{,}5(6{,}77-6{,}44)=6{,}605,
$$

$$
\mu_y=4{,}12+0{,}5(4{,}06-4{,}12)=4{,}09.
$$

### Calcular os momentos

O fator comum é:

$$
\frac{pl_x^2}{100}=\frac{6{,}00\times4{,}00^2}{100}=0{,}96.
$$

Logo:

$$
m_x=6{,}605\times0{,}96\approx6{,}34\,\mathrm{kN\,m/m},
\qquad
m_y=4{,}09\times0{,}96\approx3{,}93\,\mathrm{kN\,m/m}.
$$

O maior momento está na direção do menor vão. Os momentos normais aos bordos simplesmente apoiados são nulos no modelo ideal. Essa informação não elimina as verificações e disposições construtivas das regiões de borda e canto.

### Alterar um vínculo e interpretar a diferença

Mantenha os mesmos vãos e a mesma carga, mas engaste uma das bordas de comprimento $l_y$. No tipo 2B, a interpolação fornece $\mu_x=4{,}785$, $\mu'_x=10{,}43$ e $\mu_y=2{,}38$.

| Resultado | Quatro bordos apoiados | Uma borda de comprimento $l_y$ engastada |
|---|---:|---:|
| $m_x$ | $6{,}34$ | $4{,}59$ |
| $m_y$ | $3{,}93$ | $2{,}28$ |
| Momento no bordo engastado, direção $x$ | Não há engaste | $-10{,}01$ |

Todos os valores estão em $\mathrm{kN\,m/m}$. A restrição à rotação mobiliza momento negativo e modifica os positivos. Portanto, a escolha do vínculo precisa preceder a consulta dos coeficientes.

## Continuidade: compatibilizar os momentos dos painéis

Ao calcular duas lajes separadamente, a mesma borda interna pode receber dois valores de momento negativo. Isso acontece porque cada painel tem seus próprios vãos, vínculos e ações. Para o cálculo manual por painéis, o material-base apresenta uma compatibilização aproximada desses valores.

Se $X_1$ e $X_2$ são os módulos dos negativos dos dois lados da borda comum:

$$
X_c=\max\left[\frac{X_1+X_2}{2};\,0{,}8\max(X_1,X_2)\right].
$$

Adota-se o momento $-X_c$ nos dois lados. Antes de aplicar a expressão, verifique se os valores correspondem à **mesma borda física, à flexão normal a ela e à mesma combinação de ações**. Os eixos locais de duas lajes podem ter nomes diferentes.

### Ajuste do positivo

Se o módulo do negativo de um painel diminui, aumenta-se seu positivo na direção correspondente. Para uma borda modificada:

$$
m^+_{i,c}=m^+_i+\frac{\max(0;X_i-X_c)}{2}.
$$

Quando o negativo aumenta, conserva-se o positivo inicial nessa aproximação. Se as duas extremidades da mesma direção sofrerem redução de negativo, somam-se os dois acréscimos. Esse procedimento é uma regra prática de cálculo por painéis; não representa uma solução conjunta das rotações de toda a borda.

### Exemplo de dois painéis vizinhos

Para uma mesma combinação, os resultados iniciais são:

| Painel | Positivo na direção estudada | Módulo do negativo na borda comum |
|---|---:|---:|
| L1 | $4{,}0$ | $10{,}0$ |
| L2 | $3{,}0$ | $6{,}0$ |

Valores em $\mathrm{kN\,m/m}$. O momento comum será:

$$
X_c=\max[(10+6)/2;\,0{,}8\times10]=8{,}0\,\mathrm{kN\,m/m}.
$$

Em L1, o positivo passa a $4+(10-8)/2=5{,}0\,\mathrm{kN\,m/m}$. Em L2, permanece em $3{,}0\,\mathrm{kN\,m/m}$. Na borda, registra-se $-8{,}0\,\mathrm{kN\,m/m}$ para ambos os painéis.

```{admonition} Relação com a grelha
:class: destaque-azul

Uma análise conjunta por grelha ou placa contínua já considera a interação entre os elementos. A regra de compatibilização dos painéis isolados não deve ser aplicada automaticamente uma segunda vez aos resultados desse modelo.
```

## O que conferir além dos momentos tabelados?

### Momentos volventes e cantos

A placa também pode sofrer torção, representada por $m_{xy}$. Perto dos cantos, esse efeito pode ser relevante mesmo que os momentos $m_x$ e $m_y$ sejam pequenos. Um apoio que impede o levantamento do canto precisa transmitir a ação de retenção correspondente.

Se o canto puder perder contato com o suporte, a condição de contorno muda. Por isso, a escolha da tabela deve ser coerente com a ligação e com o detalhamento previsto. A armadura de distribuição, por si só, não comprova a resistência aos esforços de canto.

### Alcance do cálculo por tabelas

Grandes aberturas, apoios muito deformáveis, pilares diretamente sob a laje ou ações localizadas importantes podem exigir outro modelo. Não se deve substituir essas situações por um caso tabelado apenas por semelhança visual.

Os momentos obtidos ainda precisam alimentar o dimensionamento e o detalhamento. Também permanecem as verificações de cortante, deformações e fissuração, conforme a situação. Para balanços, os esforços finais de cálculo devem receber o tratamento específico previsto no material normativo adotado.

## Atividade: montar a memória de esforços

Uma laje tem vãos efetivos $4{,}00\times5{,}40\,\mathrm{m}$, carga uniforme dada de $6{,}00\,\mathrm{kN/m^2}$ e uma borda de comprimento $5{,}40\,\mathrm{m}$ engastada. As outras três são simplesmente apoiadas.

1. Oriente os eixos e desenhe os vínculos.
2. Calcule $\lambda$ e identifique o caso no recorte da tabela A-8.
3. Determine os positivos e o negativo, registrando o sinal e a direção.
4. Considere que o painel vizinho apresenta $X=7{,}00\,\mathrm{kN\,m/m}$ na borda comum, para a mesma combinação. Compatibilize os negativos e corrija o positivo da laje estudada.

**Conferência:** $\lambda=1{,}35$, tipo 2B; $m_x\approx4{,}67$, $m_y\approx2{,}25$ e $X_x\approx10{,}12\,\mathrm{kN\,m/m}$. Mantendo as casas decimais durante as operações, $X_c\approx8{,}56$ e $m_{x,c}^+\approx5{,}45\,\mathrm{kN\,m/m}$. A correção dessa borda ocorre na direção $x$.

No trabalho da disciplina, registre para cada painel: croqui, vãos efetivos, caso de apoio, $\lambda$, carga do caso analisado, coeficientes e momentos. Acrescente um quadro por borda interna com os negativos dos dois lados, o valor comum e os positivos corrigidos. Esse registro permite conferir de onde veio cada esforço utilizado no dimensionamento.

## Referências

- PEREIRA JUNIOR, Wanderlei Malaquias. *Determinação dos esforços em lajes*. Material do professor, capítulo 2. Base para a discussão dos modelos, convenções e compatibilização.
- BASTOS, Paulo Sérgio dos Santos. *Lajes de concreto armado*. UNESP, Bauru, 2023. [Material de consulta](https://wwwp.feb.unesp.br/pbastos/concreto1/Lajes.pdf). Tabela A-8, p. 90: coeficientes utilizados nos exemplos, extraídos de Bares e adaptados por Pinheiro (1994).
