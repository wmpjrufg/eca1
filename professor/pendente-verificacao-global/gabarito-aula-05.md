# Gabarito do professor: Aula 05 (verificação global do sistema)

Material **somente do professor**. Não faz parte do site publicado (fica fora de `source/`).

Os valores abaixo vêm de um solver de pórticos planos (método da rigidez, barras de Euler-Bernoulli) validado contra casos analíticos. O solver reproduz os resultados dos seus slides do Exemplo 02 (γz): deslocamento do topo de $2{,}11$ cm e $\gamma_z=1{,}08$. No Exemplo 01 (α), o solver dá $\delta_{topo}=9{,}86\times10^{-4}$ m e o seu Ftool, $9{,}677\times10^{-4}$ m (diferença de $1{,}8\%$). Os alunos devem obter valores dessa ordem. Para o Ftool, use os valores do arquivo como referência de ordem de grandeza, e não como tolerância rígida.

## Pontos a conferir antes de usar a aula

1. **Rigidez no cálculo do α.** O slide do Exemplo 01 aplica $0{,}8$ aos pilares e $0{,}4$ às vigas também no $\alpha$. A redação que lembro da NBR 6118 (item 15.5.2) usa $E_{cs}I_c$ com a seção bruta no $\alpha$, e reserva a rigidez reduzida (item 15.7.3) ao $\gamma_z$ e à análise de 2ª ordem. A aula apresenta o critério do slide como principal e pede a comparação com a seção bruta na Atividade 2. **Confira o texto da edição que usa** e ajuste o quadro "Qual rigidez usar no cálculo de α?" se necessário. Há uma evidência numérica a favor da seção bruta: no edifício do Exemplo 3, o $\alpha$ da rigidez reduzida resulta $0{,}53$ (acima de $0{,}5$) com $\gamma_z=1{,}08$, enquanto o $\alpha$ da seção bruta resulta $0{,}42$, coerente com o $\gamma_z$ (ver a tabela da discussão 1).
2. **Valores transcritos de memória**, a conferir nas normas: parâmetros $b$, $p$, $F_r$ da tabela de $S_2$ (NBR 6123) e os valores de $S_3$; o coeficiente $C_a\approx1{,}2$ lido do gráfico para $h/l_1=3$ e $l_1/l_2=1$; $\theta_{1,mín}=1/300$ (slide) em vez de $1/400$ para nós fixos; limites de deslocamento $H/1700$ e $H_i/850$ (Tabela 13.3); a tabela de $\alpha_1$; os coeficientes $\psi_0$.
3. **Detalhes dos slides.** No Exemplo 01 (slide 3), a expressão de $\alpha_i$ está escrita com $30/80$ ($f_{ck}=30$), mas o resultado $0{,}85$ corresponde a $f_{ck}=20$ ($0{,}80+0{,}20\cdot20/80=0{,}85$): é só um erro de digitação no slide. No slide 8 do Exemplo 01, a fórmula de $\alpha_1$ para $n\le3$ parece estar escrita com $0{,}40\,n$; a norma traz $0{,}2+0{,}1\,n$, que é a que está na aula. No Exemplo 02, os módulos rotulados "$E_{cs}^{cor}$" são, na verdade, $0{,}4E_{ci}$ e $0{,}8E_{ci}$.
4. **Slides do Exemplo 02.** A tabela do slide 9 ($\delta=0{,}26$ a $2{,}11$ cm; $\Delta M=47{,}9$; $\gamma_z=1{,}08$) é reproduzida pelo solver com diferença de até $0{,}01$ cm nos deslocamentos. A planta e o modelo só se reproduzem se o vento atuar na direção y (vertical na planta) e se os pilares forem: P1 e P5 com $20$ cm paralelos a y, P2 e P4 com $70$ cm paralelos a y.
5. **Aula 20 (verificações preliminares).** O arquivo com os slides da parte de estabilidade (parâmetro α, γz e limite de deslocamento) tem só as imagens das fórmulas; usei as expressões padrão da norma. Confira se as suas fórmulas coincidem.

## Atividade 1: ações horizontais

### Exercício 1: vento em terreno de categoria II

Dados: $V_0=35$ m/s, $S_1=S_3=1{,}0$, categoria II (classe A: $b=1{,}00$, $p=0{,}085$, $F_r=1{,}00$), $C_a=1{,}2$, $L=6$ m.

