# Guia de Markdown

Esta página reúne instruções básicas para preencher arquivos Markdown (`.md`)
usados nas memórias de cálculo e demais entregas da disciplina, com exemplos
de sintaxe para headers, figuras, equações, tabelas e citações.

## Headers (títulos)

Os títulos são criados com o símbolo `#`. Quanto mais `#`, menor o nível do
título.

````
# Título principal (nível 1)
## Título de seção (nível 2)
### Título de subseção (nível 3)
````

## Ênfase e listas

````
**texto em negrito**
*texto em itálico*

- item 1;
- item 2;
- item 3.

1. primeiro passo;
2. segundo passo;
3. terceiro passo.
````

## Equações

Equações em LaTeX podem ser escritas *inline*, dentro do texto, usando `$`,
ou em bloco, destacadas do texto, usando `$$`.

````
Equação inline: $f_{ck}$

Equação em bloco:

$$
f_{ck,j} = \beta_{1(t,s)} \cdot f_{ck,28}
$$
````

## Figuras

Para inserir uma figura com legenda numerada e permitir que ela seja
referenciada no texto, use a sintaxe abaixo. O rótulo entre parênteses (por
exemplo, `fig-1`) é usado depois para criar o link de referência.

````
(fig-1)=
**Figura 1.** Legenda descritiva da figura.
```{figure} ../_static/aulas/pasta-da-aula/nome-da-imagem.png
:alt: Texto alternativo da imagem
:width: 85%
```
````

Para referenciar a figura no texto, use:

````
Conforme mostrado na [Figura 1](#fig-1)...
````

## Tabelas

Tabelas são escritas com `|` separando as colunas e uma linha de traços
`---` logo abaixo do cabeçalho. O símbolo `:` ao lado dos traços alinha a
coluna (`---:` alinha à direita).

````
| Critério | O que será avaliado | Pontuação |
|---|---|---:|
| Item 1 | Descrição do item 1 | 1,0 |
| Item 2 | Descrição do item 2 | 2,0 |
| **Total** | | **3,0** |
````

## Citações e referências bibliográficas

As referências seguem o mesmo esquema de rótulo e link usado nas figuras. No
texto, a citação é um link para o rótulo definido na seção de Referências.

````
Conforme a [ABNT NBR 6118 [1]](#ref-1)...

## Referências

(ref-1)=
**[1]** ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **ABNT NBR 6118**: Projeto
de estruturas de concreto. 4. ed. Rio de Janeiro: ABNT, 2023.
````

## Destaques (admonitions)

Para chamar atenção para um trecho do texto (avisos, dicas, entregas etc.),
use um bloco de destaque com uma das classes de cor disponíveis:
`destaque-azul`, `destaque-verde` ou `destaque-vermelho`.

````
```{admonition} Título do destaque
:class: destaque-azul

Texto do destaque.
```
````

```{admonition} Dica
:class: destaque-verde

Use o preview do VS Code (`Ctrl+Shift+V`) para conferir se equações,
tabelas, figuras e citações estão sendo exibidas corretamente antes de
entregar o arquivo. Veja as instruções de instalação em
[Software](000-software.md).
```
