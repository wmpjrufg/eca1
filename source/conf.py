# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "_ext"))

project = "ECA 1 - Estruturas de Concreto Armado 1"
copyright = "2026, Wanderlei Malaquias Pereira Jr."
author = "Wanderlei Malaquias Pereira Jr."

language = "pt_BR"

extensions = [
    "myst_parser",
    "solucao_trabalho",
]

# Liberação da solução do trabalho: altere False para True após cada entrega.
# Uma linha removida ou comentada equivale a False. Depois, gere/publique o site.
solucao_entregas_liberadas = {
    1: True,  # Pré-dimensionamento, vãos efetivos e cargas
    2: False,  # Esforços e descarregamento nas vigas
    3: False,  # Cisalhamento, fissuração e flecha com armadura mínima
    4: False,  # Dimensionamento à flexão e verificações finais
    5: False,  # Detalhamento e consolidação
}

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "deflist",
    "colon_fence",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_book_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]

html_theme_options = {
    "repository_url": "https://github.com/wmpjrufg/ECA1",
    "use_repository_button": True,
    "use_download_button": False,
    "home_page_in_toc": True,
}

html_title = "ECA 1"
