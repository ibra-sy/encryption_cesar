# 🔐 Application Web - Chiffrement de César

Application web Flask pédagogique pour le chiffrement et déchiffrement de messages avec l'algorithme de César.

## 🎯 Fonctionnalités

- ✅ Chiffrement de messages avec clé personnalisée
- ✅ Déchiffrement de messages chiffrés
- ✅ Gestion complète des caractères (lettres, chiffres, symboles, accents français)
- ✅ Interface web moderne avec thème sombre type Hack The Box
- ✅ Animation de background avec caractères cryptographiques
- ✅ Conservation des valeurs de formulaire après soumission

## 🚀 Installation et utilisation

### Prérequis

- Python 3.7+
- pip

### Installation

```bash
# Cloner le dépôt
git clone https://github.com/ibra-sy/encryption_cesar.git
cd encryption_cesar

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
python app.py
```

L'application sera accessible à l'adresse : `http://localhost:5000`

## 📁 Structure du projet

```
encryption_cesar/
├── app.py                 # Application Flask principale
├── requirements.txt       # Dépendances Python
├── ALGORITHME.md         # Explication détaillée de l'algorithme
├── README.md             # Ce fichier
├── .gitignore            # Fichiers ignorés par Git
└── templates/            # Templates HTML
    ├── index.html        # Page d'accueil
    ├── choix.html        # Page de choix (chiffrer/déchiffrer)
    ├── chiffrer.html     # Page de chiffrement
    └── dechiffrer.html   # Page de déchiffrement
```

## 🔑 Algorithme

L'algorithme de chiffrement de César utilise un décalage circulaire basé sur les codes ASCII.

**Formule** :
```python
nouveau_code = ((ord(caractere) - 32 + cle) % 224) + 32
```

**Plage gérée** : Codes 32-255 (224 caractères), incluant :
- Lettres (a-z, A-Z)
- Chiffres (0-9)
- Symboles et ponctuation
- Caractères accentués français (à, é, è, ê, etc.)

Pour plus de détails, consultez [ALGORITHME.md](ALGORITHME.md).

## 🛠️ Technologies utilisées

- **Backend** : Python 3, Flask
- **Frontend** : HTML5, CSS3, Bootstrap 5
- **Fonctions Python** : `ord()`, `chr()`, arithmétique modulaire

## 📝 Utilisation

1. Accédez à la page d'accueil
2. Cliquez sur "Commencer"
3. Choisissez "Chiffrer" ou "Déchiffrer"
4. Entrez votre message et la clé
5. Visualisez le résultat

## 📄 Licence

Ce projet est destiné à des fins pédagogiques dans le cadre d'un TP de cybersécurité.

## 👤 Auteur

**ibra-sy**

---

⭐ N'hésitez pas à contribuer ou à signaler des problèmes !
