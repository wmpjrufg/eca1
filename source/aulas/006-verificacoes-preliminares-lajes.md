# Aula 07: Verificações preliminares em lajes

Na [Aula 06](006-esforcos-lajes.md), foram determinados os momentos fletores e as reações das lajes. Antes de dimensionar e detalhar as armaduras, convém verificar se a espessura adotada conduz a uma solução viável. Nesta etapa, a armadura de flexão ainda não foi calculada; por isso, as verificações são feitas com a **armadura mínima** prevista para a laje.

Esta aula trata de duas verificações preliminares:

- resistência ao cisalhamento de lajes sem armadura transversal;
- deslocamentos, incluindo a fissuração e a deformação diferida do concreto.

```{admonition} Edição normativa adotada
:class: destaque-azul

As equações, os números de itens e as tabelas desta aula seguem a ABNT NBR 6118:2023, edição adotada atualmente no repositório e no trabalho prático da disciplina. O catálogo da ABNT já relaciona a edição 2026. Uma futura migração deve revisar esta aula e as demais referências normativas do curso em conjunto.
```

```{admonition} Objetivos da aula
:class: destaque-azul

- Determinar a armadura mínima usada nas verificações preliminares.
- Verificar uma faixa de laje ao cisalhamento sem armadura transversal.
- Calcular a rigidez equivalente de uma seção fissurada com a armadura mínima.
- Estimar a flecha imediata e a flecha diferida.
- Decidir se a espessura inicial da laje pode ser mantida antes do detalhamento.
```

## Alcance da verificação preliminar

Adota-se uma faixa de laje com largura $b_w=1{,}00\text{ m}$. A área de aço é expressa por metro de laje e uma bitola provisória é usada apenas para estimar a altura útil,

$$
d=h-c_{nom}-\frac{\phi}{2}.
$$

Ainda não serão definidos os comprimentos, as emendas, as ancoragens ou a distribuição final das barras. Depois do dimensionamento à flexão, as verificações devem ser refeitas com a armadura efetivamente adotada.

| Verificação | Combinação ou esforço | Resultado principal |
|---|---|---|
| Cisalhamento | Reação de cálculo em cada borda | $V_{Sd}/V_{Rd1}$ |
| Flecha total | Combinação quase permanente | $a_t/(l/250)$ |
| Parcela da carga acidental | Ação variável considerada na verificação | $a_q/(l/350)$ |

No cisalhamento, usam-se ações de cálculo do estado-limite último. Na flecha, usam-se ações de serviço. As duas verificações não devem empregar a mesma combinação de cargas.

## Armadura mínima adotada nesta etapa

Para uma faixa de largura $b_w$, a área mínima é

$$
A_{s,min}=\rho_{s,min}\,b_w h.
$$

Na equação, a taxa deve ser usada em forma decimal: $0{,}150\%=0{,}00150$. Para as classes usuais de concreto até C50, a taxa básica $\rho_{min}$ da ABNT NBR 6118 é:

| Classe | C20 | C25 | C30 | C35 | C40 | C45 | C50 |
|---|---:|---:|---:|---:|---:|---:|---:|
| $\rho_{min}$ (%) | 0,150 | 0,150 | 0,150 | 0,164 | 0,179 | 0,194 | 0,208 |

A Tabela 19.1 da norma distingue as regiões da laje:

| Região considerada | Taxa mínima usada na verificação preliminar |
|---|---:|
| Armadura negativa | $\rho_{s,min}=\rho_{min}$ |
| Armadura positiva de laje armada em uma direção | $\rho_{s,min}=\rho_{min}$ |
| Armadura positiva, em cada direção, de laje armada em duas direções | $\rho_{s,min}=0{,}67\rho_{min}$ |

A área correspondente à região verificada deve ser usada tanto na taxa longitudinal do cisalhamento quanto no cálculo da seção fissurada. Em uma borda contínua, por exemplo, a armadura tracionada relevante pode ser a negativa, localizada na face superior.

