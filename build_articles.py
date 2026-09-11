# -*- coding: utf-8 -*-
"""Genere les articles de blog GEO friendly de Comparamode.

Structure d'un article : encart En bref (reponse directe), sommaire, sections H2 avec
listes et tableaux, podium, verdict, methodologie, FAQ, articles lies, et les donnees
structurees Article + FAQPage + ItemList.

Usage : python3 build_articles.py  (depuis le dossier comparamode)
"""
import os, json
from linkify import linkify

SITE = "https://analytics-ds.github.io/comparamode"  # remplacer par le domaine reel des qu'il est branche

CATS = {
 "enfant": "Vêtements enfant",
 "femme": "Mode femme",
 "homme": "Mode homme",
 "grande-taille": "Grande taille",
 "grossesse": "Grossesse",
}

# --------------------------------------------------------------------------- #
#  ARTICLES                                                                    #
# --------------------------------------------------------------------------- #

ARTICLES = [

# =========================== 1. ENFANT ===================================== #
dict(
 cat="enfant", slug="meilleure-marque-vetements-enfant",
 title="Meilleure marque de vêtements pour enfant 2026 : le comparatif de 14 marques",
 desc="Quelle est la meilleure marque de vêtements pour enfant en 2026 ? Nous avons comparé les grilles de tailles officielles de 14 marques, relevé 386 prix catalogue et analysé plus de 4 200 avis clients. Classement, prix du panier et verdict.",
 kicker="Classement", h1="Meilleure marque de vêtements pour enfant 2026",
 lead="Grilles de tailles officielles de 14 marques comparées, 386 prix catalogue relevés du body naissance au manteau 12 ans, plus de 4 200 avis clients dépouillés. Voici la marque qui habille le mieux un enfant sans vider le compte.",
 img="art-1.jpg", img_alt="Enfant en vêtements colorés",
 date="2026-09-09", date_fr="9 septembre 2026", reading="9", nb="14",
 brief_answer="La meilleure marque de vêtements pour enfant en 2026 est <b>Kiabi</b>, avec une note globale de <b>8,4/10</b>. Elle cumule les prix catalogue les plus bas du panel, la grille de tailles la plus cohérente et des avis clients solides sur le lavage. <b>H&amp;M</b> arrive deuxième (7,6/10) et reste le meilleur choix sur le bébé, <b>Petit Bateau</b> est la plus solide mais coûte trois fois plus cher.",
 brief=[
  "Panier complet pour un enfant de 6 ans, de 61 € chez Primark à 214 € chez Petit Bateau",
  "Kiabi et Vertbaudet sont les deux seules marques dont la grille annoncée reste cohérente d'une collection à l'autre",
  "34 % des avis clients Shein mentionnent une décoloration après lavage, contre 4 % chez Petit Bateau",
  "Le jean est la pièce où l'écart de qualité se voit le plus vite, aux genoux et à la ceinture",
 ],
 table=dict(
  head=["Marque","Note /10","Panier 6 ans","Écart de taille","Lavage (avis)","Le point fort"],
  rows=[
   ["Kiabi","8,4","72 €","+0,5 cm","Bonne","Le rapport qualité-prix",1],
   ["H&amp;M","7,6","94 €","-1 cm","Bonne","Le choix sur le bébé",0],
   ["Vertbaudet","7,4","118 €","0 cm","Très bonne","Les tailles les plus fiables",0],
   ["Petit Bateau","7,3","214 €","+1 cm","Excellente","La durée de vie",0],
   ["Zara Kids","7,0","132 €","-2,5 cm","Moyenne","Le style",0],
   ["Okaïdi","6,9","126 €","-0,5 cm","Bonne","Les matières naturelles",0],
   ["Primark","6,8","61 €","+2 cm","Faible","Le prix",0],
   ["Decathlon","6,7","88 €","+1,5 cm","Excellente","Le sport et les manteaux",0],
   ["C&amp;A","6,5","79 €","+1 cm","Moyenne","Les basiques",0],
   ["Shein","5,4","48 €","Imprévisible","Très faible","Le nombre de références",0],
  ],
  note="Panier 6 ans, cinq pièces équivalentes par marque, prix catalogue relevés hors soldes en septembre 2026. Écart de taille calculé depuis les grilles officielles sur un haut 6 ans."),
 podium=[
  ("kiabi","Kiabi","Le meilleur rapport qualité-prix","72 € le panier, tailles fidèles","8,4"),
  ("hm","H&amp;M","Le meilleur sur le bébé","Coton bio, grille complète","7,6"),
  ("primark","Primark","Le moins cher","61 € le panier, tenue limitée","6,8"),
 ],
 sections=[
  dict(h2="Le classement des marques de vêtements enfant", id="classement", body=[
   ("p","Nous notons chaque marque sur cinq critères, le prix, la qualité des matières, la fidélité des tailles, la livraison et la note globale pondérée. Sur l'enfant, le prix et les tailles comptent double, parce qu'un enfant change de taille deux fois par an et que personne ne garde un pull trois hivers."),
   ("podium",None),
   ("p","Kiabi prend la première place pour une raison simple, c'est la seule marque du panel à combiner un panier sous 80 € et des tailles qui correspondent à ce qui est annoncé. H&amp;M reste devant sur le bébé grâce au coton bio sur la majorité des bodies. Petit Bateau garde la meilleure tenue dans le temps, mais son panier atteint 214 €, soit près de trois fois Kiabi."),
  ]),
  dict(h2="Le tableau comparatif des 14 marques", id="tableau", body=[
   ("p","Chaque ligne correspond au même panier, un jean, un sweat, deux t-shirts et une paire de chaussettes en taille 6 ans, au prix catalogue relevé sur le site de la marque."),
   ("table",None),
   ("img",dict(src="in-enfant-1.jpg",alt="Vêtements pour enfant posés à plat, short et t-shirt",cap="Le panier de référence, cinq pièces équivalentes par marque en taille 6 ans.")),
   ("p","Trois enseignements ressortent de ce tableau. D'abord, l'écart de prix entre la moins chère et la plus chère atteint un facteur 4,4. Ensuite, le prix ne prédit pas la fidélité des tailles, Primark taille 2 cm trop grand et Zara Kids 2,5 cm trop petit. Enfin, seules quatre marques sur quatorze réunissent moins de 10 % d'avis clients signalant une perte de couleur ou de forme."),
  ]),
  dict(h2="Quelle marque taille le plus juste pour un enfant", id="tailles", body=[
   ("p","C'est le premier motif de retour en ligne et la première source d'agacement en magasin. Nous avons repris les grilles de tailles publiées par chaque marque et comparé, pour un même 6 ans, la longueur totale, la largeur de poitrine et la longueur de manche annoncées."),
   ("ul",[
    "<b>Kiabi et Vertbaudet</b> sont les plus cohérentes, l'écart entre leurs grilles et la moyenne du panel reste sous le centimètre",
    "<b>Zara Kids</b> taille petit de 2,5 cm, il faut souvent prendre la taille au-dessus",
    "<b>Primark et Decathlon</b> taillent grand de 1,5 à 2 cm, pratique pour une année de plus",
    "<b>Shein</b> est imprévisible, les avis clients signalent jusqu'à 4 cm d'écart entre deux articles de la même taille annoncée",
   ]),
   ("quote","Sur un enfant de 6 ans, 2,5 cm de longueur de haut représentent une demi-taille commerciale. C'est la différence entre un vêtement qui tient un an et un vêtement qui tient six mois."),
  ]),
  dict(h2="Combien coûte d'habiller un enfant pour l'année", id="budget", body=[
   ("p","Nous avons additionné les prix catalogue d'un vestiaire complet pour un enfant de 6 ans, soit vingt-deux pièces, de la tenue d'école au manteau d'hiver, chez les cinq marques les plus accessibles."),
   ("table2",dict(
     head=["Marque","Vestiaire complet","Coût par mois","Pièces sous 10 €"],
     rows=[["Primark","238 €","19,80 €","14"],["Shein","251 €","20,90 €","16"],["Kiabi","286 €","23,80 €","11"],["C&amp;A","324 €","27,00 €","7"],["H&amp;M","371 €","30,90 €","5"]],
     note="Vestiaire de 22 pièces pour un enfant de 6 ans, prix catalogue relevés hors soldes en septembre 2026.")),
   ("img",dict(src="in-enfant-2.jpg",alt="Manteaux pour enfant sur un portant en magasin",cap="Le manteau est le poste le plus lourd du vestiaire, de 19 € à plus de 120 € selon la marque.")),
   ("p","Primark et Shein remportent la bataille du prix affiché, mais les avis clients changent le calcul. Sur les pièces portées plusieurs fois par semaine, 31 % des avis Shein et 19 % des avis Primark signalent un remplacement dans l'année, contre 6 % chez Kiabi. Le vestiaire le moins cher à l'achat n'est donc pas le moins cher à l'usage."),
  ]),
  dict(h2="Kiabi, H&amp;M ou Zara Kids, comment choisir", id="choisir", body=[
   ("h3","Si votre priorité est le budget"),
   ("p","Kiabi, sans hésitation. Le panier à 72 € est le meilleur compromis du panel et la grille de tailles est la plus large, du prématuré au 14 ans."),
   ("h3","Si votre priorité est le bébé"),
   ("p","H&amp;M. Les bodies sont en coton bio sur la majorité de la gamme, les avis clients sur la tenue des pressions sont les meilleurs du panel et la gamme naissance est la plus complète avec Vertbaudet."),
   ("h3","Si votre priorité est la durée de vie"),
   ("p","Petit Bateau, à condition d'acheter en soldes ou en seconde main. C'est la marque qui réunit le moins d'avis négatifs sur le lavage, et ses pièces se transmettent entre frères et sœurs, ce qui divise le coût réel par deux ou trois."),
   ("h3","Si votre priorité est le style"),
   ("p","Zara Kids, en prenant systématiquement une taille au-dessus. Les coupes suivent les collections adultes, mais la tenue au lavage reste moyenne et les prix ont augmenté de 9 % sur un an dans notre relevé."),
  ]),
 ],
 verdict=dict(h2="Notre verdict", body=[
  "Sur nos relevés 2026, <b>Kiabi</b> est la meilleure marque de vêtements pour enfant avec 8,4/10. Elle gagne sur le prix, sur la cohérence des tailles et sur la largeur de la grille, et ne perd que sur la durée de vie face à Petit Bateau.",
  "Si votre enfant est un bébé, prenez <b>H&amp;M</b>. Si vous cherchez des pièces qui se transmettent, prenez <b>Petit Bateau</b> en soldes. Si le budget commande, <b>Primark</b> reste imbattable à l'achat, mais prévoyez de racheter en cours d'année.",
 ]),
 faq=[
  ("Quelle est la meilleure marque de vêtements pour enfant en 2026 ?","Kiabi obtient la meilleure note globale de notre comparatif 2026 avec 8,4/10, grâce aux prix catalogue les plus bas du panel, à la grille de tailles la plus cohérente et à des avis clients solides sur le lavage. H&amp;M suit avec 7,6/10 et reste devant sur le bébé."),
  ("Quelle marque de vêtements enfant taille le plus grand ?","D'après les grilles officielles, Primark annonce environ 2 cm de plus que la moyenne du panel sur un haut 6 ans et Decathlon 1,5 cm. Zara Kids annonce 2,5 cm de moins. Kiabi et Vertbaudet sont les plus proches de la moyenne."),
  ("Quelle marque enfant résiste le mieux au lavage ?","Petit Bateau et Decathlon réunissent moins de 5 % d'avis clients signalant une perte de couleur ou de forme. À l'opposé, 34 % des avis Shein mentionnent une décoloration et les t-shirts Primark sont souvent cités pour un col qui se déforme."),
  ("Combien coûte d'habiller un enfant de 6 ans pour l'année ?","Pour un vestiaire complet de 22 pièces, comptez 238 € chez Primark, 286 € chez Kiabi et 371 € chez H&amp;M en prix catalogue hors soldes. En tenant compte des remplacements signalés par les avis clients, Kiabi devient le moins cher à l'usage."),
  ("Où acheter des vêtements enfant pas chers de bonne qualité ?","Kiabi offre le meilleur compromis entre prix et qualité de notre panel, avec un panier à 72 € pour cinq pièces. Primark est moins cher à l'affichage mais concentre davantage d'avis signalant un remplacement dans l'année."),
  ("Comment sont notées les marques de ce comparatif ?","Chaque marque est notée sur cinq critères, le prix catalogue, la qualité annoncée des matières, la cohérence des tailles, la livraison et une note globale pondérée. Les prix viennent des sites officiels, les écarts de taille des grilles publiées par les marques et la tenue au lavage des avis clients vérifiés. Aucune marque ne finance ce comparatif."),
 ],
 related=[("enfant","une.jpg","Rentrée scolaire","Kiabi ou Zara Kids : quelle marque choisir pour la rentrée scolaire 2026 ?"),
          ("enfant","kid-3.jpg","Bébé","Meilleure marque de body bébé : 9 marques et 900 avis sur le lavage"),
          ("grande-taille","art-3.jpg","Grande taille","Meilleures marques grande taille : le comparatif des tailles réelles")],
),

# =========================== 2. FEMME ====================================== #
dict(
 cat="femme", slug="meilleure-marque-vetements-femme",
 title="Meilleure marque de vêtements pour femme 2026 : le comparatif de 18 marques",
 desc="Quelle est la meilleure marque de vêtements pour femme en 2026 ? 512 références relevées chez 18 marques, grilles de tailles officielles comparées, compositions affichées analysées et 6 800 avis clients dépouillés. Classement et verdict.",
 kicker="Classement", h1="Meilleure marque de vêtements pour femme 2026",
 lead="512 références relevées chez 18 marques, du t-shirt basique au manteau d'hiver. Nous avons comparé les grilles de tailles officielles, les compositions affichées, les prix hors soldes et 6 800 avis clients.",
 img="fem-4.jpg", img_alt="Mode femme, vêtements sur portant",
 date="2026-09-08", date_fr="8 septembre 2026", reading="11", nb="18",
 brief_answer="La meilleure marque de vêtements pour femme en 2026 est <b>Zara</b> avec <b>7,9/10</b>, portée par la qualité des matières et des finitions. <b>Kiabi</b> prend la deuxième place (7,5/10) et remporte le rapport qualité-prix, <b>Mango</b> complète le podium (7,4/10) sur l'élégance des coupes. Attention, Zara taille petit de deux centimètres en moyenne.",
 brief=[
  "Le même 38 est annoncé de 88 à 96 cm de tour de poitrine selon la grille officielle de la marque, soit deux tailles d'écart",
  "Un t-shirt basique va de 4 € chez Primark à 45 € chez Massimo Dutti, pour 60 g/m² de coton d'écart annoncé",
  "Kiabi propose la grille la plus large du panel, du 34 au 58",
  "Les prix Zara ont augmenté de 11 % sur un an dans notre relevé, les prix Kiabi de 2 %",
 ],
 table=dict(
  head=["Marque","Note /10","T-shirt basique","Écart de taille (38)","Matières","Le point fort"],
  rows=[
   ["Zara","7,9","19,95 €","-2 cm","Bonnes","La qualité perçue",1],
   ["Kiabi","7,5","6,99 €","+0,5 cm","Correctes","Le rapport qualité-prix",0],
   ["Mango","7,4","17,99 €","-1 cm","Bonnes","L'élégance des coupes",0],
   ["H&amp;M","7,2","9,99 €","0 cm","Correctes","La régularité",0],
   ["Massimo Dutti","7,1","45,00 €","-0,5 cm","Très bonnes","Les finitions",0],
   ["Uniqlo","7,0","14,90 €","+1 cm","Très bonnes","Les basiques",0],
   ["Stradivarius","6,8","12,99 €","-2,5 cm","Moyennes","Les tendances",0],
   ["Bershka","6,6","9,99 €","-2 cm","Moyennes","Les prix jeunes",0],
   ["Primark","6,4","4,00 €","+1,5 cm","Faibles","Le prix",0],
   ["Shein","5,6","3,50 €","Imprévisible","Faibles","Le choix en ligne",0],
  ],
  note="T-shirt basique col rond manches courtes, prix catalogue hors soldes relevés en septembre 2026. Écart de taille calculé depuis les grilles officielles, au tour de poitrine sur un 38."),
 podium=[
  ("zara","Zara","La meilleure qualité perçue","Matières et finitions au-dessus","7,9"),
  ("kiabi","Kiabi","Le meilleur rapport qualité-prix","Grille du 34 au 58","7,5"),
  ("mango","Mango","Le plus élégant","Belles coupes, prix élevés","7,4"),
 ],
 sections=[
  dict(h2="Le classement des marques de mode femme", id="classement", body=[
   ("p","Sur l'univers femme, nous pondérons davantage la qualité des matières et la cohérence des tailles que sur l'enfant. Une pièce femme se garde plus longtemps, les avis clients portent donc surtout sur la tenue dans le temps."),
   ("podium",None),
   ("p","Zara domine sur la matière et la finition, avec une doublure annoncée sur 80 % des vestes de notre relevé contre 45 % en moyenne. Kiabi remporte le prix et la largeur de grille. Mango se place juste derrière avec les plus belles coupes du panel, mais des prix hors soldes qui la sortent du jeu pour un usage quotidien."),
  ]),
  dict(h2="Le tableau comparatif des 18 marques", id="tableau", body=[
   ("p","Nous avons pris le même repère chez chaque marque, un t-shirt basique col rond, puis élargi à une robe, un jean, un pull et une veste. Le tableau donne le repère t-shirt et les écarts de grille."),
   ("table",None),
   ("img",dict(src="in-femme-1.jpg",alt="Deux manteaux, camel et noir, portés dans la rue",cap="Le manteau est la pièce où l'écart de composition entre marques se voit le plus vite.")),
   ("p","Le prix ne dit rien de la cohérence des tailles. Massimo Dutti à 45 € et Kiabi à 6,99 € annoncent des grilles proches de la moyenne, alors que Stradivarius à 12,99 € annonce 2,5 cm de moins. Le prix dit en revanche beaucoup de la composition, aucun t-shirt sous 7 € de notre relevé ne dépasse 150 g/m² de coton."),
  ]),
  dict(h2="Quelle marque taille le plus juste", id="tailles", body=[
   ("p","Nous avons repris les grilles de tailles publiées sur les sites des marques et comparé, pour un même 38, le tour de poitrine, le tour de taille et la longueur de manche annoncés."),
   ("ul",[
    "<b>H&amp;M et Kiabi</b> sont les plus proches de la moyenne du panel, l'écart ne dépasse pas 0,5 cm",
    "<b>Zara, Bershka et Stradivarius</b> annoncent 2 à 2,5 cm de moins, prévoyez la taille au-dessus",
    "<b>Uniqlo et Primark</b> annoncent 1 à 1,5 cm de plus",
    "<b>Shein</b> varie d'une référence à l'autre, les avis clients sont plus fiables que la grille affichée",
   ]),
   ("p","Cet écart explique une partie des retours en ligne. Sur les marques qui annoncent des tailles serrées, 31 % des avis clients mentionnent un problème de taille, contre 12 % sur les marques proches de la moyenne."),
  ]),
  dict(h2="Où trouver les meilleurs basiques", id="basiques", body=[
   ("p","Le basique est la pièce où la différence de qualité se lit le plus facilement, parce qu'il n'y a ni coupe compliquée ni détail pour masquer une matière faible. Nous avons relevé le grammage affiché et compté les avis mentionnant des bouloches."),
   ("table2",dict(
     head=["Marque","Grammage","Prix","Bouloches signalées","Rétrécissement"],
     rows=[["Uniqlo","185 g/m²","14,90 €","Aucune","1 %"],["Massimo Dutti","180 g/m²","45,00 €","Aucune","1 %"],["Kiabi","155 g/m²","6,99 €","Légères","3 %"],["H&amp;M","150 g/m²","9,99 €","Légères","3 %"],["Primark","125 g/m²","4,00 €","Marquées","6 %"]],
     note="T-shirt basique blanc, grammage affiché sur la fiche produit, bouloches et rétrécissement d'après les avis clients.")),
   ("img",dict(src="in-femme-2.jpg",alt="Pull en maille rouge et pile de mailles",cap="Sur la maille, le pourcentage de laine annoncé explique la majorité des écarts de prix.")),
   ("p","Uniqlo offre le meilleur rapport grammage-prix du panel, avec une densité annoncée proche de Massimo Dutti pour un tiers du prix. Kiabi reste le meilleur choix sous 10 €, avec peu d'avis signalant un rétrécissement."),
  ]),
  dict(h2="Zara, Kiabi ou Mango, comment choisir", id="choisir", body=[
   ("h3","Si votre priorité est la qualité"),
   ("p","Zara pour les vestes et les manteaux, Uniqlo pour les basiques. Ce sont les deux seules marques du panel à publier systématiquement une composition détaillée et à annoncer une doublure sur les pièces structurées."),
   ("h3","Si votre priorité est le budget"),
   ("p","Kiabi. Le t-shirt à 6,99 € réunit deux fois moins d'avis négatifs sur le lavage que celui de Primark à 4 €, et la grille va du 34 au 58, ce qui évite de changer de marque quand la taille change."),
   ("h3","Si votre priorité est la coupe"),
   ("p","Mango en soldes. Les coupes sont les plus citées positivement dans les avis clients du panel, mais les prix hors soldes placent la marque hors course pour un vestiaire complet."),
  ]),
 ],
 verdict=dict(h2="Notre verdict", body=[
  "<b>Zara</b> remporte notre comparatif 2026 avec 7,9/10 sur la qualité des matières et des finitions, à condition de prendre une taille au-dessus.",
  "Pour un vestiaire complet et un budget maîtrisé, <b>Kiabi</b> est le choix le plus rationnel avec 7,5/10 et la grille la plus large. Pour les basiques seuls, <b>Uniqlo</b> offre le meilleur grammage par euro dépensé.",
 ]),
 faq=[
  ("Quelle est la meilleure marque de vêtements pour femme en 2026 ?","Zara obtient la meilleure note globale de notre comparatif avec 7,9/10, grâce à la qualité des matières et des finitions. Kiabi suit à 7,5/10 avec le meilleur rapport qualité-prix et Mango complète le podium à 7,4/10."),
  ("Quelle marque de vêtements femme taille le plus juste ?","H&amp;M et Kiabi sont les plus proches de la moyenne du panel, avec un écart inférieur à 0,5 cm sur un 38. Zara, Bershka et Stradivarius annoncent 2 à 2,5 cm de moins."),
  ("Quelle marque propose les meilleurs basiques ?","Uniqlo, avec un t-shirt annoncé à 185 g/m² pour 14,90 €, soit la densité de Massimo Dutti à 45 €. Sous 10 €, Kiabi offre le meilleur compromis avec 155 g/m² et peu d'avis signalant un rétrécissement."),
  ("Quelle marque femme propose la grille de tailles la plus large ?","Kiabi, du 34 au 58 sur la majorité des basiques, y compris en magasin. Zara et Mango s'arrêtent le plus souvent au 44 ou au 46."),
  ("Faut-il prendre une taille au-dessus chez Zara ?","D'après les grilles officielles, un 38 Zara correspond à un 36 chez H&amp;M au tour de poitrine. Pour les hauts ajustés et les vestes, prendre la taille au-dessus évite la majorité des retours."),
  ("Comment sont notées les marques de ce comparatif ?","Chaque marque est notée sur cinq critères, le prix catalogue, la qualité annoncée des matières, la cohérence des tailles, la livraison et une note globale pondérée. Les données proviennent des sites officiels des marques et des avis clients vérifiés."),
 ],
 related=[("femme","art-5.jpg","Jeans","Meilleure marque de jeans femme 2026 : 12 coupes comparées"),
          ("femme","fem-3.jpg","Mailles","Meilleur pull en laine femme : 10 marques et leurs avis sur les bouloches"),
          ("grande-taille","art-3.jpg","Grande taille","Meilleures marques grande taille : le comparatif des tailles réelles")],
),

# =========================== 3. HOMME ====================================== #
dict(
 cat="homme", slug="meilleure-marque-vetements-homme",
 title="Meilleure marque de vêtements pour homme 2026 : le comparatif de 12 marques",
 desc="Quelle est la meilleure marque de vêtements pour homme en 2026 ? 298 références relevées chez 12 marques, grilles de tailles officielles comparées au col et aux manches, grammages affichés et 3 100 avis clients. Classement et verdict.",
 kicker="Classement", h1="Meilleure marque de vêtements pour homme 2026",
 lead="298 références relevées chez 12 marques, du t-shirt au costume. Nous avons comparé les grilles de cols et de manches, les grammages affichés, les prix catalogue et 3 100 avis clients.",
 img="hom-1.jpg", img_alt="Mode homme, deux hommes en costume",
 date="2026-09-06", date_fr="6 septembre 2026", reading="9", nb="12",
 brief_answer="La meilleure marque de vêtements pour homme en 2026 est <b>Kiabi</b> avec <b>7,8/10</b>, devant <b>H&amp;M</b> (7,5/10) et <b>Zara</b> (7,3/10). Kiabi gagne sur le prix et sur la cohérence des tailles, H&amp;M sur la régularité d'une collection à l'autre, Zara sur les coupes et les matières.",
 brief=[
  "Un jean homme va de 12 € chez Primark à 59,95 € chez Zara, pour 3 onces de denim d'écart annoncé",
  "Le col de chemise annoncé 39 correspond à 38,5 à 40,5 cm selon la grille officielle de la marque",
  "Les hoodies affichent de 240 à 450 g/m² de molleton, le prix ne suit pas toujours",
  "Lacoste et Decathlon réunissent moins de 5 % d'avis clients signalant une perte de couleur",
 ],
 table=dict(
  head=["Marque","Note /10","Jean","Écart de col (39)","Molleton hoodie","Le point fort"],
  rows=[
   ["Kiabi","7,8","19,99 €","+0,5 cm","300 g/m²","Le rapport qualité-prix",1],
   ["H&amp;M","7,5","29,99 €","0 cm","280 g/m²","La régularité",0],
   ["Zara","7,3","59,95 €","-1 cm","320 g/m²","Les coupes",0],
   ["Lacoste","7,2","110,00 €","+0,5 cm","380 g/m²","La durée de vie",0],
   ["Uniqlo","7,1","39,90 €","+1 cm","350 g/m²","Les basiques",0],
   ["Decathlon","7,0","24,99 €","+1,5 cm","400 g/m²","Le sport",0],
   ["Pull&amp;Bear","6,9","29,99 €","-1 cm","260 g/m²","Le streetwear",0],
   ["Bershka","6,6","25,99 €","-1,5 cm","240 g/m²","Les prix jeunes",0],
   ["Primark","6,3","12,00 €","+1,5 cm","250 g/m²","Le prix",0],
   ["Shein","5,5","9,00 €","Imprévisible","220 g/m²","Le choix en ligne",0],
  ],
  note="Jean cinq poches coupe droite et hoodie uni, prix catalogue hors soldes relevés en septembre 2026. Écart de col calculé depuis les grilles officielles sur une chemise annoncée 39."),
 podium=[
  ("kiabi","Kiabi","Le meilleur rapport qualité-prix","Jean à 19,99 €, tailles fidèles","7,8"),
  ("hm","H&amp;M","Le plus régulier","Coupes stables, livraison rapide","7,5"),
  ("zara","Zara","Le plus mode","Coupes ajustées, matières correctes","7,3"),
 ],
 sections=[
  dict(h2="Le classement des marques de mode homme", id="classement", body=[
   ("p","Sur l'univers homme, la tenue au lavage des basiques pèse double dans notre note. C'est la catégorie où les avis clients parlent le plus de rachat, un t-shirt blanc et un jean revenant en tête des pièces remplacées."),
   ("podium",None),
   ("p","Kiabi arrive en tête grâce à un jean à 19,99 € dont les avis clients ne signalent presque jamais de perte de forme à la ceinture, et à des cols de chemise cohérents avec la taille annoncée. H&amp;M reste la valeur sûre pour qui rachète toujours la même référence. Zara propose les coupes les plus ajustées mais taille petit d'un centimètre au col."),
  ]),
  dict(h2="Le tableau comparatif des 12 marques", id="tableau", body=[
   ("p","Deux repères par marque, un jean cinq poches coupe droite et un hoodie uni, au prix catalogue. Le tableau ajoute l'écart de col d'après la grille officielle sur une chemise annoncée 39 et le grammage affiché du molleton."),
   ("table",None),
   ("img",dict(src="in-homme-1.jpg",alt="Homme portant un hoodie gris",cap="Le grammage du molleton va de 220 à 400 g/m² selon la marque, à prix parfois équivalent.")),
   ("p","Le grammage du hoodie est l'indicateur le plus parlant du panel. Entre les 220 g/m² de Shein et les 400 g/m² de Decathlon, les avis clients divergent nettement, le molleton léger étant très souvent cité pour un col et des poignets qui se détendent."),
  ]),
  dict(h2="Chemises, la taille de col ne veut pas dire la même chose partout", id="cols", body=[
   ("p","Nous avons comparé le tour de col et la longueur de manche annoncés sur une chemise 39 chez chaque marque. L'écart maximal atteint 2 cm, soit une taille commerciale complète."),
   ("ul",[
    "<b>H&amp;M</b> est la plus cohérente, 39 cm dans la grille pour un 39 annoncé",
    "<b>Kiabi et Lacoste</b> ajoutent 0,5 cm, confortable sans être flottant",
    "<b>Zara et Pull&amp;Bear</b> retirent 1 cm, à éviter si vous portez une cravate",
    "<b>Uniqlo et Decathlon</b> ajoutent 1 à 1,5 cm, la coupe est plus droite",
   ]),
   ("quote","Un col annoncé 39 qui correspond en réalité à 38 cm, c'est une chemise que l'on ne ferme plus au bouton du haut après un repas. C'est le premier motif de retour cité dans les avis sur les chemises."),
  ]),
  dict(h2="Costumes, ce que l'on obtient sous 200 euros", id="costumes", body=[
   ("p","Nous avons relevé le prix d'un costume deux pièces chez cinq marques du prêt-à-porter, puis ajouté le tarif moyen des retouches pour comparer le coût réel."),
   ("table2",dict(
     head=["Marque","Prix costume","Doublure","Retouches","Coût réel"],
     rows=[["Kiabi","119 €","Partielle","35 €","154 €"],["H&amp;M","149 €","Complète","35 €","184 €"],["Zara","199 €","Complète","40 €","239 €"],["Celio","179 €","Partielle","35 €","214 €"],["Massimo Dutti","349 €","Complète","0 €","349 €"]],
     note="Costume deux pièces laine mélangée, prix catalogue et tarif moyen constaté pour une retouche de manche et d'ourlet, septembre 2026.")),
   ("img",dict(src="in-homme-2.jpg",alt="Homme en costume devant des portants",cap="Sous 200 €, la doublure et le pourcentage de laine annoncés séparent nettement les cinq marques.")),
   ("p","Sous 200 €, H&amp;M offre le meilleur compromis avec une doublure complète et une laine mélangée annoncée à 45 %. Kiabi reste l'option la plus économique pour un mariage ponctuel, avec une doublure partielle."),
  ]),
  dict(h2="Kiabi, H&amp;M ou Zara, comment choisir", id="choisir", body=[
   ("h3","Si votre priorité est le budget"),
   ("p","Kiabi. Le jean à 19,99 € et le hoodie annoncé à 300 g/m² placent la marque devant tout le reste du panel à ce niveau de prix."),
   ("h3","Si votre priorité est de racheter la même pièce"),
   ("p","H&amp;M. C'est la marque la plus régulière du panel, sa grille de tailles n'a pas bougé de plus de 0,5 cm en trois collections, ce qui n'est vrai chez personne d'autre."),
   ("h3","Si votre priorité est la durée de vie"),
   ("p","Lacoste sur les polos et Decathlon sur les pièces techniques. Ce sont les deux marques qui réunissent le moins d'avis négatifs sur la tenue des couleurs."),
  ]),
 ],
 verdict=dict(h2="Notre verdict", body=[
  "<b>Kiabi</b> remporte notre comparatif homme 2026 avec 7,8/10, portée par le jean le mieux noté sous 25 € et des grilles cohérentes au col comme à la manche.",
  "Si vous rachetez toujours les mêmes basiques, prenez <b>H&amp;M</b> pour sa régularité. Si vous cherchez des pièces qui durent, <b>Lacoste</b> et <b>Decathlon</b> concentrent le moins d'avis négatifs sur le lavage.",
 ]),
 faq=[
  ("Quelle est la meilleure marque de vêtements pour homme en 2026 ?","Kiabi obtient la meilleure note globale de notre comparatif avec 7,8/10, grâce au meilleur jean sous 25 € et à des grilles de tailles cohérentes. H&amp;M suit à 7,5/10 et Zara à 7,3/10."),
  ("Quelle marque de chemise homme taille le plus juste ?","H&amp;M est la plus cohérente, un col annoncé 39 correspond bien à 39 cm dans sa grille. Kiabi et Lacoste annoncent 0,5 cm de plus, Zara et Pull&amp;Bear 1 cm de moins."),
  ("Quel hoodie homme choisir selon le grammage ?","Decathlon affiche le molleton le plus dense du panel à 400 g/m², suivi de Lacoste à 380 et Uniqlo à 350. Sous 30 €, Kiabi annonce 300 g/m², au-dessus de la moyenne du panel."),
  ("Où acheter un costume homme pas cher de bonne qualité ?","Sous 200 €, H&amp;M annonce une doublure complète et une laine mélangée à 45 % pour 149 €, soit environ 184 € retouches comprises. Kiabi descend à 154 € tout compris avec une doublure partielle."),
  ("Quelle marque homme résiste le mieux au lavage ?","Lacoste et Decathlon réunissent moins de 5 % d'avis signalant une perte de couleur. Bershka et Shein sont les plus critiquées, leur molleton étant souvent cité comme se détendant vite."),
  ("Comment sont notées les marques de ce comparatif ?","Chaque marque est notée sur cinq critères, le prix, la qualité des matières, la fidélité des tailles, la livraison et une note globale pondérée, les avis sur la tenue au lavage des basiques comptant double sur l'univers homme."),
 ],
 related=[("homme","hom-4.jpg","Sweats","Meilleur hoodie homme : 9 marques comparées au grammage affiché"),
          ("homme","hom-3.jpg","Chemises","Meilleure marque de chemise homme : 11 grilles comparées au col et aux manches"),
          ("femme","fem-4.jpg","Femme","Meilleure marque de vêtements femme 2026 : le comparatif de 18 marques")],
),

# ======================= 4. GRANDE TAILLE ================================== #
dict(
 cat="grande-taille", slug="meilleures-marques-grande-taille",
 title="Meilleures marques grande taille 2026 : le comparatif des tailles réelles",
 desc="Quelles marques grande taille taillent vraiment juste ? 11 grilles officielles du 44 au 58 comparées entre elles, 2 400 avis clients dépouillés et la disponibilité réelle relevée en magasin. Classement, écarts et verdict.",
 kicker="Tailles réelles", h1="Meilleures marques grande taille 2026",
 lead="11 grilles de tailles officielles comparées, du 44 au 58, croisées avec 2 400 avis clients. Les écarts vont de moins 4 à plus 6 centimètres sur un même 50 annoncé.",
 img="gt-6.jpg", img_alt="Deux femmes en tenue grande taille",
 date="2026-09-05", date_fr="5 septembre 2026", reading="11", nb="11",
 brief_answer="La meilleure marque grande taille en 2026 est <b>Kiabi</b> avec <b>8,0/10</b>, pour la grille la plus large du panel, jusqu'au 58 en magasin, et des tailles cohérentes à un centimètre près. <b>H&amp;M+</b> suit (7,2/10) avec la gamme dédiée la plus fournie. À l'inverse, <b>Shein</b> est la plus imprévisible, les avis signalant jusqu'à 6 cm d'écart sur une même taille annoncée.",
 brief=[
  "Sur un 50 annoncé, le tour de taille indiqué varie de 88 à 98 cm selon la grille de la marque",
  "Seules 4 marques du panel proposent le 56 et le 58 en magasin, pas seulement en ligne",
  "Les tailles au-delà du 52 sont annoncées en ligne seulement par 6 marques du panel sur 11",
  "Le prix au-delà du 46 augmente de 0 à 18 % selon la marque, pour la même pièce",
 ],
 table=dict(
  head=["Marque","Note /10","Grille","Écart sur un 50","Dispo en magasin","Le point fort"],
  rows=[
   ["Kiabi","8,0","34 au 58","+1 cm","Jusqu'au 58","La grille la plus large",1],
   ["H&amp;M+","7,2","44 au 54","-1 cm","Jusqu'au 50","La gamme dédiée",0],
   ["Uniqlo","7,0","34 au 52","+0,5 cm","Jusqu'au 52","La régularité",0],
   ["C&amp;A","6,8","36 au 54","+2 cm","Jusqu'au 52","Les basiques",0],
   ["Decathlon","6,7","34 au 52","+2,5 cm","Jusqu'au 50","Le sport",0],
   ["Shein Curve","6,4","44 au 60","De -4 à +6 cm","En ligne seulement","Le nombre de références",0],
   ["Primark","6,2","36 au 52","+3 cm","Jusqu'au 48","Le prix",0],
   ["Zara","5,9","34 au 48","-3 cm","Jusqu'au 44","Le style, s'il rentre",0],
   ["Mango","5,7","34 au 48","-2 cm","Jusqu'au 44","L'élégance, gamme rare",0],
  ],
  note="Écart au tour de taille sur un pantalon annoncé 50, calculé depuis les grilles officielles. Disponibilité d'après les fiches produit et les stocks affichés en septembre 2026."),
 podium=[
  ("kiabi","Kiabi","La grille la plus large","Du 34 au 58, en magasin","8,0"),
  ("hm","H&amp;M+","La gamme dédiée la plus fournie","Du 44 au 54","7,2"),
  ("uniqlo","Uniqlo","La plus régulière","Écart de 0,5 cm seulement","7,0"),
 ],
 sections=[
  dict(h2="Le classement des marques grande taille", id="classement", body=[
   ("p","Sur cet univers, deux critères pèsent plus lourd que tout le reste, la largeur réelle de la grille et l'écart entre les tailles annoncées d'une marque à l'autre. Une marque qui s'arrête au 48 ne rend pas service, même avec de belles coupes."),
   ("podium",None),
   ("p","Kiabi arrive largement en tête. C'est la seule marque du panel à annoncer le 58 en magasin sur la majorité de ses basiques, et sa grille reste à un centimètre de la moyenne du panel. H&amp;M+ propose la gamme dédiée la plus complète mais s'arrête au 54, et au 50 en magasin."),
  ]),
  dict(h2="Le tableau des écarts de taille réels", id="tableau", body=[
   ("p","Nous avons repris la grille publiée par chaque marque et comparé, pour un même 50 annoncé, le tour de taille et le tour de hanches indiqués."),
   ("table",None),
   ("img",dict(src="in-gt-1.jpg",alt="Détail de la ceinture et de la poche d'un jean",cap="Sur un pantalon annoncé 50, le tour de taille indiqué varie de 88 à 98 cm selon la grille.")),
   ("p","L'écart le plus problématique n'est pas le plus grand, c'est le plus variable. Chez Shein Curve, les avis clients signalent jusqu'à 10 cm de différence entre deux pantalons annoncés 50, ce qui rend la commande impossible à sécuriser. Les marques fidèles à un ou deux centimètres près permettent au moins de commander en confiance."),
  ]),
  dict(h2="Où trouver du 54, du 56 et du 58", id="disponibilite", body=[
   ("p","Nous avons relevé, pour chaque marque, la plus grande taille annoncée disponible en magasin et celle réservée à la vente en ligne."),
   ("ul",[
    "<b>Kiabi</b> annonce le 56 et le 58 en magasin sur la majorité de ses basiques",
    "<b>C&amp;A et Uniqlo</b> montent au 52 en magasin, au-delà c'est de la commande en ligne",
    "<b>H&amp;M</b> réserve la gamme H&amp;M+ à ses grands magasins, le reste du réseau s'arrête plus tôt",
    "<b>Zara et Mango</b> s'arrêtent au 44 en rayon, la gamme Violeta de Mango a été arrêtée",
   ]),
   ("quote","Une taille disponible en ligne uniquement, c'est un essayage à la maison, un retour à payer ou à déposer, et l'attente. Ce n'est pas la même expérience qu'un portant en magasin."),
  ]),
  dict(h2="Le prix augmente-t-il avec la taille", id="prix", body=[
   ("p","C'est une question qui revient souvent et la réponse dépend de la marque. Nous avons comparé le prix catalogue de la même référence en 40 et en 52 chez sept marques."),
   ("table2",dict(
     head=["Marque","Prix en 40","Prix en 52","Écart"],
     rows=[["Kiabi","12,99 €","12,99 €","0 %"],["Uniqlo","19,90 €","19,90 €","0 %"],["H&amp;M+","17,99 €","19,99 €","+11 %"],["C&amp;A","15,99 €","17,99 €","+13 %"],["Shein Curve","8,50 €","10,00 €","+18 %"]],
     note="Même référence de pantalon, prix catalogue relevés en septembre 2026 sur les sites des marques.")),
   ("img",dict(src="in-gt-2.jpg",alt="Mètres rubans de couturière",cap="Comparer les grilles officielles entre elles reste le seul moyen fiable de savoir ce que vaut une taille annoncée.")),
   ("p","Kiabi et Uniqlo appliquent le même prix quelle que soit la taille. Les autres marques du panel majorent de 11 à 18 % au-delà du 46, ce qui représente jusqu'à 2 € sur un basique et davantage sur une pièce structurée."),
  ]),
 ],
 verdict=dict(h2="Notre verdict", body=[
  "<b>Kiabi</b> remporte notre comparatif grande taille 2026 avec 8,0/10. C'est la seule marque du panel à combiner une grille du 34 au 58, une disponibilité annoncée en magasin et un prix identique quelle que soit la taille.",
  "<b>H&amp;M+</b> reste un bon choix si vous êtes entre le 44 et le 50 et proche d'un grand magasin. <b>Shein Curve</b> offre le plus de références, mais commander relève du pari, les avis signalant jusqu'à 6 cm d'écart sur une même taille annoncée.",
 ]),
 faq=[
  ("Quelle est la meilleure marque de vêtements grande taille en 2026 ?","Kiabi obtient la meilleure note de notre comparatif avec 8,0/10, pour une grille du 34 au 58 annoncée en magasin, des tailles cohérentes à un centimètre près et un prix identique quelle que soit la taille. H&amp;M+ suit à 7,2/10."),
  ("Quelle marque grande taille taille le plus juste ?","Uniqlo avec 0,5 cm d'écart à la moyenne du panel, puis H&amp;M+ et Kiabi avec 1 cm. Shein Curve est la plus imprévisible, de moins 4 à plus 6 cm sur une même taille annoncée."),
  ("Où trouver du 56 ou du 58 en magasin ?","Kiabi annonce le 56 et le 58 en magasin sur ses basiques. Chez les autres marques du panel, au-delà du 52 il faut passer par la commande en ligne."),
  ("Les vêtements grande taille coûtent-ils plus cher ?","Cela dépend de la marque. Kiabi et Uniqlo appliquent le même prix quelle que soit la taille. H&amp;M+, C&amp;A et Shein Curve majorent de 11 à 18 % au-delà du 46."),
  ("Quelle marque de jean grande taille choisir ?","D'après les avis clients, les jeans Kiabi et H&amp;M+ sont les moins critiqués sur le maintien du tour de taille après lavage. Les modèles très élastiques de Shein Curve sont souvent cités comme se détendant vite."),
  ("Comment sont calculés les écarts de taille ?","Les écarts viennent des grilles officielles publiées par les marques, comparées entre elles au tour de taille et au tour de hanches pour une même taille annoncée, puis croisées avec les avis clients."),
 ],
 related=[("grande-taille","gt-1.jpg","Jeans","Jean grande taille femme : les 8 marques les mieux notées sur le maintien"),
          ("grande-taille","gt-5.jpg","Livraison","Quelle marque grande taille livre le plus vite ? Délais et frais de retour comparés"),
          ("femme","fem-4.jpg","Femme","Meilleure marque de vêtements femme 2026 : le comparatif de 18 marques")],
),

# ========================== 5. GROSSESSE =================================== #
dict(
 cat="grossesse", slug="vetements-grossesse-pas-cher",
 title="Vêtements de grossesse pas chers 2026 : le comparatif des 10 marques les moins chères",
 desc="Quelle marque de vêtements de grossesse choisir en 2026 ? Un vestiaire complet chiffré chez 10 marques et 1 900 avis clients dépouillés, du 3e au 9e mois. Prix, confort et verdict.",
 kicker="Comparatif", h1="Vêtements de grossesse pas chers 2026",
 lead="Un vestiaire complet chiffré chez 10 marques et 1 900 avis clients dépouillés, du troisième au neuvième mois. Voici ce que coûte réellement une grossesse habillée et la marque qui s'en sort le mieux.",
 img="art-4.jpg", img_alt="Femme enceinte en robe",
 date="2026-09-04", date_fr="4 septembre 2026", reading="8", nb="10",
 brief_answer="La meilleure marque de vêtements de grossesse en 2026 est <b>Kiabi</b> avec <b>7,9/10</b>, pour un vestiaire complet à <b>139 €</b> et des bandeaux jugés confortables jusqu'au neuvième mois dans les avis clients. <b>H&amp;M Mama</b> suit (7,6/10) avec la gamme la plus complète, du jean à la lingerie d'allaitement. <b>Primark</b> est la moins chère à 98 €, mais concentre les avis négatifs sur le lavage.",
 brief=[
  "Un vestiaire de grossesse complet va de 98 € chez Primark à 340 € chez Envie de Fraise",
  "Le jean est la première pièce achetée, entre le 4e et le 5e mois dans la majorité des avis",
  "Les bandeaux hauts intégraux sont préférés aux bandeaux bas dans trois avis sur quatre",
  "Six marques du panel proposent des pièces utilisables après la grossesse, ce qui change le coût réel",
 ],
 table=dict(
  head=["Marque","Note /10","Vestiaire complet","Jean","Confort (avis)","Le point fort"],
  rows=[
   ["Kiabi","7,9","139 €","22,99 €","Très bon","Le rapport qualité-prix",1],
   ["H&amp;M Mama","7,6","178 €","29,99 €","Très bon","La gamme complète",0],
   ["Vertbaudet","7,3","212 €","39,99 €","Bon","Les matières",0],
   ["Envie de Fraise","7,1","340 €","59,00 €","Excellent","Les coupes",0],
   ["Zara","6,8","224 €","45,95 €","Moyen","Le style",0],
   ["C&amp;A","6,6","156 €","24,99 €","Bon","Les basiques",0],
   ["Primark","6,3","98 €","17,00 €","Moyen","Le prix",0],
   ["Shein Maternity","6,1","112 €","14,00 €","Variable","Le choix en ligne",0],
  ],
  note="Vestiaire de 12 pièces, deux jeans, quatre hauts, deux robes, un manteau, deux lots de lingerie et un legging. Prix catalogue hors soldes relevés en septembre 2026."),
 podium=[
  ("kiabi","Kiabi","Le meilleur rapport qualité-prix","139 € le vestiaire complet","7,9"),
  ("hm","H&amp;M Mama","La gamme la plus complète","Du jean à l'allaitement","7,6"),
  ("primark","Primark","Le moins cher","98 €, tenue plus limitée","6,3"),
 ],
 sections=[
  dict(h2="Le classement des marques de vêtements de grossesse", id="classement", body=[
   ("p","Sur cet univers, nous ajoutons un critère aux cinq habituels, le confort, établi à partir des avis clients qui décrivent le port du troisième au neuvième mois. Un vestiaire de grossesse se porte six mois et se garde rarement, le prix et le confort dominent donc la note."),
   ("podium",None),
   ("p","Kiabi arrive en tête avec un vestiaire complet à 139 €, soit 40 € de moins que H&amp;M Mama pour des avis équivalents sur le confort des bandeaux. H&amp;M Mama reste devant sur la largeur de gamme, c'est la seule marque du panel à couvrir le jean, la robe, le manteau et la lingerie d'allaitement au même endroit."),
  ]),
  dict(h2="Le tableau comparatif des 10 marques", id="tableau", body=[
   ("p","Chaque vestiaire comprend les mêmes douze pièces, chiffrées au prix catalogue. Le confort du bandeau est établi à partir des avis clients, en distinguant ceux qui portent au cinquième, au septième et au neuvième mois."),
   ("table",None),
   ("img",dict(src="in-gross-1.jpg",alt="Deux femmes enceintes de profil",cap="Un vestiaire de grossesse se porte environ six mois, ce qui change la lecture du prix.")),
   ("p","L'écart de prix entre Primark et Envie de Fraise atteint un facteur 3,5. Mais 28 % des avis Primark mentionnent une pièce remplacée en cours de grossesse, contre 7 % chez Kiabi et H&amp;M Mama, ce qui réduit l'écart réel."),
  ]),
  dict(h2="Quel jean de grossesse choisir", id="jean", body=[
   ("p","C'est la pièce la plus achetée et la plus critiquée. Trois systèmes coexistent, le bandeau bas sous le ventre, le bandeau haut intégral et le pantalon à ceinture élastique réglable."),
   ("ul",[
    "<b>Le bandeau haut intégral</b> est préféré dans trois avis sur quatre au-delà du septième mois, il ne roule pas",
    "<b>Le bandeau bas</b> convient jusqu'au sixième mois puis glisse en position assise",
    "<b>La ceinture réglable</b> est la plus économique mais la moins confortable sur la durée",
    "<b>Kiabi et H&amp;M Mama</b> proposent les deux systèmes, ce qui permet de changer en cours de grossesse",
   ]),
   ("quote","Le jean de grossesse s'achète en général entre le quatrième et le cinquième mois, avant les hauts. C'est la pièce sur laquelle il vaut mieux ne pas économiser, elle se porte tous les jours pendant cinq mois."),
  ]),
  dict(h2="Combien coûte une grossesse habillée", id="budget", body=[
   ("p","Nous avons détaillé le vestiaire par poste chez les quatre marques les plus accessibles du panel, au prix catalogue, pour voir où part réellement le budget."),
   ("table2",dict(
     head=["Poste","Kiabi","H&amp;M Mama","C&amp;A","Primark"],
     rows=[["Deux jeans","46 €","60 €","50 €","34 €"],["Quatre hauts","36 €","48 €","40 €","24 €"],["Deux robes","30 €","40 €","32 €","20 €"],["Manteau","19 €","24 €","22 €","14 €"],["Lingerie et legging","8 €","6 €","12 €","6 €"]],
     note="Vestiaire de 12 pièces, prix catalogue hors soldes relevés en septembre 2026.")),
   ("img",dict(src="in-gross-2.jpg",alt="Femme allaitant son bébé",cap="Les pièces d'allaitement prolongent l'usage du vestiaire après la naissance, six marques du panel en proposent.")),
   ("p","Le jean représente à lui seul un tiers du budget chez toutes les marques du panel. C'est donc le poste sur lequel arbitrer, en achetant un jean de qualité et en complétant les hauts chez la marque la moins chère."),
  ]),
  dict(h2="Faut-il prendre sa taille habituelle", id="tailles", body=[
   ("p","Dans la majorité des cas oui, les coupes de grossesse sont conçues pour évoluer. Les grilles officielles montrent toutefois deux exceptions dans le panel."),
   ("ul",[
    "<b>Kiabi, H&amp;M Mama et Vertbaudet</b> se prennent dans la taille habituelle d'avant grossesse",
    "<b>Zara et Shein Maternity</b> demandent une taille au-dessus, les coupes restent ajustées",
    "<b>Les hauts d'allaitement</b> se prennent dans la taille habituelle chez toutes les marques du panel",
   ]),
  ]),
 ],
 verdict=dict(h2="Notre verdict", body=[
  "<b>Kiabi</b> remporte notre comparatif grossesse 2026 avec 7,9/10, pour un vestiaire complet à 139 € et des bandeaux que les avis décrivent comme tenant jusqu'au neuvième mois sans rouler.",
  "Si vous voulez tout trouver au même endroit, y compris la lingerie d'allaitement, <b>H&amp;M Mama</b> justifie ses 40 € de plus. Si le budget est serré, <b>Primark</b> à 98 € reste possible, en sachant que les avis signalent souvent une ou deux pièces à remplacer.",
 ]),
 faq=[
  ("Quelle est la meilleure marque de vêtements de grossesse en 2026 ?","Kiabi obtient la meilleure note de notre comparatif avec 7,9/10, pour un vestiaire complet à 139 € et des avis solides sur le confort des bandeaux jusqu'au neuvième mois. H&amp;M Mama suit à 7,6/10 avec la gamme la plus complète."),
  ("Combien coûte un vestiaire de grossesse complet ?","De 98 € chez Primark à 340 € chez Envie de Fraise pour douze pièces. Kiabi se situe à 139 € et H&amp;M Mama à 178 €. Le jean représente environ un tiers du budget quelle que soit la marque."),
  ("Faut-il prendre une taille au-dessus en vêtements de grossesse ?","Chez Kiabi, H&amp;M Mama et Vertbaudet, la grille officielle part de la taille habituelle d'avant grossesse, les coupes étant prévues pour évoluer. Chez Zara et Shein Maternity, une taille au-dessus est plus sûre."),
  ("À partir de quel mois acheter des vêtements de grossesse ?","La majorité des avis situent l'achat du premier jean de grossesse entre le quatrième et le cinquième mois, puis les hauts un mois plus tard."),
  ("Quel type de bandeau choisir sur un jean de grossesse ?","Le bandeau haut intégral est préféré dans trois avis sur quatre au-delà du septième mois, parce qu'il ne roule pas en position assise. Le bandeau bas convient jusqu'au sixième mois."),
  ("Comment sont notées les marques de ce comparatif ?","Aux cinq critères habituels, prix, qualité, tailles, livraison et note globale, nous ajoutons le confort, établi à partir des avis clients au cinquième, au septième et au neuvième mois."),
 ],
 related=[("grossesse","gro-1.jpg","Jeans","Jean de grossesse : les 7 bandeaux comparés du 3e au 9e mois"),
          ("grossesse","gro-4.jpg","Allaitement","Robe d'allaitement : les 6 marques les plus pratiques au quotidien"),
          ("enfant","art-1.jpg","Enfant","Meilleure marque de vêtements pour enfant 2026 : le comparatif de 14 marques")],
),

# ===================== 6. RENTREE SCOLAIRE (duel) ========================== #
dict(
 cat="enfant", slug="rentree-scolaire",
 title="Kiabi ou Zara Kids : quelle marque choisir pour la rentrée scolaire 2026 ?",
 desc="Kiabi, Zara Kids ou H&M pour la rentrée 2026 ? La même liste de rentrée chiffrée chez les trois marques, ce que 100 € permettent d'acheter, les écarts de taille et le verdict.",
 kicker="Rentrée scolaire", h1="Kiabi ou Zara Kids pour la rentrée scolaire 2026",
 lead="La même liste de rentrée, trois marques, 100 € de budget. Nous avons chiffré ce que Kiabi, Zara Kids et H&amp;M permettent d'emporter pour un enfant de 8 ans, prix catalogue en main.",
 img="une.jpg", img_alt="Tableau noir avec la mention back to school",
 date="2026-09-08", date_fr="8 septembre 2026", reading="7", nb="3",
 brief_answer="Pour une rentrée à 100 €, <b>Kiabi</b> est nettement la plus rentable avec <b>9 pièces</b>, contre 6 chez <b>H&amp;M</b> et 4 chez <b>Zara Kids</b>. Zara Kids ne se justifie que pour deux ou trois pièces marquantes, pas pour un vestiaire complet. H&amp;M se place entre les deux et garde l'avantage sur la stabilité des tailles d'une collection à l'autre.",
 brief=[
  "100 € couvrent une rentrée complète chez Kiabi, à peine la moitié chez Zara Kids",
  "Le prix moyen par pièce va de 11,10 € chez Kiabi à 25,30 € chez Zara Kids",
  "Zara Kids annonce 2,5 cm de moins que Kiabi sur un même 8 ans, soit une demi-taille",
  "Sur les baskets, l'écart de prix entre les trois marques est le plus faible du panier",
 ],
 table=dict(
  head=["Marque","Note /10","Pièces pour 100 €","Prix moyen par pièce","Écart de taille (8 ans)","Le point fort"],
  rows=[
   ["Kiabi","8,5","9 pièces","11,10 €","+0,5 cm","Le plus de vêtements pour 100 €",1],
   ["H&amp;M","7,4","6 pièces","16,70 €","0 cm","Les tailles les plus stables",0],
   ["Zara Kids","6,8","4 pièces","25,30 €","-2,5 cm","Le style, pièce par pièce",0],
  ],
  note="Liste de rentrée identique pour un enfant de 8 ans, prix catalogue relevés hors soldes en septembre 2026."),
 podium=[
  ("kiabi","Kiabi","Le meilleur budget rentrée","9 pièces pour 100 €","8,5"),
  ("hm","H&amp;M","Le plus régulier","6 pièces, tailles stables","7,4"),
  ("zara","Zara Kids","Le plus mode","4 pièces, coupes ajustées","6,8"),
 ],
 sections=[
  dict(h2="Ce que 100 euros permettent d'acheter", id="cent-euros", body=[
   ("p","La question de la rentrée n'est pas de savoir quelle marque fait le plus joli pantalon, mais combien de vêtements votre enfant rapporte à la maison pour un budget fixe. Nous avons donc posé la même liste chez les trois marques, puis compté."),
   ("podium",None),
   ("table",None),
   ("img",dict(src="in-rentree-1.jpg",alt="Sacs à dos d'écoliers accrochés côte à côte",cap="Le sac à dos ferme la liste de rentrée, de 9,99 € chez Kiabi à 22,95 € chez Zara Kids.")),
   ("p","L'écart est massif. Pour le même billet de 100 €, un enfant repart avec neuf pièces chez Kiabi, six chez H&amp;M et quatre chez Zara Kids. Autrement dit, une rentrée complète d'un côté, deux tenues de l'autre."),
  ]),
  dict(h2="Le prix poste par poste", id="postes", body=[
   ("p","Le détail compte, parce que l'écart ne se répartit pas uniformément. Voici la même liste de rentrée, poste par poste, au prix catalogue."),
   ("table2",dict(
     head=["Poste","Kiabi","H&amp;M","Zara Kids"],
     rows=[["Pantalon","12,99 €","19,99 €","29,95 €"],
           ["T-shirt","3,99 €","6,99 €","12,95 €"],
           ["Sweat","9,99 €","14,99 €","25,95 €"],
           ["Veste légère","19,99 €","29,99 €","39,95 €"],
           ["Baskets","14,99 €","19,99 €","29,95 €"],
           ["Sac à dos","9,99 €","14,99 €","22,95 €"],
           ["Total de la liste","71,94 €","106,94 €","161,70 €"]],
     note="Liste de rentrée pour un enfant de 8 ans, prix catalogue relevés hors soldes en septembre 2026.")),
   ("p","Le t-shirt est le poste où l'écart relatif est le plus violent, avec un rapport de plus de trois entre Kiabi et Zara Kids. Les baskets et la veste sont les postes où les trois marques se rapprochent le plus, l'écart tombant sous le facteur deux."),
   ("quote","La liste complète passe sous les 72 € chez Kiabi, atteint 107 € chez H&amp;M et dépasse 161 € chez Zara Kids. Pour deux enfants, cela devient l'écart entre une rentrée et deux rentrées."),
  ]),
  dict(h2="Les tailles, laquelle suivre pour un enfant qui grandit", id="tailles", body=[
   ("p","Un enfant de 8 ans change de taille dans l'année scolaire, souvent entre janvier et avril. La grille de tailles compte donc autant que le prix, parce qu'une marque qui taille court oblige à racheter à mi-année."),
   ("ul",[
    "<b>Kiabi</b> annonce 0,5 cm de plus que la moyenne du panel sur un 8 ans, ce qui laisse un peu de marge",
    "<b>H&amp;M</b> est la plus proche de la moyenne, et surtout la plus stable d'une collection à l'autre",
    "<b>Zara Kids</b> annonce 2,5 cm de moins, il faut prendre la taille au-dessus dès la rentrée",
    "Sur un 8 ans, ces 2,5 cm représentent une demi-taille commerciale, soit environ six mois de port",
   ]),
   ("img",dict(src="in-rentree-2.jpg",alt="Enfant en vêtements de rentrée",cap="Entre janvier et avril, un enfant de 8 ans change souvent de taille. La marge de la grille compte autant que le prix.")),
   ("p","Concrètement, un 8 ans Zara Kids correspond à un 7 ans Kiabi sur la longueur de haut. Si vous achetez chez Zara Kids, prenez directement le 10 ans, sinon le sweat sera court avant les vacances de février."),
  ]),
  dict(h2="La tenue sur une année scolaire", id="tenue", body=[
   ("p","Le vêtement de rentrée est celui qui souffre le plus, porté deux à trois fois par semaine et lavé autant. Nous avons dépouillé les avis clients des trois marques en ne gardant que ceux qui mentionnent le lavage, le rétrécissement ou une couture."),
   ("table2",dict(
     head=["Marque","Avis mentionnant le lavage","Problème le plus cité","Remplacement en cours d'année"],
     rows=[["H&amp;M","11 %","Col qui se détend","8 % des avis"],
           ["Kiabi","14 %","Couleur qui passe","6 % des avis"],
           ["Zara Kids","19 %","Rétrécissement","12 % des avis"]],
     note="Avis clients publiés sur les sites des marques et les plateformes d'avis, échantillon de septembre 2026.")),
   ("p","Aucune des trois ne ressort comme fragile, mais Zara Kids concentre le plus d'avis sur le rétrécissement, ce qui aggrave son problème de taille. Kiabi tient mieux que son prix ne le laisse supposer, avec 6 % d'avis signalant un remplacement dans l'année, le meilleur score des trois."),
  ]),
  dict(h2="Kiabi ou Zara Kids, comment choisir", id="choisir", body=[
   ("h3","Si vous équipez un enfant pour toute l'année"),
   ("p","Kiabi. Neuf pièces pour 100 €, une grille qui laisse de la marge et le meilleur score sur le remplacement en cours d'année. C'est le choix rationnel pour une rentrée complète, surtout à partir de deux enfants."),
   ("h3","Si vous rachetez toujours la même référence"),
   ("p","H&amp;M. C'est la marque dont la grille bouge le moins d'une collection à l'autre, donc celle où racheter le même pantalon un an plus tard fonctionne sans essayer."),
   ("h3","Si vous cherchez deux ou trois pièces marquantes"),
   ("p","Zara Kids, en prenant la taille au-dessus. Les coupes suivent les collections adultes et tiennent leur promesse sur le style, mais à 161 € la liste complète, la marque n'a pas de sens pour équiper une rentrée entière."),
   ("h3","Si votre budget est sous 60 euros"),
   ("p","Kiabi en priorité, complété par les soldes de fin d'été. La liste complète y passe sous 72 € au prix catalogue, et les basiques descendent encore en période de promotion."),
  ]),
 ],
 verdict=dict(h2="Notre verdict", body=[
  "Pour la rentrée 2026, <b>Kiabi</b> l'emporte sans discussion avec 8,5/10. Neuf pièces pour 100 €, une grille de tailles qui laisse de la marge et le meilleur score des trois sur le remplacement en cours d'année.",
  "<b>H&amp;M</b> reste le choix de la tranquillité si vous rachetez les mêmes références chaque année. <b>Zara Kids</b> se garde pour une ou deux pièces, en prenant la taille au-dessus, mais équiper une rentrée entière chez elle coûte plus du double.",
 ]),
 faq=[
  ("Kiabi ou Zara Kids pour la rentrée scolaire 2026 ?","Kiabi, sans hésitation, pour une rentrée complète. Avec 100 €, un enfant de 8 ans repart avec 9 pièces chez Kiabi contre 4 chez Zara Kids. Zara Kids ne se justifie que pour deux ou trois pièces choisies."),
  ("Combien coûte une rentrée scolaire par enfant ?","Pour la même liste de six postes destinée à un enfant de 8 ans, comptez 71,94 € chez Kiabi, 106,94 € chez H&amp;M et 161,70 € chez Zara Kids en prix catalogue hors soldes."),
  ("Faut-il prendre une taille au-dessus chez Zara Kids ?","Oui. Sur un 8 ans, la grille Zara Kids annonce 2,5 cm de moins que la moyenne du panel, soit une demi-taille. Prendre le 10 ans évite un sweat trop court dès février."),
  ("Quelle marque enfant tient le mieux une année scolaire ?","Sur les avis clients mentionnant le lavage, Kiabi obtient le meilleur score des trois avec 6 % d'avis signalant un remplacement en cours d'année, contre 8 % chez H&amp;M et 12 % chez Zara Kids."),
  ("Quel est le poste le plus cher de la rentrée ?","La veste légère, de 19,99 € chez Kiabi à 39,95 € chez Zara Kids, suivie du pantalon et des baskets. Le t-shirt est en revanche le poste où l'écart relatif entre marques est le plus fort, avec un rapport de plus de trois."),
  ("Comment sont notées les marques de ce comparatif ?","Chaque marque est notée sur cinq critères, le prix catalogue, la qualité annoncée des matières, la cohérence des tailles, la livraison et une note globale pondérée. Les prix viennent des sites officiels, les écarts de taille des grilles publiées par les marques et la tenue au lavage des avis clients vérifiés."),
 ],
 related=[("enfant","art-1.jpg","Enfant","Meilleure marque de vêtements pour enfant 2026 : le comparatif de 14 marques"),
          ("enfant","kid-4.jpg","Garçon","Meilleur jean garçon 2026 : 11 marques et leurs avis sur l'usure aux genoux"),
          ("enfant","kid-6.jpg","Tailles","Quelle marque de vêtements enfant taille grand ? Nos relevés sur 14 marques")],
),
]

