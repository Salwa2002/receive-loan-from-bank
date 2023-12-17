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
Les modèles ont été sauvegardés au format Joblib pour faciliter le déploiement, et notre choix de créer la route utilisant le modèle de la plus haute précision(SVC). 

# Développement de l'API avec FastAPI :
. On a utilisé FastAPI pour créer une API qui prend en entrée des caractéristiques sous forme d'entiers.
. La première version de l'API affiche toutes les fonctionnalités, ce qui inclut celles normalisées lors de la phase de prétraitement des données.

# Prédiction de l'Éligibilité au Crédit :
. L'API joue un rôle crucial dans la prédiction de l'éligibilité au crédit. L'utilisation d'APIs pour l'évaluation des risques et la prise de décision automatisée peut grandement améliorer l'efficacité du processus en se basant sur les caractéristiques fournies.

# Stockage des Résultats :
.Les résultats des prédictions (combien de personnes peuvent ou ne peuvent pas obtenir un crédit) sont stockés pour analyse ultérieure.

# Dockerization de l'Application :
. On a utilisé Docker pour faciliter le déploiement de l'application en encapsulant toutes les dépendances d'une application dans un conteneur. Cela garantit que l'application fonctionnera de manière cohérente, indépendamment de l'environnement sous-jacent. 

. Des images Docker ont été créées pour l'application API principale, permettant une mise en production plus facile.

# Configuration de Prometheus et Grafana :
. Prometheus a été configuré pour collecter des métriques à partir de l'application déployée et les stocker sous forme de séries temporelles. Cela permet de suivre l'évolution des performances au fil du temps. 

. Grafana a été mis en place pour visualiser les métriques liées aux performances de notre application, offrant une surveillance en temps réel de la performance du modèle en créant des tableaux de bord personnalisés et affichant des graphiques en temps réel .
# Affichage des Statistiques :
. Les statistiques, telles que le nombre de personnes obtenant un crédit ou non, sont visualisées à l'aide de Grafana.

. Celui-ci sert comme un moyen pour vérifier le bon fonctionnement du modèle en production.
