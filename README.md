# 🚦 Optimisation de la Mobilité à Marrakech

## 📝 Description du Projet
[cite_start]Ce dépôt présente la modélisation mathématique et la résolution algorithmique d'un problème de Programmation Linéaire pour l'optimisation des flux de trafic routier entre Guéliz et la Médina de Marrakech[cite: 107, 108]. [cite_start]Le projet vise à maximiser l'efficacité du déplacement tout en respectant les limites physiques des infrastructures routières[cite: 112].

## 🎯 Contexte et Objectifs
[cite_start]Marrakech connaît des goulots d'étranglement majeurs sur ses axes structurants aux heures de pointe[cite: 109]. Ce projet se concentre sur deux artères principales :
* [cite_start]L'Avenue Mohammed V[cite: 119].
* [cite_start]L'Avenue Hassan II[cite: 119].

## 📐 Modèle Mathématique
[cite_start]Le problème est formulé sous forme de Programme Linéaire[cite: 121]:

* **Variables de décision** :
  * [cite_start]x1 : Nombre de voitures sur l'Avenue Mohammed V[cite: 123].
  * [cite_start]x2 : Nombre de voitures sur l'Avenue Hassan II[cite: 123].
* [cite_start]**Fonction Objectif** : Maximiser le flux total de véhicules, Max Z = x1 + x2[cite: 125, 126].
* **Contraintes de capacité** :
  * [cite_start]Limite de l'Avenue Mohammed V : x1 <= 1000[cite: 129].
  * [cite_start]Limite de l'Avenue Hassan II : x2 <= 800[cite: 131].
  * [cite_start]Capacité totale de l'intersection : x1 + x2 <= 1500[cite: 132].
  * [cite_start]Condition de non-négativité : x1 >= 0 et x2 >= 0[cite: 132].

## ⚙️ Méthodologie et Résolution
Le problème a été modélisé, résolu et validé à l'aide de trois approches :
1. [cite_start]**Méthode Graphique** : Identification visuelle de la région réalisable via GeoGebra[cite: 133, 259].
2. [cite_start]**Méthode du Simplexe** : Résolution mathématique validée avec le solveur d'Excel[cite: 290, 295].
3. [cite_start]**Conception Informatique** : Développement d'un algorithme natif en Python en adoptant une architecture Orientée Objet (POO), évaluant automatiquement les sommets de la zone réalisable sans bibliothèques externes[cite: 428, 437].

## 💻 Installation et Utilisation
[cite_start]Le programme informatique a été conçu pour être interactif via une interface en ligne de commande (CLI)[cite: 445]. 

**Prérequis :**
* Python 3.11

**Exécution :**
1. Clonez ce dépôt.
2. Lancez le script principal :
   ```bash
   python lineaire.py