```{admonition} Hipótese, não detalhamento
:class: destaque-azul

Usar $A_{s,min}$ não significa que essa será a armadura final. A hipótese serve para identificar lajes cuja espessura já é inviável antes de concluir o dimensionamento à flexão.
```

## Verificação ao cisalhamento

Para lajes sem armadura transversal, o item 19.4.1 da ABNT NBR 6118 estabelece:

$$
V_{Sd}\leq V_{Rd1},
$$

com

$$
V_{Rd1}=\left[\tau_{Rd}\,k\left(1{,}2+40\rho_1\right)+0{,}15\sigma_{cp}\right]b_wd,
$$

$$
\tau_{Rd}=0{,}25f_{ctd},
\qquad
\rho_1=\frac{A_{s1}}{b_wd}\leq0{,}02,
$$

$$
k=1{,}6-d\geq1{,}0.
$$

Na expressão de $k$, a altura útil $d$ é inserida em metros. As demais grandezas podem ser calculadas de forma conveniente em milímetros e megapascais, lembrando que $1\text{ MPa}=1\text{ N/mm}^2$.

| Símbolo | Significado |
|---|---|
| $V_{Sd}$ | força cortante de cálculo na faixa considerada |
| $V_{Rd1}$ | resistência de cálculo da laje sem armadura transversal |
| $A_{s1}$ | armadura longitudinal tracionada que atravessa a região verificada e possui ancoragem adequada |
| $\sigma_{cp}=N_{Sd}/A_c$ | tensão normal de compressão; em lajes usuais sem força normal, adota-se $\sigma_{cp}=0$ |
| $b_w$ | largura da faixa, usualmente $1000\text{ mm}$ |

A verificação deve ser feita em cada borda com a reação correspondente. Em lajes bidirecionais, não se deve substituir a reação distribuída obtida no modelo por $p_dl/2$ sem justificar uma faixa unidirecional equivalente.

### Exemplo 1: cisalhamento de uma faixa unidirecional

Considere uma laje unidirecional simplesmente apoiada, com:

- vão $l=5{,}00\text{ m}$;
- espessura $h=12\text{ cm}$;
- concreto C30 e $\gamma_c=1{,}4$;
- cobrimento nominal $c_{nom}=25\text{ mm}$;
- bitola provisória $\phi=6{,}3\text{ mm}$;
- carga uniforme de cálculo $p_d=11{,}20\text{ kN/m}^2$.

Para C30, $\rho_{min}=0{,}150\%$. Como a faixa é unidirecional,

$$
A_{s,min}=0{,}00150\times1000\times120
=180\text{ mm}^2/\text{m}=1{,}80\text{ cm}^2/\text{m}.
$$

A altura útil provisória é

$$
d=120-25-\frac{6{,}3}{2}=91{,}85\text{ mm}.
$$

Para a faixa simplesmente apoiada,

$$
V_{Sd}=\frac{p_dl}{2}
=\frac{11{,}20\times5{,}00}{2}
=28{,}0\text{ kN/m}.
$$

As propriedades de tração do concreto são:

$$
f_{ctm}=0{,}3f_{ck}^{2/3}=2{,}90\text{ MPa},
$$

$$
f_{ctd}=\frac{0{,}7f_{ctm}}{\gamma_c}=1{,}45\text{ MPa},
\qquad
\tau_{Rd}=0{,}25f_{ctd}=0{,}362\text{ MPa}.
$$

Como $\sigma_{cp}=0$,

$$
\rho_1=\frac{180}{1000\times91{,}85}=0{,}00196,
\qquad
k=1{,}6-0{,}09185=1{,}508.
$$

Logo,

$$
V_{Rd1}=0{,}362\times1{,}508
\times(1{,}2+40\times0{,}00196)
\times1000\times91{,}85
\approx64{,}1\text{ kN/m}.
$$

$$
\frac{V_{Sd}}{V_{Rd1}}=\frac{28{,}0}{64{,}1}=0{,}44<1{,}0.
$$

A laje atende à verificação preliminar de cisalhamento. Essa conclusão não antecipa o resultado da flecha.

