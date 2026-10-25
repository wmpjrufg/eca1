## Entrega 4: Dimensionamento à flexão e verificações finais

Referências: [Aula 08](../aulas/008-armadura-simples.md),
[Aula 07](../aulas/007-verificacoes-preliminares-lajes.md) e
[Aula 09](../aulas/009-detalhamento-secoes.md).

### Dimensionamento de cada direção e região

Use os momentos **finais e compatibilizados** da Entrega 2. Para cada
positivo de L1 a L4 e cada negativo sobre V2 e V5, tome uma faixa de 1 m,
$b_w=1000\text{ mm}$, e determine a altura útil a partir da camada real.

Com $M_d$ em N mm, $d$ em mm e resistências em MPa:

$$
\mu=\frac{M_d}{b_wd^2f_{cd}},\qquad
\xi=\frac{x}{d}=1{,}25\left(1-\sqrt{1-\frac{2\mu}{0{,}85}}\right),
\qquad\varphi=1-0{,}4\xi.
$$

Para o C30 desta solução, verifique $\xi\leq0{,}45$ e o domínio da seção.
Quando o domínio 2 for aplicável, siga a limitação do método simplificado
ensinado na Aula 08:

$$
\varphi_{adot}=\min(\varphi;0{,}930864),\qquad
A_s=\frac{M_d}{f_{yd}\varphi_{adot}d}.
$$

No domínio 3, use o braço de alavanca correspondente, sem aplicar a
limitação destinada ao domínio 2. A área necessária é

$$
A_{s,nec}=\max(A_s;A_{s,min}),
$$

com o mínimo adequado à armadura positiva ou negativa da Entrega 3.
Se o limite de ductilidade não for atendido, reveja a seção antes de
simplesmente acrescentar aço.

### Exemplo numérico do procedimento

**Exemplo de cálculo, sem atribuir um momento ainda não obtido à planta:**
considere uma região com $m_d=12\text{ kN m/m}$, $h=12\text{ cm}$,
cobrimento de 25 mm e barras de 8 mm na camada externa.

$$
d=120-25-8/2=91\text{ mm},\qquad
\mu=\frac{12\times10^6}{1000\times91^2\times(30/1{,}4)}
\approx0{,}06762,
$$

$$
\xi\approx0{,}10375<0{,}45,\qquad
\varphi\approx0{,}95850.
$$

O enquadramento é no domínio 2. Pelo método adotado na aula:

$$
A_s=\frac{12\times10^6}{434{,}78\times0{,}930864\times91}
\approx325{,}8\text{ mm}^2/\text{m}=3{,}258\text{ cm}^2/\text{m}.
$$

Esse valor supera os mínimos positivo e negativo calculados para 12 cm.
Com $A_\phi=\pi8^2/4=50{,}265\text{ mm}^2$:

$$
s\leq\frac{1000A_\phi}{A_{s,nec}}
=154{,}3\text{ mm}.
$$

Adotando **$\phi8$ c/15**, obtém-se
$A_{s,ef}=335{,}1\text{ mm}^2/\text{m}=3{,}351\text{ cm}^2/\text{m}$.
O espaçamento é inferior a $\min(2h;200)=200\text{ mm}$ e a bitola é inferior
a $h/8=15\text{ mm}$. A seção ainda depende das verificações de serviço.

### Armaduras do pavimento

Repita a sequência para as seguintes regiões, separando pavimento-tipo e
cobertura:

| Regiões | Momento de entrada | Altura útil e mínimo |
|---|---|---|
| Positivas $x$ de L1 a L4 | $m_{x,d,c}$ | Camada de barras na direção $x$; mínimo positivo bidirecional |
| Positivas $y$ de L1 a L4 | $m_{y,d,c}$ | Camada de barras na direção $y$; mínimo positivo bidirecional |
| Negativas de V2, trecho esquerdo e direito | $X_{c,d}$ de L1/L3 e L2/L4 | Barras superiores na direção $x$; mínimo negativo |
| Negativas de V5, trecho superior e inferior | $X_{c,d}$ de L1/L2 e L3/L4 | Barras superiores na direção $y$; mínimo negativo |

No encontro de V2 e V5 há sobreposição das negativas. Confira as alturas
úteis e o alojamento das duas direções. Complete as armaduras de borda e de
canto pelo caso efetivo e pelos critérios apresentados na Aula 10.

### Resultado de flexão do pavimento-tipo

Adotando barras de 8 mm nas duas direções, coloque as barras $x$ mais
próximas da face tracionada e as $y$ imediatamente na segunda camada. Isso
fornece $d_x=91\text{ mm}$ e $d_y=83\text{ mm}$, tanto nos positivos como
nos negativos, respeitada a inversão de face. Com os momentos finais da
Entrega 2, as áreas necessárias são:

| Laje | $A_{sx,+}$ | $A_{sx,-}$ sobre V2 | $A_{sy,+}$ | $A_{sy,-}$ sobre V5 |
|---|---:|---:|---:|---:|
| L1 | 2,078 | 4,789 | 1,720 | 4,930 |
| L2 | 2,277 | 5,084 | 1,713 | 4,930 |
| L3 | 1,972 | 4,789 | 1,529 | 4,520 |
| L4 | 2,134 | 5,084 | 1,496 | 4,520 |

Unidades: $\mathrm{cm^2/m}$. Todas essas regiões se enquadram no domínio 2,
com $x/d<0{,}45$, usando o procedimento da Aula 08. Uma primeira escolha
padronizada de barras para o pavimento-tipo é:

| Regiões | Armadura escolhida | $A_{s,ef}$ (cm²/m) |
|---|---|---:|
| Positivas nas duas direções de L1 a L4 | Ø8 c/20 | 2,513 |
| Negativas da direção $x$ sobre V2 | Ø8 c/9 | 5,585 |
| Negativas da direção $y$ sobre V5 | Ø8 c/10 | 5,027 |

Essas escolhas atendem à área, à bitola máxima e ao espaçamento máximo
principal para $h=12\text{ cm}$. A padronização é uma escolha didática;
pode-se estudar economia por região. A aprovação final depende dos ELS,
do cisalhamento, das armaduras complementares e das ancoragens. A tabela
não representa a armadura da cobertura, cujo carregamento deve ser tratado
separadamente.

### Verificações com a armadura efetivamente escolhida

Para cada região, registre $M_d$, $h$, $d$, $x/d$, $A_s$, $A_{s,min}$,
bitola, espaçamento e $A_{s,ef}$. Refaça as verificações da Entrega 3 com
$A_{s,ef}$ e o novo $d$, incluindo a rigidez fissurada, a abertura de fissuras
e a flecha final.

Se a espessura mudar, atualize peso próprio, vãos efetivos, relações entre
vãos, coeficientes, esforços, reações e armaduras. Aumentar apenas a área de
aço na tabela não corrige automaticamente uma flecha excessiva.

### Erros frequentes nesta entrega

- Usar $b_w=150\text{ mm}$, largura da viga, no lugar da faixa de laje de 1000 mm.
- Esquecer a conversão de kN m para N mm.
- Usar a bitola de 6,3 mm no cálculo de $d$ depois de escolher barras de 8 mm.
- Escolher o espaçamento só pelo limite de 20 cm, sem atender à área calculada.
- Manter a flecha calculada com armadura mínima após escolher as barras finais.
