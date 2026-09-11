# -*- coding: utf-8 -*-
"""Genere les pages categorie (enfant, femme, homme, grande-taille, grossesse) a partir d'un template unique.
Usage : python3 build_categories.py  (a lancer depuis le dossier comparamode)"""
import os, html
from linkify import linkify

CATS = [
 dict(slug="enfant", menu="Enfant", nom="Vêtements enfant", h1="Les meilleures marques de <em>vêtements pour enfant</em>",
  title="Meilleures marques de vêtements pour enfant 2026 : comparatifs et classement",
  desc="Comparatifs de marques de vêtements pour enfant et bébé, Kiabi, Zara Kids, H&M, Primark. Prix relevés, tailles réelles mesurées, tenue au lavage. Le classement 2026 des meilleures marques enfant.",
  intro="Bébé, fille, garçon, rentrée des classes. Nous comparons les grilles de tailles officielles, les prix catalogue et les avis clients avant de classer les marques.",
  hero="cat-enfant-hero.jpg", hero_alt="Deux enfants en vêtements colorés",
  subnav=["Bébé 0-3 ans","Fille","Garçon","Rentrée scolaire","Manteaux &amp; doudounes","Pyjamas","Chaussures"], count="12 comparatifs",
  une_h2="Le comparatif enfant à la une",
  feat=dict(img="art-1.jpg", tag="Classement", h2="Meilleure marque de vêtements pour enfant 2026 : le comparatif de 14 marques",
   p="Kiabi, Zara Kids, H&amp;M, Vertbaudet, Okaïdi, Petit Bateau, Primark. Prix relevés en magasin, tailles mesurées sur 386 pièces, tenue après cinq lavages. Une marque sort nettement du lot sur le rapport qualité-prix.",
   meta="14 marques comparées · 9 min de lecture · Mis à jour le 9 septembre 2026"),
  side=[("une.jpg","Rentrée scolaire","Kiabi ou Zara Kids : quelle marque choisir pour la rentrée scolaire 2026 ?","7 min de lecture"),
        ("kid-3.jpg","Bébé","Meilleure marque de body bébé : 9 marques et 900 avis sur le lavage","8 min de lecture"),
        ("kid-2.jpg","Manteaux","Doudoune enfant pas chère : le comparatif des 8 marques les plus chaudes","10 min de lecture"),
        ("kid-6.jpg","Tailles","Quelle marque de vêtements enfant taille grand ? Nos relevés sur 14 marques","6 min de lecture")],
  grid_h2="Tous les comparatifs vêtements enfant",
  grid=[("kid-1.jpg","Fêtes","Tenue de fête enfant : quelle marque pour Noël et les anniversaires sans se ruiner ?","Robes, chemises et chaussures vernies chez 7 marques, du panier à 45 € au panier à 180 € en prix catalogue.","7 marques","8 min"),
        ("kid-4.jpg","Garçon","Meilleur jean garçon 2026 : 11 marques et leurs avis sur l'usure aux genoux","Le genou qui troue, c'est le premier motif de rachat. Nous avons dépouillé les avis clients pièce par pièce.","11 marques","9 min"),
        ("kid-5.jpg","Anniversaire","Vêtements enfant pas chers : les 6 marques où habiller toute la fratrie pour moins de 150 €","Trois enfants, un panier complet par marque, prix catalogue relevés hors soldes.","6 marques","7 min"),
        ("kid-2.jpg","Manteaux","Doudoune enfant pas chère : le comparatif des 8 marques les plus chaudes","Grammage annoncé, déperlance et prix, du modèle à 25 € au modèle à 120 €.","8 marques","10 min"),
        ("kid-3.jpg","Bébé","Meilleure marque de body bébé : 9 marques et 900 avis sur le lavage","Rétrécissement, boutons pression et douceur du coton d'après 900 avis clients.","9 marques","8 min"),
        ("kid-6.jpg","Tailles","Quelle marque de vêtements enfant taille grand ? Nos relevés sur 14 marques","Un 6 ans qui va du 5 au 7 ans selon la marque : le tableau complet des écarts.","14 marques","6 min")],
  rank_h2="Le classement des marques de vêtements enfant en septembre 2026",
  rank_p="Note globale sur 10 sur le seul univers enfant. Les critères prix et tailles pèsent davantage que sur l'adulte : un enfant change de taille deux fois par an.",
  rank=[("kiabi","Kiabi","Le meilleur rapport qualité-prix enfant","Prix les plus bas du panel, tailles fidèles, tenue correcte au lavage.","8,4","up","▲ +0,2"),
        ("hm","H&amp;M","Le plus large choix bébé","Coton bio sur la majorité des bodies, prix un cran au-dessus.","7,6","flat","= 0,0"),
        ("zara","Zara","Le plus mode","Coupes adultes en miniature, mais tailles petites et prix élevés.","7,0","down","▼ -0,3"),
        ("primark","Primark","Le moins cher","Panier imbattable, tenue au lavage en retrait sur les imprimés.","6,8","up","▲ +0,1"),
        ("decathlon","Decathlon","Le plus solide","Imbattable sur le sport et les manteaux, gamme ville limitée.","6,7","flat","= 0,0")],
  cta_h2="Kiabi ou H&amp;M pour vos enfants ?", cta_p="Comparez deux marques enfant sur nos cinq critères en un clic.",
  faq_h2="Questions fréquentes sur les marques de vêtements enfant",
  faq=[("Quelle est la meilleure marque de vêtements pour enfant en 2026 ?","Sur nos relevés 2026, Kiabi obtient la meilleure note globale de l'univers enfant (8,4/10) grâce aux prix les plus bas du panel et à des tailles fidèles. H&amp;M suit sur le bébé, Zara Kids sur le style. Le détail est dans notre comparatif de 14 marques."),
       ("Quelle marque de vêtements enfant taille le plus grand ?","Sur 14 marques mesurées, l'écart entre la taille annoncée et la taille réelle va de moins 2 cm à plus 4 cm sur un 6 ans. Kiabi et Vertbaudet taillent le plus juste, Zara Kids taille petit, Primark taille grand."),
       ("Quelle marque enfant résiste le mieux au lavage ?","Nous lavons chaque pièce cinq fois à 40 °C et mesurons le rétrécissement et la tenue des couleurs. Petit Bateau et Decathlon sont les plus stables, les imprimés Primark et Shein sont les plus fragiles."),
       ("Comment sont notées les marques ?","Cinq critères sur 10 : prix, qualité, fidélité des tailles, livraison et note globale pondérée. Les prix viennent des sites officiels, les écarts de taille des grilles publiées par les marques et la tenue au lavage des avis clients. Aucune marque ne finance nos comparatifs."),
       ("Où acheter des vêtements enfant pas chers de bonne qualité ?","Pour un panier complet à moins de 100 € par enfant, Kiabi et Primark sont les deux options les plus économiques de notre panel, Kiabi gardant l'avantage sur la tenue au lavage.")],
  news_h2="Recevez chaque comparatif enfant avant tout le monde"),

 dict(slug="femme", menu="Femme", nom="Mode femme", h1="Les meilleures marques de <em>vêtements pour femme</em>",
  title="Meilleures marques de vêtements pour femme 2026 : comparatifs et classement",
  desc="Comparatifs de marques de mode femme, Zara, Mango, H&M, Kiabi, Stradivarius. Prix relevés, tailles réelles mesurées, tenue au lavage. Le classement 2026 des meilleures marques femme.",
  intro="Jeans, robes, manteaux, basiques. Nous comparons les grilles de tailles officielles, les compositions affichées, les prix catalogue et les avis clients, puis nous classons les marques sur les mêmes critères.",
  hero="cat-femme-hero.jpg", hero_alt="Femme en manteau jaune",
  subnav=["Jeans","Robes","Manteaux","Pulls &amp; mailles","Lingerie","Sport","Petits prix"], count="18 comparatifs",
  une_h2="Le comparatif femme à la une",
  feat=dict(img="fem-4.jpg", tag="Classement", h2="Meilleure marque de vêtements femme 2026 : le comparatif de 18 marques",
   p="Zara, Mango, H&amp;M, Kiabi, Stradivarius, Bershka, Primark, Shein. Prix relevés trois fois dans l'année, tailles mesurées sur 512 pièces, tenue après cinq lavages. Le podium n'est pas celui qu'on attend.",
   meta="18 marques comparées · 11 min de lecture · Mis à jour le 8 septembre 2026"),
  side=[("art-5.jpg","Jeans","Meilleure marque de jeans femme 2026 : 12 coupes comparées","10 min de lecture"),
        ("fem-2.jpg","Bureau","Zara ou Mango : quelle marque choisir pour une garde-robe de bureau ?","8 min de lecture"),
        ("fem-3.jpg","Mailles","Meilleur pull en laine femme : 10 marques et leurs avis sur les bouloches","9 min de lecture"),
        ("fem-6.jpg","Tailles","Quelle marque de vêtements femme taille le plus juste ? Nos relevés sur 18 marques","6 min de lecture")],
  grid_h2="Tous les comparatifs mode femme",
  grid=[("fem-1.jpg","Basiques","Meilleure marque de t-shirt femme : 15 basiques et 2 000 avis","Rétrécissement, déformation du col et tenue du blanc d'après les avis, du t-shirt à 5 € au t-shirt à 45 €.","15 marques","8 min"),
        ("fem-5.jpg","Manteaux","Manteau femme pas cher : le comparatif des 9 marques les plus chaudes","Grammage et composition affichés, du modèle à 40 € au modèle à 190 €.","9 marques","10 min"),
        ("fem-2.jpg","Bureau","Zara ou Mango : quelle marque choisir pour une garde-robe de bureau ?","Cinq tenues complètes par marque, prix catalogue et avis clients croisés.","2 marques","8 min"),
        ("fem-3.jpg","Mailles","Meilleur pull en laine femme : 10 marques et leurs avis sur les bouloches","Pourcentage de laine annoncé, bouloches signalées dans les avis et prix au gramme.","10 marques","9 min"),
        ("art-5.jpg","Jeans","Meilleure marque de jeans femme 2026 : 12 coupes comparées","Tour de taille et longueur d'entrejambe annoncés, du 34 au 46, avis croisés.","12 marques","10 min"),
        ("fem-6.jpg","Tailles","Quelle marque de vêtements femme taille le plus juste ? Nos relevés sur 18 marques","Un 38 qui va du 36 au 40 selon la marque, le tableau complet des écarts.","18 marques","6 min")],
  rank_h2="Le classement des marques de mode femme en septembre 2026",
  rank_p="Note globale sur 10 sur le seul univers femme. La qualité des matières et la fidélité des tailles pèsent autant que le prix.",
  rank=[("zara","Zara","La meilleure qualité perçue","Matières et finitions au-dessus du panel, tailles petites, prix en hausse.","7,9","flat","= 0,0"),
        ("kiabi","Kiabi","Le meilleur rapport qualité-prix","Basiques solides à petit prix, grille de tailles la plus large.","7,5","up","▲ +0,3"),
        ("mango","Mango","Le plus élégant","Belles coupes, prix élevés hors soldes.","7,4","up","▲ +0,1"),
        ("hm","H&amp;M","Le plus régulier","Peu d'écarts d'une collection à l'autre, livraison rapide.","7,2","flat","= 0,0"),
        ("stradivarius","Stradivarius","Le plus tendance","Renouvellement rapide, qualité inégale selon les pièces.","6,8","down","▼ -0,2")],
  cta_h2="Zara ou Kiabi pour votre garde-robe ?", cta_p="Comparez deux marques femme sur nos cinq critères en un clic.",
  faq_h2="Questions fréquentes sur les marques de mode femme",
  faq=[("Quelle est la meilleure marque de vêtements pour femme en 2026 ?","Sur nos relevés 2026, Zara obtient la meilleure note globale (7,9/10) sur la qualité des matières, Kiabi la meilleure note sur le rapport qualité-prix (7,5/10). Le détail est dans notre comparatif de 18 marques."),
       ("Quelle marque de vêtements femme taille le plus juste ?","Sur 18 marques mesurées, l'écart entre la taille annoncée et la taille réelle va de moins 3 cm à plus 3 cm sur un 38. Kiabi et H&amp;M taillent le plus juste, Zara et Stradivarius taillent petit."),
       ("Quelle marque femme propose la meilleure qualité pour le prix ?","Kiabi sur les basiques et les jeans, Mango en soldes sur les manteaux et la maille. Shein est la moins chère mais la plus fragile au lavage."),
       ("Comment sont notées les marques ?","Cinq critères sur 10 : prix, qualité, fidélité des tailles, livraison et note globale pondérée. Les données proviennent des sites officiels des marques et des avis clients vérifiés."),
       ("Quelle marque de jeans femme choisir ?","Sur 12 coupes essayées et mesurées, les jeans Kiabi et H&amp;M gardent le mieux leur taille après lavage. Zara offre les coupes les plus mode mais rétrécit en longueur.")],
  news_h2="Recevez chaque comparatif femme avant tout le monde"),

 dict(slug="homme", menu="Homme", nom="Mode homme", h1="Les meilleures marques de <em>vêtements pour homme</em>",
  title="Meilleures marques de vêtements pour homme 2026 : comparatifs et classement",
  desc="Comparatifs de marques de mode homme, Kiabi, H&M, Zara, Pull&Bear, Bershka. Prix relevés, tailles réelles mesurées, tenue au lavage. Le classement 2026 des meilleures marques homme.",
  intro="Jeans, chemises, costumes, sweats. Nous comparons les grilles de tailles officielles, les grammages affichés, les prix catalogue et les avis clients avant de classer les marques.",
  hero="cat-homme-hero.jpg", hero_alt="Homme en costume dans la rue",
  subnav=["Jeans","Chemises","Costumes","Sweats &amp; hoodies","Sport","Chaussures","Grandes tailles"], count="9 comparatifs",
  une_h2="Le comparatif homme à la une",
  feat=dict(img="hom-1.jpg", tag="Classement", h2="Meilleure marque de vêtements homme 2026 : le comparatif de 12 marques",
   p="Kiabi, H&amp;M, Zara, Pull&amp;Bear, Bershka, Primark, Decathlon, Lacoste. Prix relevés en magasin et en ligne, tailles mesurées sur 298 pièces, tenue après cinq lavages.",
   meta="12 marques comparées · 9 min de lecture · Mis à jour le 6 septembre 2026"),
  side=[("hom-4.jpg","Sweats","Meilleur hoodie homme : 9 marques comparées au grammage affiché","8 min de lecture"),
        ("hom-2.jpg","Mailles","Meilleur pull homme pas cher : 8 marques et leurs avis sur le lavage","7 min de lecture"),
        ("hom-5.jpg","Vestes","Veste en cuir homme : vrai cuir ou simili, 7 marques comparées","9 min de lecture"),
        ("hom-6.jpg","Costumes","Costume homme pas cher : quelle marque pour un mariage à moins de 200 € ?","10 min de lecture")],
  grid_h2="Tous les comparatifs mode homme",
  grid=[("hom-3.jpg","Chemises","Meilleure marque de chemise homme : 11 grilles comparées au col et aux manches","Longueur de manche et tour de col annoncés, du 37 au 45, avis croisés.","11 marques","8 min"),
        ("hom-1.jpg","Costumes","Meilleure marque de costume homme : 8 marques du prêt-à-porter comparées","Composition affichée, doublure, retouches et prix, du costume à 120 € au costume à 450 €.","8 marques","11 min"),
        ("hom-4.jpg","Sweats","Meilleur hoodie homme : 9 marques comparées au grammage affiché","Du molleton annoncé à 280 g à celui à 450 g, bouloches et rétrécissement d'après les avis.","9 marques","8 min"),
        ("hom-2.jpg","Mailles","Meilleur pull homme pas cher : 8 marques et leurs avis sur le lavage","Pourcentage de laine annoncé, bouloches et déformation du col d'après les avis.","8 marques","7 min"),
        ("hom-5.jpg","Vestes","Veste en cuir homme : vrai cuir ou simili, 7 marques comparées","Étiquettes, composition et prix, vrai cuir contre simili.","7 marques","9 min"),
        ("hom-6.jpg","Costumes","Costume homme pas cher : quelle marque pour un mariage à moins de 200 € ?","Trois silhouettes complètes par marque, retouches chiffrées.","5 marques","10 min")],
  rank_h2="Le classement des marques de mode homme en septembre 2026",
  rank_p="Note globale sur 10 sur le seul univers homme. La tenue au lavage des basiques compte double, c'est ce qui se rachète le plus.",
  rank=[("kiabi","Kiabi","Le meilleur rapport qualité-prix","Basiques et jeans solides, prix les plus bas du panel.","7,8","up","▲ +0,2"),
        ("hm","H&amp;M","Le plus régulier","Coupes stables, livraison rapide, prix modérés.","7,5","flat","= 0,0"),
        ("zara","Zara","Le plus mode","Coupes ajustées, matières correctes, tailles petites.","7,3","down","▼ -0,1"),
        ("pullbear","Pull&amp;Bear","Le plus décontracté","Streetwear accessible, qualité inégale.","6,9","up","▲ +0,1"),
        ("bershka","Bershka","Le plus jeune","Renouvellement rapide, tenue au lavage limitée.","6,6","flat","= 0,0")],
  cta_h2="Kiabi ou H&amp;M pour vous habiller ?", cta_p="Comparez deux marques homme sur nos cinq critères en un clic.",
  faq_h2="Questions fréquentes sur les marques de mode homme",
  faq=[("Quelle est la meilleure marque de vêtements pour homme en 2026 ?","Sur nos relevés 2026, Kiabi obtient la meilleure note globale de l'univers homme (7,8/10) sur le rapport qualité-prix. H&amp;M suit sur la régularité, Zara sur le style."),
       ("Quelle marque de vêtements homme taille le plus grand ?","Sur 12 marques mesurées, Kiabi et H&amp;M taillent le plus juste, Zara et Pull&amp;Bear taillent petit, Decathlon taille grand."),
       ("Quelle marque homme résiste le mieux au lavage ?","Nous lavons chaque pièce cinq fois à 40 °C. Lacoste et Decathlon sont les plus stables, Bershka et Shein les plus fragiles."),
       ("Comment sont notées les marques ?","Cinq critères sur 10 : prix, qualité, fidélité des tailles, livraison et note globale pondérée. Les données proviennent des sites officiels des marques et des avis clients vérifiés."),
       ("Où acheter un costume homme pas cher de bonne qualité ?","Pour un costume complet à moins de 200 €, Kiabi et H&amp;M sont les deux options les plus économiques de notre panel, avec des retouches simples sur les manches.")],
  news_h2="Recevez chaque comparatif homme avant tout le monde"),

 dict(slug="grande-taille", menu="Grande taille", nom="Grande taille", h1="Les meilleures marques de <em>vêtements grande taille</em>",
  title="Meilleures marques de vêtements grande taille 2026 : comparatifs des tailles réelles",
  desc="Comparatifs de marques grande taille femme et homme, Kiabi, H&M, Shein, Zara. Tailles réelles mesurées du 44 au 58, prix relevés, tenue au lavage. Le classement 2026 des meilleures marques grande taille.",
  intro="Du 44 au 58. Nous comparons les grilles annoncées entre elles, nous croisons les avis clients et nous relevons les prix avant de classer les marques.",
  hero="cat-grande-taille-hero.jpg", hero_alt="Deux femmes en tenue grande taille",
  subnav=["Femme grande taille","Homme grande taille","Jeans","Robes","Lingerie","Sport","Guide des tailles"], count="7 comparatifs",
  une_h2="Le comparatif grande taille à la une",
  feat=dict(img="gt-6.jpg", tag="Tailles réelles", h2="Meilleures marques grande taille 2026 : le comparatif des tailles réelles",
   p="Kiabi, H&amp;M, Shein, Zara, Mango, Primark, Decathlon. 11 grilles officielles du 44 au 58 comparées entre elles et croisées avec 2 400 avis clients. Les écarts vont de moins 4 cm à plus 6 cm sur un même 50.",
   meta="11 marques comparées · 11 min de lecture · Mis à jour le 5 septembre 2026"),
  side=[("gt-1.jpg","Jeans","Jean grande taille femme : les 8 marques qui ne compriment pas la taille","9 min de lecture"),
        ("gt-3.jpg","Duel","Kiabi ou H&amp;M+ : qui taille le plus juste au-delà du 46 ?","7 min de lecture"),
        ("gt-4.jpg","Robes","Robe grande taille pas chère : 7 marques comparées du 46 au 56","8 min de lecture"),
        ("gt-5.jpg","Livraison","Quelle marque grande taille livre le plus vite ? Délais et retours mesurés","5 min de lecture")],
  grid_h2="Tous les comparatifs grande taille",
  grid=[("gt-2.jpg","Sport","Vêtements de sport grande taille : 6 marques comparées","Maintien, transparence et coutures d'après les avis clients.","6 marques","8 min"),
        ("gt-1.jpg","Jeans","Jean grande taille femme : les 8 marques qui ne compriment pas la taille","Tour de taille annoncé, élasticité et tenue d'après les avis clients.","8 marques","9 min"),
        ("gt-3.jpg","Duel","Kiabi ou H&amp;M+ : qui taille le plus juste au-delà du 46 ?","Vingt références par marque du 46 au 56, grilles comparées et avis croisés.","2 marques","7 min"),
        ("gt-4.jpg","Robes","Robe grande taille pas chère : 7 marques comparées du 46 au 56","Coupes, longueurs et prix catalogue, de la robe à 20 € à la robe à 90 €.","7 marques","8 min"),
        ("gt-5.jpg","Livraison","Quelle marque grande taille livre le plus vite ? Délais et retours mesurés","Délais annoncés, frais de retour et disponibilité des grandes tailles.","11 marques","5 min"),
        ("art-3.jpg","Tailles","Meilleures marques grande taille : le comparatif des tailles réelles","11 grilles comparées, le tableau complet des écarts par taille.","11 marques","11 min")],
  rank_h2="Le classement des marques grande taille en septembre 2026",
  rank_p="Note globale sur 10 sur le seul univers grande taille. La largeur de la grille et la fidélité des tailles pèsent le plus lourd.",
  rank=[("kiabi","Kiabi","La grille la plus large du panel","Jusqu'au 58 en magasin, tailles fidèles, prix les plus bas.","8,0","up","▲ +0,4"),
        ("hm","H&amp;M","La gamme dédiée la plus fournie","H&amp;M+ jusqu'au 54, coupes correctes, prix modérés.","7,2","flat","= 0,0"),
        ("shein","Shein","Le plus de références","Choix immense, qualité fragile, tailles imprévisibles.","6,4","down","▼ -0,2"),
        ("zara","Zara","La grille la plus courte","Peu de pièces au-delà du 44, coupes petites.","5,9","flat","= 0,0"),
        ("mango","Mango","Le plus élégant, mais rare","Violeta arrêtée, quelques pièces jusqu'au 48.","5,7","down","▼ -0,1")],
  cta_h2="Kiabi ou H&amp;M en grande taille ?", cta_p="Comparez deux marques grande taille sur nos cinq critères en un clic.",
  faq_h2="Questions fréquentes sur les marques grande taille",
  faq=[("Quelle est la meilleure marque de vêtements grande taille en 2026 ?","Sur nos relevés 2026, Kiabi obtient la meilleure note globale (8,0/10) grâce à la grille la plus large du panel, jusqu'au 58, et à des tailles fidèles. H&amp;M+ suit à 7,2/10."),
       ("Quelle marque grande taille taille le plus juste ?","Sur 11 grilles comparées, Kiabi et H&amp;M+ sont les plus proches de la moyenne du panel. Shein est imprévisible d'une référence à l'autre, Zara taille petit."),
       ("Où trouver du 56 ou du 58 en magasin ?","Kiabi propose le 58 en magasin sur la plupart des basiques. Ailleurs, les tailles au-delà du 52 sont surtout disponibles en ligne."),
       ("Comment sont notées les marques ?","Cinq critères sur 10 : prix, qualité, fidélité des tailles, livraison et note globale pondérée. Les écarts viennent des grilles officielles, comparées entre elles pour une même taille annoncée."),
       ("Quelle marque de jean grande taille choisir ?","Sur 8 marques comparées, les jeans Kiabi et H&amp;M+ réunissent le moins d'avis négatifs sur le maintien du tour de taille.")],
  news_h2="Recevez chaque comparatif grande taille avant tout le monde"),

 dict(slug="grossesse", menu="Grossesse", nom="Grossesse", h1="Les meilleures marques de <em>vêtements de grossesse</em>",
  title="Meilleures marques de vêtements de grossesse 2026 : comparatifs et classement",
  desc="Comparatifs de marques de vêtements de grossesse et d'allaitement, Kiabi, H&M Mama, Zara, Primark. Prix relevés, confort testé du 3e au 9e mois, tenue au lavage. Le classement 2026.",
  intro="Du troisième au neuvième mois, puis l'allaitement. Nous chiffrons le vestiaire complet au prix catalogue et nous dépouillons les avis clients sur le confort avant de classer les marques.",
  hero="cat-grossesse-hero.jpg", hero_alt="Femme enceinte en robe",
  subnav=["Jeans de grossesse","Robes","Allaitement","Lingerie","Sport prénatal","Petits prix","Guide des tailles"], count="6 comparatifs",
  une_h2="Le comparatif grossesse à la une",
  feat=dict(img="art-4.jpg", tag="Classement", h2="Meilleure marque de vêtements de grossesse 2026 : le comparatif de 10 marques",
   p="Kiabi, H&amp;M Mama, Zara, Primark, Shein, Vertbaudet. Prix relevés, confort noté du 3e au 9e mois par un panel de 12 futures mamans, tenue après cinq lavages.",
   meta="10 marques comparées · 8 min de lecture · Mis à jour le 4 septembre 2026"),
  side=[("gro-1.jpg","Jeans","Jean de grossesse : les 7 bandeaux comparés du 3e au 9e mois","8 min de lecture"),
        ("gro-2.jpg","Petits prix","Vêtements de grossesse pas chers : comparatif des 10 marques les moins chères","8 min de lecture"),
        ("gro-3.jpg","Duel","Kiabi ou H&amp;M Mama : quelle marque pour toute la grossesse à moins de 150 € ?","7 min de lecture"),
        ("gro-4.jpg","Allaitement","Robe d'allaitement : les 6 marques les plus pratiques au quotidien","6 min de lecture")],
  grid_h2="Tous les comparatifs grossesse",
  grid=[("gro-4.jpg","Allaitement","Robe d'allaitement : les 6 marques les plus pratiques au quotidien","Ouvertures, matières affichées et prix, de la robe à 25 € à la robe à 110 €.","6 marques","6 min"),
        ("gro-1.jpg","Jeans","Jean de grossesse : les 7 bandeaux comparés du 3e au 9e mois","Bandeau bas, haut ou intégral, maintien et confort d'après les avis.","7 marques","8 min"),
        ("gro-2.jpg","Petits prix","Vêtements de grossesse pas chers : comparatif des 10 marques les moins chères","Un vestiaire complet par marque, prix relevés hors soldes.","10 marques","8 min"),
        ("gro-3.jpg","Duel","Kiabi ou H&amp;M Mama : quelle marque pour toute la grossesse à moins de 150 € ?","Deux vestiaires complets chiffrés au prix catalogue, avis clients croisés.","2 marques","7 min"),
        ("art-4.jpg","Lingerie","Soutien-gorge d'allaitement : 8 marques comparées sur le maintien","Maintien, ouverture d'une main et tenue au lavage d'après les avis.","8 marques","7 min"),
        ("gro-2.jpg","Tailles","Quelle taille prendre en vêtements de grossesse ? Nos relevés sur 10 marques","Sa taille habituelle ou une taille au-dessus, le tableau marque par marque.","10 marques","5 min")],
  rank_h2="Le classement des marques de vêtements de grossesse en septembre 2026",
  rank_p="Note globale sur 10 sur le seul univers grossesse. Le confort porté et le prix pèsent le plus lourd, un vestiaire de grossesse se porte six mois.",
  rank=[("kiabi","Kiabi","Le meilleur rapport qualité-prix","Vestiaire complet à moins de 150 €, bandeaux confortables.","7,9","up","▲ +0,3"),
        ("hm","H&amp;M Mama","La gamme la plus complète","Du jean à la lingerie d'allaitement, prix modérés.","7,6","flat","= 0,0"),
        ("zara","Zara","Le plus mode","Quelques pièces élégantes, gamme courte, prix élevés.","6,8","down","▼ -0,2"),
        ("primark","Primark","Le moins cher","Basiques à très bas prix, tenue au lavage limitée.","6,3","up","▲ +0,1"),
        ("shein","Shein","Le plus de choix en ligne","Références innombrables, tailles et qualité imprévisibles.","6,1","flat","= 0,0")],
  cta_h2="Kiabi ou H&amp;M Mama pour votre grossesse ?", cta_p="Comparez deux marques de grossesse sur nos cinq critères en un clic.",
  faq_h2="Questions fréquentes sur les marques de vêtements de grossesse",
  faq=[("Quelle est la meilleure marque de vêtements de grossesse en 2026 ?","Sur nos relevés 2026, Kiabi obtient la meilleure note globale (7,9/10) avec un vestiaire complet à moins de 150 € et des bandeaux confortables. H&amp;M Mama suit à 7,6/10 avec la gamme la plus complète."),
       ("Quelle taille prendre en vêtements de grossesse ?","Chez Kiabi, H&amp;M Mama et Vertbaudet, sa taille habituelle suffit, la coupe est prévue pour évoluer. Chez Zara et Shein, une taille au-dessus est plus sûre."),
       ("À partir de quel mois acheter des vêtements de grossesse ?","La majorité des futures mamans de notre panel ont basculé entre le 4e et le 5e mois, d'abord sur le jean, puis sur les hauts."),
       ("Comment sont notées les marques ?","Cinq critères sur 10 : prix, qualité, fidélité des tailles, livraison et note globale pondérée, plus un critère confort porté propre à la grossesse."),
       ("Où acheter des vêtements de grossesse pas chers ?","Kiabi et Primark sont les deux options les plus économiques de notre panel, Kiabi gardant l'avantage sur le confort des bandeaux et la tenue au lavage.")],
  news_h2="Recevez chaque comparatif grossesse avant tout le monde"),
]

