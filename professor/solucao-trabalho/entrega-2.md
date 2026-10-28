## Entrega 2: Esforços nas lajes e descarregamento nas vigas

Referências: [Aula 05](../aulas/005-esforcos-lajes.md),
[Aula 03](../aulas/003-carregamentos.md) e
[Aula 04](../aulas/004-modelos-estruturais.md).

### Modelo de apoio e correspondência das bordas

Para o cálculo manual por painéis, adota-se continuidade sobre V2 e V5 e
apoio simples no contorno externo. É uma hipótese de cálculo a confrontar
com a rigidez dos apoios; os painéis não são quatro lajes simplesmente
apoiadas independentes.

| Laje | Bordas internas com continuidade | Bordas externas apoiadas |
|---|---|---|
| L1 | V2 e V5 | V1 e V4 |
| L2 | V2 e V5 | V1 e V6 |
| L3 | V2 e V5 | V3 e V4 |
| L4 | V2 e V5 | V3 e V6 |

Em cada painel, as duas bordas contínuas são adjacentes. Como $x$ é vertical,
os negativos sobre **V2 são da direção $x$**; sobre **V5, da direção $y$**.
Selecione na tabela de Bares/Pinheiro o caso cujo desenho corresponde a
esses vínculos, girando ou espelhando o croqui sem perder os eixos.

### Solução dos momentos por coeficientes

Os momentos de cada laje saem da solução de placa da disciplina, com
$\nu=0{,}20$, reunida nas [tabelas de Bares](../disciplina/000-tabelas-bares.md).
Para cada ação de carga uniforme $p$ (neste caso, $g_k$, $q_k$ ou $p_d$),

$$
m_x=\mu_x F,\quad m_y=\mu_y F,\quad
m'_x=\mu'_x F,\quad m'_y=\mu'_y F,
\qquad F=\frac{pl_x^2}{100}.
$$

