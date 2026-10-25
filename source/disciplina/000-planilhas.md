# Planilhas de cálculo

Esta página reúne as planilhas de apoio da disciplina. Use-as para consultar
coeficientes e conferir cálculos do [trabalho prático](000-trabalho-pratico.md).
A memória de cálculo continua sendo sua: registre de onde veio cada valor.

```{admonition} Planilha de tabelas de lajes
:class: destaque-azul

{download}`Baixar a planilha de tabelas de lajes (Excel) <../_static/aulas/esforcos-lajes/Tabelas_lajes.xlsx>`
```

## Tabelas de lajes

A planilha traz os coeficientes de lajes retangulares com carga uniforme,
calculados pela solução de placa da disciplina com **coeficiente de Poisson
$\nu=0{,}20$**. Ela cobre os nove tipos de vinculação (bordas apoiadas ou
engastadas), com $\lambda=l_y/l_x$ de 1,00 a 2,00, a cada 0,05. O uso dos
coeficientes está explicado na [Aula 06](../aulas/006-esforcos-lajes.md).

| Aba | Conteúdo |
|---|---|
| **Capa** | Desenho dos nove tipos de laje e links para as demais abas. |
| **Bares mx, my, mx neg, my neg** | Momentos fletores: $m=\mu\,p\,l_x^2/100$. Uma tabela por coeficiente, com os tipos lado a lado. |
| **Bares mxy** | Momento volvente nos cantos entre bordas apoiadas, usado na armadura de canto. |
| **Bares aw** | Coeficiente da flecha elástica: $w=\alpha_w\,p\,l_x^4/(100\,E\,h^3)$. |
| **Bares kx, kx eng, ky, ky eng** | Reações médias nas bordas apoiadas e engastadas: $r=k\,p\,l_x/10$. |
| **Tipo 1 a Tipo 6** | Todos os resultados de uma vinculação, incluindo o volvente de cada canto com sinal. |
| **Precisao, Convergencia, Extremos, Metadados** | Dados de verificação do cálculo; não são necessários para o uso no trabalho. |

Nas abas Bares, o traço indica que o coeficiente não existe naquele tipo, por
exemplo, momento negativo em uma laje sem engaste. Os valores podem diferir
ligeiramente das tabelas de Bares e Pinheiro, que adotam outro coeficiente de
Poisson. Em uma mesma memória de cálculo, não misture coeficientes das duas
fontes.