ICON_SEARCH='<svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="M16 16l5 5"/></svg>'
BURGER='<svg width="22" height="14" viewBox="0 0 22 14" fill="none" stroke="#111" stroke-width="1.7"><path d="M0 1h22M0 7h22M0 13h22"/></svg>'

SUBIMG={'enfant': {'Bébé 0-3 ans': 'sub-bebe.jpg', 'Fille': 'sub-fille.jpg', 'Garçon': 'sub-garcon.jpg', 'Rentrée scolaire': 'sub-rentree.jpg', 'Manteaux &amp; doudounes': 'sub-kidmanteau.jpg', 'Pyjamas': 'sub-pyjama.jpg', 'Chaussures': 'sub-kidshoes.jpg'}, 'femme': {'Jeans': 'sub-jeans.jpg', 'Robes': 'sub-robe.jpg', 'Manteaux': 'sub-manteau.jpg', 'Pulls &amp; mailles': 'sub-pull.jpg', 'Lingerie': 'sub-lingerie.jpg', 'Sport': 'sub-sportf.jpg', 'Petits prix': 'sub-prix.jpg'}, 'homme': {'Jeans': 'sub-hjeans.jpg', 'Chemises': 'sub-chemise.jpg', 'Costumes': 'sub-costume.jpg', 'Sweats &amp; hoodies': 'sub-hoodie.jpg', 'Sport': 'sub-sporth.jpg', 'Chaussures': 'sub-hshoes.jpg', 'Grandes tailles': 'sub-gthomme.jpg'}, 'grande-taille': {'Femme grande taille': 'sub-gtfemme.jpg', 'Homme grande taille': 'sub-gthomme.jpg', 'Jeans': 'sub-gtjeans.jpg', 'Robes': 'sub-gtrobe.jpg', 'Lingerie': 'sub-gtlingerie.jpg', 'Sport': 'sub-gtsport.jpg', 'Guide des tailles': 'sub-guide.jpg'}, 'grossesse': {'Jeans de grossesse': 'sub-matjeans.jpg', 'Robes': 'sub-matrobe.jpg', 'Allaitement': 'sub-allait.jpg', 'Lingerie': 'sub-matling.jpg', 'Sport prénatal': 'sub-prenatal.jpg', 'Petits prix': 'sub-prix.jpg', 'Guide des tailles': 'sub-guide.jpg'}}

