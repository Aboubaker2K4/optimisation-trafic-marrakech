# 🚦 Optimisation de la Mobilité à Marrakech

## 📝 Description du Projet
Ce dépôt présente la modélisation mathématique et la résolution algorithmique d'un problème de Programmation Linéaire pour l'optimisation des flux de trafic routier entre Guéliz et la Médina de Marrakech 
Le projet vise à maximiser l'efficacité du déplacement tout en respectant les limites physiques des infrastructures routières.

## 🎯 Contexte et Objectifs
Marrakech connaît des goulots d'étranglement majeurs sur ses axes structurants aux heures de pointe. Ce projet se concentre sur deux artères principales :
*L'Avenue Mohammed V.
* L'Avenue Hassan II.

## 📐 Modèle Mathématique
Le problème est formulé sous forme de Programme Linéaire:

* **Variables de décision** :
  * x1 : Nombre de voitures sur l'Avenue Mohammed V.
  * x2 : Nombre de voitures sur l'Avenue Hassan II.
  *  **Fonction Objectif** : Maximiser le flux total de véhicules, Max Z = x1 + x2.
* **Contraintes de capacité** :
  * Limite de l'Avenue Mohammed V : x1 <= 1000.
  * Limite de l'Avenue Hassan II : x2 <= 800.
  * Capacité totale de l'intersection : x1 + x2 <= 1500.
  * Condition de non-négativité : x1 >= 0 et x2 >= 0.

## ⚙️ Méthodologie et Résolution
Le problème a été modélisé, résolu et validé à l'aide de trois approches :
1. **Méthode Graphique** : Identification visuelle de la région réalisable via GeoGebra.
2. **Méthode du Simplexe** : Résolution mathématique validée avec le solveur d'Excel.
3.**Conception Informatique** : Développement d'un algorithme natif en Python en adoptant une architecture Orientée Objet (POO), évaluant automatiquement les sommets de la zone réalisable sans bibliothèques externes.

## 💻 Installation et Utilisation
Le programme informatique a été conçu pour être interactif via une interface en ligne de commande (CLI). 

**Prérequis :**
* Python 3.11

**Exécution :**
1. Clonez ce dépôt.
2. Lancez le script principal :
   ```bash
   python lineaire.py
