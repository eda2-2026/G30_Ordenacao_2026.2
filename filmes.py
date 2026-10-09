import csv
import os

CAMINHO_CSV_PADRAO = os.path.join(os.path.dirname(__file__), "movies.csv")


class Filme:
    def __init__(self, codigo, titulo, ano, genero):
        self.codigo = codigo
        self.titulo = titulo
        self.ano = ano
        self.genero = genero

    def __str__(self):
        return f"[{self.codigo:>7}] {self.titulo} ({self.ano}) - {self.genero}"


def _extrair_ano(release_date):
    """'2009-12-10' -> 2009. Datas ausentes/mal formadas viram 0."""
    release_date = (release_date or "").strip()
    if len(release_date) >= 4 and release_date[:4].isdigit():
        return int(release_date[:4])
    return 0


def carregar_filmes(caminho_csv=CAMINHO_CSV_PADRAO):
    filmes = []
    with open(caminho_csv, newline="", encoding="utf-8") as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)
        for linha in leitor:
            genero = linha["genres"].strip() or "Desconhecido"
            filmes.append(
                Filme(
                    codigo=int(linha["id"]),
                    titulo=linha["title"],
                    ano=_extrair_ano(linha["release_date"]),
                    genero=genero,
                )
            )
    return filmes
