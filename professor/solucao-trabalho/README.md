# Controle da solução do trabalho

Edite `source/conf.py` e altere somente os valores das entregas que deseja liberar:

```python
solucao_entregas_liberadas = {
    1: True,
    2: False,
    3: False,
    4: False,
    5: False,
}
```

Use `True` e `False` com inicial maiúscula, sem aspas, pois o arquivo é Python.
Comentar ou remover a linha de uma entrega também a mantém oculta. As liberações
são independentes: liberar a Entrega 2 não libera automaticamente a Entrega 1.

Edite a solução de cada entrega no respectivo `entrega-N.md` desta pasta. Os
links para as aulas usam `../aulas/`, pois o texto é renderizado na página
`source/disciplina/000-solucao-trabalho.md`. Mantenha os títulos de entrega em
nível 2 (`##`) e as etapas em nível 3 (`###`).

Gere o site com `sphinx-build -b html source build/html` e confira
`build/html/disciplina/000-solucao-trabalho.html`. No fluxo atual, o push em
`main` reconstrói e publica o site pelo GitHub Actions. Para retirar uma parte
já liberada, volte seu valor para `False` e publique novamente.

Os arquivos desta pasta ficam fora de `source/`. Só o conteúdo marcado como
`True` é incluído na página, na busca e nos artefatos gerados pelo Sphinx.
Não há ocultação por CSS, JavaScript ou caixas recolhíveis. O controle vale para
o site publicado: se o repositório for público, estes arquivos e seu histórico
continuam acessíveis pelo GitHub. Conteúdo já publicado também pode ter sido salvo.

## Hipóteses e limites da memória

As cotas confirmadas pelo professor são 585, 620, 510 e 485 **cm**, apesar da
unidade impressa na figura. A solução de referência adota lajes maciças e
numeração L1/L2 na linha superior e L3/L4 na inferior. O pré-dimensionamento usa
12 cm inicialmente, sem antecipar aprovação em ELS.

O professor confirmou que todas as paredes ficam sobre as vigas. Não há carga
de alvenaria diretamente nas lajes. A altura livre e os trechos ocupados por
paredes ainda dependem da definição das vigas e da arquitetura. As parcelas
dependentes desses dados são mantidas explicitamente nas equações. As etapas 2 a 5 apresentam a
solução analítica, exemplos identificados e os critérios de conferência; não
devem ser interpretadas como um projeto executivo fechado de todos os painéis.
Os momentos e as áreas de aço do pavimento-tipo foram calculados para o caso
de duas bordas adjacentes contínuas. Complete as reações e os dados do modelo
das vigas, as verificações de serviço e o caso da cobertura antes de liberar
o fechamento numérico final. As aulas 02, 03, 05, 06, 07, 08,
09 e 10 são as referências; mantém-se a edição normativa adotada no curso.