| Pavimento | $z$ (m) | $S_2$ | $V_k$ (m/s) | $q$ (kN/m²) | $C_a q$ (kN/m²) | $F_{ve}$ (kN) |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 3 | $0{,}943$ | $33{,}0$ | $0{,}667$ | $0{,}801$ | $14{,}42$ |
| 2 | 6 | $0{,}958$ | $33{,}5$ | $0{,}688$ | $0{,}826$ | $14{,}87$ |
| 3 | 9 | $0{,}991$ | $34{,}7$ | $0{,}738$ | $0{,}885$ | $15{,}93$ |
| 4 | 12 | $1{,}016$ | $35{,}6$ | $0{,}775$ | $0{,}929$ | $16{,}73$ |
| 5 | 15 | $1{,}035$ | $36{,}2$ | $0{,}805$ | $0{,}965$ | $17{,}38$ |
| 6 | 18 | $1{,}051$ | $36{,}8$ | $0{,}830$ | $0{,}996$ | $8{,}96$ |
| **Soma** | | | | | | **$88{,}3$** |

Momento de tombamento na base: $\sum F_{ve,i}z_i=899\text{ kN}\cdot\text{m}$. Observação: em $z=3$ m, $S_2$ usa $z=5$ m (valor constante abaixo de $5$ m).

**Comparação.** Categoria IV (Exemplo 1): $65{,}1$ kN e $672\text{ kN}\cdot\text{m}$. A categoria II dá cerca de $36\%$ mais força e $34\%$ mais momento. A estimativa de $0{,}80\text{ kN/m}^2$ (soma $79{,}2$ kN; $778\text{ kN}\cdot\text{m}$) fica entre as duas e representa bem a **categoria II nos pavimentos baixos** (onde $C_aq\approx0{,}80$); para a categoria IV, é conservadora.

### Exercício 2: vento ou desaprumo

1. $H=18$ m: $\theta_1=1/(100\sqrt{18})=1/424=2{,}36\times10^{-3}$, menor que $1/300$; adota-se $\theta_1=1/300=3{,}33\times10^{-3}$. Com $n=5$: $\theta_a=3{,}33\times10^{-3}\sqrt{(1+1/5)/2}=2{,}58\times10^{-3}$.
2. $F_{D,i}=2{,}58\times10^{-3}\cdot432=1{,}12$ kN por pavimento (para o $P_i$ característico). Momento do desaprumo na base: $1{,}12\cdot63=70\text{ kN}\cdot\text{m}$.
3. O momento do vento (categoria II, $899\text{ kN}\cdot\text{m}$) é cerca de $13$ vezes o do desaprumo: **o vento governa** e o desaprumo não é combinado com ele.
4. O desaprumo governa em edifícios altos e esbeltos com área frontal pequena (pouco vento) e muito pesados, em regiões de vento fraco ou na direção em que a área exposta é pequena.

## Atividade 2: o parâmetro α (Exemplo 2)

$N_k=1920$ kN; $H_{tot}=12$ m; $\alpha_1=0{,}5$ (só pórticos, $n=4$).

| Caso | $\delta_{topo}$ (m) | $EI_{eq}$ (kN·m²) | $\alpha$ | $\alpha\le0{,}5$? |
|---|---:|---:|---:|---|
| Reduzida, P2 e P5 com $40$ cm no plano | $9{,}86\times10^{-4}$ | $5{,}84\times10^{5}$ | $0{,}69$ | Não |
| Bruta ($E_{cs}$), P2 e P5 com $40$ cm no plano | $6{,}14\times10^{-4}$ | $9{,}38\times10^{5}$ | $0{,}54$ | Não |
| Reduzida, P2 e P5 com $20$ cm no plano | $1{,}18\times10^{-3}$ | $4{,}86\times10^{5}$ | $0{,}75$ | Não |
| Reduzida, vigas $12\times50$ | $6{,}65\times10^{-4}$ | $8{,}67\times10^{5}$ | $0{,}57$ | Não |
| Reduzida, vigas $12\times60$ | $4{,}98\times10^{-4}$ | $1{,}16\times10^{6}$ | $0{,}49$ | Sim |
| Reduzida, vigas $20\times50$ | $5{,}05\times10^{-4}$ | $1{,}14\times10^{6}$ | $0{,}49$ | Sim |
| Reduzida, P2 e P5 $20\times60$ | $7{,}91\times10^{-4}$ | $7{,}28\times10^{5}$ | $0{,}62$ | Não |
| Reduzida, P2 e P5 $20\times100$ | $4{,}57\times10^{-4}$ | $1{,}26\times10^{6}$ | $0{,}47$ | Sim |

Com o valor do seu Ftool ($9{,}677\times10^{-4}$ m), o caso 1 dá $EI_{eq}=5{,}95\times10^{5}$ e $\alpha=0{,}68$.

