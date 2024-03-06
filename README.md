## Résumé

Site web d'Orange County Lettings

## Documentation

Accéder à la documentation complète du projet : `https://documentation-p13.readthedocs.io/en/latest/`

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Variables d'environnement virtuel

- Créer un fichier `.env` et ajouter le contenu de `.env.exemple`
- Ajouter les valeurs des variables correspondantes dans le fichier `.env`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `python manage.py test`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

### Docker

Utiliser Docker pour lancer l'application en local :

- Installer Docker desktop ou Docker sur votre machine https://www.docker.com/
- Faire un pull de l'image de l'application, `docker pull fabroyer/lettings`
- Lancer l'image Docker `docker run -p 8000:8000 fabroyer/lettings`
- Aller sur http://localhost:8000

## Déploiement

Le déploiement se fait automatiquement à partir du pipeline CI/CD de Github Actions.
Ce projet a utilisé render.
Les étapes à suivre sont les suivantes :
- Depuis Github, ajouter les variables d'environnement suivantes :

  - SECRET_KEY: la secret_key du projet.
  - DSN: le dsn Sentry.
  - DOCKER_USERNAME: l'username de Dockerhub.
  - DOCKER_PASSWORD: le password de Dockerhub.
  - DOCKER_REGISTRY: le registry de Dockerhub.
  - DOCKER_IMAGE: le nom de l'image de Docker.
  - RENDER_DEPLOY_HOOK: l'url du hook de Render.

- Aller sur `https://render.com` et créer un compte.
- Ensuite créer un service, utiliser `web service`.
- Choisir `Deploy an existing image from a registry`
- Ajouter l'url de l'image Docker.
- Ajouter les variables d'environnement.
- Le déploiement s'exécute après chaque commit sur la branche principale.

## Technologies et langages utilisés

- Python 3.12.5
- Django 3.0
- Docker
- Render
- Git
- Github Actions
- Readthedocs
- Sphinx