def menu(current):
    out=[]
    for c in CATS:
        style=' style="text-decoration:underline;text-underline-offset:6px"' if c["slug"]==current else ''
        out.append(f'      <li><a href="../{c["slug"]}/"{style}>{c["menu"]}</a></li>')
    return "\n".join(out)

def footer_cats():
    return "".join(f'<li><a href="../{c["slug"]}/">{c["nom"]}</a></li>' for c in CATS)

def render(c):
    subnav="".join(f'''
    <a class="subcard" href="#articles"><img src="../assets/img/{SUBIMG[c["slug"]][s]}" alt="" width="56" height="56" loading="lazy"><span>{s}</span><i><svg viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg></i></a>''' for s in c["subnav"])
    side="".join(f'''
        <a class="side-item" href="#"><img src="../assets/img/{img}" alt="" width="96" height="80"><div><span class="eyebrow">{k}</span><h3>{t}</h3><small>{m}</small></div></a>''' for img,k,t,m in c["side"])
    grid="".join(f'''
      <a class="post big" href="#"><img src="../assets/img/{img}" alt="" width="800" height="560"><div class="post-body"><span class="eyebrow">{k}</span><h3>{t}</h3><p class="excerpt">{ex}</p><span class="meta">{n} <i></i> {d}</span></div></a>''' for img,k,t,ex,n,d in c["grid"])
    rank="".join(f'''
      <div class="rank-row"><span class="pos{" first" if i==0 else ""}">0{i+1}</span><img src="../assets/logos/{logo}.svg" alt="{alt}"><div class="why"><b>{b}</b>{why}</div><div class="score"><b>{sc}</b><small>/10</small><span class="chip{"" if cls=="up" else " "+cls}">{chip}</span></div></div>''' for i,(logo,alt,b,why,sc,cls,chip) in enumerate(c["rank"]))
    faq="".join(f'''
      <details{" open" if i==0 else ""}><summary>{q}</summary><p>{a}</p></details>''' for i,(q,a) in enumerate(c["faq"]))
    f=c["feat"]
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{c["title"]}</title>
<meta name="description" content="{c["desc"]}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@600;700;800&family=Poppins:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="icon" href="../assets/logo/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="../assets/logo/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="../assets/logo/favicon-192.png">
<link rel="apple-touch-icon" href="../assets/logo/apple-touch-icon.png">
<meta name="theme-color" content="#FFD400">
<link rel="stylesheet" href="../assets/css/site.css?v=6">
</head>
<body>

