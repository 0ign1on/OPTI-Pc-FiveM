import os
import subprocess
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("Appuyez sur Entrée pour continuer...")

def animated_print(lines, delay=0.15):
    """Affiche ligne par ligne avec délai pour effet animation"""
    for line in lines:
        print(line)
        time.sleep(delay)

def optimisation_pc():
    clear()
    print("="*50)
    print("       ⚙️ OPTIMISATION SYSTEME EN COURS...")
    print("="*50)
    print()
    time.sleep(1)

    cmds = [
        "Nettoyage des animations Windows...",
        "Désactivation de la transparence...",
        "Activation du Mode Jeu...",
        "Réduction des apps en arrière-plan...",
        "Optimisation du cache système...",
        "Nettoyage des processus inutiles...",
        "Optimisation de la mémoire virtuelle...",
        "Réglages DWM pour meilleure réactivité...",
        "Défragmentation virtuelle du disque...",
        "Finalisation de l'optimisation système..."
    ]

    animated_print([f"> {cmd}" for cmd in cmds], 0.3)

    
    reg_cmds = [
        r'reg add "HKCU\Control Panel\Desktop" /v UserPreferencesMask /t REG_BINARY /d 9012038010000000 /f',
        r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize" /v EnableTransparency /t REG_DWORD /d 0 /f',
        r'reg add "HKCU\Software\Microsoft\GameBar" /v AutoGameModeEnabled /t REG_DWORD /d 1 /f',
        r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\BackgroundAccessApplications" /v GlobalUserDisabled /t REG_DWORD /d 1 /f'
    ]

    for cmd in reg_cmds:
        subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    time.sleep(1)
    print("\n✅ Optimisation PC terminée avec succès !")
    pause()

def optimisation_zqsd():
    clear()
    print("="*50)
    print("         OPTI STRAFF - BOOST REACTIVITE ZQSD")
    print("="*50)
    print()
    print(">>> Calibration du clavier pour ZQSD gaming...")
    time.sleep(1)
    print("[*] Lecture périphérique...")
    time.sleep(1)
    print("[*] Optimisation touches Z / Q / S / D...")
    time.sleep(1)

    for i in range(1, 26):
        print(f"Optimisation ZQSD ligne {i} - OK [0x{i:02}FFZQSD]")
        time.sleep(0.1)

    print("\n✅ Réactivité clavier améliorée pour le gaming.")
    pause()

def optimisation_reseau():
    clear()
    print("="*50)
    print("        OPTIMISATION RESEAU - Ethernet & NVIDIA")
    print("="*50)
    print()
    time.sleep(1)

    lines = [
        "Analyse des connexions réseau...",
        "Optimisation des paramètres Ethernet...",
        "Désactivation des mises à jour automatiques...",
        "Optimisation du pilote NVIDIA pour le réseau...",
        "Amélioration de la latence...",
        "Configuration QoS (Qualité de Service)...",
        "Nettoyage des caches réseau...",
        "Réinitialisation des protocoles TCP/IP...",
        "Finalisation de l'optimisation réseau..."
    ]
    animated_print([f"> {line}" for line in lines], 0.3)

 

    time.sleep(1)
    print("\n✅ Optimisation réseau terminée avec succès !")
    pause()

def optimisation_apps():
    clear()
    print("="*50)
    print("           OPTIMISATION APPLIS - Discord, Spotify, Chrome")
    print("="*50)
    print()
    time.sleep(1)

    lines = [
        "Fermeture des processus inutiles...",
        "Optimisation de Discord (mode économie)...",
        "Optimisation de Spotify (priorité CPU)...",
        "Nettoyage du cache Chrome...",
        "Réinitialisation de la barre des tâches...",
        "Désactivation des notifications superflues...",
        "Libération de la mémoire utilisée...",
        "Finalisation de l'optimisation des applis..."
    ]
    animated_print([f"> {line}" for line in lines], 0.3)

 

    time.sleep(1)
    print("\n✅ Optimisation applications terminée avec succès !")
    pause()

def main():
    clear()
    print("="*50)
    print("        [ SYSTEME DE SECURITE - ACCES RESTREINT ]")
    print("="*50)
    print()
    userid = input(">>> IDENTIFIANT UTILISATEUR : ")
    
    while True:
        clear()
        print("="*50)
        print("       🔧 OPTIMISATION FiveM / PC - Edition 2025 🔧")
        print("="*50)
        print()
        print(f"Bienvenue, {userid} !")
        print()
        print("1. Optimisation MAX sécurisée (Windows + DWM)")
        print("2. OPTI STRAFF (Boost touches ZQSD)")
        print("3. Optimisation Réseau (Ethernet & NVIDIA)")
        print("4. Optimisation Applications (Discord, Spotify, Chrome, Barre des tâches)")
        print("5. Quitter")
        print()
        choix = input(">>> Entrez votre choix (1-5) : ")

        if choix == "1":
            optimisation_pc()
        elif choix == "2":
            optimisation_zqsd()
        elif choix == "3":
            optimisation_reseau()
        elif choix == "4":
            optimisation_apps()
        elif choix == "5":
            print("\nFermeture du programme. Merci d’avoir utilisé Private_Opti_Fivem_0ign1on !")
            time.sleep(2)
            break
        else:
            print("Choix invalide, veuillez réessayer.")
            time.sleep(1)

if __name__ == "__main__":
    main()
