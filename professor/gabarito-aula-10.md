# Gabarito do professor: Aula 09 (detalhamento de lajes maciças)

Material **somente do professor**. Fica fora de `source/` e não é publicado.

## Pontos a conferir

1. **Armadura negativa de borda.** As fotos (Carvalho e Figueiredo Filho, item 7.4.11.6) dizem que a recomendação não foi mantida na versão final da NBR 6118:2023. A aula adota $\rho_s\geq0{,}67\rho_{min}$ (valor da Tabela 19.1 da edição de 2014) e extensão de $0{,}15\,l_x$ a partir da face do apoio, que é a prática usual que conheço, mas **não está nas fotos**. Confirme ou troque o critério no quadro vermelho da aula (por exemplo, $0{,}25\,l_x$, mais conservador).
2. **Fórmula de $a_1$.** O texto da apostila da EESC-USP diz "com $a_1$ igual ao menor valor entre", mas a expressão traz "$\geq$" e "em geral, maior valor". A aula usa o maior dos dois valores, coerente com o diagrama (a barra precisa cobrir a base do trapézio mais $10\phi$ e ter $\ell_b$ além do ponto de tensão máxima).
3. **Barras inferiores alternadas** ($0{,}85l$ e $0{,}70l$): transcritas da Figura 8 da apostila; a aula as apresenta só como opção.
4. **Malha de canto inferior.** Na Figura 9 da apostila, a malha que substitui a armadura inferior de canto está indicada como "$2a_{sc}$". A aula descreve a substituição sem fixar esse valor; no exemplo, a malha positiva atende mesmo na interpretação mais exigente.
5. **Momentos do exemplo.** São dados do enunciado (ordem de grandeza obtida com $p_d\approx9{,}1\ \text{kN/m}^2$ e coeficientes de tabela como na Aula 05), não um resultado a conferir.
6. As áreas de aço usam o procedimento simplificado da Aula 07 ($\varphi_{adot}=\min(\varphi;0{,}931)$). Se a outra versão da Aula 07 mudar esse procedimento, as áreas do exemplo mudam um pouco (menos de $5\%$), sem alterar as bitolas adotadas.

## Exercício 1: completar o exemplo

**Negativas de borda.** $A_s\geq0{,}67\cdot0{,}150\%\cdot100\cdot12=1{,}21\ \text{cm}^2/\text{m}$: $\phi6{,}3$ c/20 ($1{,}56$).

| Borda | Laje | Extensão $0{,}15l_x$ | Reto ($11{,}5+$ext., arred.) | $C$ com ganchos de 7 cm | Distribuição | Quantidade |
|---|---|---:|---:|---:|---|---:|
| V1 | L1 | 60 | 75 | 89 | 486 cm | 25 |
| V4 e V5 | L1 | 60 | 75 | 89 | 386 cm (cada) | 20 + 20 |
| V3 | L2 | 54 | 70 | 84 | 486 cm | 25 |
| V4 e V5 | L2 | 54 | 70 | 84 | 346 cm (cada) | 18 + 18 |

Comprimento total: L1, $65\cdot0{,}89=57{,}85$ m; L2, $61\cdot0{,}84=51{,}24$ m; soma $109{,}1$ m de $\phi6{,}3$.

**Cantos.** Os quatro cantos externos (V1-V4, V1-V5, V3-V4, V3-V5) têm duas bordas simplesmente apoiadas.

- L1: $a_{sc}\geq2{,}08/2=1{,}04\ \text{cm}^2/\text{m}$, região de $l_x/5=80$ cm.
- L2: $a_{sc}\geq1{,}64/2=0{,}82\ \text{cm}^2/\text{m}$, região de $72$ cm ($75$ cm).
- Superior: a malha das negativas de borda tem $1{,}56\ \text{cm}^2/\text{m}$ em cada direção (atende à área), mas só se estende $60$ cm (L1) e $54$ cm (L2), menos que $l_x/5$. Solução: nas faixas de $80$ cm (L1) e $75$ cm (L2) junto aos cantos, alongar as barras de borda para $11{,}5+80\to95$ cm retos ($C=109$ cm) em L1 e $11{,}5+72\to85$ cm ($C=99$ cm) em L2; são 4 barras por borda em cada canto. Acréscimo: L1, $2\cdot8\cdot0{,}20=3{,}2$ m; L2, $2\cdot8\cdot0{,}15=2{,}4$ m.
- Inferior: a malha positiva (L1: $2{,}08$ e $1{,}56$; L2: $1{,}64$ e $1{,}56\ \text{cm}^2/\text{m}$) já atende, em cada direção, a $a_{sc}$ (e também a $2a_{sc}$ na soma), em toda a laje.

**Tabela atualizada.** $\phi6{,}3$: $460{,}85+109{,}1+5{,}6=575{,}5$ m, $141{,}0$ kg; $\phi8$: $28{,}4$ kg. Total $\approx169{,}4$ kg ($+28$ kg, cerca de $20\%$).

## Exercício 2: laje armada em uma direção

$\lambda=7{,}50/3{,}00=2{,}5>2$: **armada em uma direção**.

| Opção | $d$ (cm) | $A_{s,calc}$ | $s_{max}$ pela área | Limite $\min(20;2h=20)$ | Adotado | $A_{s,ef}$ |
|---|---:|---:|---:|---:|---|---:|
| $\phi6{,}3$ | 7,19 | 2,06 | 15,1 | 20 | c/15 | 2,08 |
| $\phi8$ | 7,10 | 2,09 | 24,1 | 20 | c/20 | 2,52 |

$A_{s,min}=0{,}150\%\cdot100\cdot10=1{,}50\ \text{cm}^2/\text{m}$ (principal de laje unidirecional): atendida. Melhor: $\phi6{,}3$ c/15 (menos aço).

Distribuição: $\max(0{,}2\cdot2{,}08=0{,}42;\ 0{,}9;\ 0{,}5\cdot1{,}50=0{,}75)=0{,}90\ \text{cm}^2/\text{m}$: $\phi5{,}0$ c/20 ($0{,}98$) ou $\phi6{,}3$ c/33 ($0{,}94$); $s\leq33$ cm.

Comprimentos e quantidades: principal $C=286+23=309\to305$ cm, $\lceil736/15\rceil=50$ barras; distribuição $C=736+23=759\to755$ cm, $\lceil286/20\rceil=15$ barras ($\phi5{,}0$ c/20) ou $\lceil286/33\rceil=9$ ($\phi6{,}3$ c/33).

Item 4: o critério de $20\%$ da principal governa quando a principal passa de $4{,}5\ \text{cm}^2/\text{m}$; o de $0{,}5\rho_{min}$, quando $0{,}5\rho_{min}bh>0{,}9$ (lajes mais espessas, $h>12$ cm para $\rho_{min}=0{,}150\%$).