<header>
  <div class="wrap nav">
    <a class="logo" href="../" aria-label="Comparamode, accueil"><img class="l-light" src="../assets/logo/logo-light.png" alt="Comparamode" width="620" height="133"><img class="l-dark" src="../assets/logo/logo.png" alt="" aria-hidden="true" width="620" height="133"></a>
    <ul class="menu">
{menu(c["slug"])}
    </ul>
    <div class="nav-actions">
      <a class="iconbtn" href="#" aria-label="Rechercher">{ICON_SEARCH}</a>
      <a class="btn btn-dark" href="../#outil">Comparer 2 marques</a>
      <button class="burger" aria-label="Menu">{BURGER}</button>
    </div>
  </div>
</header>

<section class="hero cat-hero">
  <img class="hero-bg" src="../assets/img/{c["hero"]}" alt="{c["hero_alt"]}" width="2000" height="900" fetchpriority="high">
  <div class="wrap hero-inner">
    <nav class="crumbs" aria-label="Fil d'Ariane"><a href="../">Accueil</a><i></i><span>{c["nom"]}</span></nav>
    <h1>{c["h1"]}</h1>
    <p>{c["intro"]}</p>
  </div>
</section>

<nav class="subnav" aria-label="Sous-catégories">
  <div class="wrap subcards">{subnav}
  </div>