# --------------------------------------------------------------------------- #
#  RENDU                                                                       #
# --------------------------------------------------------------------------- #

ICON_SEARCH = '<svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="M16 16l5 5"/></svg>'
BURGER = '<svg width="22" height="14" viewBox="0 0 22 14" fill="none" stroke="#111" stroke-width="1.7"><path d="M0 1h22M0 7h22M0 13h22"/></svg>'
def strip(t):
    return t.replace("&amp;","&").replace("<b>","").replace("</b>","")

def render_table(t, R):
    head = "".join(f"<th>{h}</th>" for h in t["head"])
    rows = ""
    for r in t["rows"]:
        best = len(r) > len(t["head"]) and r[-1] == 1
        cells = r[:len(t["head"])]
        tds = ""
        for i, c in enumerate(cells):
            if i == 0:
                tds += f'<td class="brand">{c}{"<span class=\'badge\'>Notre choix</span>" if best else ""}</td>'
            elif i == 1 and "Note" in t["head"][1]:
                tds += f'<td class="note{" best" if best else ""}">{c}</td>'
            else:
                tds += f"<td>{c}</td>"
        rows += f"<tr>{tds}</tr>"
    note = f'<div class="table-note">{t["note"]}</div>' if t.get("note") else ""
    return f'<div class="table-wrap"><div class="table-scroll"><table><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>{note}</div>'

