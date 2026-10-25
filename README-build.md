# ECA 1 — Estruturas de Concreto Armado 1

Repositório das aulas e materiais da disciplina de Estruturas de Concreto Armado 1. O site é gerado com [Sphinx](https://www.sphinx-doc.org/) a partir de arquivos Markdown (MyST) e publicado automaticamente no GitHub Pages a cada push em `main`.

## Estrutura

```
source/
  conf.py           # configuração do Sphinx
  index.md          # página inicial / índice (toctree)
  aulas/            # arquivos .md de cada aula
    001-hist-prop.md
```

## Adicionando uma nova aula

1. Crie um arquivo `.md` em `source/aulas/`, por exemplo `source/aulas/002-flexao-simples.md`.
2. Adicione o nome do arquivo (sem extensão) ao `toctree` em `source/index.md`.
3. Equações em LaTeX funcionam nativamente (extensão `dollarmath`/`amsmath` do MyST):

   ```markdown
   $$
   f_{ck,j} = \beta_{1(t,s)} \cdot f_{ck,28}
   $$
   ```

## Gerador de tabelas de placas para o Colab

O [gerador de coeficientes de placas](ferramentas/placas/README.md) resolve
a equação de Kirchhoff–Love com Poisson de 0,20 e exporta um Excel único,
com capa ilustrada e abas por tipo de laje, incluindo reações. Exporta também
CSV, LaTeX e desenhos em PDF/SVG/PNG para as aulas. As funções ficam em
`ferramentas/placas/placas.py`; o notebook `Gerar_tabelas_placas.ipynb`
contém apenas a preparação, a seleção e a produção dos resultados.

## Build local do site

```bash
pip install -r requirements.txt
sphinx-build -b html source build/html
# ou, usando o Makefile:
make html
```

O resultado fica em `build/html/index.html`.

## Solução do trabalho: liberação por entrega

A página **Solução do trabalho** aparece no menu da disciplina. Para publicar
uma parte, altere a entrega correspondente de `False` para `True` em
`source/conf.py`, no dicionário `solucao_entregas_liberadas`, e reconstrua o site
(ou publique pelo fluxo de push em `main`). Todas começam ocultas.

Os textos ficam em `professor/solucao-trabalho/entrega-N.md`. Consulte as
[instruções de edição e liberação](professor/solucao-trabalho/README.md), incluindo
o alcance do controle quando o repositório é público.

## Publicação no GitHub Pages

O workflow em `.github/workflows/pages.yml` builda o site e publica no GitHub Pages a cada push em `main`. É necessário habilitar, uma única vez, em **Settings → Pages → Build and deployment → Source: GitHub Actions**.
