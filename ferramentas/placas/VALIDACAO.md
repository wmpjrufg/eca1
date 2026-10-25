# Verificação do gerador de placas

Verificação executada em 25/10/2026, com Python 3.12 e Poisson padrão de 0,20.

## Testes independentes

Os onze testes de `tests/test_placas.py` passaram. Eles cobrem várias
geometrias e condições de contorno:

- série dupla de Navier: relações de vãos 1,00, 1,35 e 2,00, com Poisson
  0,00, 0,20 e 0,30; comparação de flecha e momentos em ponto fora do centro;
- solução de Lévy: tipos 2B e 4B, relações 1,00, 1,50 e 2,00, com pontos
  internos e momento no engaste;
- deslocamento no contorno e condições de rotação/momento nos nove tipos;
- equivalência por rotação dos pares 2A/2B, 4A/4B e 5A/5B em placa quadrada;
- simetria da placa quadrada engastada, máximos da placa apoiada e
  conversões dimensionais;
- parâmetros inválidos, duas confirmações de convergência e bloqueio de
  exportação quando a precisão está pendente;
- planilhas abertas novamente com `openpyxl`, incluindo células numéricas,
  capa com imagem, abas de dois tipos, abas de Bares, metadados e arquivos no ZIP;
- reações integradas e forças de canto comparadas com a série independente
  de Navier em três geometrias e três valores de Poisson; equilíbrio dos nove tipos.
  As forças de canto não são exportadas, mas entram nessa verificação;
- momento volvente no vértice comparado com a série de Navier;
- tabelas de Bares: um coeficiente por tabela, traço onde o coeficiente não
  existe no tipo e reações separadas por borda apoiada e engastada.

A série de Navier é implementada independentemente da base polinomial do
solver. A referência de Lévy resolve uma EDO analítica de quarta ordem para
cada termo de Fourier. Nenhuma dessas referências usa a matriz de Ritz
para gerar seu resultado esperado.
Na referência das reações de Navier, a cauda de ordem $1/N$ é removida
por extrapolação com 600 e 1.200 termos ímpares em cada direção.

## Varredura do intervalo padrão

Foram calculadas **189 linhas**: nove tipos, de $\lambda=1,00$ a $2,00$,
com passo de $0,05$. Todas atenderam ao critério de duas mudanças
sucessivas inferiores a **0,1%**, agora incluindo reações e forças de canto.
Todas também atenderam à tolerância de equilíbrio, sem reescalar as forças.

| Tipo | Linhas | Maior ordem | Maior mudança final (%) | Maior desequilíbrio (%) |
|---|---:|---:|---:|---:|
| 1 | 21 | 24 | 0,0284 | 0,0202 |
| 2A | 21 | 24 | 0,0374 | 0,0177 |
| 2B | 21 | 28 | 0,0335 | 0,0144 |
| 3 | 21 | 28 | 0,0360 | 0,0221 |
| 4A | 21 | 28 | 0,0352 | 0,0249 |
| 4B | 21 | 32 | 0,0436 | 0,0109 |
| 5A | 21 | 28 | 0,0298 | 0,0302 |
| 5B | 21 | 32 | 0,0387 | 0,0226 |
| 6 | 21 | 32 | 0,0264 | 0,0385 |

“Mudança relativa final” mede a diferença entre duas ordens do método;
não é erro absoluto em relação à solução exata. Resultados fora desse
intervalo devem ser avaliados pelo seu próprio histórico de convergência.

## Notebook e apresentação

O notebook foi executado integralmente em um kernel Jupyter local: célula
de instalação, parâmetros, cálculo do tipo 3 em 21 relações de vãos,
apresentação e exportação. As chamadas de seleção e download de arquivos
do Google Colab ficam nos caminhos específicos desse ambiente; a execução
local usou o módulo ao lado do notebook e o link local para o ZIP.

As tabelas dos nove tipos foram exportadas para **um único Excel**, com
capa ilustrada e abas por tipo, além dos formatos de publicação. O Excel
completo, a prancha dos nove desenhos e tabelas do tipo 3 estão em `exemplos/`.
As tabelas de Bares (momentos, flecha e reações) estão em `exemplos/bares/`,
e os desenhos individuais, em `exemplos/desenhos/`.
A prancha e as figuras de tabelas foram conferidas visualmente.

Para reproduzir a varredura:

```python
from placas import gerar_tabelas
tabelas = gerar_tabelas("Todos", inicio=1, fim=2, passo=0.05)
assert all(item.tabela["convergiu"].all() for item in tabelas.values())
```
