## Entrega 3: Checagens iniciais com armadura mínima

Referência principal: [Aula 06](../aulas/006-verificacoes-preliminares-lajes.md).
Usam-se os esforços da Entrega 2 e a espessura inicial de 12 cm. Uma
verificação que não atenda deve produzir uma providência e o recálculo das
etapas afetadas, antes de se declarar aprovada a laje.

### Propriedades dos materiais

Para C30 e CA-50, com os coeficientes adotados nas aulas:

$$
f_{cd}=\frac{30}{1{,}4}=21{,}43\text{ MPa},
\qquad f_{yd}=\frac{500}{1{,}15}=434{,}78\text{ MPa},
$$

$$
f_{ctm}=0{,}3\times30^{2/3}=2{,}896\text{ MPa},
$$

$$
f_{ctk,inf}=0{,}7f_{ctm}=2{,}028\text{ MPa},
\qquad f_{ctd}=\frac{2{,}028}{1{,}4}=1{,}448\text{ MPa}.
$$

Na hipótese de agregado com $\alpha_E=1{,}0$, usada nos exemplos da Aula 06:

$$
E_{ci}=5600\sqrt{30}=30{,}67\text{ GPa},
\qquad \alpha_i=0{,}8+0{,}2\frac{30}{80}=0{,}875,
$$

$$
E_{cs}=\alpha_iE_{ci}=26{,}84\text{ GPa}.
$$

Registre o agregado adotado; alterar $\alpha_E$ altera a rigidez e as flechas.

### Armadura mínima e altura útil

Para uma faixa de $b_w=1000\text{ mm}$, $h=120\text{ mm}$ e
$\rho_{min}=0{,}00150$:

$$
A_{s,min,+}=0{,}67\rho_{min}b_wh
=120{,}6\text{ mm}^2/\text{m}=1{,}206\text{ cm}^2/\text{m},
$$

$$
A_{s,min,-}=\rho_{min}b_wh
=180{,}0\text{ mm}^2/\text{m}=1{,}800\text{ cm}^2/\text{m}.
$$

Esses valores valem para L1 a L4 enquanto $h=12\text{ cm}$ for mantido.
Com cobrimento de 25 mm e bitola provisória de 6,3 mm na camada externa:

$$
d=120-25-6{,}3/2=91{,}85\text{ mm}.
$$

Se a outra direção ficar imediatamente sobre essa camada, sua altura útil
é $120-25-6{,}3-6{,}3/2=85{,}55\text{ mm}$. A posição da armadura precisa
acompanhar a direção e a face tracionada analisadas.

Por área, $\phi6{,}3$ c/20 fornece $1{,}559\text{ cm}^2/\text{m}$, e
$\phi6{,}3$ c/17 fornece $1{,}834\text{ cm}^2/\text{m}$, atendendo aos mínimos
positivo e negativo, respectivamente. No cálculo preliminar pedido pelo
enunciado, use a área mínima teórica; ao avaliar as barras escolhidas,
identifique a área efetivamente fornecida.

### Cisalhamento em cada borda

Com $\sigma_{cp}=0$ e a armadura tracionada da região verificada:

$$
V_{Rd1}=\tau_{Rd}k(1{,}2+40\rho_1)b_wd,
\quad\tau_{Rd}=0{,}25f_{ctd},
\quad\rho_1=\frac{A_{s1}}{b_wd}\leq0{,}02,
$$

$$
k=\max(1{,}0;1{,}6-d_{[m]}).
$$

Para a camada externa positiva, com $A_{s1}=120{,}6\text{ mm}^2$ na faixa:

$$
\rho_1=0{,}001313,\quad k=1{,}50815,
\quad V_{Rd1}\approx62{,}82\text{ kN}
\quad\text{na faixa de 1 m}.
$$

Compare com a reação de cálculo da mesma borda e da mesma faixa:
$\eta_V=V_{Sd}/V_{Rd1}\leq1$. Nas bordas de continuidade, use a armadura
negativa e a altura útil correspondente. Recalcule a resistência na outra
camada; não replique 62,82 kN em todas as regiões.

