# -*- coding: utf-8 -*-
"""Table des articles publies et remplacement automatique des href="#".

Chaque generateur appelle linkify() avant d'ecrire un fichier. Un lien reste en "#"
tant que l'article correspondant n'existe pas, ce qui evite les liens morts.
"""
import re

# fragment de titre  ->  chemin de l'article depuis la racine du site
LINKS = [
 ("Meilleure marque de vêtements pour enfant 2026", "enfant/meilleure-marque-vetements-enfant/"),
 ("Meilleure marque de vêtements femme 2026",       "femme/meilleure-marque-vetements-femme/"),
 ("Meilleure marque de vêtements homme 2026",       "homme/meilleure-marque-vetements-homme/"),
 ("Meilleures marques grande taille",               "grande-taille/meilleures-marques-grande-taille/"),
 ("Vêtements de grossesse pas chers",               "grossesse/vetements-grossesse-pas-cher/"),
]

_A = re.compile(r'<a([^>]*?)href="#"([^>]*?)>(.*?)</a>', re.S)

def linkify(html, prefix=""):
    """Remplace href="#" par l'URL de l'article quand le libelle du lien le designe."""
    def sub(m):
        before, after, inner = m.group(1), m.group(2), m.group(3)
        for frag, url in LINKS:
            if frag in inner:
                return f'<a{before}href="{prefix}{url}"{after}>{inner}</a>'
        return m.group(0)
    return _A.sub(sub, html)
