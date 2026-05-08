class OptimisationMobilite:
    def __init__(self, cap_mohammed_v, cap_hassan_ii, cap_intersection):
        """
        Constructeur : Initialise les attributs de la classe avec les capacités.
        """
        self.cap_m5 = cap_mohammed_v
        self.cap_h2 = cap_hassan_ii
        self.cap_inter = cap_intersection

    def evaluer_flux(self, x1, x2):
        """
        Méthode pour calculer la fonction objectif Z = x1 + x2.
        """
        return x1 + x2

    def trouver_solution_optimale(self):
        """
        Détermine la meilleure combinaison de véhicules (x1, x2) en testant
        les sommets de la région réalisable (logique de la méthode graphique).
        """
        # Liste qui va stocker les tuples des points (x1, x2) valides
        sommets_possibles = []

        # Point A : Saturation de l'Avenue Mohammed V (x1 max)
        x2_calc_A = self.cap_inter - self.cap_m5
        if 0 <= x2_calc_A <= self.cap_h2:
            sommets_possibles.append((self.cap_m5, x2_calc_A))

        # Point B : Saturation de l'Avenue Hassan II (x2 max)
        x1_calc_B = self.cap_inter - self.cap_h2
        if 0 <= x1_calc_B <= self.cap_m5:
            sommets_possibles.append((x1_calc_B, self.cap_h2))
            
        # Point C : Seulement Mohammed V (sans Hassan II)
        if self.cap_m5 <= self.cap_inter:
            sommets_possibles.append((self.cap_m5, 0))
            
        # Point D : Seulement Hassan II (sans Mohammed V)
        if self.cap_h2 <= self.cap_inter:
            sommets_possibles.append((0, self.cap_h2))

        # Variables pour stocker le meilleur résultat
        meilleur_x1 = 0
        meilleur_x2 = 0
        flux_maximum = 0

        # Parcours de la liste des sommets pour trouver le max (Algorithmique classique)
        for point in sommets_possibles:
            x1 = point[0]
            x2 = point[1]
            z_actuel = self.evaluer_flux(x1, x2)
            
            # Si le Z calculé est supérieur au max actuel, on met à jour
            if z_actuel > flux_maximum:
                flux_maximum = z_actuel
                meilleur_x1 = x1
                meilleur_x2 = x2

        return meilleur_x1, meilleur_x2, flux_maximum


# --- Programme Principal (Main) ---
if __name__ == "__main__":
    print("-" * 50)
    print(" PROGRAMME D'OPTIMISATION DE TRAFIC - MARRAKECH ")
    print("-" * 50)
    
    try:
        # Saisie des données par l'utilisateur
        val_m5 = int(input("Capacité maximale Avenue Mohammed V (ex: 1000) : "))
        val_h2 = int(input("Capacité maximale Avenue Hassan II (ex: 800) : "))
        val_inter = int(input("Capacité maximale de l'intersection (ex: 1500) : "))
        
        # Instanciation de l'objet (Création de l'instance de la classe)
        projet = OptimisationMobilite(val_m5, val_h2, val_inter)
        
        # Appel de la méthode de résolution
        x1_opt, x2_opt, z_max = projet.trouver_solution_optimale()
        
        # Affichage formaté des résultats
        print("\n--- RÉSULTATS OBTENUS ---")
        print(f"Nombre optimal de voitures (Avenue Mohammed V) : {x1_opt}")
        print(f"Nombre optimal de voitures (Avenue Hassan II)  : {x2_opt}")
        print(f"-> FLUX TOTAL MAXIMAL (Z) : {z_max} véhicules")
        print("-" * 50)

    except ValueError:
        print("\nErreur de saisie : Vous devez entrer des nombres entiers valides.")