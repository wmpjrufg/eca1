# Tabelas de Bares

Esta página reúne as tabelas de Bares da disciplina, em Excel, para consultar
os coeficientes de lajes e conferir os cálculos do
[trabalho prático](000-trabalho-pratico.md). A memória de cálculo continua
sendo sua: registre de onde veio cada valor.

```{admonition} Tabelas de Bares da disciplina
:class: destaque-azul

{download}`Baixar as tabelas de Bares (Excel) <../_static/aulas/esforcos-lajes/Tabelas_lajes.xlsx>`
```

## O que as tabelas contêm

As tabelas trazem os coeficientes de lajes retangulares com carga uniforme,
no formato de Bares, calculados pela solução de placa da disciplina com
**coeficiente de Poisson $\nu=0{,}20$**. Elas cobrem os nove tipos de
vinculação (bordas apoiadas ou engastadas), com $\lambda=l_y/l_x$ de 1,00 a
2,00, a cada 0,05. O uso dos coeficientes está explicado na
[Aula 05](../aulas/005-esforcos-lajes.md).

| Aba | Conteúdo |
|---|---|
| **Capa** | Desenho dos nove tipos de laje e links para as demais abas. |
| **Bares mx, my, mx neg, my neg** | Momentos fletores: $m=\mu\,p\,l_x^2/100$. Uma tabela por coeficiente, com os tipos lado a lado. |
| **Bares mxy** | Momento volvente nos cantos entre bordas apoiadas, usado na armadura de canto. |
| **Bares aw** | Coeficiente da flecha elástica: $w=\alpha_w\,p\,l_x^4/(100\,E\,h^3)$. |
| **Bares kx, kx eng, ky, ky eng** | Reações médias nas bordas apoiadas e engastadas: $r=k\,p\,l_x/10$. |
| **Tipo 1 a Tipo 6** | Todos os resultados de uma vinculação, incluindo o volvente de cada canto com sinal. |

O traço indica que o coeficiente não existe naquele tipo, por exemplo,
momento negativo em uma laje sem engaste. Os valores podem diferir
ligeiramente das tabelas de Bares adaptadas por Pinheiro, que adotam outro
coeficiente de Poisson. Em uma mesma memória de cálculo, não misture
coeficientes das duas fontes.