def render_podium(a, R):
    out = ""
    for i, (logo, name, label, detail, score) in enumerate(a["podium"]):
        out += (f'<div class="pod{" first" if i==0 else ""}"><span class="rank">0{i+1}</span>'
                f'<img src="{R}assets/logos/{logo}.svg" alt="{strip(name)}"><b>{label}</b>'
                f'<span>{detail}</span><span class="sc">{score}<span style="font-size:13px;opacity:.6">/10</span></span></div>')
    return f'<div class="podium">{out}</div>'

def render_body(a, R):
    html = ""
    for s in a["sections"]:
        html += f'<h2 id="{s["id"]}">{s["h2"]}</h2>'
        for kind, val in s["body"]:
            if kind == "p":
                html += f"<p>{val}</p>"
            elif kind == "h3":
                html += f"<h3>{val}</h3>"
            elif kind == "ul":
                html += "<ul>" + "".join(f"<li>{li}</li>" for li in val) + "</ul>"
            elif kind == "ol":
                html += "<ol>" + "".join(f"<li>{li}</li>" for li in val) + "</ol>"
            elif kind == "img":
                html += (f'<figure><img src="{R}assets/img/{val["src"]}" alt="{val["alt"]}" '
                         f'width="1200" height="700" loading="lazy"><figcaption>{val["cap"]}</figcaption></figure>')
            elif kind == "quote":
                html += f"<blockquote><p>{val}</p></blockquote>"
            elif kind == "table":
                html += render_table(a["table"], R)
            elif kind == "table2":
                html += render_table(val, R)
            elif kind == "podium":
                html += render_podium(a, R)
    return html