## Verificação da flecha

A deformação depende da combinação de serviço, da rigidez da seção e do tempo de atuação das cargas. Para uma edificação residencial com $\psi_2=0{,}3$, a carga quase permanente é

$$
p_{qp}=g_k+\psi_2q_k.
$$

O momento de serviço $M_a$ deve vir do mesmo modelo estrutural adotado para a laje, agora com essa combinação. Na faixa unidirecional simplesmente apoiada,

$$
M_a=\frac{p_{qp}l^2}{8}.
$$

### Momento de fissuração

Para uma faixa retangular,

$$
I_c=\frac{b_wh^3}{12},
\qquad
y_t=\frac{h}{2},
$$

$$
M_r=\alpha\frac{f_{ctm}I_c}{y_t},
$$

com $\alpha=1{,}5$ para a seção retangular. Se $M_a\leq M_r$, adota-se $I_{eq}=I_c$.

### Inércia da seção fissurada

Quando $M_a>M_r$, calcula-se a seção no Estádio II. Para uma faixa retangular com armadura simples:

$$
\alpha_e=\frac{E_s}{E_{cs}},
$$

$$
\frac{b_wx_{II}^2}{2}
=\alpha_eA_s(d-x_{II}),
$$

$$
I_{II}=\frac{b_wx_{II}^3}{3}
+\alpha_eA_s(d-x_{II})^2.
$$

Nesta etapa, usa-se $A_s=A_{s,min}$ da região tracionada. Despreza-se a contribuição do concreto tracionado na seção fissurada.

### Rigidez equivalente de Branson

Para $M_a>M_r$, o item 17.3.2.1 da ABNT NBR 6118 permite estimar:

$$
I_{eq}=\left(\frac{M_r}{M_a}\right)^3I_c
+\left[1-\left(\frac{M_r}{M_a}\right)^3\right]I_{II}
\leq I_c.
$$

O material original da disciplina apresenta $I_{eq}\approx0{,}30I_c$ como estimativa rápida para uma seção fissurada. Na memória do projeto, deve-se usar a expressão de Branson, pois ela incorpora a armadura mínima e a intensidade do momento de serviço.

### Flecha imediata

Para uma faixa submetida a carga uniforme,

$$
a_i=C_a\frac{p_{qp}l^4}{E_{cs}I_{eq}}.
$$

| Condição idealizada da faixa | $C_a$ |
|---|---:|
| Simplesmente apoiada | $5/384$ |
| Engastada nas duas extremidades | $1/384$ |
| Balanço | $1/8$ |

Os coeficientes acima pertencem a barras. Para lajes bidirecionais, deve-se empregar um coeficiente de placa ou obter o deslocamento pelo modelo estrutural adotado. Não se deve somar flechas de duas faixas independentes sem uma hipótese compatível com o comportamento da placa.

### Deformação diferida

A parcela diferida é estimada por

$$
a_f=\alpha_fa_i,
\qquad
a_t=a_i+a_f=a_i(1+\alpha_f),
$$

$$
\alpha_f=\frac{\Delta\xi}{1+50\rho'},
\qquad
\rho'=\frac{A_s'}{b_wd},
$$

$$
\Delta\xi=\xi(t)-\xi(t_0),
$$

$$
\xi(t)=
\begin{cases}
0{,}68(0{,}996)^t t^{0{,}32}, & t\leq70\text{ meses},\\
2{,}0, & t>70\text{ meses}.
\end{cases}
$$

$t_0$ é a idade, em meses, no início da atuação da carga considerada. Na verificação preliminar sem armadura de compressão, adota-se $\rho'=0$.

### Limites

Para a situação usual tratada no projeto da disciplina, com $l$ igual ao menor vão efetivo:

- aceitabilidade visual: $a_t\leq l/250$;
- vibrações: parcela devida às cargas acidentais $a_q\leq l/350$.

O limite deve ser escolhido conforme o efeito analisado e a Tabela 13.3 da ABNT NBR 6118. Uma única flecha não deve ser comparada indiscriminadamente com todos os limites da tabela.