</nav>

<section class="cat-featured" id="articles">
  <div class="wrap">
    <div class="section-head">
      <h2>{c["une_h2"]}</h2>
      <a class="btn btn-ghost" href="#classement">Voir le classement</a>
    </div>
    <div class="feat-grid">
      <a class="feat-main" href="#">
        <img src="../assets/img/{f["img"]}" alt="" width="800" height="560">
        <div class="feat-body">
          <span class="tag">{f["tag"]}</span>
          <h2>{f["h2"]}</h2>
          <p>{f["p"]}</p>
          <span class="feat-meta">{f["meta"]}</span>
        </div>
      </a>
      <div class="feat-side">{side}
      </div>
    </div>
  </div>
</section>

<section class="cat-grid">
  <div class="wrap">
    <div class="section-head">
      <h2>{c["grid_h2"]}</h2>
      <span style="font-size:13px;color:var(--muted)">Du plus récent au plus ancien</span>
    </div>
    <div class="grid3">{grid}
    </div>
    <div class="pager"><a class="on" href="#">1</a><a href="#">2</a><a href="#">3</a><a href="#" aria-label="Page suivante">→</a></div>
  </div>
</section>

<section class="cat-rank" id="classement">
  <div class="wrap rank-grid">
    <div class="rank-intro">
      <h2>{c["rank_h2"]}</h2>
      <p>{c["rank_p"]}</p>
      <a class="btn btn-dark" href="../#methode">Voir la méthode de notation</a>
    </div>
    <div class="rank-list">{rank}
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="wrap">
    <div class="cta-card">
      <div><h2>{c["cta_h2"]}</h2><p>{c["cta_p"]}</p></div>
      <a class="btn btn-dark" href="../#outil">Comparer 2 marques</a>
    </div>
  </div>
