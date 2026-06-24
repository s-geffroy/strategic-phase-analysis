#!/usr/bin/env python3
"""Génère le dossier `docs/` du site MkDocs à partir de la source de vérité.

Source de vérité : method/, cases/, outputs/, publication/, README.md.
Le vocabulaire métallurgique (bijection interne) est confiné à UNE SEULE page :
`docs/annexe-scientifique.md`. Toutes les autres pages publiques sont vérifiées
contre la liste de termes interdits ; toute fuite fait échouer le build.
"""
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

# Termes métallurgiques interdits hors annexe scientifique.
FORBIDDEN = [
    "ferritic", "austenitic", "pearlitic", "bainitic", "martensitic", "cementitic",
    "ferritique", "austénitique", "perlitique", "bainitique", "martensitique", "cémentitique",
]

# Titres FR des cas (clé = nom de dossier).
CASE_TITLES = {
    "p0_red_sea_bab_el_mandeb": "Mer Rouge / Bab el-Mandeb",
    "p0_hormuz": "Détroit d'Ormuz",
    "p0_taiwan_semiconductors_south_china_sea": "Taïwan / semi-conducteurs / mer de Chine",
    "p0_ukraine_black_sea_grain_energy": "Ukraine / mer Noire / céréales / énergie",
}

# Pages de méthode PUBLIQUES (01–06). 07 (bijection) et 08 (vocabulaire) -> annexe.
METHOD_PUBLIC = {
    "01_method_specification.md": "Spécification de la méthode",
    "02_phase_taxonomy.md": "Taxonomie des phases",
    "03_scoring_rules.md": "Règles de scoring",
    "04_transition_watch_rules.md": "Règles de transition watch",
    "05_evidence_requirements.md": "Exigences de preuve",
    "06_validation_rules.md": "Règles de validation",
    "09_method_corrections_log.md": "Journal de corrections & feuille V1.1",
}

# Ordre d'assemblage des fichiers d'un cas dans sa page.
CASE_FILE_ORDER = [
    ("00_short_diagnostic.md", None),
    ("01_full_analytical_fiche.md", None),
    ("03_decision_synthesis.md", None),
    ("04_evidence_notes.md", None),
    ("05_validation_log.md", None),
]


def write(rel_path: str, content: str):
    path = DOCS / rel_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


REPO_BLOB = "https://github.com/s-geffroy/strategic-phase-analysis/blob/main"


def build_index():
    readme = read(ROOT / "README.md")
    # Les fichiers de dépôt (licences, contributing) ne sont pas des pages du site :
    # on pointe vers GitHub pour éviter les liens cassés en build --strict.
    for target in ("CONTRIBUTING.md", "LICENSE-CONTENT.md", "LICENSE"):
        readme = readme.replace(f"]({target})", f"]({REPO_BLOB}/{target})")
    write("index.md", readme)


def build_method():
    for filename, title in METHOD_PUBLIC.items():
        src = ROOT / "method" / filename
        if src.exists():
            write(f"methode/{filename}", read(src))


def build_cases():
    cases_dir = ROOT / "cases"
    for case_dir in sorted(p for p in cases_dir.iterdir() if p.is_dir()):
        title = CASE_TITLES.get(case_dir.name, case_dir.name)
        parts = [
            f"# {title}",
            "",
            "!!! warning \"Statut : revue analyste requise\"",
            "    Cette fiche est **préremplie et sourcée** mais n'est pas validée. "
            "Conformément à la méthode, le diagnostic final doit être validé par un analyste humain.",
            "",
        ]
        for filename, _ in CASE_FILE_ORDER:
            fpath = case_dir / filename
            if fpath.exists():
                parts.append(read(fpath).strip())
                parts.append("\n---\n")
        # Bloc machine YAML en fin de page.
        yaml_path = case_dir / "02_machine_output.yaml"
        if yaml_path.exists():
            parts.append("## Bloc machine (YAML)\n")
            parts.append("```yaml\n" + read(yaml_path).strip() + "\n```")
        write(f"cas/{case_dir.name}.md", "\n".join(parts))


def build_matrix():
    md_path = ROOT / "outputs" / "comparative_matrix_p0.md"
    intro = (
        "# Matrice comparative P0\n\n"
        "Synthèse comparative des quatre cas P0, générée à partir des blocs machine "
        "(`02_machine_output.yaml`). Les scores sont des indicateurs d'appui (0–5), "
        "pas des mesures.\n\n"
    )
    body = read(md_path) if md_path.exists() else ""
    # On retire le H1 du fichier généré pour éviter un double titre.
    body = "\n".join(line for line in body.splitlines() if not line.startswith("# "))
    write("matrice.md", intro + body)


def build_publication():
    pub_dir = ROOT / "publication"
    mapping = {
        "01_scientific_publication_explanation.md": "Angle — publication scientifique",
        "02_conflits_publication_explanation.md": "Angle — publication grand public",
        "03_article_scientifique.md": "Article scientifique",
        "04_article_grand_public.md": "Article grand public",
    }
    for filename in mapping:
        src = pub_dir / filename
        if src.exists():
            write(f"publication/{filename}", read(src))


def build_annex():
    """Seule page autorisée à contenir le vocabulaire métallurgique."""
    parts = [
        "# Annexe scientifique — origine analogique",
        "",
        "!!! note \"Usage\"",
        "    Cette annexe documente l'origine conceptuelle de la méthode. Le vocabulaire "
        "métallurgique **n'apparaît jamais dans les diagnostics publics** : il est réservé "
        "à cette annexe méthodologique, conformément aux règles de publication.",
        "",
    ]
    for filename in ("07_internal_public_bijection.md", "08_publication_vocabulary_rules.md"):
        src = ROOT / "method" / filename
        if src.exists():
            parts.append(read(src).strip())
            parts.append("\n---\n")
    write("annexe-scientifique.md", "\n".join(parts))


def guard_forbidden_terms():
    """Échoue si un terme métallurgique apparaît hors de l'annexe scientifique."""
    leaks = []
    for md in DOCS.rglob("*.md"):
        if md.name == "annexe-scientifique.md":
            continue
        text = md.read_text(encoding="utf-8").lower()
        for term in FORBIDDEN:
            if term in text:
                leaks.append((md.relative_to(DOCS), term))
    if leaks:
        print("[FAIL] Termes métallurgiques détectés hors annexe :")
        for rel, term in leaks:
            print(f"  - {rel} : '{term}'")
        sys.exit(1)
    print("[OK] Aucun terme interdit hors annexe scientifique.")


def main():
    if DOCS.exists():
        shutil.rmtree(DOCS)
    DOCS.mkdir(parents=True)

    build_index()
    build_method()
    build_cases()
    build_matrix()
    build_publication()
    build_annex()
    guard_forbidden_terms()
    print(f"[OK] Site généré dans {DOCS}")


if __name__ == "__main__":
    main()
