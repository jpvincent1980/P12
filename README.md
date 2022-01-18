![forthebadge](https://www.djangoproject.com/m/img/badges/djangopowered126x54.gif)

![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)

# Projet P12

Développez une architecture back-end sécurisée en utilisant Django ORM.

Le langage utilisé est Python et les frameworks sont Django et Django-Rest Framework (DRF).

## Documentation

La documentation (en anglais) de l'API SoftDesk est disponible en cliquant sur le logo ci-dessous:
<a href="https://documenter.getpostman.com/view/16167513/UVXhrcyp">
<img src="https://www.postman.com/assets/logos/pm-orange-logo-horiz.svg" />
</a>

## Pré-requis

Depuis un terminal de type GitBash, déplacez-vous dans le répertoire dans lequel vous souhaitez récupérer les fichiers et saisissez la commande ci-dessous:

``git clone https://github.com/jpvincent1980/P12``

Créez vous un environnement virtuel intitulé ``env`` en tapant la commande suivante:

``python -m venv env``

puis installez-y toutes les bibliothèques nécessaires au bon fonctionnement du projet en saisissant la commande:

``pip install -r requirements.txt``

Activez votre environnement virtuel en saisissant la commande suivante:

sous Windows -> ``env/Scripts/activate.bat``

sous Mac/Linux -> ``source/env/bin/activate``

## Base de données PostgreSQL

L'application Epic Events fonctionne avec une base de données PostgreSQL.

Si PostgreSql n'est pas installé sur votre poste, suivez la marche à suivre au lien suivant.

Une fois PostgreSQL installée sur votre poste, créez une nouvelle base de données avec les paramètres suivants:

Nom de la base -> ``EPICDB``

Utilisateur -> ``epicuser``

Mot de passe -> ``EPICPASSWORD``

Host -> ``localhost``

Port -> ``5432``


## Démarrage

Toujours dans le même terminal et au niveau du répertoire contenant le fichier ``manage.py`` du projet, tapez la commande ci-dessous:

``python manage.py runserver``

puis rendez-vous à l'adresse ci-dessous dans votre navigateur :

``http://127.0.0.1:8000/`` ou ``http://localhost:8000``

Vous trouverez ci-dessous un compte utilisateur disponible pour tester l'API SoftDesk :

username -> ``epicuser`` / Mot de Passe -> ``EPICPASSWORD``


## IDE utilisé

[PyCharm Community Edition](https://www.jetbrains.com/fr-fr/pycharm/)

## Auteur

[Jean-Philippe Vincent](https://twitter.com/JeanPhilippeV15)

![forthebadge](https://forthebadge.com/images/badges/powered-by-coffee.svg)