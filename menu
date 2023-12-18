import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import json
import socket
# import threading

class PlanningPokerApp:

    _instance = None  # Variable de classe pour stocker l'instance unique

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, root, chemin_backlog):
        # Initialisation de la classe
        self.root = root
        self.root.title("Planning Poker")
        self.root.geometry("900x600")
        self.chemin_backlog = chemin_backlog
        self.charger_backlog()
        self.afficher_backlog()

        # Variables
        self.num_players_var = tk.StringVar()
        self.current_players_vars = []
        self.game_mode_var = tk.StringVar()
        self.players_names = []  # Liste pour stocker les noms des joueurs

        # Cadre principal
        main_frame = ttk.Frame(self.root, padding=(20, 20, 20, 20))
        main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Étiquettes
        ttk.Label(main_frame, text="Nombre de joueurs :").grid(column=0, row=0, sticky=tk.W, pady=10)
        ttk.Label(main_frame, text="Mode de jeu :").grid(column=0, row=2, sticky=tk.W, pady=10)
        ttk.Label(main_frame, text="Pseudos des joueurs :").grid(column=0, row=3, sticky=tk.W, pady=10)

        # Champ pour le nombre de joueurs
        self.num_players_var.set("0")
        num_players_entry = ttk.Entry(main_frame, textvariable=self.num_players_var, validate="key", validatecommand=(root.register(self.validate_num_players), "%P"))
        num_players_entry.grid(column=1, row=0, sticky=tk.W, pady=10)
        num_players_entry.bind('<FocusOut>', lambda e: self.update_player_name_entries())

        # Bouton pour charger un fichier JSON
        ttk.Button(main_frame, text="Charger Backlog", command=self.load_backlog).grid(column=0, row=1, columnspan=2, pady=10)

        # Menu déroulant pour le mode de jeu
        game_modes = ["Strict", "Moyenne"]
        game_mode_combobox = ttk.Combobox(main_frame, values=game_modes, textvariable=self.game_mode_var, state="readonly")
        game_mode_combobox.grid(column=1, row=2, sticky=tk.W, pady=10)

        # Conteneur des champs de noms des joueurs
        self.player_name_entries_container = ttk.Frame(main_frame)
        self.player_name_entries_container.grid(column=1, row=3, sticky=tk.W, pady=10)

        # Bouton pour procéder
        ttk.Button(main_frame, text="Valider pseudos", command=self.proceed).grid(column=0, row=12, columnspan=4, pady=20)

        # Bouton pour jouer en local
        ttk.Button(main_frame, text="Jouer en local", command=self.play_local).grid(column=0, row=13, columnspan=2, pady=20)

        # Bouton pour jouer à distance
        ttk.Button(main_frame, text="Jouer à distance", command=self.play_remote).grid(column=2, row=13, columnspan=2, pady=20)

    def update_player_name_entries(self):
        num_players = int(self.num_players_var.get())

        # Effacer les entrées précédentes
        for widget in self.player_name_entries_container.winfo_children():
            widget.destroy()

        # Réinitialiser la liste des variables actuelles
        self.current_players_vars = []

        # Entrées pour les noms des joueurs
        for i in range(num_players):
            player_name_var = tk.StringVar()
            self.current_players_vars.append(player_name_var)
            ttk.Entry(self.player_name_entries_container, textvariable=player_name_var).grid(row=i, pady=5)

    def proceed(self):
        num_players = int(self.num_players_var.get())
        self.players_names = []

        # Mettre à jour la liste des noms des joueurs
        self.players_names = [var.get() for var in self.current_players_vars]

        # Afficher les informations
        print("Nombre de joueurs :", num_players)
        print("Noms des joueurs :", self.players_names)

    def validate_num_players(self, input_text):
        # Fonction de rappel pour valider la saisie dans le champ num_players_entry
        return input_text.isdigit()

    def charger_backlog(self):
        # Charger le fichier JSON dans une variable
        with open(self.chemin_backlog, 'r') as fichier:
            self.contenu = json.load(fichier)

    def afficher_backlog(self):
        # Afficher le contenu du backlog
        print(self.contenu)

    # Méthode pour charger le backlog depuis un fichier JSON
    def load_backlog(self):
        file_path = filedialog.askopenfilename(
            title="Sélectionner un fichier JSON",
            filetypes=[("Fichiers JSON", "*.json"), ("Tous les fichiers", "*.*")]
        )

        if file_path:
            self.chemin_backlog = file_path
            self.charger_backlog()
            self.afficher_backlog()

    def play_local(self):
        # Afficher une fenêtre pour le mode de jeu local
        mode = self.game_mode_var.get()
        if not mode and not self.players_names:
            messagebox.showerror("Erreur", "Veuillez choisir un mode de jeu.")
            return
        messagebox.showinfo("Mode de jeu local", f"Vous jouez en local au mode : {mode}")