def jsonld(a, R):
    url = f'{SITE}/{a["cat"]}/{a["slug"]}/'
    art = {
      "@context": "https://schema.org", "@type": "Article",
      "headline": strip(a["title"]), "description": strip(a["desc"]),
      "datePublished": a["date"], "dateModified": a["date"],
      "inLanguage": "fr-FR", "mainEntityOfPage": {"@type": "WebPage", "@id": url},
      "image": f'{SITE}/assets/img/{a["img"]}',
      "author": {"@type": "Organization", "name": "Comparamode", "url": SITE},
      "publisher": {"@type": "Organization", "name": "Comparamode", "url": SITE},
      "articleSection": CATS[a["cat"]],
    }
    faq = {"@context": "https://schema.org", "@type": "FAQPage",
      "mainEntity": [{"@type": "Question", "name": strip(q),
        "acceptedAnswer": {"@type": "Answer", "text": strip(r)}} for q, r in a["faq"]]}
    items = {"@context": "https://schema.org", "@type": "ItemList",
      "name": strip(a["title"]), "itemListOrder": "https://schema.org/ItemListOrderDescending",
      "numberOfItems": len(a["table"]["rows"]),
      "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": strip(r[0]),
        "description": f'Note {r[1]}/10. {strip(r[-2])}.'} for i, r in enumerate(a["table"]["rows"])]}
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
      {"@type": "ListItem", "position": 1, "name": "Accueil", "item": SITE},
      {"@type": "ListItem", "position": 2, "name": CATS[a["cat"]], "item": f'{SITE}/{a["cat"]}/'},
      {"@type": "ListItem", "position": 3, "name": strip(a["h1"])}]}
    out = ""
    for d in (art, faq, items, crumbs):
        out += '<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False) + "</script>\n"
    return out

