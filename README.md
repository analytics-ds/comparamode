# Comparamode

Comparateur indépendant de marques de mode. Site statique, sans dépendance ni build.

## Structure

| Chemin | Rôle |
|---|---|
| `index.html` | Page d'accueil (hero, bandeau de marques, outil de comparaison, classement, méthode) |
| `enfant/`, `femme/`, `homme/`, `grande-taille/`, `grossesse/` | Pages catégorie |
| `<catégorie>/<slug>/` | Articles comparatifs |
| `assets/css/site.css` | Feuille de style unique |
| `assets/js/site.js` | Zoom du hero, bandeau défilant, header au scroll |
| `assets/img/`, `assets/logos/` | Images et logos de marques |

## Régénérer les pages

Les pages catégorie et les articles sont générés depuis des fichiers de données.

```bash
python3 build_categories.py   # les 5 pages catégorie
python3 build_articles.py     # les articles comparatifs
```

`linkify.py` branche automatiquement les liens internes vers les articles publiés. Un lien
reste en `#` tant que l'article correspondant n'existe pas, ce qui évite les liens morts.

## Avant mise en ligne publique

- Remplacer les chiffres de démonstration (notes, prix, volumes d'avis) par de vrais relevés
- Remplacer les images par des visuels dont les droits sont acquis
- Mettre `SITE` dans `build_articles.py` sur le domaine définitif, puis régénérer
- Compléter les mentions légales

## Développement local

```bash
python3 -m http.server 8778
```
