Projet DBT ATOS

Appercy
Ce projet DBT a été initié par Mansour GUEYE, Ousseynou Diop et Moustapha Dioum pour analyser les données Airbnb concernant les annonces de logements (listings) et les hôtes (hosts). Le projet vise à répondre à plusieurs questions importantes liées aux locations à court terme, aux licences nécessaires et aux politiques de logement dans différentes villes et régions.

Données
Les données utilisées dans ce projet comprennent des informations sur les annonces Airbnb (listings) et les hôtes (hosts). Ces données contiennent des détails sur les types de chambres, les activités, les licences, les locations à court terme, les revenus et bien d'autres informations pertinentes.

Objectifs du Projet
Le projet DBT Atos vise à répondre à plusieurs questions clés, notamment :
Impact sur le Logement : Évaluer si les locations Airbnb ont un impact sur le logement en analysant la fréquence des locations et leur effet potentiel sur l'offre de logements.
Conformité Légale : Identifier les annonces non licenciées et celles qui prétendent à tort être exemptées de licences, ainsi que celles que Airbnb continue à promouvoir.
Politiques de Logement : Analyser les politiques de logement dans différentes villes et régions en se basant sur le paramètre "minimum nights" des annonces pour détecter les changements de tendance vers des séjours plus longs.
Évolution des Annonces : Étudier les changements dans le type de logements offerts par Airbnb, notamment le passage à des séjours plus longs pour échapper aux réglementations sur les locations à court terme.

Structure du Projet
Le projet est structuré de la manière suivante :
Dossiers Source (staging) : Contient les fichiers sources, y compris stg_hosts et stg_listings.
Dossier Mart (marts) : Contient les fichiers résultant de la jointure des fichiers sources. Ces fichiers sont utilisés pour l'analyse des données.
Dossier Dimensions (dim) : Contient les KPI (Key Performance Indicators) résultant de l'analyse des données. Ces KPI fournissent des insights précieux pour répondre aux questions du projet.
Dossier Expositions (exposures) : Contient le fichier exposure.yml, qui contient toutes les informations nécessaires pour la création de tableaux de bord et la visualisation des données.

Exécution du Projet
Le projet est orchestré par Airflow et est planifié pour s'exécuter tous les jours à 8h du matin. Cette planification permet de mettre à jour les données et de récupérer de nouvelles données pour une analyse continue.

Base de Données
Nous avons utilisé une base de données PostgreSQL pour stocker les données nécessaires à ce projet. Les données sources ont été préalablement chargées dans cette base de données pour faciliter l'analyse et le traitement.

Dépendances
Le projet dépend des packages suivants, que vous pouvez installer à l'aide de pip :

Apache Airflow: Un framework open-source pour la programmation et la planification de workflows.

pip install apache-airflow

DBT (Data Build Tool): Un outil open-source pour l'analyse de données qui facilite la transformation, la validation et la documentation des données.

pip install dbt

Assurez-vous d'installer ces dépendances avant d'exécuter le projet


Contributeurs
Mansour GUEYE
Ousseynou Diop
Moustapha Dioum