### Exemplo 2: flecha com armadura mínima

Considere uma faixa unidirecional simplesmente apoiada com os mesmos materiais e dimensões do Exemplo 1, agora sob:

- $g_k=4{,}50\text{ kN/m}^2$;
- $q_k=2{,}00\text{ kN/m}^2$;
- $\psi_2=0{,}3$;
- $E_s=210\text{ GPa}$.

A carga quase permanente é

$$
p_{qp}=4{,}50+0{,}3\times2{,}00
=5{,}10\text{ kN/m}^2.
$$

Para a faixa de $1\text{ m}$, $p_{qp}=5{,}10\text{ kN/m}=5{,}10\text{ N/mm}$. Para o concreto C30,

$$
E_{cs}\approx26{,}84\text{ GPa},
\qquad
I_c=\frac{1000\times120^3}{12}
=144{,}0\times10^6\text{ mm}^4.
$$

O momento de fissuração e o momento atuante são:

$$
M_r=1{,}5\frac{2{,}90\times144{,}0\times10^6}{60}
\approx10{,}43\text{ kN m/m},
$$

$$
M_a=\frac{5{,}10\times5{,}00^2}{8}
=15{,}94\text{ kN m/m}.
$$

Como $M_a>M_r$, a seção fissura. Com $A_s=A_{s,min}=180\text{ mm}^2/\text{m}$,

$$
\alpha_e=\frac{210000}{26840}=7{,}82.
$$

A solução da equação da linha neutra fornece

$$
x_{II}\approx14{,}74\text{ mm},
\qquad
I_{II}\approx9{,}44\times10^6\text{ mm}^4.
$$

A inércia equivalente é

$$
I_{eq}\approx47{,}1\times10^6\text{ mm}^4.
$$

A flecha imediata resulta em

$$
a_i=\frac{5\times5{,}10\times5000^4}
{384\times26840\times47{,}1\times10^6}
\approx32{,}8\text{ mm}.
$$

Para $t_0=1$ mês e $t>70$ meses,

$$
\xi(1)=0{,}677,
\qquad
\Delta\xi=2{,}0-0{,}677=1{,}323.
$$

Sem armadura de compressão, $\rho'=0$ e $\alpha_f=1{,}323$. Portanto,

$$
a_t=32{,}8(1+1{,}323)
\approx76{,}2\text{ mm}.
$$

$$
\frac{l}{250}=\frac{5000}{250}=20{,}0\text{ mm}.
$$

A laje não atende. A parcela imediata associada a $q_k$, calculada com a mesma rigidez de serviço, é aproximadamente $12{,}9\text{ mm}$, inferior a $l/350=14{,}3\text{ mm}$. Mesmo assim, a flecha total reprova a espessura adotada.

#### Revisão da espessura

Se a espessura aumentar para $h=16\text{ cm}$, o peso próprio cresce $1{,}00\text{ kN/m}^2$. Assim, $p_{qp}$ passa a $6{,}10\text{ kN/m}^2$. Recalculando todos os parâmetros:

| Grandeza | $h=12\text{ cm}$ | $h=16\text{ cm}$ |
|---|---:|---:|
| $A_{s,min}$ ($\text{cm}^2/\text{m}$) | 1,80 | 2,40 |
| $d$ (mm) | 91,9 | 131,9 |
| $M_r$ ($\text{kN m/m}$) | 10,43 | 18,54 |
| $M_a$ ($\text{kN m/m}$) | 15,94 | 19,06 |
| $I_{eq}$ ($10^6\text{ mm}^4$) | 47,1 | 316,0 |
| $a_i$ (mm) | 32,8 | 5,85 |
| $a_t$ (mm) | 76,2 | 13,6 |

Com $h=16\text{ cm}$, a estimativa passa a atender $l/250=20\text{ mm}$. O aumento de espessura exige atualizar o peso próprio, os esforços, as reações e a verificação ao cisalhamento.

## Exemplos para desenvolver em sala

### Atividade 1: cisalhamento de uma laje bidirecional

