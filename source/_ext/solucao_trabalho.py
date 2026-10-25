"""Inclui no site somente as entregas explicitamente liberadas pelo professor."""

from pathlib import Path

from sphinx.errors import ConfigError, ExtensionError


ENTREGAS = {
    1: "Pré-dimensionamento, vãos efetivos e cargas nas lajes",
    2: "Esforços nas lajes e descarregamento nas vigas",
    3: "Checagens iniciais com armadura mínima",
    4: "Dimensionamento à flexão e verificações finais",
    5: "Detalhamento das lajes e consolidação",
}
DOCUMENTO = "disciplina/000-solucao-trabalho"


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


def incluir_entregas(app, docname, source):
    if docname != DOCUMENTO:
        return

    pasta = Path(app.srcdir).parent / "professor" / "solucao-trabalho"
    texto = source[0]
    for numero, titulo in ENTREGAS.items():
        marcador = f"<!-- solucao:entrega-{numero} -->"
        if texto.count(marcador) != 1:
            raise ExtensionError(f"Esperado um único marcador {marcador} em {DOCUMENTO}.")

        arquivo = pasta / f"entrega-{numero}.md"
        # Também detecta edições dos arquivos em builds incrementais.
        app.env.note_dependency(str(arquivo))
        if app.config.solucao_entregas_liberadas.get(numero, False):
            if not arquivo.is_file():
                raise ExtensionError(f"Solução liberada sem arquivo: {arquivo}")
            conteudo = arquivo.read_text(encoding="utf-8")
        else:
            conteudo = (
                f"## Entrega {numero}: {titulo}\n\n"
                "A solução desta entrega ainda não foi liberada.\n"
            )
        texto = texto.replace(marcador, conteudo, 1)
    source[0] = texto


def setup(app):
    app.add_config_value("solucao_entregas_liberadas", {}, "env", types=[dict])
    app.connect("config-inited", validar_configuracao)
    app.connect("source-read", incluir_entregas)
    return {"version": "1.0", "parallel_read_safe": True, "parallel_write_safe": True}
