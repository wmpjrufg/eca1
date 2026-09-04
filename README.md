# ECA 1 — Estruturas de Concreto Armado 1

Repositório das aulas e materiais da disciplina de Estruturas de Concreto Armado 1. O site é gerado com [Sphinx](https://www.sphinx-doc.org/) a partir de arquivos Markdown (MyST) e publicado automaticamente no GitHub Pages a cada push em `main`.

## Estrutura

```
source/
  conf.py           # configuração do Sphinx
  index.md          # página inicial / índice (toctree)
  aulas/            # arquivos .md de cada aula
    001-introducao.md
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

## Build local

```bash
pip install -r requirements.txt
sphinx-build -b html source build/html
# ou, usando o Makefile:
make html
```

O resultado fica em `build/html/index.html`.

## Publicação

O workflow em `.github/workflows/pages.yml` builda o site e publica no GitHub Pages a cada push em `main`. É necessário habilitar, uma única vez, em **Settings → Pages → Build and deployment → Source: GitHub Actions**.