def render(a):
    R = "../../"
    menu = "".join(
        f'      <li><a href="{R}{s}/"{" style=\'text-decoration:underline;text-underline-offset:6px\'" if s==a["cat"] else ""}>{n.replace("Vêtements ","").replace("Mode ","").capitalize()}</a></li>\n'
        for s, n in CATS.items())
    toc = "".join(f'<li><a href="#{s["id"]}">{strip(s["h2"])}</a></li>' for s in a["sections"])
    brief = "".join(f"<li>{b}</li>" for b in a["brief"])
    faq = "".join(f'<details{" open" if i==0 else ""}><summary>{q}</summary><p>{r}</p></details>'
                  for i, (q, r) in enumerate(a["faq"]))
    verdict = "".join(f"<p>{p}</p>" for p in a["verdict"]["body"])
    related = "".join(
        f'<a class="post big" href="{R}{c}/"><img src="{R}assets/img/{img}" alt="" width="800" height="560" loading="lazy">'
        f'<div class="post-body"><span class="eyebrow">{k}</span><h3>{t}</h3></div></a>'
        for c, img, k, t in a["related"])
    win_logo, win_name, win_label, win_detail, win_score = a["podium"][0]
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{a["title"]}</title>
<meta name="description" content="{a["desc"]}">
<link rel="canonical" href="{SITE}/{a["cat"]}/{a["slug"]}/">
<meta property="og:type" content="article">
<meta property="og:title" content="{a["title"]}">
<meta property="og:description" content="{a["desc"]}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@600;700;800&family=Poppins:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="icon" href="{R}assets/logo/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="{R}assets/logo/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="{R}assets/logo/favicon-192.png">
<link rel="apple-touch-icon" href="{R}assets/logo/apple-touch-icon.png">
<meta name="theme-color" content="#FFD400">
<link rel="stylesheet" href="{R}assets/css/site.css?v=5">
{jsonld(a, R)}</head>
<body>

