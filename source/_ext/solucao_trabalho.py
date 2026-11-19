"""Inclui no site somente as entregas explicitamente liberadas pelo professor.

Cada entrega é uma página própria (``disciplina/000-solucao-entrega-N``), que
aparece como subitem de "Solução do trabalho" no menu lateral. O arquivo da
página contém apenas o marcador ``<!-- solucao:entrega-N -->``; o texto vem de
``professor/solucao-trabalho/entrega-N.md`` quando a entrega está liberada.
"""

import re
from pathlib import Path

from sphinx.errors import ConfigError, ExtensionError


ENTREGAS = {
    1: "Pré-dimensionamento, vãos efetivos e cargas nas lajes",
    2: "Esforços nas lajes e descarregamento nas vigas",
    3: "Checagens iniciais com armadura mínima",
    4: "Dimensionamento à flexão e verificações finais",
    5: "Detalhamento das lajes e consolidação",
}
DOCUMENTOS = {f"disciplina/000-solucao-entrega-{numero}": numero for numero in ENTREGAS}
TITULO = re.compile(r"^(#{2,6})(\s)")


def validar_configuracao(app, config):
    liberadas = config.solucao_entregas_liberadas
    if not isinstance(liberadas, dict) or any(
        type(numero) is not int
        or numero not in ENTREGAS
        or type(liberada) is not bool
        for numero, liberada in liberadas.items()
    ):
        raise ConfigError(
            "solucao_entregas_liberadas deve ser um dicionário com chaves "
            "de 1 a 5 e valores True ou False (sem aspas)."
        )


def preparar_conteudo(texto):
    """Remove o título da entrega e sobe um nível dos demais títulos.

    No arquivo da entrega, o título é de nível 2 (##) e as etapas são de nível
    3 (###). Na página própria, o título (nível 1) vem do cabeçalho gerado
    aqui e as etapas passam a nível 2, que é o que o menu da direita lista.
    Linhas dentro de blocos de código não são alteradas.
    """
    linhas = texto.splitlines()
    saida, em_bloco, titulo_removido = [], False, False
    for linha in linhas:
        if linha.lstrip().startswith(("```", "~~~")):
            em_bloco = not em_bloco
        elif not em_bloco and linha.startswith("#"):
            if not titulo_removido and linha.startswith("## "):
                titulo_removido = True
                continue
            if TITULO.match(linha) and linha.startswith("###"):
                linha = linha[1:]
        saida.append(linha)
    return "\n".join(saida).strip() + "\n"


def incluir_entrega(app, docname, source):
    numero = DOCUMENTOS.get(docname)
    if numero is None:
        return

    marcador = f"<!-- solucao:entrega-{numero} -->"
    texto = source[0]
    if texto.count(marcador) != 1:
        raise ExtensionError(f"Esperado um único marcador {marcador} em {docname}.")

    arquivo = Path(app.srcdir).parent / "professor" / "solucao-trabalho" / f"entrega-{numero}.md"
    # Também detecta edições dos arquivos em builds incrementais.
    app.env.note_dependency(str(arquivo))
    cabecalho = f"# Entrega {numero}: {ENTREGAS[numero]}\n\n"
    if app.config.solucao_entregas_liberadas.get(numero, False):
        if not arquivo.is_file():
            raise ExtensionError(f"Solução liberada sem arquivo: {arquivo}")
        conteudo = cabecalho + preparar_conteudo(arquivo.read_text(encoding="utf-8"))
    else:
        conteudo = cabecalho + "A solução desta entrega ainda não foi liberada.\n"
    source[0] = texto.replace(marcador, conteudo, 1)


def setup(app):
    app.add_config_value("solucao_entregas_liberadas", {}, "env", types=[dict])
    app.connect("config-inited", validar_configuracao)
    app.connect("source-read", incluir_entrega)
    return {"version": "2.0", "parallel_read_safe": True, "parallel_write_safe": True}