### Fissuração na combinação frequente

Para a faixa retangular:

$$
I_c=\frac{1000\times120^3}{12}=144\times10^6\text{ mm}^4,
\qquad y_t=60\text{ mm}.
$$

A Aula 06 usa, na estimativa da rigidez e da flecha:

$$
M_r=1{,}5\frac{f_{ctm}I_c}{y_t}
=10{,}43\text{ kN m}\quad\text{na faixa de 1 m}.
$$

Para verificar a formação de fissuras, registre também a resistência à
tração adotada no critério normativo correspondente. Com $f_{ctk,inf}$ no
mesmo modelo, obtém-se $M_{r,inf}=7{,}30\text{ kN m}$.
Não substitua silenciosamente o critério de formação de fissuras pelo
$M_r$ com $f_{ctm}$ usado em Branson.

Compare os momentos frequentes da Entrega 2 com o limite adotado. Se houver
fissuração, determine a linha neutra no Estádio II, a tensão nas barras e a
abertura característica pelo item 17.3.3 da referência do enunciado:

$$
\alpha_e=\frac{E_s}{E_{cs}},\qquad
\frac{b_wx_{II}^2}{2}=\alpha_eA_s(d-x_{II}),
$$

$$
I_{II}=\frac{b_wx_{II}^3}{3}+\alpha_eA_s(d-x_{II})^2,
\qquad
\sigma_s=\alpha_e\frac{M_{freq}(d-x_{II})}{I_{II}}.
$$

Use $M_{freq}$ em N mm para obter $\sigma_s$ em MPa. A determinação de
$w_k$ exige bitola, espaçamento, área de concreto de envolvimento e condição
de aderência. Compare $w_k$ com $0{,}3\text{ mm}$ para a CAA II adotada no
trabalho; não conclua que a abertura atende apenas porque $M_r$ foi calculado.

### Rigidez equivalente e flecha

Para o caso positivo da camada externa com armadura mínima:

$$
\alpha_e\approx7{,}8246,\quad x_{II}\approx12{,}26\text{ mm},
\quad I_{II}\approx6{,}592\times10^6\text{ mm}^4.
$$

Use o momento $M_a$ da combinação quase permanente e $M_r$ calculado com
$f_{ctm}$:

$$
I_{eq}=\begin{cases}
I_c,&M_a\leq M_r,\\
\left(\dfrac{M_r}{M_a}\right)^3I_c+
\left[1-\left(\dfrac{M_r}{M_a}\right)^3\right]I_{II},&M_a>M_r.
\end{cases}
$$

Determine a flecha imediata por um modelo de **placa com os vínculos da
Entrega 2**, ou por um modelo estrutural equivalente justificado. O fator
$5/384$ da faixa simplesmente apoiada da Aula 06 não é o coeficiente desta
placa com duas bordas contínuas.

Para $t_0=1$ mês, longo prazo e $\rho'=0$:

$$
\xi(1)=0{,}68(0{,}996)^1\approx0{,}6773,
\quad\alpha_f=2-0{,}6773=1{,}3227,
\quad a_t=2{,}3227a_i.
$$

Os limites solicitados no enunciado resultam em:

| Lajes | Menor vão efetivo (mm) | $l/250$ (mm) | $l/350$ (mm) |
|---|---:|---:|---:|
| L1 e L2 | 5022 | 20,088 | 14,349 |
| L3 e L4 | 4772 | 19,088 | 13,634 |

Compare a flecha total com $l/250$ e a parcela da ação variável com
$l/350$, usando os casos de carga correspondentes. A conclusão deve
informar separadamente cisalhamento, fissuração e flecha.

### Erros frequentes nesta entrega

- Aplicar a taxa negativa de 0,15% a toda armadura positiva bidirecional.
- Usar $d$ em milímetros na expressão de $k$ que exige metros.
- Usar a mesma altura útil nas duas camadas sem conferir a sobreposição.
- Usar $p_d$ na flecha ou ignorar a perda de rigidez por fissuração.
- Declarar que a laje atende sem calcular $w_k$ e as flechas aplicáveis.
