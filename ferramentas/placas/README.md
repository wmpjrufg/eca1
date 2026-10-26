# Tabelas de placas no Colab — Poisson 0,20

O notebook **Gerar_tabelas_placas.ipynb** seleciona os casos, executa os
cálculos e baixa os resultados. O solver, a geração de figuras e a exportação
ficam em **placas.py**, que é o único arquivo de código a acompanhar o notebook.
Não é necessário Streamlit, servidor ou conexão com Google Drive.

## Como usar

1. Abra `Gerar_tabelas_placas.ipynb` no [Google Colab](https://colab.research.google.com/),
   usando **Arquivo → Fazer upload de notebook**.
2. Execute **Preparar o ambiente**. Quando aparecer a seleção de arquivo,
   envie `placas.py` desta mesma pasta.
3. No formulário, escolha o tipo de laje e o intervalo de $\lambda=l_y/l_x$.
   O padrão é tipo 3, de 1,00 a 2,00, a cada 0,05, com **$\nu=0,20$**.
4. Execute as células seguintes para calcular, visualizar e exportar.
   **Todos** produz um único Excel com os nove tipos em abas separadas.
5. O último passo baixa um ZIP. Se alguma linha não convergir, aumente a
   ordem máxima nas opções de precisão e recalcule; a exportação será bloqueada
   até que todas as linhas atendam.

As células de preparação e precisão começam recolhidas no Colab. O notebook
não contém definições de funções nem classes. Localmente, instale
`pip install -r ferramentas/placas/requirements.txt` e execute o notebook
nesta pasta, ou importe o módulo diretamente.

## O que é exportado

O arquivo **Tabelas_lajes.xlsx** reúne todos os tipos selecionados:

- **Capa**: prancha dos nove esquemas e links para as abas de resultados.
- **Tipo 1, Tipo 2A, …**: desenho dos vínculos, momentos e flecha, volventes,
  e reações médias por borda (k).
- **Bares mx, Bares my, Bares mx neg, Bares my neg, Bares mxy, Bares aw,
  Bares kx, Bares kx eng, Bares ky, Bares ky eng**: tabelas no formato de
  Bares, **uma por coeficiente** ($\mu_x$, $\mu_y$, $\mu'_x$, $\mu'_y$,
  $\mu_{xy}$, $\alpha_w$, $k_x$, $k'_x$, $k_y$ e $k'_y$), com $\lambda$ nas
  linhas e os tipos selecionados nas colunas. O traço indica que o coeficiente
  não existe no tipo: $\mu'$ e $k'$ sem engaste na direção, $k$ sem borda
  apoiada na direção, ou $\mu_{xy}$ sem canto com duas bordas apoiadas. Em $\mu_{xy}$ aparece o módulo; os cantos livres de um
  mesmo tipo têm o mesmo valor por simetria. O sinal de cada canto está na aba do tipo.
- **Precisao, Convergencia, Extremos e Metadados**: auditoria consolidada,
  identificada por tipo e Poisson, incluindo a verificação do equilíbrio.

O ZIP também inclui:

- **Tipos_de_lajes.pdf/.svg/.png**: prancha dos nove tipos pronta para aula.
- **Desenhos individuais** de cada tipo selecionado em PDF, SVG e PNG.
- **CSV**: separador `;`, vírgula decimal e UTF-8 com BOM.
- **LaTeX `.tex`**: ambiente `tabular` para inserir no livro.
- **PDF e SVG**: tabela e desenho dos apoios; gráficos vetoriais para diagramação.
  Cada família de resultados tem sua própria tabela; as tabelas de Bares saem
  em `bares_<coeficiente>_nu_0p20_tabela_N`. Tabelas longas são
  divididas em páginas com até 41 linhas.
- **JSON**: parâmetros, versões das bibliotecas e hash do solver.

O ZIP inclui a cópia exata do módulo que gerou as tabelas. Os arquivos não
sobrescrevem resultados anteriores: cada execução cria uma pasta identificada
pelo horário UTC. A pasta `exemplos/` contém o Excel completo dos nove tipos,
a prancha de desenhos, as tabelas de Bares em `exemplos/bares/` e uma
amostra das tabelas do tipo 3.

## Casos e orientação

**A** = apoio simples; **E** = engaste. $x$ é sempre a direção do **menor vão**,
$l_y/l_x\geq1$. A borda $x=0$ tem comprimento $l_y$, enquanto a borda $y=0$
tem comprimento $l_x$. Os esquemas desenhados acompanham a tabela:

| Tipo | $x=0$ | $x=l_x$ | $y=0$ | $y=l_y$ |
|---|---|---|---|---|
| 1 | A | A | A | A |
| 2A | A | A | E | A |
| 2B | E | A | A | A |
| 3 | E | A | E | A |
| 4A | A | A | E | E |
| 4B | E | E | A | A |
| 5A | E | A | E | E |
| 5B | E | E | E | A |
| 6 | E | E | E | E |

Esses são os nove arranjos apoiados/engastados da família usada nas aulas.
Um espelhamento preserva os coeficientes máximos; trocar os eixos exige
trocar também os vínculos e os momentos. Os casos com borda livre não estão
implementados nesta versão.

## Equação, hipóteses e coeficientes

Resolve-se a equação linear da placa delgada isotrópica de Kirchhoff–Love,
com espessura constante e carga uniforme:

$$
D\left(w_{,xxxx}+2w_{,xxyy}+w_{,yyyy}\right)=p,\qquad
D=\frac{Eh^3}{12(1-\nu^2)}.
$$

Os momentos por unidade de largura são:

$$
m_x=-D(w_{,xx}+\nu w_{,yy}),\qquad
m_y=-D(w_{,yy}+\nu w_{,xx}),\qquad
m_{xy}=-D(1-\nu)w_{,xy}.
$$

$w$ é positivo no sentido da carga; momento positivo corresponde à flexão
no vão. Nos engastes, os coeficientes negativos são apresentados em módulo.
Na tabela:

$$
m_x^{max}=\mu_x\frac{p l_x^2}{100},\quad
m_y^{max}=\mu_y\frac{p l_x^2}{100},\quad
|m_x^-|=\mu'_x\frac{p l_x^2}{100},\quad
|m_y^-|=\mu'_y\frac{p l_x^2}{100},
$$

$$
w_{max}=\alpha_w\frac{p l_x^4}{100Eh^3}.
$$

**O denominador da flecha usa $Eh^3$, não $D$.** Na normalização alternativa
$w_{max}=\bar\alpha p l_x^4/D$, vale
$\bar\alpha=\alpha_w/[1200(1-\nu^2)]$.

Os máximos positivos e a flecha são buscados na superfície da placa. Os
negativos são buscados ao longo das bordas engastadas, separadamente por
borda, e o maior módulo de cada direção aparece na tabela resumida.
As coordenadas de todos esses pontos são exportadas na aba `Extremos`.
Nos apoios simples, o momento **normal à borda** é zero.

## Momento volvente e malha de canto

Nos cantos em que **duas bordas apoiadas** se encontram, calcula-se o momento
volvente $m_{xy}$. A tabela **Volventes** traz o valor assinado em cada
vértice, $m_{xy}=\mu_{xy}\,p l_x^2/100$. No vértice adjacente a um engaste,
$m_{xy}=0$ nas condições de contorno adotadas.

Para armar o canto, o volvente é convertido em momentos nas direções das
barras. Pela envoltória de armadura ortogonal (Wood–Armer sem reduções):

$$
m_{x,arm}^{\inf}=\max(0,m_x+|m_{xy}|),\quad
m_{y,arm}^{\inf}=\max(0,m_y+|m_{xy}|),
$$

$$
m_{x,arm}^{\sup}=\max(0,-m_x+|m_{xy}|),\quad
m_{y,arm}^{\sup}=\max(0,-m_y+|m_{xy}|).
$$

No vértice, $m_x=m_y=0$; portanto, a demanda local é $|m_{xy}|$ em x e em y,
nas faces inferior e superior. **Não se divide $|m_{xy}|$ por dois.** Essa
conversão e a uniformização da malha de canto são feitas à mão, na
[aula 05](../../source/aulas/005-esforcos-lajes.md), a partir da tabela de
$\mu_{xy}$. A conversão segue a composição de momentos descrita na
[documentação de Wood–Armer](https://help.autodesk.com/cloudhelp/2020/CHS/RSAPRO-UsersGuide/files/GUID-80FE7814-C14D-4A89-A6DF-68EB9E7E4815.htm),
com a convenção deste módulo: positivo traciona a face inferior.

As forças concentradas de canto, $|C|=2|m_{xy}|$, servem apenas para o
equilíbrio das reações. Elas não substituem a armadura de canto.

São **coeficientes calculados pelo programa**, com a apresentação e a
tipologia usuais das tabelas de Bares. Uma comparação com uma tabela
publicada precisa igualar Poisson, vínculos, posição do momento e
normalização. O programa não reproduz números históricos por consulta.

Os cantos permanecem impedidos de levantar e os apoios são ideais.
O modelo não inclui fissuração, fluência, plastificação, grandes
deslocamentos, apoio unilateral, rigidez das vigas nem aberturas.

## Reações de apoio

As reações elásticas incluem o cortante efetivo de Kirchhoff:

$$
r_{x=0}=-D[w_{,xxx}+(2-\nu)w_{,xyy}],\qquad
r_{x=l_x}=+D[w_{,xxx}+(2-\nu)w_{,xyy}],
$$

com expressões análogas nas bordas em $y$. A integração ao longo de cada
borda fornece sua resultante $R_i$ e a reação média $\bar r_i=R_i/L_i$.
As tabelas usam $\bar r_i=k\,p\,l_x/10$; esse $k$ não é o coeficiente de Poisson.

Nas tabelas de Bares, $k_x$ e $k'_x$ são as reações das bordas $x=0$ e
$x=l_x$ (comprimento $l_y$), apoiada e engastada, respectivamente; $k_y$ e
$k'_y$ referem-se às bordas $y=0$ e $y=l_y$ (comprimento $l_x$). A aba de cada
tipo traz as quatro bordas separadamente (kx0, kx1, ky0, ky1).

**Exportam-se apenas as reações de borda.** O momento volvente gera também
forças concentradas nos cantos entre bordas apoiadas,
$C_{ij}=2(-1)^{i+j}m_{xy}(i\,l_x,j\,l_y)$, que puxam a placa para baixo.
Por isso, a soma das reações de borda **supera a carga total**: na laje
quadrada apoiada, cerca de 30%. Usar só os coeficientes $k$ no carregamento
das vigas fica a favor da segurança. As forças de canto continuam sendo
calculadas para verificar $\sum R_i+\sum C_{ij}=p\,l_x\,l_y$; o erro dessa
soma é exportado em **Precisao** e deve atender à tolerância da convergência.
As fórmulas seguem a
[aula de Kirchhoff da Universidade de Wuppertal, páginas 22–23](https://cam.uni-wuppertal.de/fileadmin/bauing/baumechanik/FEM_1/Vorlesungen/L11_A_Kirchhoff.pdf).

## Método numérico e convergência

Usa-se Rayleigh–Ritz com produtos de polinômios de Legendre integrados duas
vezes. Todas as funções satisfazem $w=0$ no contorno. As condições
$\partial w/\partial n=0$ dos engastes são impostas exatamente na base; a
condição natural $m_{nn}=0$ dos apoios simples é satisfeita na convergência
da formulação variacional.

A energia de flexão usada é:

$$
U=\frac D2\int_\Omega
\left[w_{,xx}^2+w_{,yy}^2+2\nu w_{,xx}w_{,yy}+
2(1-\nu)w_{,xy}^2\right]\,dA.
$$

Como $w=0$ em todas as bordas, a integração por partes fornece
$\int f''g=-\int f'g'$. Os termos cruzados se combinam e o sistema normalizado
por $D$ fica independente de $\nu$. **Poisson continua presente** em $D$,
nos momentos e na conversão do coeficiente de flecha.

Com $l_x=1$, $l_y=\lambda$ e bases ortonormais na segunda derivada:

$$
K=\lambda(I\otimes M_y)+\lambda^{-3}(M_x\otimes I)
       +2\lambda^{-1}(G_x\otimes G_y),\qquad
F=\lambda(f_x\otimes f_y).
$$

$M$ e $G$ são os produtos integrais das funções e das primeiras derivadas;
$f$ contém as integrais das funções. As integrais polinomiais são avaliadas
por ortogonalidade, e o sistema esparso recebe escalonamento diagonal.
Uma ordem $n$ usa $n^2$ amplitudes. A busca dos extremos combina amostragem
com refinamento contínuo de múltiplos candidatos.

O padrão testa ordens 8, 12, 16, …, 40 e exige **duas mudanças sucessivas
de até 0,1%** nos coeficientes de momentos, flecha, reações médias e forças
de canto, além de desequilíbrio relativo de até 0,1% nas duas ordens.
A diferença usa o maior módulo entre duas ordens e um piso de $10^{-3}$
para coeficientes próximos de zero. O resíduo do sistema linear também é
verificado. O histórico completo fica no Excel.

A mudança entre ordens é um indicador de convergência, **não uma estimativa
rigorosa do erro absoluto**. As casas exibidas na tabela não representam
uma garantia de precisão em todas elas. Para uma edição do livro, arquive
os parâmetros e o histórico junto às tabelas e escolha o arredondamento
de acordo com a convergência obtida.

## Uso direto em Python

```python
from placas import gerar_tabelas, exportar_resultados

tabelas = gerar_tabelas(
    tipos="Todos",  # ou uma lista, como ["1", "3", "6"]
    inicio=1.0, fim=2.0, passo=0.05,
    poisson=0.20,
)
arquivo_zip = exportar_resultados(tabelas)
```

Para uma placa individual, sem geração de tabela:

```python
from placas import resolver_placa

solucao = resolver_placa("3", razao=1.5, poisson=0.20, ordem=24)
valores = solucao.valores_fisicos(
    lx=4.0, espessura=0.12, E=30_000_000, carga=5.0,
    u=0.5, v=0.5,
)
```

Nessa função, comprimentos estão em **m**, $E$ em **kN/m²** e $p$ em
**kN/m²**. O exemplo usa $E=30$ GPa. A saída traz flecha em m e momentos em
kN m/m. A chamada de ordem única não verifica convergência; para tabelas,
use `gerar_tabelas`.

## Validação

O [relatório de validação](VALIDACAO.md) registra a varredura dos nove casos
e a execução completa do notebook.

```bash
python -m unittest discover -s ferramentas/placas/tests -v
```

Os testes comparam a solução com a série dupla independente de **Navier**
para bordas apoiadas e com a solução independente de **Lévy** para casos
com engastes. Conferem também vínculos, rotação dos casos A/B, simetria,
escalas de carga/comprimento/espessura, extremos, convergência, células
numéricas dos arquivos Excel e bloqueio de exportação de linhas pendentes.

Para uma placa quadrada apoiada, $\nu=0,20$:
$\mu_x=\mu_y\approx4,4203$, $\alpha_w\approx4,6798$ e
$Dw_{max}/(p l_x^4)\approx0,00406235$. Esses valores permitem conferir a
normalização de uma nova instalação.

## Referências

- [RWTH Aachen — Kirchhoff–Love plate equation, seção 6.11.4](https://mbd.pages.rwth-aachen.de/courses/cmm/content/script/chapters/linearelastics.html).
  Equação, condições de contorno e solução de Navier.
- [Bastos — Lajes de concreto armado](https://wwwp.feb.unesp.br/pbastos/concreto1/Lajes.pdf).
  Tipologia e convenção de apresentação adotadas nas aulas da disciplina.
  [Cópia do material do autor na PUC Goiás](https://professor.pucgoias.edu.br/SiteDocente/admin/arquivosUpload/3922/material/Paulo%20Bastos_Lajes%20de%20Concreto_2015.pdf).
