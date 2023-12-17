# MLOps Monitoring

Prérequis:
- Installer docker
- Python
- Un IDE: Pycharm ou Vscode

Pour créer une image docker de l'application api titanic, dans un terminal, se placer dans le dossier du projet

```
docker build -t receive_loan_from_bank . 
```

Pour démarrer l'application dans un conteneur docker:

```
docker run -p 5000:5000 -it receive_loan_from_bank
```

En mode dev, le plus simple c'est de démarrer l'application via vscode ou pycharm, cela nous permet de debugger plus facilement si besoin.

Pour démarrer le tendem prometheus/grafana:

```
docker compose up -d
```

# Explication de la structure:

# Choix du Modèle :
On a effectué le processus d'entraînement de plusieurs modèles, pour sélectionner le Support Vector Classifier (SVC) pour sa plus haute précision.

# Normalisation des Features lors de l'Entraînement :
Lors de la phase de prétraitement des données pour l'entraînement du modèle, une normalisation a été effectuée.
Les features, bien que représentés comme des entiers en entrée dans l'API, ont subi une normalisation pendant la phase de nettoyage des données.

# Sauvegarde du Modèle :
Le modèle choisi (SVC) a été sauvegardé au format Joblib pour faciliter le déploiement.

# Développement de l'API avec FastAPI :
. On a utilisé FastAPI pour créer une API qui prend en entrée des caractéristiques sous forme d'entiers.
. La première version de l'API affiche toutes les fonctionnalités, ce qui inclut celles normalisées lors de la phase de prétraitement des données.

# Prédiction de l'Éligibilité au Crédit :
. L'API permet d'exécuter des prédictions pour déterminer si une personne peut obtenir un crédit ou non, basé sur les caractéristiques fournies.

# Stockage des Résultats :
.Les résultats des prédictions (combien de personnes obtiennent ou ne peuvent pas obtenir un crédit) sont stockés pour analyse ultérieure.

# Dockerization de l'Application :
. On a installé Docker pour faciliter le déploiement de l'application.
. Des images Docker ont été créées pour l'application API principale, permettant une mise en production plus facile.

# Configuration de Prometheus et Grafana :
. Prometheus a été configuré pour collecter des métriques à partir de l'application déployée.
. Grafana a été mis en place pour visualiser les statistiques, offrant une surveillance en temps réel de la performance du modèle.

# Affichage des Statistiques :
. Les statistiques, telles que le nombre de personnes obtenant ou se faisant refuser un crédit, sont visualisées à l'aide de Grafana.
. Ceci sert comme moyen de vérifier le bon fonctionnement du modèle en production.