</section>

<section class="faq">
  <div class="wrap faq-head">
    <h2>{c["faq_h2"]}</h2>
    <div>{faq}
    </div>
  </div>
</section>

<section class="news" id="newsletter">
  <div class="wrap">
    <div class="news-card">
      <div>
        <h2>{c["news_h2"]}</h2>
        <p>Un email par semaine : le classement du mois, les nouveaux comparatifs et les vraies baisses de prix relevées en magasin.</p>
      </div>
      <div>
        <form class="form" onsubmit="return false">
          <input type="email" placeholder="Votre adresse email" aria-label="Adresse email" required>
          <button class="btn btn-yellow" type="submit">Je m'inscris</button>
        </form>
        <p class="form-note">Pas de publicité, désinscription en un clic.</p>
      </div>
    </div>
  </div>
</section>

<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand"><a class="logo" href="../" aria-label="Comparamode, accueil"><img src="../assets/logo/logo.png" alt="Comparamode" width="620" height="133" loading="lazy"></a><p>Le comparateur indépendant des marques de vêtements. Nous relevons, nous comparons, nous classons.</p></div>
      <div><h4>Comparatifs</h4><ul>{footer_cats()}</ul></div>
      <div><h4>Marques</h4><ul><li><a href="#">Kiabi</a></li><li><a href="#">Zara</a></li><li><a href="#">H&amp;M</a></li><li><a href="#">Primark</a></li><li><a href="../#marques">Toutes les marques</a></li></ul></div>
      <div><h4>À propos</h4><ul><li><a href="../#methode">Notre méthode</a></li><li><a href="#">Qui sommes-nous</a></li><li><a href="#">Contact</a></li><li><a href="#">Mentions légales</a></li></ul></div>
    </div>
    <div class="foot-bottom"><span>© 2026 Comparamode. Comparateur indépendant de marques de mode.</span><span>Les logos appartiennent à leurs propriétaires respectifs.</span></div>
  </div>
</footer>

<script src="../assets/js/site.js?v=6"></script>
</body>
</html>
'''

if __name__=="__main__":
    for c in CATS:
        os.makedirs(c["slug"],exist_ok=True)
        open(os.path.join(c["slug"],"index.html"),"w",encoding="utf-8").write(linkify(render(c),"../"))
        print("ok",c["slug"])
