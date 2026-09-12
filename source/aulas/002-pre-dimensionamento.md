# Aula 02: Pré-dimensionamento dos elementos estruturais

Antes do lançamento estrutural definitivo e da análise detalhada de esforços,
é usual estimar as dimensões iniciais de vigas, lajes e pilares por meio de
critérios práticos de pré-dimensionamento. Essas estimativas permitem montar
um modelo estrutural coerente, evitar retrabalho na modelagem e servem como
ponto de partida para o dimensionamento final em concreto armado.

## Pré-dimensionamento de vigas

A ABNT NBR 6118 [[1]](#ref-1) faz uma ressalva quanto à largura de vigas de
concreto armado ou protendido no item 15.10, que trata da segurança à
instabilidade lateral. Segundo a norma, essa segurança deve ser garantida por
meio de procedimentos apropriados; para tanto, são estabelecidos critérios que
definem uma largura mínima para a viga em função das condições de
contraventamento lateral, expressos pelas Equações (1) e (2):

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
- $l_0$ é o comprimento do flange comprimido, medido entre os suportes que
  garantem o contraventamento lateral;
- $\beta_{fl}$ é um coeficiente que depende da forma da seção transversal da
  viga presente na Figura [1](#figura1).

(figura1)=
**Figura 1.** Coeficiente $\beta_{fl}$ para seções de viga.
```{figure} ../_static/aulas/pre-dimensionamento/quadro-beta-fl-vigas.png
:alt: Coeficiente beta_fl para seções de viga, em função da tipologia da seção transversal
:width: 75%
:align: center
```

## Pré-dimensionamento de lajes

Diversos autores apresentam procedimentos para a determinação da geometria da
forma em lajes maciças e nervuradas. Nesta aula, o foco adotado é o trabalho
de Rebello [[2]](#ref-2).

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

Como as lajes nervuradas se dividem em diversos grupos, adotam-se critérios
distintos para as lajes unidirecionais e para as lajes bidirecionais.

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

Segundo Rebello [[2]](#ref-2), para estruturas usuais em concreto armado a altura da capa ($h_f$) esse
pode variar de 4 a 7 cm. 

Já as distâncias intereixos em lajes nervuradas moldadas *in loco* não decorrem de uma
formulação de pré-dimensionamento, mas sim do elemento de enchimento (EPS, cerâmica etc.)
adotado pelo projetista, cujas dimensões comerciais definem a largura da nervura e o vão
entre eixos. 

b) Lajes bidirecionais (em grelha):

$$
h = 4\%\cdot\frac{l_y+l_x}{2}
\tag{9}
$$

$$
b_w = \frac{1}{4}h \text{ a } \frac{1}{3}h
\tag{10}
$$

Segundo Rebello [[2]](#ref-2), o espaçamento $a$ entre nervuras dessas lajes bidirecionais
varia de $1{,}5\,h$ a $2{,}0\,h$.

### Coeficiente adicional de segurança para lajes em balanço

Além dos critérios de pré-dimensionamento apresentados, as lajes em balanço
estão sujeitas a um coeficiente adicional de segurança $\gamma_n$, prescrito
pela ABNT NBR 6118 [[1]](#ref-1) em função da altura da laje, conforme o
[Quadro 1](#quadro1).

(quadro1)=
**Quadro 1 — Valores do coeficiente adicional $\gamma_n$ para lajes em
balanço.**

| $h$ (cm) | ≥ 19 | 18 | 17 | 16 | 15 | 14 | 13 | 12 | 11 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $\gamma_n$ | 1,00 | 1,05 | 1,10 | 1,15 | 1,20 | 1,25 | 1,30 | 1,35 | 1,40 | 1,45 |


O [Quadro 1](#quadro1) pode ser expresso pela Equação (11), em que $h$ é
a altura da laje em centímetros:

$$
\gamma_n = 1{,}95 - 0{,}05\,h
\tag{11}
$$

O coeficiente $\gamma_n$ deve majorar os esforços solicitantes finais de
cálculo nas lajes em balanço, quando de seu dimensionamento.

## Pré-dimensionamento de pilares

### Área de influência

Bacarji [[3]](#ref-3) orienta a divisão da área de influência dos pilares em
faixas proporcionais ao vão, de acordo com a posição do pilar na planta:

- $0{,}45\cdot l$: pilar de extremidade ou de canto, na direção da menor
  dimensão do pilar ($b$);
- $0{,}50\cdot l$: pilar de extremidade ou de canto, na direção da maior
  dimensão do pilar ($h$);
- $0{,}55\cdot l$: complemento dos casos anteriores (demais faixas, incluindo
  pilares intermediários).

(figura2)=
**Figura 2.** Planta de estimativa da área de influência de um pilar de concreto armado.
```{figure} ../_static/aulas/pre-dimensionamento/planta-carga-pilar.png
:alt: planta de cargas
:width: 75%
:align: center
```

### Carga estimada e seção transversal do pilar

Após a determinação da área de influência e do carregamento estimado no
pavimento, a seção transversal do pilar pode ser obtida pela Equação (12):

$$
A_c = \frac{N_d^{*}}{0{,}85\,f_{cd} + \rho\,\sigma_{s,\varepsilon=0,2\%}}
\tag{12}
$$

em que:

- $A_c$ é a área da seção transversal do pilar, em $\mathrm{cm^2}$;
- $N_d^{*}$ é a força normal de cálculo para pré-dimensionamento, em $\mathrm{kN}$;
- $f_{cd} = f_{ck}/1{,}40$ é a resistência à compressão de cálculo do
  concreto, em $\mathrm{kN/cm^2}$;
- $\sigma_{s,\varepsilon=0,2\%}$ é a tensão no aço correspondente a uma
  deformação de $0{,}20\%$, que para o aço CA-50 vale $420\ \mathrm{MPa}$;
- $\rho$ é a taxa de armadura do pilar; da Costa [[4]](#ref-4) recomenda,
  como valor intermediário, $\rho = 2\%$ (inserido na Equação (12) como
  $\rho = 2/100$, e não em taxa percentual).

Para determinar a carga atuante de pré-dimensionamento, utilizam-se as
Equações (13) a (16):

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

em que $N_k^{*}$ é a carga característica para pré-dimensionamento; $Q_{tot}$
é a carga total no pavimento; $A_i$ é a área de influência do pilar $i$
analisado; $N_k^{tipo}$ é a carga em um pilar do pavimento tipo; $n_{tipo}$ é
o número de pavimentos tipo acima do nível calculado; $N_k^{cob}$ é a carga
em um pilar do pavimento de cobertura; $n_{cob}$ é o número de pavimentos de
cobertura acima do nível calculado; e $\alpha$ é um coeficiente de majoração
da carga de pré-dimensionamento, que leva em conta os esforços de flexão não
considerados nessa etapa.

## Síntese

```{admonition} Caminho básico para o pré-dimensionamento
:class: destaque-azul

1. Verificar, para vigas sem travamento lateral por lajes, a largura mínima
   dada pelas Equações (1) e (2).
2. Estimar a altura das lajes maciças ou nervuradas com base nos vãos $l_x$
   e $l_y$ do painel.
3. Majorar os esforços de lajes em balanço pelo coeficiente $\gamma_n$,
   conforme o [Quadro 1](#quadro1).
4. Definir a área de influência de cada pilar a partir das faixas de
   Bacarji.
5. Estimar a carga característica e de cálculo do pilar e obter a área da
   seção transversal pela Equação (12).
```

## Referências

(ref-1)=
**[1]** ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **ABNT NBR 6118**: Projeto de
estruturas de concreto. 4. ed. Rio de Janeiro: ABNT, 2023.

(ref-2)=
**[2]** REBELLO, Yopanan Conrado Pereira. **Bases para projeto estrutural
na arquitetura**. 2. ed. São Paulo: Zigurate Editora, 2007.

(ref-3)=
**[3]** BACARJI, Edgar. **Análise de estruturas de edifícios: projeto de
pilares**. 1993. Dissertação (Mestrado em Engenharia de Estruturas) — Escola
de Engenharia de São Carlos, Universidade de São Paulo, São Carlos, 1993.

(ref-4)=
**[4]** COSTA, *[referência incompleta — confirmar nome completo, título,
editora e ano da obra para completar a citação]*.