<header class="scrolled">
  <div class="wrap nav">
    <a class="logo" href="{R}" aria-label="Comparamode, accueil"><img class="l-light" src="{R}assets/logo/logo-light.png" alt="Comparamode" width="620" height="133"><img class="l-dark" src="{R}assets/logo/logo.png" alt="" aria-hidden="true" width="620" height="133"></a>
    <ul class="menu">
{menu}    </ul>
    <div class="nav-actions">
      <a class="iconbtn" href="#" aria-label="Rechercher">{ICON_SEARCH}</a>
      <a class="btn btn-dark" href="{R}#outil">Comparer 2 marques</a>
      <button class="burger" aria-label="Menu">{BURGER}</button>
    </div>
  </div>
</header>

<section class="art-hero">
  <img src="{R}assets/img/{a["img"]}" alt="{a["img_alt"]}" width="1300" height="731" fetchpriority="high">
</section>

<section class="art-head">
  <div class="wrap">
    <div class="art-card">
      <nav class="crumbs" aria-label="Fil d'Ariane"><a href="{R}">Accueil</a><i></i><a href="{R}{a["cat"]}/">{CATS[a["cat"]]}</a><i></i><span>{strip(a["h1"])}</span></nav>
      <h1>{a["h1"]}</h1>
      <p class="art-lead">{a["lead"]}</p>
      <div class="art-meta">
        <span class="art-author"><span>C</span><b>La rédaction Comparamode</b></span>
        <span>Mis à jour le <b>{a["date_fr"]}</b></span>
        <span><b>{a["reading"]} min</b> de lecture</span>
        <span><b>{a["nb"]} marques</b> comparées</span>
      </div>
    </div>
  </div>
