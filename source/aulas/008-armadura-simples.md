# Aula 08: Dimensionamento de seções retangulares com armadura simples

Na [Aula 07](007-verificacoes-preliminares-lajes.md), a armadura mínima permitiu avaliar preliminarmente as lajes. Agora vamos determinar a armadura longitudinal necessária para resistir ao momento fletor de cálculo. O mesmo equilíbrio de uma seção retangular serve para uma viga e para uma faixa de laje, desde que a largura e as unidades sejam coerentes.

Esta aula sintetiza o capítulo 4, *Dimensionamento de seções retangulares com armadura simples*, do material fornecido pelo professor. A dedução concentra-se nas equações gerais. Os limites entre domínios, as expressões de verificação e as disposições construtivas aparecem em sua forma final. As referências normativas correspondem à NBR 6118:2023, versão corrigida de 2024, adotada no capítulo.

```{admonition} Objetivos da aula
:class: destaque-azul

- Relacionar deformações, tensões e forças internas no estado-limite último.
- Deduzir as expressões da linha neutra e da área de aço pelo equilíbrio da seção.
- Distinguir domínio de deformação e limite de ductilidade.
- Dimensionar a armadura simples de uma viga e de uma faixa de laje.
- Conferir a armadura mínima e a altura útil antes de escolher as barras.
```

## O que significa armadura simples?

No modelo resistente, o concreto equilibra a compressão e a armadura longitudinal equilibra a tração. Não se conta com armadura comprimida para resistir ao momento solicitante. Uma viga pode possuir barras construtivas na face comprimida e, ainda assim, ser dimensionada como seção com armadura simples.

Consideramos flexão sem força normal, $N_d=0$. O dimensionamento à flexão também se aplica quando existe cortante, mas a verificação desse esforço constitui uma etapa própria. Seções T, armadura dupla e flexocompressão exigem outros equacionamentos.

Para momento positivo, a armadura principal fica usualmente na face inferior. Para momento negativo, invertem-se as faces tracionada e comprimida. Nos cálculos seguintes, $M_d$ representa o **módulo do momento de cálculo** e as distâncias partem da face comprimida.

| Símbolo | Significado |
|---|---|
| $b_w$, $h$ | Largura e altura total da seção retangular |
| $d$ | Distância da face comprimida ao centro de gravidade da armadura tracionada |
| $x$ | Profundidade da linha neutra, indicada por $X$ no desenho do capítulo |
| $A_s$ | Área da armadura longitudinal tracionada |
| $R_{cd}$, $R_{sd}$ | Resultantes de compressão no concreto e de tração no aço |
| $z$ | Braço de alavanca entre as resultantes, indicado por $Z$ no desenho |
| $\xi=x/d$ | Profundidade relativa da linha neutra |
| $\varphi=z/d$ | Braço de alavanca adimensional, distinto da bitola $\phi$ |
| $\mu=M_d/(b_wd^2f_{cd})$ | Momento fletor adimensional |

Usaremos N, mm e MPa nas substituições: $1\text{ MPa}=1\text{ N/mm}^2$, $1\text{ kN m}=10^6\text{ N mm}$ e $1\text{ cm}^2=100\text{ mm}^2$.

## Modelo da seção no ELU

As hipóteses empregadas são: seções planas permanecem planas, aderência perfeita entre os materiais, resistência à tração do concreto desprezada no ELU e tensões dos materiais obtidas de seus diagramas de cálculo. Essas hipóteses permitem representar a seção por um diagrama linear de deformações e por duas resultantes de forças.

```{figure} ../_static/aulas/armadura-simples/secao-elu.png
:alt: Seção retangular com armadura tracionada, diagrama linear de deformações e bloco retangular de compressão equilibrado pela força no aço
:width: 100%
:align: center

Seção, deformações e resultantes no domínio 3. Fonte: capítulo 4 fornecido pelo professor, Figura 4.9. A linha neutra fica a uma distância $x$ da face comprimida; o bloco equivalente tem altura $\lambda x$.
```

As resistências de cálculo são

$$
f_{cd}=\frac{f_{ck}}{\gamma_c},\qquad
f_{yd}=\frac{f_{yk}}{\gamma_s},\qquad
\varepsilon_{yd}=\frac{f_{yd}}{E_s}.
$$