**Comentários para a discussão.**

- Com a seção bruta, o $\alpha$ diminui cerca de $20\%$, mas continua acima de $0{,}5$: a conclusão (calcular o $\gamma_z$) é a mesma. O resultado é robusto à escolha da rigidez; o que muda é a margem.
- Girar P2 e P5 (lado de $40$ cm perpendicular ao plano) aumenta o $\alpha$ em $9\%$ ($0{,}69\to0{,}75$). Mostra o peso da **orientação dos pilares** no projeto: a planta de fôrma define a rigidez nas duas direções.
- A **altura das vigas** é muito eficaz: vigas de $12\times60$ ($+50\%$ de altura) reduzem o $\alpha$ de $0{,}69$ para $0{,}49$, enquanto dobrar o pilar P2/P5 de $40$ para $100$ cm leva só a $0{,}47$. Em pórticos de poucos pilares e vigas esbeltas, a rigidez das vigas controla a rigidez lateral. Aumentar a altura da viga costuma ser mais barato do que alargar pilares, mas pode conflitar com o pé-direito e com a arquitetura.

## Atividade 3: o coeficiente γz (Exemplo 3)

### Exercício 4: reprodução do Exemplo 3

Deslocamentos do solver (rigidez reduzida), em cm:

| Combinação | $\delta_1$ | $\delta_2$ | $\delta_3$ | $\delta_4$ | $\delta_5$ | $\delta_6$ |
|---|---:|---:|---:|---:|---:|---:|
| 1 | $0{,}27$ | $0{,}76$ | $1{,}25$ | $1{,}65$ | $1{,}93$ | $2{,}11$ |
| 2 | $0{,}45$ | $1{,}27$ | $2{,}08$ | $2{,}75$ | $3{,}22$ | $3{,}52$ |

| Combinação | $M_{1,tot,d}$ (kN·m) | $\Delta M_{tot,d}$ (kN·m) | $\gamma_z$ |
|---|---:|---:|---:|
| 1 | $653{,}4$ | $48{,}2$ | $1{,}080$ |
| 2 | $1088{,}6$ | $64{,}3$ | $1{,}063$ |

A combinação 1 governa. Estrutura de nós fixos ($\gamma_z\le1{,}1$).

**ELS-frequente** ($0{,}3F_{ve,k}$, rigidez reduzida): $\delta_{topo}=0{,}75$ cm $<H/1700=1{,}06$ cm; maior deslocamento relativo entre pavimentos $0{,}18$ cm $<H_i/850=0{,}35$ cm. Atende. Com a rigidez bruta ($E_{cs}$ no lugar da reduzida), o deslocamento do topo no ELS-frequente seria $0{,}47$ cm.

**Item 6 (α do Exemplo 3).** $N_k=2592$ kN; $H_{tot}=18$ m; $\alpha_1=0{,}5$.

| Rigidez | $\delta_{topo}$ (m) | $EI_{eq}$ (kN·m²) | $\alpha$ |
|---|---:|---:|---:|
| Reduzida | $6{,}60\times10^{-4}$ | $2{,}94\times10^{6}$ | $0{,}53$ |
| Bruta ($E_{cs}$) | $4{,}02\times10^{-4}$ | $4{,}84\times10^{6}$ | $0{,}42$ |

### Exercício 5: o que muda no γz

| Caso | $\delta_{topo}$ (cm) | $M_{1,tot,d}$ (kN·m) | $\Delta M_{tot,d}$ (kN·m) | $\gamma_z$ | Classificação |
|---|---:|---:|---:|---:|---|
| Exemplo 3, comb. 1 | $2{,}11$ | $653{,}4$ | $48{,}2$ | $1{,}080$ | Nós fixos |
| Exemplo 3, comb. 2 | $3{,}52$ | $1088{,}6$ | $64{,}3$ | $1{,}063$ | Nós fixos |
| P3 contraventando | $2{,}11$ | $653{,}4$ | $48{,}1$ | $1{,}079$ | Nós fixos |
| Vento da categoria II (comb. 1) | $2{,}46$ | $754{,}8$ | $55{,}8$ | $1{,}080$ | Nós fixos |
| Pilares todos com $20$ cm no plano | $3{,}25$ | $653{,}4$ | $82{,}6$ | $1{,}145$ | Nós móveis |
| 8 pavimentos | $4{,}19$ | $1161{,}6$ | $127{,}7$ | $1{,}124$ | Nós móveis |
| 10 pavimentos | $7{,}05$ | $1815{,}0$ | $269{,}1$ | $1{,}174$ | Nós móveis |
| 12 pavimentos | $10{,}78$ | $2613{,}6$ | $492{,}7$ | $1{,}232$ | Nós móveis |
| 16 pavimentos | $21{,}17$ | $4646{,}4$ | $1277{,}1$ | $1{,}379$ | Nós móveis, $\gamma_z>1{,}3$ |