Uma laje bidirecional de concreto C30 tem $h=14\text{ cm}$, $c_{nom}=25\text{ mm}$ e bitola provisória $\phi=6{,}3\text{ mm}$. Em uma borda, $V_{Sd}=35\text{ kN/m}$. Considere a armadura positiva mínima da laje bidirecional, $\sigma_{cp}=0$ e $\gamma_c=1{,}4$.

1. Calcule $A_{s,min}$ por direção.
2. Determine $d$, $\rho_1$, $k$ e $V_{Rd1}$.
3. Calcule a razão de utilização e conclua.

**Conferência:** $A_{s,min}=1{,}41\text{ cm}^2/\text{m}$, $d=111{,}9\text{ mm}$, $\rho_1=0{,}00126$, $k=1{,}488$, $V_{Rd1}\approx75{,}3\text{ kN/m}$ e $V_{Sd}/V_{Rd1}\approx0{,}46$. A borda atende.

### Atividade 2: flecha de uma faixa não fissurada

Uma laje unidirecional simplesmente apoiada tem $l=4{,}00\text{ m}$, $h=14\text{ cm}$, concreto C30, $c_{nom}=25\text{ mm}$, bitola provisória $\phi=6{,}3\text{ mm}$, $g_k=5{,}00\text{ kN/m}^2$ e $q_k=2{,}00\text{ kN/m}^2$. Adote $\psi_2=0{,}3$, $t_0=1$ mês, $t>70$ meses, $A_s'=0$ e a armadura mínima da laje unidirecional.

1. Calcule $A_{s,min}$, $d$, $p_{qp}$, $M_a$ e $M_r$.
2. Identifique se a seção fissura.
3. Determine $a_i$, $a_t$ e compare com $l/250$.

**Conferência:** $A_{s,min}=2{,}10\text{ cm}^2/\text{m}$, $d=111{,}9\text{ mm}$, $p_{qp}=5{,}60\text{ kN/m}^2$, $M_a=11{,}20\text{ kN m/m}$ e $M_r\approx14{,}19\text{ kN m/m}$. A seção não fissura, $I_{eq}=I_c$, $a_i\approx3{,}04\text{ mm}$ e $a_t\approx7{,}06\text{ mm}<l/250=16{,}0\text{ mm}$.

## Sequência para a memória de cálculo

Para cada laje, registre:

1. identificação, vãos, vínculos, espessura, concreto e cobrimento;
2. $A_{s,min}$ em cada direção e região, além da bitola provisória usada no cálculo de $d$;
3. reação $V_{Sd}$ por borda, $V_{Rd1}$ e $V_{Sd}/V_{Rd1}$;
4. combinação quase permanente, $M_a$, $M_r$, $I_c$, $I_{II}$ e $I_{eq}$;
5. flecha imediata, fator diferido, flecha total e limites aplicáveis;
6. conclusão: mantém a espessura, aumenta a espessura ou aguarda armadura calculada para nova verificação.

Uma tabela-síntese pode seguir o formato:

| Laje | Região ou borda | $A_{s,min}$ | $d$ | $V_{Sd}/V_{Rd1}$ | $M_a/M_r$ | $a_t$ | Limite | Conclusão |
|---|---|---:|---:|---:|---:|---:|---:|---|
| L1 | Borda A |  |  |  |  |  |  |  |

```{admonition} Quando a espessura muda
:class: destaque-verde

Atualize o peso próprio e repita as combinações, os esforços e as reações. A nova geometria também altera $d$, $A_{s,min}$, $V_{Rd1}$, $M_r$, $I_c$, $I_{II}$ e a flecha.
```

## Referências

- ABNT — ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. *NBR 6118: Projeto de estruturas de concreto*. Rio de Janeiro, 2023. Itens 17.3.1, 17.3.2.1 e 19.4.1; Tabelas 13.3, 17.3 e 19.1.
- PEREIRA JUNIOR, Wanderlei Malaquias. *Verificações preliminares do sistema estrutural*. Material do professor, 2021.