Nos exemplos, adotaremos $\gamma_c=1{,}4$, $\gamma_s=1{,}15$ e $E_s=210000\text{ MPa}$. Para o aço CA-50, $f_{yd}=434{,}78\text{ MPa}$ e $\varepsilon_{yd}=2{,}070\text{‰}$. Os momentos dos exemplos já são de cálculo e não recebem nova majoração.

### Bloco retangular equivalente

Na seção de largura constante, o capítulo representa a compressão por um bloco de altura $\lambda x$ e tensão uniforme $\alpha_c\eta_cf_{cd}$. Os coeficientes finais são:

$$
\lambda=\begin{cases}
0{,}8,& f_{ck}\leq50\text{ MPa},\\
0{,}8-\dfrac{f_{ck}-50}{400},&50<f_{ck}\leq90\text{ MPa},
\end{cases}
$$

$$
\alpha_c=\begin{cases}
0{,}85,&f_{ck}\leq50\text{ MPa},\\
0{,}85\left[1-\dfrac{f_{ck}-50}{200}\right],&50<f_{ck}\leq90\text{ MPa},
\end{cases}
$$

$$
\eta_c=\begin{cases}
1,&f_{ck}\leq40\text{ MPa},\\
\left(\dfrac{40}{f_{ck}}\right)^{1/3},&40<f_{ck}\leq90\text{ MPa}.
\end{cases}
$$

Inserir $f_{ck}$ em MPa. Em C45 e C50, $\lambda$ e $\alpha_c$ mantêm os valores usuais, mas $\eta_c$ já é menor que 1. Portanto, a forma numérica simplificada para C20 a C40 não deve ser estendida automaticamente até C50.

## Dedução das equações gerais

### Compatibilidade de deformações

Pela semelhança de triângulos no diagrama linear, usando os módulos das deformações,

$$
\frac{\varepsilon_c}{x}=\frac{\varepsilon_s}{d-x}.
$$

Dividindo as distâncias por $d$ e isolando as variáveis:

$$
\boxed{\xi=\frac{\varepsilon_c}{\varepsilon_c+\varepsilon_s}},
\qquad
\boxed{\varepsilon_s=\varepsilon_c\frac{1-\xi}{\xi}}.
$$

No domínio 3, $\varepsilon_c=\varepsilon_{cu}$ e o aço tracionado já escoou. No domínio 2, a deformação do aço alcança o limite convencional de $10\text{‰}$ antes de o concreto alcançar $\varepsilon_{cu}$.

### Equilíbrio das forças e braço de alavanca

A resultante de compressão é a tensão do bloco multiplicada por sua área:

$$
R_{cd}=\alpha_c\eta_cf_{cd}\,b_w\lambda x.
$$

Como a tensão é uniforme, a resultante atua no centro do bloco, a $\lambda x/2$ da face comprimida. Logo,

$$
z=d-\frac{\lambda x}{2}
=d\left(1-\frac{\lambda\xi}{2}\right),
\qquad
\boxed{\varphi=1-\frac{\lambda\xi}{2}}.
$$

Na ausência de força normal externa, as forças internas devem se equilibrar:

$$
R_{cd}=R_{sd}=A_s\sigma_{sd}.
$$

### Equilíbrio de momentos e posição da linha neutra

Tomando momentos em relação ao centro da armadura tracionada,

$$
M_d=R_{cd}z
=\alpha_c\eta_cf_{cd}b_w\lambda x
\left(d-\frac{\lambda x}{2}\right).
$$

Substituindo $x=\xi d$ e dividindo por $b_wd^2f_{cd}$,

$$
\mu=\alpha_c\eta_c\lambda\xi
\left(1-\frac{\lambda\xi}{2}\right).
$$

A reorganização dessa expressão fornece uma equação do segundo grau:

$$
\frac{\lambda^2}{2}\xi^2-\lambda\xi
+\frac{\mu}{\alpha_c\eta_c}=0.
$$

Escolhendo a menor raiz, compatível com a região comprimida da seção em flexão,

$$
\boxed{\xi=\frac{1}{\lambda}
\left(1-\sqrt{1-\frac{2\mu}{\alpha_c\eta_c}}\right)}.
$$

A existência de uma raiz real não basta para aprovar a seção: ainda é necessário verificar o domínio e a ductilidade.

### Área da armadura tracionada

Tomando momentos em relação à resultante de compressão,