1. **P3.** Um pilar de $20\times20$ isolado quase não altera a rigidez lateral: $\gamma_z$ passa de $1{,}0797$ para $1{,}0794$. A hipótese do enunciado (P3 não contraventa) é razoável. P3 ainda **recebe** carga vertical, e essa carga entra em $\Delta M$ pelo peso total do pavimento.
2. **Categoria II.** O $\gamma_z$ não muda ($1{,}080$): vento maior aumenta $M_1$ e $\Delta M$ na mesma proporção. Esta é a discussão central da aula.
3. **Pilares na posição desfavorável.** $\gamma_z=1{,}145$, estrutura de nós móveis. Fator de amplificação dos esforços horizontais: $0{,}95\cdot1{,}145=1{,}088$ (acréscimo de $8{,}8\%$ nos esforços do vento; as cargas verticais não são majoradas). Mostra a influência da orientação dos pilares.
4. **Pavimentos.** Com 6 pavimentos, $\gamma_z=1{,}08$; com 7, $\gamma_z=1{,}10$ (no limite); com 8, $\gamma_z=1{,}12$: a estrutura deixa de ser de nós fixos a partir de 8 pavimentos (com 7 está na fronteira). Com 14 pavimentos, $\gamma_z=1{,}300$ (limite); com 15, $1{,}34$ e com 16, $1{,}38$: o processo aproximado ($0{,}95\gamma_z$) deixa de valer a partir de 15 pavimentos. A norma também restringe o processo $\gamma_z$ a estruturas reticuladas com **no mínimo 4 andares**. Neste exemplo, as forças por pavimento são mantidas iguais ($12{,}10$ kN), o que subestima o vento nos pavimentos altos; o $\gamma_z$ real cresceria mais depressa.

### Para discutir em sala (notas)

**1. $\alpha$ da rigidez reduzida contra $\gamma_z$.** Para a mesma planta do Exemplo 3, ampliada em número de pavimentos (forças horizontais por pavimento constantes):

| Pavimentos | $\alpha$ (bruta, $E_{cs}$) | $\alpha$ (reduzida) | $\gamma_z$ |
|---:|---:|---:|---:|
| 6 | $0{,}42$ | $0{,}53$ | $1{,}080$ |
| 8 | $0{,}50$ | $0{,}64$ | $1{,}124$ |
| 10 | $0{,}58$ | $0{,}74$ | $1{,}174$ |
| 12 | $0{,}66$ | $0{,}84$ | $1{,}232$ |
| 14 | $0{,}73$ | $0{,}93$ | $1{,}300$ |

O $\alpha$ da seção bruta atinge $\alpha_1=0{,}5$ quando o $\gamma_z$ é cerca de $1{,}12$, de acordo com a ideia de que $\alpha=\alpha_1$ corresponde aproximadamente a $\gamma_z\approx1{,}1$. O $\alpha$ da rigidez reduzida ultrapassa $0{,}5$ já com 6 pavimentos ($\gamma_z=1{,}08$): classifica como "possivelmente móvel" uma estrutura que o $\gamma_z$ considera de nós fixos. Daí o aviso do item 1 da lista de pontos a conferir.

**2. Sobre o vento e o $\gamma_z$.** $\gamma_z=1/(1-\Delta M/M_1)$ e $\Delta M\propto P\cdot\delta\propto P\cdot F$, $M_1\propto F\cdot z$: o $F$ se cancela. O $\gamma_z$ depende da razão $P/\text{rigidez}$ e da distribuição em altura do vento, não da intensidade. A combinação entra pelo fator das cargas verticais.

**3. Como reduzir o $\gamma_z$.** Aumentar a rigidez lateral: altura das vigas, seção e orientação dos pilares, pilares-parede ou núcleos rígidos. Decisão da fase de planta de fôrma (pré-dimensionamento), não do detalhamento.

**4. Limites do pórtico equivalente.** Lajes tratadas como diafragma rígido (lajes flexíveis ou aberturas grandes invalidam), torção ignorada, ligação viga-pilar rígida, fundação engastada (recalque e rotação da fundação aumentam os deslocamentos), cargas distribuídas sem pilares-parede, vento só em uma direção.
