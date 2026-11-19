# Gabarito do professor: Aula 09 (detalhamento de seções retangulares)

Material **somente do professor**. Fica fora de `source/` e não é publicado.

## Notas sobre os slides da aula 35

1. Os cálculos manuscritos dos slides estão gravados como tinta digital (InkML) e não aparecem na conversão para Markdown nem no LibreOffice. Para lê-los, foi preciso substituir a tinta pela imagem de reserva de cada traço.
2. Slide 4: o número de barras por camada foi calculado com $a_h=4$ cm (circulado em vermelho), enquanto o mínimo normativo é $3{,}0$ cm. A aula explica a escolha como folga para o vibrador e mostra que, com $3{,}0$ cm, o resultado também é 4 barras ($4{,}9$).
3. Slide 5: $y_1=3+0{,}63+1{,}3/2=4{,}28$ cm arredonda $\phi$ para $1{,}3$ cm; o valor exato é $4{,}26$ cm. A aula mantém $4{,}28$ para coincidir com os slides.
4. Slide 6: a distância entre eixos de camadas foi tomada como $3{,}5$ cm (anotado como "$a_v=3{,}5$ cm"). O mínimo seria $\phi+a_v=1{,}25+2{,}0=3{,}25$ cm; $3{,}5$ é um arredondamento a favor da execução. No mesmo slide, "$4\phi16=A_s=4\cdot1{,}227$" deve ser $4\phi12{,}5$.
5. Slide 9: $2{,}25/0{,}32=7{,}03\approx7$ barras de pele. Com $A_\phi=0{,}312$ cm², são $7{,}2$, logo 8 barras de $\phi6{,}3$ por face (7 barras dão $2{,}18$ cm², 3% abaixo). A aula adota 8.
6. Slides 10 e 11: a pele foi concentrada entre a armadura tracionada e a linha neutra. A aula mantém essa leitura e comenta que, em viga contínua, é comum distribuí-la em toda a altura.
7. $x=35{,}83$ cm corresponde a $\xi=x/d=0{,}448$, praticamente no limite de ductilidade $0{,}45$ usado na Aula 08. Vale comentar com a turma.

## Exercício 1: outras bitolas ($A_{s,nec}=19{,}51$ cm², $b_{disp}=17{,}74$ cm, $a_h=3{,}0$, $a_v=2{,}0$)

| Bitola | $n$ | $A_{s,ef}$ (cm²) | Barras por camada | Camadas | $y_{cg}$ (cm) | $d_{real}$ (cm) | $a=y_{cg}-y_1$ (cm) |
|---|---:|---:|---:|---|---:|---:|---:|
| $\phi12{,}5$ (slides) | 16 | 19,63 | 4 ($4{,}88$) | 4+4+4+4 | 9,53 | 80,47 | 5,25 |
| $\phi16$ | 10 | 20,11 | 4 ($4{,}51$) | 4+4+2 | 7,31 | 82,69 | 2,88 |
| $\phi20$ | 7 | 21,99 | 4 ($4{,}15$) | 4+3 | 6,34 | 83,66 | 1,71 |

Posições: $\phi16$: $y=4{,}43$; $8{,}03$; $11{,}63$ cm (eixos a $3{,}6$ cm). $\phi20$: $y=4{,}63$; $8{,}63$ cm (eixos a $4{,}0$ cm). Todos atendem ao critério de $0{,}10h=9{,}0$ cm.

Discussão: $\phi20$ tem menos barras e o maior $d$, mas $13\%$ de área em excesso, espaço livre de só $3{,}25$ cm na camada de 4 (sem folga para vibrador) e ancoragem $60\%$ maior que a de $\phi12{,}5$. $\phi16$ é um bom compromisso: 3 camadas, $3\%$ de excesso, espaço livre de $3{,}78$ cm.

## Exercício 2: seção de vão ($A_{s,nec}=11{,}0$ cm², $\phi16$)

$n=6$ ($12{,}06$ cm²); 4 barras na 1ª camada e 2 na 2ª (alinhadas com as barras de canto). $y_1=4{,}43$ cm; $y_2=8{,}03$ cm; $y_{cg}=(4\cdot4{,}43+2\cdot8{,}03)/6=5{,}63$ cm; $d_{real}=84{,}37$ cm $\geq80$ cm. $a=1{,}20$ cm $\leq9{,}0$ cm. Pele: igual ao exemplo, $2{,}25$ cm² por face (8 $\phi6{,}3$ ou 5 $\phi8$). Porta-estribos: 2 barras de $8$ a $10$ mm no topo (que, na região do apoio, serão complementadas pela armadura negativa).

## Exercício 3: viga $14\times50$ ($b_{disp}=14-2(3{,}0+0{,}5)=7{,}0$ cm; $a_h=\max(2;\phi;2{,}28)=2{,}28$ cm; $a_v=2{,}0$ cm)

| Bitola | $n$ | $A_{s,ef}$ | Por camada | Camadas | $y_{cg}$ | $d_{real}$ | $d_{real}\geq44$? |
|---|---:|---:|---:|---|---:|---:|---|
| $\phi10$ | 6 | 4,71 | 2 ($2{,}83$) | 2+2+2 | 7,00 | 43,00 | Não |
| $\phi12{,}5$ | 4 | 4,91 | 2 ($2{,}63$) | 2+2 | 5,75 | 44,25 | Sim |
| $\phi16$ | 3 | 6,03 | 2 ($2{,}39$) | 2+1 | 5,50 | 44,50 | Sim |

Com $\phi10$, $d_{real}<d$: recalcula-se $A_s$ com $d=43$ cm (aproximadamente $4{,}20\cdot44/43=4{,}30$ cm², ainda atendido pelas 6 barras, $4{,}71$ cm²); o arranjo continua válido, mas com três camadas em uma viga de $14$ cm. Melhor solução: $4\phi12{,}5$. $\phi16$ tem $44\%$ de excesso. Critério de concentração: $\phi10$: $a=3{,}0$ cm $\leq5{,}0$ cm, OK; os demais também.

## Exercício 4: ancoragem (C25, $\phi12{,}5$)

$f_{ctd}=0{,}7\cdot0{,}3\cdot25^{2/3}/1{,}4=1{,}282$ MPa. Boa aderência: $f_{bd}=2{,}25\cdot1{,}282=2{,}886$ MPa, $\ell_b=(12{,}5/4)\cdot(434{,}8/2{,}886)=471$ mm. Má aderência: $f_{bd}=2{,}020$ MPa, $\ell_b=673$ mm.

As barras superiores da viga de $90$ cm estão nos $30$ cm superiores: **má aderência**. As inferiores (mais de $30$ cm abaixo do topo): boa aderência.

$\ell_{b,nec}=0{,}7\cdot673\cdot19{,}51/19{,}63=468$ mm; $\ell_{b,min}=\max(0{,}3\cdot673=202;\ 125;\ 100)=202$ mm. Adota-se cerca de $47$ cm (arredondando, $50$ cm).