$$
M_d=R_{sd}z=A_s\sigma_{sd}\varphi d.
$$

Portanto,

$$
\boxed{A_s=\frac{M_d}{\sigma_{sd}\varphi d}}.
$$

Quando o aço escoa, $\sigma_{sd}=f_{yd}$. No domínio 3, as expressões do bloco equivalente conduzem às duas formas equivalentes:

$$
\boxed{A_s=\frac{M_d}{f_{yd}\varphi d}
=\frac{\alpha_c\eta_cf_{cd}b_w\lambda\xi d}{f_{yd}}}.
$$

A primeira usa o equilíbrio de momentos; a segunda, o equilíbrio de forças. Ambas devem fornecer o mesmo resultado para o mesmo modelo.

## Domínios e ductilidade: expressões finais

As fronteiras obtidas pela compatibilidade são

$$
\xi_{2a/2b}=\frac{\varepsilon_{c2}}{\varepsilon_{c2}+0{,}010},\qquad
\xi_{2/3}=\frac{\varepsilon_{cu}}{\varepsilon_{cu}+0{,}010},\qquad
\xi_{3/4}=\frac{\varepsilon_{cu}}{\varepsilon_{cu}+\varepsilon_{yd}}.
$$

Para C20 a C50, $\varepsilon_{c2}=2\text{‰}$ e $\varepsilon_{cu}=3{,}5\text{‰}$. Com CA-50:

| Região | Intervalo de $\xi$ | Condição no ELU |
|---|---|---|
| Domínio 2a | $0<\xi<0{,}167$ | Aço a $10\text{‰}$ e concreto abaixo de $\varepsilon_{c2}$ |
| Domínio 2b | $0{,}167\leq\xi<0{,}259$ | Aço a $10\text{‰}$ e concreto entre $\varepsilon_{c2}$ e $\varepsilon_{cu}$ |
| Domínio 3 | $0{,}259\leq\xi\leq0{,}628$ | Concreto a $\varepsilon_{cu}$, com escoamento da armadura tracionada |
| Domínio 4 | $0{,}628<\xi<1$ | Concreto alcança $\varepsilon_{cu}$ antes do escoamento da armadura |

As fronteiras expressam compatibilidade física de deformações. No cálculo simplificado do domínio 2, a posição obtida pelo bloco retangular é uma estimativa de enquadramento; a correção do braço de alavanca será apresentada adiante.

Para C55 a C90, usam-se nas mesmas expressões:

$$
\varepsilon_{c2}=\left[2+0{,}085(f_{ck}-50)^{0{,}53}\right]\text{‰},
\qquad
\varepsilon_{cu}=\left[2{,}6+35\left(\frac{90-f_{ck}}{100}\right)^4\right]\text{‰}.
$$

### Limite de ductilidade

Para os exercícios desta aula, sem redistribuição de momentos, adotaremos em todas as seções:

$$
\xi\leq\xi_{lim}=\begin{cases}
0{,}45,&f_{ck}\leq50\text{ MPa},\\
0{,}35,&50<f_{ck}\leq90\text{ MPa}.
\end{cases}
$$

O limite $0{,}45$ é mais restritivo que a fronteira $0{,}628$ do CA-50. Uma seção pode estar no domínio 3 e ainda exceder o limite de ductilidade adotado.

As formas finais úteis para verificar a capacidade e estimar a altura são:

$$
\mu_{lim}=\alpha_c\eta_c\lambda\xi_{lim}
\left(1-\frac{\lambda\xi_{lim}}2\right),
$$

$$
M_{d,lim}=\mu_{lim}b_wd^2f_{cd},
\qquad
d_{min}=\sqrt{\frac{M_d}{\mu_{lim}b_wf_{cd}}}.
$$

Para C20 a C40, $\mu_{lim}=0{,}25092\approx0{,}251$. Se $M_d>M_{d,lim}$, convém rever a seção ou estudar armadura dupla. Simplesmente acrescentar aço tracionado não resolve o excesso de profundidade da linha neutra.

## Aplicação no domínio 2

O capítulo apresenta um método iterativo de correção da tensão de compressão e uma alternativa simplificada de limitação do braço de alavanca. Adotaremos a alternativa simplificada para os cálculos manuais.

Calculam-se inicialmente $\mu$, $\xi$ e $\varphi$ pelas expressões do bloco retangular. Para o domínio 2, limita-se então:

$$
\varphi_{max}=1-\frac{\lambda\varepsilon_{cu}}
{3(\varepsilon_{cu}+0{,}010)},
\qquad
\varphi_{adot}=\min(\varphi,\varphi_{max}),
$$

$$
\boxed{A_s=\frac{M_d}{f_{yd}\varphi_{adot}d}}.
$$

Para C20 a C50, $\varphi_{max}=0{,}930864\approx0{,}931$. As deformações da expressão devem estar na mesma unidade.

Essa limitação é o procedimento simplificado apresentado pelos autores do capítulo, e não uma exigência adicional da NBR 6118. Quando ela atua, calcula-se $A_s$ pela expressão de momentos acima. Não se deve usar a expressão de forças com o $x$ do bloco original como se ela ainda fosse equivalente, nem interpretar esse $x$ como a linha neutra exata da seção corrigida.

## Fórmulas de consulta para C20 a C40

Com $\alpha_c=0{,}85$, $\eta_c=1$ e $\lambda=0{,}8$:

| Etapa | Expressão final |
|---|---|
| Momento adimensional | $\mu=M_d/(b_wd^2f_{cd})$ |
| Linha neutra relativa | $\xi=1{,}25\left(1-\sqrt{1-2\mu/0{,}85}\right)$ |
| Braço de alavanca | $\varphi=1-0{,}4\xi$ |
| Domínio 3 | $A_s=M_d/(f_{yd}\varphi d)$ |
| Domínio 2, método do capítulo | $A_s=M_d/[f_{yd}d\min(\varphi;0{,}930864)]$ |
| Limite adotado de ductilidade | $\xi\leq0{,}45$ ou $\mu\leq0{,}25092$ |

## Armadura mínima e escolha das barras

Para vigas, o capítulo apresenta o dimensionamento para o momento mínimo:

$$
M_{d,min}=0{,}8W_0f_{ctk,sup},\qquad
W_0=\frac{b_wh^2}{6},\qquad f_{ctk,sup}=1{,}3f_{ctm}.
$$

Para calcular a resistência média à tração, com as resistências em MPa:

$$
f_{ctm}=\begin{cases}
0{,}3f_{ck}^{2/3},&f_{ck}\leq50\text{ MPa},\\
2{,}12\ln(1+0{,}11f_{ck}),&50<f_{ck}\leq90\text{ MPa}.
\end{cases}
$$

Se $A_s(M_{d,min})$ indica a área obtida dimensionando a seção para esse momento,

$$
A_{s,min}=\max\left[A_s(M_{d,min});\,0{,}0015b_wh\right],
\qquad
A_{s,nec}=\max(A_s;A_{s,min}).
$$

Como alternativa, a Tabela 17.3 da edição adotada fornece taxas para CA-50, com as hipóteses de cálculo indicadas no capítulo. Para outras hipóteses, utiliza-se o procedimento do momento mínimo. Em lajes, aplicam-se os mínimos específicos de cada direção e região da Tabela 19.1, retomados na Aula 07.

A seleção das barras começa pelas expressões finais

$$
A_\phi=\frac{\pi\phi^2}{4},\qquad
n=\left\lceil\frac{A_{s,nec}}{A_\phi}\right\rceil.
$$

Em uma faixa de laje de $1000\text{ mm}$, com $A_{s,nec}$ em $\text{mm}^2/\text{m}$ e $\phi$ em mm:

$$
s\leq\frac{1000A_\phi}{A_{s,nec}}\quad\text{(mm)}.
$$

Essa conta atende à área. A escolha final também precisa respeitar os limites construtivos de espaçamento e diâmetro.

### Altura útil e arranjo transversal

Para uma camada de barras em viga com estribo de diâmetro $\phi_t$:

$$
d=h-c_{nom}-\phi_t-\frac\phi2.
$$

Para a camada mais externa de uma laje sem estribos, $d=h-c_{nom}-\phi/2$. Na outra direção, a sobreposição das barras pode reduzir a altura útil. Para várias camadas:

$$
y_{CG}=\frac{\sum A_{si}y_i}{\sum A_{si}},\qquad d=h-y_{CG},
$$

medindo $y_i$ a partir da face tracionada. A área de aço deve ser recalculada se o arranjo reduzir o $d$ usado no dimensionamento.

Para barras isoladas em vigas, os espaçamentos livres mínimos, apresentados aqui apenas em sua forma final, são:

$$
a_h\geq\max(20\text{ mm};\phi;1{,}2d_{ag}),\qquad
a_v\geq\max(20\text{ mm};\phi;0{,}5d_{ag}),
$$

em que $d_{ag}$ é a dimensão máxima característica do agregado. Nas camadas com bitolas diferentes, considerar a maior bitola. O detalhamento longitudinal, com ancoragens, emendas e interrupções, constitui uma etapa posterior.

## Exemplo 1: viga no domínio 3

Uma viga tem $b_w=20\text{ cm}$, $h=50\text{ cm}$, $d=45\text{ cm}$, concreto C30 e aço CA-50. O momento de cálculo é $M_d=180\text{ kN m}$. Determine a área de aço necessária.

Com $f_{cd}=30/1{,}4=21{,}43\text{ MPa}$ e $f_{yd}=434{,}78\text{ MPa}$:

$$
\mu=\frac{180\times10^6}{200\times450^2\times21{,}4286}
=0{,}20741,
$$

$$
\xi=1{,}25\left(1-\sqrt{1-\frac{2\times0{,}20741}{0{,}85}}\right)
=0{,}35559.
$$

Como $0{,}259<\xi<0{,}45$, a seção está no domínio 3 e atende ao limite adotado de ductilidade. A deformação do aço confirma a hipótese de escoamento:

$$
\varepsilon_s=3{,}5\frac{1-0{,}35559}{0{,}35559}
=6{,}34\text{‰}>2{,}07\text{‰}.
$$

O braço de alavanca e a área de aço são:

$$
\varphi=1-0{,}4\times0{,}35559=0{,}85776,\qquad
z=386{,}0\text{ mm},
$$

$$
A_s=\frac{180\times10^6}{434{,}78\times386{,}0}
=1072{,}6\text{ mm}^2=10{,}73\text{ cm}^2.
$$

Para conferir o mínimo, $f_{ctm}=0{,}3\times30^{2/3}=2{,}896\text{ MPa}$ fornece $M_{d,min}=25{,}10\text{ kN m}$. O dimensionamento para esse momento, pelo método simplificado do domínio 2, fornece $A_s(M_{d,min})\approx1{,}38\text{ cm}^2$, enquanto $0{,}0015b_wh=1{,}50\text{ cm}^2$. Logo, prevalece a área calculada de **$10{,}73\text{ cm}^2$**.

Por área, quatro barras de $20\text{ mm}$ fornecem $12{,}57\text{ cm}^2$. Isso ainda não define um arranjo viável: é preciso verificar se as barras cabem na largura disponível e se preservam a altura útil de $45\text{ cm}$.

## Exemplo 2: armadura positiva de uma laje

Para uma direção de uma laje bidirecional de concreto C30 e aço CA-50, considere $h=16\text{ cm}$, cobrimento de $25\text{ mm}$ e barras provisórias de $8\text{ mm}$ na camada mais externa. O momento positivo de cálculo é $m_d=15\text{ kN m/m}$.

Na faixa de $1\text{ m}$, $b_w=1000\text{ mm}$ e $M_d=15\text{ kN m}$. A altura útil é

$$
d=160-25-\frac82=131\text{ mm}.
$$

O cálculo pelo bloco retangular fornece

$$
\mu=0{,}04079,\qquad\xi\approx0{,}06150,\qquad
\varphi\approx0{,}97540.
$$

O enquadramento é no domínio 2. Pelo método simplificado do capítulo:

$$
\varphi_{adot}=\min(0{,}97540;0{,}930864)=0{,}930864,
$$

$$
A_s=\frac{15\times10^6}{434{,}78\times0{,}930864\times131}
=282{,}9\text{ mm}^2/\text{m}=2{,}83\text{ cm}^2/\text{m}.
$$

Para a armadura positiva bidirecional, a taxa mínima adotada é $0{,}67\times0{,}150\%$:

$$
A_{s,min}=0{,}67\times0{,}0015\times1000\times160
=160{,}8\text{ mm}^2/\text{m}.
$$

Prevalece a área calculada. Para barras de $8\text{ mm}$, $A_\phi=50{,}27\text{ mm}^2$ e

$$
s\leq\frac{1000\times50{,}27}{282{,}9}=177{,}7\text{ mm}.
$$