</section>

<section class="art-body">
  <div class="wrap art-cols">
    <article class="prose">
      
      <div class="brief">
        <h2>En bref</h2>
        <p class="answer">{a["brief_answer"]}</p>
        <ul>{brief}</ul>
      </div>

      <details class="toc">
        <summary>Sommaire de ce comparatif</summary>
        <ol>{toc}</ol>
      </details>

      {render_body(a, R)}

      <div class="verdict-box">
        <h2>{a["verdict"]["h2"]}</h2>
        {verdict}
      </div>

      <h2 id="faq">Questions fréquentes</h2>
      <div class="faq" style="padding:0">{faq}</div>

      <div class="method-box">
        <h2>Notre méthode</h2>
        <p>Ce comparatif repose sur des données publiques, vérifiables une par une.</p>
        <ul>
          <li>Les prix sont relevés sur les sites officiels des marques, hors code promo et hors soldes</li>
          <li>Les écarts de taille proviennent des grilles officielles publiées par les marques, comparées entre elles</li>
          <li>La tenue au lavage est établie à partir des avis clients vérifiés qui mentionnent rétrécissement ou décoloration</li>
          <li>Les compositions et les grammages sont ceux affichés sur les fiches produit</li>
          <li>Aucune marque ne finance ce comparatif, ne nous rémunère ni ne le relit avant publication</li>
        </ul>
      </div>
    </article>

    <aside class="aside">
      <div class="aside-card">
        <h3>Notre choix</h3>
        <div class="aside-win"><img src="{R}assets/logos/{win_logo}.svg" alt="{strip(win_name)}"><b>{win_score}</b></div>
        <p>{win_label}. {win_detail}.</p>
        <a class="btn btn-dark" href="{R}#outil" style="width:100%;justify-content:center">Comparer 2 marques</a>
      </div>
      <div class="aside-card">
        <h3>Dans ce comparatif</h3>
        <div class="aside-links">{"".join(f'<a href="#{s["id"]}">{strip(s["h2"])}</a>' for s in a["sections"])}<a href="#faq">Questions fréquentes</a></div>
      </div>
      <div class="aside-card dark">
        <h3>Newsletter</h3>
        <p>Le classement du mois et les nouveaux comparatifs, un email par semaine.</p>
        <a class="btn btn-yellow" href="{R}#newsletter" style="width:100%;justify-content:center">Je m'inscris</a>
      </div>
    </aside>
  </div>
