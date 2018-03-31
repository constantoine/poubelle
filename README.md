# La poubelle de Cléo
## Installation

Les scripts sont faits pour fonctionner sous windows, avec python 3.5, mais après ils fontionnent peut être sur d'autres OS

Pour commencer, [vous pouvez installer python 3.5 ici]("https://www.python.org/downloads/"> si vous ne le possédez pas déjà. Bon, pour installer un programme, je vous fais confiance. Je vous retrouve pour la suite <br> <br>

Une fois python installé sur votre windows, vous allez devoir installer tweepy, une extension qui permet de faire des trucs avec twitter. Pour se faire, ouvrez une invite de commande en mode administrateur. (En gros, tapez "cmd" dans la barre de recherche du menu démarrer, faites un clic droit sur "invite de commande" et cliquer sur "exécuter en tant qu'administrateur")

Ensuite, tapez  `pip install tweepy ` et appuyez sur enter

Une fois l'installation terminée, vous pouvez lancer les scripts. Voilà. Je vous conseille de télécharger tout le dépot de la poubelle, et de tout mettre dans un dossier vide, histoire d'éviter des conflits en cas d'utilisation de fichiers de configuration

Sauf que voilà, c'est pas fini. Pour pouvoir utiliser les scripts, il va falloir remplir des "credentials". Vous pouvez regarder si vous voulez, aucun bout de code ne me permet de les récupérer. Pour avoir ces credentials, vous allez avoir besoin de faire une application twitter.

Pour pouvoir en faire une, il faut que votre compte soir vérifié (= vous devez avoir associé un numéro de portable)

[Rendez vous donc à cette adresse](https://apps.twitter.com/)

![](img/create_app.PNG)

![](img/app_2.PNG)

![](img/app_3.png)


### Ensuite, allez dans "keys and access tokens" et cliquez sur "change app permissions"


![](img/app_4.png)

![](img/app_5.png)

### Maintenant retournez dans "keys and access tokens" et générez votre token

![](img/app_6.png)


Ne donnez aucun des quatre codes à quique ce soit. En effet, ces codes permettent à votre application ici de lire vos MPs et de tweeter à votre place. Voilà pourquoi vous devez être les seuls à les connaître. Je vous rappelle ici que vous pouvez utiliser la même applications pour plusieurs programmes en python, mais que pour éviter d'avoir des problèmes avec l'API, qui limite le nombre de requêtes sur 15 minutes, si jamais vous voulez faire tourner plusieurs programmes simultanément, peut-être vaut-il mieux d'avoir une application pour chaque programme. Maintenant dans le programme que vous voulez utiliser, copiez vos codes. Pour ce faire, clic droit > Ouvrir avec > bloc-note (Ou un autre éditeur de texte, mais surtout ne l'ouvrez pas comme ça, sinon vous allez le lancer) Et remplacez les "xoxoxoxoxo" par les codes à droite sur les lignes correspondantes

![](img/app_6.png)

Et voilà ! C'est terminé, vous êtes prêts à utiliser les programmes ! o/

## Une idée ? Une demande de programme ? Un bug ? Une suggestion ?

Vous pouvez m'envoyer un [message privé sur twitter](https://twitter.com/Lazy_Bouquine), mes DMs sont ouverts. N'hésitez pas ^^

## Ninou.py

### Pourquoi ?
	
Ce cher connard de Zeke voulait pouvoir autoblock toute personne tweetant "Ninou". Suffisait de demander

### Quoi ?

C'est un script qui bloque toute personne utilisant un mot

### Comment l'utiliser ?

Une fois les codes renseignés comme décrit dans le chapitre "installation", la seule chose que vous avez à faire, c'est personnaliser les filtres. Vous pouvez soit rechercher un seul mot, soit rechercher les tweets qui contiennent au moins un des mots de la liste :

![]("img/ninou_1.png")

![]("img/ninou_2.png")

### Que dire de plus ?

Vous pouvez vous amuser à ne pas bloquer vos followers et/ou vos followings. Si vous n'y arrivez pas, je veux bien vous venir en aide, bien entendu ^^

## Filter.py

### Pourquoi ?

Nox avait évoqué que le fait que le terme "Nox" était souvent utilisé, c'était compliqué de rechercher ses indirects. Alors voilà
	
### Quoi ?

Ce script affiche les tweets contenant un ou plusieurs termes (Même procédure pour choisir lesdits termes que sur Ninou.py) qui sont tweetés par les followers. Ainsi, une personne lambda tweetant tel ou tel mot ne sera pas concernée par le programme

### Comment l'utiliser ?

Tout pareil que Ninou.py pour la recherche des termes. Pour le reste, le programme s'en charge

### Que dire de plus ?

Et bien, même si j'ai eu la flemme de le faire, vous pouvez aussi y inclure vos followings, voire n'y inclure que vos followings
