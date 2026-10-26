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

Para cada laje e cada combinação:

$$
m_x=\mu_x F,\quad m_y=\mu_y F,\quad
X_x=\mu'_x F,\quad X_y=\mu'_y F,
\qquad F=\frac{pl_x^2}{100}.
$$

Os coeficientes são os do caso de **duas bordas adjacentes engastadas**, nas
[tabelas indicadas na Aula 05](../aulas/005-esforcos-lajes.md).
Não se podem usar os coeficientes do exemplo de quatro bordas apoiadas.
Entre duas linhas do mesmo caso, interpole cada coluna:

$$
\mu=\mu_a+
\frac{\lambda-\lambda_a}{\lambda_b-\lambda_a}(\mu_b-\mu_a).
$$

Com $h=12\text{ cm}$ e as cargas do pavimento-tipo sem paredes sobre a laje:

| Laje | $\lambda$ | $F_d=p_dl_x^2/100$ | $F_{freq}=p_{freq}l_x^2/100$ | $F_{qp}=p_{qp}l_x^2/100$ |
|---|---:|---:|---:|---:|
| L1 | 1,1493 | 2,1803 | 1,3304 | 1,2925 |
| L2 | 1,2190 | 2,1803 | 1,3304 | 1,2925 |
| L3 | 1,2096 | 1,9686 | 1,2012 | 1,1671 |
| L4 | 1,2829 | 1,9686 | 1,2012 | 1,1671 |

Os fatores acima, multiplicados pelo coeficiente da coluna correspondente,
fornecem momentos em $\mathrm{kN\,m/m}$. Por exemplo, a solução de L1 no ELU é

$$
(m_{x,d},m_{y,d},X_{x,d},X_{y,d})
=2{,}1803(\mu_x,\mu_y,\mu'_x,\mu'_y).
$$

O caso corresponde ao **tipo 3 da tabela A-9**. A interpolação resulta em:

| Laje | $\mu_x$ | $\mu'_x$ | $\mu_y$ | $\mu'_y$ |
|---|---:|---:|---:|---:|
| L1 | 3,4170 | 8,2746 | 2,6503 | 7,4982 |
| L2 | 3,7300 | 8,8194 | 2,5972 | 7,6643 |
| L3 | 3,6901 | 8,7550 | 2,6085 | 7,6472 |
| L4 | 3,9916 | 9,2537 | 2,5205 | 7,7792 |

Fonte dos coeficientes: Bastos, tabela A-9, conforme a família de tabelas
adotada na Aula 05; [cópia do material do autor na PUC Goiás](https://professor.pucgoias.edu.br/SiteDocente/admin/arquivosUpload/3922/material/Paulo%20Bastos_Lajes%20de%20Concreto_2015.pdf#page=100).
Consultam-se aqui os coeficientes elásticos; os critérios de dimensionamento
seguem as aulas e a edição normativa adotada no curso.

Antes da compatibilização, os momentos de cálculo são:

| Laje | $m_{x,d}$ | $X_{x,d}$ | $m_{y,d}$ | $X_{y,d}$ |
|---|---:|---:|---:|---:|
| L1 | 7,450 | 18,041 | 5,778 | 16,348 |
| L2 | 8,132 | 19,229 | 5,663 | 16,711 |
| L3 | 7,264 | 17,235 | 5,135 | 15,055 |
| L4 | 7,858 | 18,217 | 4,962 | 15,314 |

Unidades: $\mathrm{kN\,m/m}$. Os valores $X$ são módulos de momentos negativos.
Para a cobertura, substitua $p$ e repita os cálculos.

### Compatibilização dos negativos

Para os módulos $X_1$ e $X_2$ dos dois lados da mesma borda:

$$
X_c=\max\left(\frac{X_1+X_2}{2};\,0{,}8\max(X_1;X_2)\right).
$$

As quatro compatibilizações físicas são:

| Viga e trecho | Par de lajes | Momentos usados |
|---|---|---|
| V2, trecho esquerdo | L1 e L3 | $X_x$ de L1 e de L3 |
| V2, trecho direito | L2 e L4 | $X_x$ de L2 e de L4 |
| V5, trecho superior | L1 e L2 | $X_y$ de L1 e de L2 |
| V5, trecho inferior | L3 e L4 | $X_y$ de L3 e de L4 |

Adota-se $-X_c$ nos dois lados. Para cada positivo cuja borda tenha redução
do módulo negativo:

$$
m^+_{i,c}=m_i^++\frac{\max(0;X_i-X_c)}{2}.
$$

**Exemplo apenas do procedimento:** se uma borda tiver módulos 10 e
6 kN m/m, $X_c=8\text{ kN m/m}$. O positivo do lado com negativo inicial 10
aumenta 1 kN m/m; o outro positivo permanece igual. Esses valores ilustram
a regra da Aula 05 e não substituem os momentos calculados da planta.

Aplicando a regra à planta, os módulos comuns sobre V2 são 17,638 kN m/m
no trecho esquerdo e 18,723 kN m/m no direito. Sobre V5, são 16,529 kN m/m
no trecho superior e 15,185 kN m/m no inferior. Os momentos finais são:

| Laje | $m_{x,d,c}$ | $X_{x,d,c}$ | $m_{y,d,c}$ | $X_{y,d,c}$ |
|---|---:|---:|---:|---:|
| L1 | 7,652 | 17,638 | 5,778 | 16,529 |
| L2 | 8,385 | 18,723 | 5,753 | 16,529 |
| L3 | 7,264 | 17,638 | 5,135 | 15,185 |
| L4 | 7,858 | 18,723 | 5,027 | 15,185 |

Unidades: $\mathrm{kN\,m/m}$. Para as combinações de serviço do mesmo
carregamento uniforme, os momentos compatibilizados escalam pela relação
$p_{freq}/p_d$ ou $p_{qp}/p_d$.

### Reações e áreas de influência

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

### Erros frequentes nesta entrega

- Trocar $X_x$ por $X_y$ ao compatibilizar sobre V2 ou V5.
- Usar $l_y^2$ na expressão de $m_y$ cuja tabela exige $l_x^2$.
- Majorar novamente um momento já obtido com $p_d$.
- Usar momentos de ELU nas verificações de serviço.
- Somar cargas médias, comprimentos e áreas de geometrias diferentes.
