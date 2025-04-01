import time

class Processus:
    def __init__(self, pid, nom, priorite, temps_prevue):
        self.pid = pid
        self.nom = nom
        self.priorite = priorite
        self.temps_prevue = temps_prevue
        self.temps_ecoule = 0
        self.status = "ready"

processus_liste = [
    Processus("A0001", "Gestionnaire", "Normal", 2),  # Temps réduit pour tests
    Processus("A0002", "Explorateur", "Normal", 3),
    Processus("A0003", "Antivirus", "Haut", 4),
    Processus("A0004", "Navigateur", "Normal", 1)
]

def executer_systeme():
    while True:
        # A. Sélection avec vraie gestion des priorités
        prochain = None
        for p in processus_liste:
            if p.status == "ready":
                if not prochain or (p.priorite == "Haut" and prochain.priorite != "Haut"):
                    prochain = p
        
        # B. Vérification complète de l'arrêt
        if not prochain and all(p.status == "terminated" for p in processus_liste):
            print("\nTous les processus sont terminés")
            break
        elif not prochain:
            time.sleep(1)
            continue
            
        # C. Exécution avec meilleur affichage
        prochain.status = "running"
        print(f"\n● EXÉCUTION {prochain.pid} ({prochain.nom}) [Priorité: {prochain.priorite}]")
        
        while prochain.temps_ecoule < prochain.temps_prevue:
            time.sleep(1)
            prochain.temps_ecoule += 1
            print(f"⏳ Progression: {prochain.temps_ecoule}s/{prochain.temps_prevue}s")
        
        # D. Finalisation
        prochain.status = "terminated"
        print(f"✓ TERMINÉ {prochain.pid}")

print("=== SYSTÈME D'EXPLOITATION SIMULÉ ===")
executer_systeme()