### Partie à distance 
        
    def play_remote(self):
        # Afficher une fenêtre pour choisir entre Hôte et Joueur
        remote_window = tk.Toplevel(self.root)
        remote_window.title("Jouer à distance")
        remote_window.geometry("75x100")
        ttk.Button(remote_window, text="Hôte", command=self.host_game).grid(column=0, row=0, pady=10)
        ttk.Button(remote_window, text="Joueur", command=self.join_game).grid(column=0, row=1, pady=10)
        remote_window.grid_columnconfigure(0, weight=1)

    def host_game(self):
        # L'utilisateur choisit d'être l'hôte
        host_window = tk.Toplevel(self.root)
        host_window.title("Configurer le serveur")
        host_window.geometry("300x150")

        ttk.Label(host_window, text="Configurer le serveur :").grid(row=0, column=0, columnspan=2, pady=10)

        port_label = ttk.Label(host_window, text="Port :")
        port_label.grid(row=1, column=0, pady=5)
        port_entry = ttk.Entry(host_window)
        port_entry.grid(row=1, column=1, pady=5)

        start_button = ttk.Button(host_window, text="Démarrer le serveur", command=lambda: self.start_server(port_entry.get(), host_window))
        start_button.grid(row=2, column=0, columnspan=2, pady=10)

    def accept_connections(self, server_socket, host_window):
        # Attendre les connexions entrantes
        while True:
            client_socket, client_address = server_socket.accept()
            ttk.Label(host_window, text=f"Connexion établie avec {client_address}").grid(row=4, column=0, columnspan=2, pady=5)
            # Ajouter ici le code pour gérer la communication avec le client

    def start_server(self, port, host_window):
        # Démarrer le serveur sur le port spécifié
        try:
            port = int(port)
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.bind(('0.0.0.0', port))
            server_socket.listen(1)

            ttk.Label(host_window, text=f"Serveur démarré sur le port {port}").grid(row=3, column=0, columnspan=2, pady=10)

           # threading.Thread(target=self.accept_connections, args=(server_socket, host_window)).start()

        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un numéro de port valide.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors du démarrage du serveur : {str(e)}")

    def join_game(self):
        # L'utilisateur choisit d'être un joueur
        join_window = tk.Toplevel(self.root)
        join_window.title("Rejoindre la partie")

        ttk.Label(join_window, text="Entrez l'adresse IP/Code de l'hôte :").grid(row=0, pady=10)
        ip_entry = ttk.Entry(join_window)
        ip_entry.grid(row=1, pady=10)
        ttk.Button(join_window, text="Rejoindre", command=lambda: self.join_game_action(ip_entry.get())).grid(row=2, pady=10)

    def join_game_action(self, host_address):
        # Fonction pour traiter l'action de rejoindre la partie
        # Vous pouvez ajouter ici le code pour connecter le joueur à la partie de l'hôte
        # Dans la méthode join_game_action
        messagebox.showinfo("Rejoindre la partie", f"Vous rejoignez la partie de l'hôte à l'adresse IP : {host_address} (port Docker)")


if __name__ == "__main__":
    root = tk.Tk()
    app = PlanningPokerApp(root, "backlog/backlog.json")
    root.mainloop()