Os coeficientes são os do caso de **duas bordas adjacentes engastadas**, o
**tipo 3** da [Aula 05](../aulas/005-esforcos-lajes.md), com o desenho
espelhado conforme a posição de cada laje. Não se podem usar os coeficientes
do exemplo de quatro bordas apoiadas. A [Tabela 13](#tabela-e2-coef) traz os
coeficientes de cada laje, **interpolados linearmente** entre as duas linhas de
$\lambda$ vizinhas da tabela (passo de 0,05), com os vãos efetivos da
[Tabela 7](#tabela-vaos),

$$
\mu=\mu_a+
\frac{\lambda-\lambda_a}{\lambda_b-\lambda_a}(\mu_b-\mu_a).
$$

Por exemplo, em L1 ($\lambda=5{,}922/5{,}172=1{,}1450$), entre as linhas
$\lambda_a=1{,}10$ e $\lambda_b=1{,}15$, o coeficiente $\mu_x$ resulta em

$$
\mu_x=3{,}5979+\frac{1{,}1450-1{,}10}{1{,}15-1{,}10}(3{,}8569-3{,}5979)=3{,}831.
$$

(tabela-e2-coef)=
**Tabela 13.** Coeficientes do tipo 3 interpolados para cada laje.

| Laje | $\lambda$ | Linhas usadas | $\mu_x$ | $\mu_y$ | $\mu'_x$ | $\mu'_y$ | $k_x$ | $k'_x$ | $k_y$ | $k'_y$ | $\alpha_w$ |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| L1 | 1,1450 | 1,10 e 1,15 | 3,8310 | 3,0411 | 8,2076 | 7,4636 | 2,1014 | 3,7174 | 1,9213 | 3,4668 | 3,2453 |
| L2 | 1,2127 | 1,20 e 1,25 | 4,1628 | 2,9993 | 8,7231 | 7,6308 | 2,1881 | 3,8548 | 1,9285 | 3,4930 | 3,5481 |
| L3 | 1,2032 | 1,20 e 1,25 | 4,1184 | 3,0067 | 8,6550 | 7,6109 | 2,1766 | 3,8367 | 1,9278 | 3,4900 | 3,5074 |
| L4 | 1,2743 | 1,25 e 1,30 | 4,4441 | 2,9479 | 9,1509 | 7,7511 | 2,2609 | 3,9694 | 1,9325 | 3,5109 | 3,8061 |

O eixo $x$ é vertical na planta. Assim, os negativos sobre **V2 são da direção
$x$** ($m'_x$) e os de **V5, da direção $y$** ($m'_y$). Em todas as lajes as duas
bordas contínuas (V2 e V5) são adjacentes e as demais bordas são apoiadas,
como nas hipóteses do modelo de apoio.

### Esforços devidos a $g_k$

Com as cargas permanentes da [Tabela 11](#tabela-cargas-lajes) (8,774 kN/m² em
L1 e 4,150 kN/m² nas demais lajes dos pavimentos-tipo e 6,690 kN/m² na
cobertura), a [Tabela 14](#tabela-e2-mom-g) apresenta os momentos
característicos, ainda sem compatibilização.

(tabela-e2-mom-g)=
**Tabela 14.** Momentos devidos a $g_k$ (kN m/m), antes da compatibilização.

| Pavimento | Laje | $p$ (kN/m²) | $F=pl_x^2/100$ | $m_x$ | $m_y$ | $m'_x$ | $m'_y$ |
|---|---|---:|---:|---:|---:|---:|---:|
| Tipo | L1 | 8,774 | 2,3470 | 8,991 | 7,137 | 19,263 | 17,517 |
| Tipo | L2 | 4,150 | 1,1101 | 4,621 | 3,330 | 9,684 | 8,471 |
| Tipo | L3 | 4,150 | 1,0054 | 4,141 | 3,023 | 8,702 | 7,652 |
| Tipo | L4 | 4,150 | 1,0054 | 4,468 | 2,964 | 9,200 | 7,793 |
| Cobertura | L1 | 6,690 | 1,7895 | 6,856 | 5,442 | 14,688 | 13,356 |
| Cobertura | L2 | 6,690 | 1,7895 | 7,450 | 5,367 | 15,610 | 13,656 |
| Cobertura | L3 | 6,690 | 1,6207 | 6,675 | 4,873 | 14,027 | 12,335 |
| Cobertura | L4 | 6,690 | 1,6207 | 7,203 | 4,778 | 14,831 | 12,562 |

### Esforços devidos a $q_k$

As sobrecargas são 1,50 kN/m² nos pavimentos-tipo e 0,50 kN/m² na cobertura
([Tabela 11](#tabela-cargas-lajes)). Como $q_k$ é uniforme e igual nas quatro
lajes de cada pavimento, os momentos diferem apenas pelos coeficientes e por
$l_x^2$. A [Tabela 15](#tabela-e2-mom-q) reúne os resultados.

(tabela-e2-mom-q)=
**Tabela 15.** Momentos devidos a $q_k$ (kN m/m), antes da compatibilização.

| Pavimento | Laje | $p$ (kN/m²) | $F=pl_x^2/100$ | $m_x$ | $m_y$ | $m'_x$ | $m'_y$ |
|---|---|---:|---:|---:|---:|---:|---:|
| Tipo | L1 | 1,500 | 0,4012 | 1,537 | 1,220 | 3,293 | 2,995 |
| Tipo | L2 | 1,500 | 0,4012 | 1,670 | 1,203 | 3,500 | 3,062 |
| Tipo | L3 | 1,500 | 0,3634 | 1,497 | 1,093 | 3,145 | 2,766 |
| Tipo | L4 | 1,500 | 0,3634 | 1,615 | 1,071 | 3,325 | 2,817 |
| Cobertura | L1 | 0,500 | 0,1337 | 0,512 | 0,407 | 1,098 | 0,998 |
| Cobertura | L2 | 0,500 | 0,1337 | 0,557 | 0,401 | 1,167 | 1,021 |
| Cobertura | L3 | 0,500 | 0,1211 | 0,499 | 0,364 | 1,048 | 0,922 |
| Cobertura | L4 | 0,500 | 0,1211 | 0,538 | 0,357 | 1,108 | 0,939 |

### Reações de apoio das lajes

As reações médias por borda saem dos coeficientes $k$ da
[Tabela 13](#tabela-e2-coef), com

$$
r=k\frac{p\,l_x}{10}\quad(\mathrm{kN/m}).
$$

Os coeficientes $k_x$ e $k_y$ valem para as bordas apoiadas (de comprimento
$l_y$ e $l_x$) e $k'_x$ e $k'_y$ para as engastadas. Nas lajes desta planta, as
bordas correspondem às vigas assim

| Laje | $k_x$ (apoiada, comprimento $l_y$) | $k'_x$ (engastada, comprimento $l_y$) | $k_y$ (apoiada, comprimento $l_x$) | $k'_y$ (engastada, comprimento $l_x$) |
|---|---|---|---|---|
| L1 | V1 | V2 | V4 | V5 |
| L2 | V1 | V2 | V6 | V5 |
| L3 | V3 | V2 | V4 | V5 |
| L4 | V3 | V2 | V6 | V5 |

A [Tabela 16](#tabela-e2-reacoes) apresenta as reações características devidas a
$g_k$ e a $q_k$. Elas são reações efetivas de placa, que já incluem o efeito do
momento volvente ao longo da borda. Por isso, a soma das quatro reações
multiplicadas pelos comprimentos das bordas supera a carga total $pA$ da laje. A
diferença é compensada pelas forças concentradas de canto, de sentido oposto,
nos cantos entre bordas apoiadas, que não constam da tabela.

(tabela-e2-reacoes)=
**Tabela 16.** Reações médias de apoio devidas a $g_k$ e a $q_k$ (kN/m).

| Pavimento | Laje | $g_k$: $r_x$ | $g_k$: $r'_x$ | $g_k$: $r_y$ | $g_k$: $r'_y$ | $q_k$: $r_x$ | $q_k$: $r'_x$ | $q_k$: $r_y$ | $q_k$: $r'_y$ |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Tipo | L1 | 9,54 | 16,87 | 8,72 | 15,73 | 1,63 | 2,88 | 1,49 | 2,69 |
| Tipo | L2 | 4,70 | 8,27 | 4,14 | 7,50 | 1,70 | 2,99 | 1,50 | 2,71 |
| Tipo | L3 | 4,45 | 7,84 | 3,94 | 7,13 | 1,61 | 2,83 | 1,42 | 2,58 |
| Tipo | L4 | 4,62 | 8,11 | 3,95 | 7,17 | 1,67 | 2,93 | 1,43 | 2,59 |
| Cobertura | L1 | 7,27 | 12,86 | 6,65 | 12,00 | 0,54 | 0,96 | 0,50 | 0,90 |
| Cobertura | L2 | 7,57 | 13,34 | 6,67 | 12,09 | 0,57 | 1,00 | 0,50 | 0,90 |
| Cobertura | L3 | 7,17 | 12,63 | 6,35 | 11,49 | 0,54 | 0,94 | 0,47 | 0,86 |
| Cobertura | L4 | 7,44 | 13,07 | 6,36 | 11,56 | 0,56 | 0,98 | 0,48 | 0,86 |

### Flecha elástica das lajes

A flecha máxima de placa homogênea e não fissurada, com a mesma tabela de Bares, é

$$
w=\alpha_w\frac{p\,l_x^4}{100\,E_{cs}h^3},
$$

com $E_{cs}=26{,}84\text{ GPa}=26{,}84\times10^6\text{ kN/m}^2$ (C30, como na
[Aula 06](../aulas/006-verificacoes-preliminares-lajes.md)) e $h=0{,}12\text{ m}$.
A [Tabela 17](#tabela-e2-flecha) traz as parcelas imediatas de $g_k$ e de $q_k$
em milímetros. São flechas elásticas com a seção bruta. Os efeitos da fissuração e
da deformação diferida entram na verificação de serviço, na Entrega 3.

(tabela-e2-flecha)=
**Tabela 17.** Flechas elásticas imediatas (mm).

| Pavimento | Laje | $\alpha_w$ | $w_g$ | $w_q$ | $w_g+w_q$ |
|---|---|---:|---:|---:|---:|
| Tipo | L1 | 3,2453 | 4,39 | 0,75 | 5,14 |
| Tipo | L2 | 3,5481 | 2,27 | 0,82 | 3,09 |
| Tipo | L3 | 3,5074 | 1,84 | 0,67 | 2,51 |
| Tipo | L4 | 3,8061 | 2,00 | 0,72 | 2,72 |
| Cobertura | L1 | 3,2453 | 3,35 | 0,25 | 3,60 |
| Cobertura | L2 | 3,5481 | 3,66 | 0,27 | 3,94 |
| Cobertura | L3 | 3,5074 | 2,97 | 0,22 | 3,19 |
| Cobertura | L4 | 3,8061 | 3,22 | 0,24 | 3,46 |

### Momentos de cálculo antes da compatibilização

No ELU, $p_d=1{,}4(g_k+q_k)$. Como os coeficientes são os mesmos, os momentos
de cálculo valem 1,4 vez a soma da [Tabela 14](#tabela-e2-mom-g) com a
[Tabela 15](#tabela-e2-mom-q). A [Tabela 18](#tabela-e2-mom-d) apresenta os
resultados.

(tabela-e2-mom-d)=
**Tabela 18.** Momentos de cálculo antes da compatibilização (kN m/m).

| Pavimento | Laje | $p_d$ (kN/m²) | $m_{x,d}$ | $m'_{x,d}$ | $m_{y,d}$ | $m'_{y,d}$ |
|---|---|---:|---:|---:|---:|---:|
| Tipo | L1 | 14,384 | 14,740 | 31,579 | 11,701 | 28,717 |
| Tipo | L2 | 7,910 | 8,808 | 18,457 | 6,346 | 16,146 |
| Tipo | L3 | 7,910 | 7,892 | 16,585 | 5,762 | 14,585 |
| Tipo | L4 | 7,910 | 8,516 | 17,536 | 5,649 | 14,853 |
| Cobertura | L1 | 10,066 | 10,315 | 22,100 | 8,189 | 20,097 |
| Cobertura | L2 | 10,066 | 11,209 | 23,488 | 8,076 | 20,547 |
| Cobertura | L3 | 10,066 | 10,043 | 21,106 | 7,332 | 18,560 |
| Cobertura | L4 | 10,066 | 10,837 | 22,315 | 7,189 | 18,902 |

### Compatibilização dos negativos

Para os módulos $m'_1$ e $m'_2$ dos dois lados da mesma borda,

$$
m'_c=\max\left(\frac{m'_1+m'_2}{2};\,0{,}8\max(m'_1;m'_2)\right).
$$

As quatro compatibilizações físicas são

| Viga e trecho | Par de lajes | Momentos usados |
|---|---|---|
| V2, trecho esquerdo | L1 e L3 | $m'_x$ de L1 e de L3 |
| V2, trecho direito | L2 e L4 | $m'_x$ de L2 e de L4 |
| V5, trecho superior | L1 e L2 | $m'_y$ de L1 e de L2 |
| V5, trecho inferior | L3 e L4 | $m'_y$ de L3 e de L4 |

Adota-se $-m'_c$ nos dois lados. Para cada positivo cuja borda tenha redução
do módulo negativo,

$$
m^+_{i,c}=m_i^++\frac{\max(0;m'_i-m'_c)}{2}.
$$

**Exemplo apenas do procedimento.** Se uma borda tiver módulos 10 e
6 kN m/m, $m'_c=8\text{ kN m/m}$. O positivo do lado com negativo inicial 10
aumenta 1 kN m/m e o outro positivo permanece igual. Esses valores ilustram
a regra da [Aula 05](../aulas/005-esforcos-lajes.md) e não substituem os momentos calculados da planta.

Aplicando a regra aos valores da [Tabela 18](#tabela-e2-mom-d), os módulos comuns
$m'_c$ resultam na [Tabela 19](#tabela-e2-mc).

(tabela-e2-mc)=
**Tabela 19.** Momentos negativos comuns $m'_c$ (kN m/m).

| Pavimento | V2, trecho esquerdo | V2, trecho direito | V5, trecho superior | V5, trecho inferior |
|---|---:|---:|---:|---:|
| Tipo | 25,263 | 17,996 | 22,973 | 14,719 |
| Cobertura | 21,603 | 22,902 | 20,322 | 18,731 |

Os momentos finais compatibilizados estão na [Tabela 20](#tabela-e2-mom-dc).

(tabela-e2-mom-dc)=
**Tabela 20.** Momentos de cálculo compatibilizados (kN m/m).

| Pavimento | Laje | $m_{x,d,c}$ | $m'_{x,d,c}$ | $m_{y,d,c}$ | $m'_{y,d,c}$ |
|---|---|---:|---:|---:|---:|
| Tipo | L1 | 17,898 | 25,263 | 14,572 | 22,973 |
| Tipo | L2 | 9,038 | 17,996 | 6,346 | 22,973 |
| Tipo | L3 | 7,892 | 25,263 | 5,762 | 14,719 |
| Tipo | L4 | 8,516 | 17,996 | 5,716 | 14,719 |
| Cobertura | L1 | 10,564 | 21,603 | 8,189 | 20,322 |
| Cobertura | L2 | 11,502 | 22,902 | 8,188 | 20,322 |
| Cobertura | L3 | 10,043 | 21,603 | 7,332 | 18,731 |
| Cobertura | L4 | 10,837 | 22,902 | 7,274 | 18,731 |

Para as combinações de serviço, os momentos de cada ação podem ser tomados
da [Tabela 14](#tabela-e2-mom-g) e da [Tabela 15](#tabela-e2-mom-q) e combinados
com os fatores da combinação. A compatibilização de serviço será feita sobre a
combinação correspondente.

### Resumo dos esforços e deslocamentos das lajes

A [Tabela 21](#tabela-e2-resumo) reúne, para cada laje, os momentos de cálculo
compatibilizados, as reações de cálculo $r_d=1{,}4(r_{g}+r_{q})$ sobre cada viga
de apoio e a flecha elástica imediata total. As reações vêm da
[Tabela 16](#tabela-e2-reacoes) e não foram compatibilizadas.

(tabela-e2-resumo)=
**Tabela 21.** Resumo dos esforços das lajes.

| Pavimento | Laje | $m_{x,d,c}$ | $m'_{x,d,c}$ | $m_{y,d,c}$ | $m'_{y,d,c}$ | Reações $r_d$ (kN/m) | $w_g+w_q$ (mm) |
|---|---|---:|---:|---:|---:|---|---:|
| Tipo | L1 | 17,90 | 25,26 | 14,57 | 22,97 | V1 15,6, V2 27,7, V4 14,3, V5 25,8 | 5,14 |
| Tipo | L2 | 9,04 | 18,00 | 6,35 | 22,97 | V1 9,0, V2 15,8, V6 7,9, V5 14,3 | 3,09 |
| Tipo | L3 | 7,89 | 25,26 | 5,76 | 14,72 | V3 8,5, V2 14,9, V4 7,5, V5 13,6 | 2,51 |
| Tipo | L4 | 8,52 | 18,00 | 5,72 | 14,72 | V3 8,8, V2 15,5, V6 7,5, V5 13,7 | 2,72 |
| Cobertura | L1 | 10,56 | 21,60 | 8,19 | 20,32 | V1 10,9, V2 19,4, V4 10,0, V5 18,0 | 3,60 |
| Cobertura | L2 | 11,50 | 22,90 | 8,19 | 20,32 | V1 11,4, V2 20,1, V6 10,0, V5 18,2 | 3,94 |
| Cobertura | L3 | 10,04 | 21,60 | 7,33 | 18,73 | V3 10,8, V2 19,0, V4 9,6, V5 17,3 | 3,19 |
| Cobertura | L4 | 10,84 | 22,90 | 7,27 | 18,73 | V3 11,2, V2 19,7, V6 9,6, V5 17,4 | 3,46 |

Momentos em kN m/m, reações em kN/m e flechas em mm. Os valores $m'$ são
módulos de momentos negativos.

### Reações e áreas de influência

As reações médias da [Tabela 16](#tabela-e2-reacoes) servem de estimativa inicial
para o carregamento das vigas. Para a distribuição ao longo de cada borda, siga
o roteiro das charneiras e confronte as resultantes com aquela tabela.

Desenhe as charneiras em cada painel: 45° entre apoios de mesmo tipo e 60°
a partir do engastado no encontro com um apoio simples, conforme o roteiro
do enunciado. Determine os polígonos de influência de cada borda.
No modelo de carga média equivalente:

$$
R_{i,j}=p_i A_{i,j},\qquad
r_{i,j}=\frac{R_{i,j}}{L_{borda,j}}.
$$

$R_{i,j}$ está em kN e $r_{i,j}$, em kN/m. Use área e comprimento referentes
à mesma geometria. Confira $\sum_jA_{i,j}=A_i$ e $\sum_jR_{i,j}=p_iA_i$.
Uma carga média conserva a resultante; a forma triangular ou trapezoidal
original deve ser preservada quando for relevante para os esforços da viga.

### Carregamento e solução das vigas

Para cada trecho de V1 a V6:

$$
w_k=\sum_i r_{k,i}+g_{viga}+g_{parede,lin}.
$$

Se a carga das lajes já inclui seu peso próprio na faixa da viga, conte
somente a parcela adicional abaixo da laje:

$$
g_{viga}=25\times0{,}15(h_v-h).
$$

Caso o modelo use áreas de lajes livres, excluindo integralmente a faixa
das vigas, contabilize a seção completa da viga, com a geometria coerente.
Acrescente as cargas concentradas de outras vigas, quando existirem.

V1, V2 e V3 têm tramos horizontais entre eixos de 6,00 m e 6,35 m; V4, V5 e
V6 têm tramos verticais de 5,25 m e 5,00 m. A posição dos pilares, as
seções e a rigidez das ligações definem o modelo de análise da Aula 04.
Não aplique $wl^2/8$ a todos os tramos de uma viga contínua.

Para conferir diagramas e reações, use $dV/ds=-w(s)$ e $dM/ds=V(s)$ com a
convenção de sinais do modelo, além de equilíbrio global de forças e momentos.
Registre nas plantas as cargas de cada laje, os momentos compatibilizados
e as reações nos pilares.