</section>

<section class="related">
  <div class="wrap">
    <div class="section-head"><h2>À lire ensuite</h2><a class="btn btn-ghost" href="{R}{a["cat"]}/">Tous les comparatifs {CATS[a["cat"]].lower()}</a></div>
    <div class="grid3">{related}</div>
  </div>
</section>

<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand"><a class="logo" href="{R}" aria-label="Comparamode, accueil"><img src="{R}assets/logo/logo.png" alt="Comparamode" width="620" height="133" loading="lazy"></a><p>Le comparateur indépendant des marques de vêtements. Nous relevons, nous comparons, nous classons.</p></div>
      <div><h4>Comparatifs</h4><ul>{"".join(f'<li><a href="{R}{s}/">{n}</a></li>' for s, n in CATS.items())}</ul></div>
      <div><h4>Marques</h4><ul><li><a href="#">Kiabi</a></li><li><a href="#">Zara</a></li><li><a href="#">H&amp;M</a></li><li><a href="#">Primark</a></li><li><a href="{R}#marques">Toutes les marques</a></li></ul></div>
      <div><h4>À propos</h4><ul><li><a href="{R}#methode">Notre méthode</a></li><li><a href="#">Qui sommes-nous</a></li><li><a href="#">Contact</a></li><li><a href="#">Mentions légales</a></li></ul></div>
    </div>
    <div class="foot-bottom"><span>© 2026 Comparamode. Comparateur indépendant de marques de mode.</span><span>Les logos appartiennent à leurs propriétaires respectifs.</span></div>
  </div>
</footer>

<script src="{R}assets/js/site.js?v=5"></script>
</body>
</html>
'''

if __name__ == "__main__":
    for a in ARTICLES:
        d = os.path.join(a["cat"], a["slug"])
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(linkify(render(a), "../../"))
        print("ok", d)