Adotando **$\phi8$ a cada $17\text{ cm}$**, obtêm-se $2{,}96\text{ cm}^2/\text{m}$. O espaçamento também é inferior a $\min(2h;20\text{ cm})=20\text{ cm}$ e a bitola é inferior a $h/8=20\text{ mm}$. A outra direção deve ser calculada com seu momento e sua própria altura útil.

Após selecionar as armaduras, refazem-se as verificações de serviço da Aula 07 com a área efetiva. O dimensionamento no ELU, isoladamente, não verifica a flecha.

## Exemplo 3: seção no domínio 3 que excede a ductilidade

Mantenha a seção $20\times50\text{ cm}$, $d=45\text{ cm}$, C30 e CA-50 do Exemplo 1, mas aumente o momento de cálculo para $250\text{ kN m}$.

$$
\mu=0{,}28807,\qquad \xi=0{,}54047.
$$

Embora $\xi<0{,}628$, o limite $0{,}45$ é ultrapassado. A capacidade no limite adotado é

$$
M_{d,lim}=0{,}25092\times200\times450^2\times21{,}4286
=217{,}76\text{ kN m}<250\text{ kN m}.
$$

Mantendo a largura e os materiais, a altura útil mínima é

$$
d_{min}=\sqrt{\frac{250\times10^6}
{0{,}25092\times200\times21{,}4286}}
=482{,}2\text{ mm}.
$$

Uma seção com $h=55\text{ cm}$ e $d=50\text{ cm}$ fornece $\xi=0{,}41056$ e $A_s=13{,}76\text{ cm}^2$, atendendo ao limite para o momento dado. No projeto completo, a mudança de seção também exige atualizar o peso próprio e os esforços afetados.

## Exercícios para resolver em sala

```{admonition} Exercício 1: dimensionamento de uma viga
:class: destaque-verde

Uma seção de viga tem $b_w=20\text{ cm}$, $h=50\text{ cm}$ e $d=45\text{ cm}$, com C30, CA-50 e $M_d=120\text{ kN m}$. Calcule $\mu$, $\xi$ e $\varphi$, identifique o domínio e determine $A_{s,nec}$ pelo procedimento desta aula. Verifique a ductilidade e o mínimo. Use $\gamma_c=1{,}4$ e $\gamma_s=1{,}15$.
```

```{admonition} Exercício 2: quando a armadura mínima governa
:class: destaque-verde

Repita o Exemplo 2 para $m_d=3\text{ kN m/m}$. Calcule a área necessária e proponha um espaçamento de barras de $8\text{ mm}$ que atenda simultaneamente à área e ao limite construtivo de espaçamento. Explique por que o espaçamento obtido apenas pela divisão da área pode não ser adotado.
```

```{admonition} Exercício 3: efeito da classe do concreto
:class: destaque-verde

Repita o Exemplo 1 com concreto C50, mantendo as demais informações. Calcule $\eta_c$, $\mu$, $\xi$, $\varphi$ e a armadura de tração, aplicando o procedimento do domínio correspondente. Compare com o resultado para C30 e explique por que a redução da armadura não é proporcional ao aumento de $f_{ck}$.
```

## Roteiro de dimensionamento

1. Identificar a face tracionada e registrar $M_d$, $b_w$, $h$ e $d$.
2. Obter $f_{cd}$, $f_{yd}$ e os coeficientes do bloco equivalente.
3. Calcular $\mu$ e $\xi$, conferir o domínio e o limite de ductilidade.
4. Obter $\varphi$ e aplicar a limitação do capítulo quando se tratar do domínio 2.
5. Calcular $A_s$, verificar o mínimo e determinar $A_{s,nec}$.
6. Escolher barras, conferir o arranjo e recalcular se houver mudança de altura útil.
7. Completar as verificações de serviço e o detalhamento longitudinal.

## Referências

- *Dimensionamento de seções retangulares com armadura simples*. Capítulo 4 do material fornecido pelo professor, arquivo `ECA_Livro_2025-02_-_cap4_-_revisado`. Base da dedução geral, do esquema da seção, dos limites e do método simplificado para o domínio 2.
- ABNT — ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. *NBR 6118: Projeto de estruturas de concreto*. Rio de Janeiro, 2023, versão corrigida de 2024. Edição de referência do capítulo, especialmente itens 14.6.4.3, 17.2.2, 17.3.5.2.1 e 20.1.
