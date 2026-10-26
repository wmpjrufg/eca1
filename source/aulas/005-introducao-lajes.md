# Aula 05: Introdução ao projeto de lajes

```{admonition} Objetivos da aula
:class: destaque-azul

- Reconhecer os sistemas de laje e os tipos de seção transversal.
- Representar os apoios e determinar os vãos efetivos de cada painel.
- Estimar a espessura da laje.
- Preparar os dados para o cálculo dos esforços da [Aula 06](006-esforcos-lajes.md).
```

## Aplicações

(fig-1)=
**Figura 1.** Aplicações do conceito de lajes em edifícios de múltiplos pavimentos.
```{figure} ../_static/aulas/introducao-lajes/exemplos-lajes-abc.png
:alt: Exemplos de laje maciça, laje lisa e laje nervurada
:width: 90%
:align: center
```

## Vão livre, distância entre eixos e vão efetivo

O dimensionamento estrutural inicia-se pela determinação do **vão efetivo**. Para cada direção do painel, identifique primeiro a distância livre entre as faces dos apoios. A [Figura 2](#fig-2) apresenta a idealização do vão efetivo de uma laje, análoga à de uma viga. O procedimento segue o item 14.6.2.4 da [ABNT NBR 6118 [1]](#ref-1).

(fig-2)=
**Figura 2.** Geometria para determinação do vão efetivo.
```{figure} ../_static/aulas/introducao-lajes/vao-efetivo.png
:alt: Vão livre de uma laje e parcelas de apoio utilizadas para obter seu vão efetivo
:width: 70%
:align: center
```

A Equação (1) apresenta o cálculo do vão efetivo:

```{list-table}
:class: eq-table
:widths: 90 10

* - $\displaystyle l_{ef}=l_0+a_1+a_2, \qquad a_i=\min\left(\frac{t_i}{2};\,0{,}3h\right)$
  - (1)
```

$l_0$ é o vão livre, medido entre as faces dos apoios; $t_i$ é a largura do apoio $i$, medida na direção estudada; e $h$ é a espessura da laje. Calcula-se uma parcela $a_i$ para cada extremidade do vão, usando a largura do respectivo apoio. Todas as dimensões devem estar na mesma unidade.

```{admonition} Exemplo 1
:class: destaque-verde

Considere um painel com distâncias entre eixos de $4{,}00\times5{,}00\,\mathrm{m}$, vigas de $20\,\mathrm{cm}$ em todo o contorno e espessura inicial de $10\,\mathrm{cm}$. Como as vigas têm a mesma largura nos dois lados de cada direção, o vão livre é a distância entre eixos menos $20\,\mathrm{cm}$:

$$
l_{0x}=4{,}00-0{,}20=3{,}80\,\mathrm{m},
\qquad
l_{0y}=5{,}00-0{,}20=4{,}80\,\mathrm{m}.
$$

Em cada apoio, $t_i=0{,}20\,\mathrm{m}$; portanto, metade da largura do apoio é $t_i/2=0{,}10\,\mathrm{m}$. O outro valor do mínimo vem da espessura da laje: $0{,}3h=0{,}3\times0{,}10=0{,}03\,\mathrm{m}$. Logo, em cada extremidade:

$$
a_i=\min\left(\frac{0{,}20}{2};\,0{,}3\times0{,}10\right)
=\min(0{,}10;\,0{,}03)=0{,}03\,\mathrm{m}.
$$

Somando ao vão livre as parcelas dos dois apoios:

$$
l_x=l_{0x}+2a_i=3{,}80+2(0{,}03)=3{,}86\,\mathrm{m},
$$

$$
l_y=l_{0y}+2a_i=4{,}80+2(0{,}03)=4{,}86\,\mathrm{m}.
$$

Neste exemplo, $l_x$ é o menor vão efetivo e $l_y$, o maior. Se a espessura adotada mudar, as parcelas $a_i$ devem ser recalculadas.
```

## Uma ou duas direções principais?

Para um painel retangular apoiado nos quatro lados, a relação entre os vãos ajuda a escolher a aproximação de cálculo, conforme a Equação (2):

```{list-table}
:class: eq-table
:widths: 90 10

* - $\displaystyle \lambda=\frac{l_y}{l_x},\qquad l_x\leq l_y$
  - (2)
```

Se $\lambda\leq2$, a laje tem comportamento bidirecional, e os momentos devem ser determinados nas duas direções. Se $\lambda>2$, o comportamento é predominantemente unidirecional, e a análise é feita em faixas na direção do menor vão.

No painel do exemplo, $\lambda=4{,}86/3{,}86\approx1{,}26$, conduzindo ao estudo em duas direções.

Os apoios precisam ser verificados antes dessa classificação. Um painel sustentado apenas em dois lados opostos vence o vão entre esses apoios, mesmo que sua planta seja quadrada. Um balanço também depende da posição da ligação resistente e da borda livre.

## Estimativa inicial da espessura

O pré-dimensionamento fornece uma seção para iniciar a análise. Depois, resistência, deformações, fissuração e disposição das armaduras podem exigir sua revisão. As relações abaixo são as estimativas de Rebello adotadas no material do professor; são critérios de partida, não verificações de segurança.

### Lajes maciças

| Situação | Estimativa de $h$ |
|---|---|
| Duas direções | $h\approx0{,}02(l_x+l_y)/2$ |
| Uma direção | $h\approx0{,}02l_x$ |
| Balanço | $h\approx0{,}04l_b$ |

$l_b$ é o comprimento do balanço. Use a mesma unidade para os vãos e para $h$.

Para o painel de $3{,}86\times4{,}86\,\mathrm{m}$:

$$
h_{est}=0{,}02\frac{3{,}86+4{,}86}{2}
=0{,}0872\,\mathrm{m}=8{,}72\,\mathrm{cm}.
$$

Pode-se manter $h=10\,\mathrm{cm}$ como escolha inicial para organizar o pavimento e prosseguir com as verificações. A estimativa de $8{,}72\,\mathrm{cm}$ não justifica, sozinha, reduzir a espessura.

### Lajes nervuradas

Para as configurações consideradas no material-base:

| Configuração | Estimativa da altura total |
|---|---|
| Unidirecional, intereixo de $50\,\mathrm{cm}$ | $h\approx0{,}03l_x$ |
| Unidirecional, intereixo de $100\,\mathrm{cm}$ | $h\approx0{,}04l_x$ |
| Bidirecional | $h\approx0{,}04(l_x+l_y)/2$ |

A altura total precisa ser compatibilizada com a mesa, a largura das nervuras e o sistema de fôrmas ou enchimento. Os intereixos indicados identificam as situações da estimativa; outros arranjos precisam de avaliação própria. Na solução com componentes pré-fabricados, também é necessário considerar suas características e condições de montagem.

### Limites geométricos e escolha da seção

O material-base adota a NBR 6118:2023. Entre os limites mínimos apresentados para as situações estudadas estão:

| Laje maciça de concreto armado | Espessura mínima no material-base |
|---|---:|
| Cobertura sem balanço | $7\,\mathrm{cm}$ |
| Piso sem balanço | $8\,\mathrm{cm}$ |
| Balanço | $10\,\mathrm{cm}$ |
| Suporte de veículos com peso total até $30\,\mathrm{kN}$ | $10\,\mathrm{cm}$ |
| Suporte de veículos com peso total acima de $30\,\mathrm{kN}$ | $12\,\mathrm{cm}$ |
| Lisa | $16\,\mathrm{cm}$ |
| Cogumelo, fora do capitel | $14\,\mathrm{cm}$ |

Para a mesa de lajes nervuradas sem tubulações horizontais embutidas, o material indica $h_f\geq\max(l_0/15;4\,\mathrm{cm})$, sendo $l_0$ a distância livre **entre as faces das nervuras**. A largura da nervura deve ser de pelo menos $5\,\mathrm{cm}$; abaixo de $8\,\mathrm{cm}$, não se admite armadura de compressão. Tubulações embutidas exigem conferir os limites específicos de espessura da mesa.

Esses mínimos são uma etapa da escolha geométrica. Para um projeto, a edição normativa aplicável e as demais exigências da situação precisam acompanhar a memória de cálculo.

### Espessura total e altura útil

```{figure} ../_static/aulas/introducao-lajes/secao-trans-laje.png
:alt: Seção de laje maciça indicando espessura total, altura útil, cobrimento e posição da armadura
:width: 70%
:align: center

Posição da armadura na seção. Figura do material do professor.
```

A altura útil $d$ é medida da face comprimida até o centro da armadura tracionada. Para uma camada junto à face oposta:

$$
d=h-c-\frac{\phi}{2}.
$$

Com $h=10\,\mathrm{cm}$, cobrimento adotado no exemplo de $2{,}5\,\mathrm{cm}$ e barra de $8\,\mathrm{mm}$, obtém-se $d=7{,}1\,\mathrm{cm}$. O cobrimento deste exemplo é um dado, cuja escolha no projeto depende das condições de exposição e execução.

Em uma laje bidirecional, as barras se cruzam em alturas diferentes. Por isso, as duas direções podem apresentar alturas úteis distintas, mesmo com uma única espessura de laje.

## Atividade: preparar o painel para a análise

Considere uma laje de piso maciça, com quatro bordos apoiados em vigas de $20\,\mathrm{cm}$, dimensões entre eixos de $4{,}20\times5{,}40\,\mathrm{m}$ e espessura inicial de $12\,\mathrm{cm}$. Há continuidade monolítica com um painel semelhante ao longo de um dos bordos de maior comprimento; os demais bordos são externos e serão idealizados como simplesmente apoiados.

1. Desenhe os vínculos e indique a hipótese adotada para o bordo interno.
2. Calcule os dois vãos efetivos e a relação $\lambda$.
3. Escolha a aproximação de uma ou duas direções.
4. Estime a espessura e compare-a com o mínimo de piso do material-base.
5. Registre quais verificações ainda faltam para confirmar a espessura.

**Conferência:** com $a_i=3{,}6\,\mathrm{cm}$, os vãos são $4{,}072\,\mathrm{m}$ e $5{,}272\,\mathrm{m}$; $\lambda\approx1{,}295$ e $h_{est}\approx9{,}34\,\mathrm{cm}$. O painel será estudado em duas direções. A espessura de $12\,\mathrm{cm}$ permanece como hipótese inicial até as verificações posteriores.

Para cada laje do trabalho, entregue uma linha com identificação, tipo, vãos, vínculos, relação $\lambda$ e espessura adotada, acompanhada de um croqui. Esses dados serão a entrada da próxima aula.

## Referências

(ref-1)=
[1] ABNT — ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. *NBR 6118: Projeto de estruturas de concreto*. 4. ed. Rio de Janeiro, 2023.
