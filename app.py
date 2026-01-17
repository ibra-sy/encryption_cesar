"""
Application Flask - TP Cybersécurité : Chiffrement de César
Application web pédagogique pour le chiffrement et déchiffrement de messages
"""

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


def chiffrer(message, cle):
    """
    Chiffre un message avec l'algorithme de César.
    
    Args:
        message (str): Le message à chiffrer
        cle (int): La clé de décalage (nombre de positions)
    
    Returns:
        str: Le message chiffré
    """
    message_chiffre = ""
    
    for caractere in message:
        # Convertir le caractère en code (ASCII/Unicode)
        code_caractere = ord(caractere)
        
        # Gérer la plage étendue pour inclure les caractères accentués
        # Plage 32-255 couvre ASCII étendu et Latin-1 (ISO-8859-1)
        # Cela inclut les caractères accentués français (à, é, è, ê, etc.)
        # Il y a 224 caractères dans cette plage (255 - 32 + 1 = 224)
        
        # Vérifier si le caractère est dans la plage gérée
        if 32 <= code_caractere <= 255:
            # Appliquer le décalage avec modulo pour le décalage circulaire
            nouveau_code = ((code_caractere - 32 + cle) % 224) + 32
            # Convertir le nouveau code en caractère
            message_chiffre += chr(nouveau_code)
        else:
            # Si le caractère n'est pas dans la plage, le laisser tel quel
            # (pour les caractères spéciaux UTF-8 non pris en charge)
            message_chiffre += caractere
    
    return message_chiffre


def dechiffrer(message, cle):
    """
    Déchiffre un message chiffré avec l'algorithme de César.
    
    Args:
        message (str): Le message chiffré
        cle (int): La clé de décalage utilisée pour chiffrer
    
    Returns:
        str: Le message déchiffré
    """
    # Déchiffrer revient à chiffrer avec la clé négative
    return chiffrer(message, -cle)


# Route 1 : Page de présentation
@app.route('/')
def index():
    """Page d'accueil avec présentation du projet."""
    return render_template('index.html')


# Route 2 : Page de choix (chiffrer ou déchiffrer)
@app.route('/choix')
def choix():
    """Page permettant de choisir entre chiffrement et déchiffrement."""
    return render_template('choix.html')


# Route 3a : Page de chiffrement
@app.route('/chiffrer', methods=['GET', 'POST'])
def page_chiffrer():
    """Page pour chiffrer un message."""
    message_chiffre = None
    message_input = ''
    cle_input = ''
    
    if request.method == 'POST':
        message_input = request.form.get('message', '')
        cle_input = request.form.get('cle', '')
        try:
            cle = int(cle_input) if cle_input else 0
            if message_input:
                message_chiffre = chiffrer(message_input, cle)
        except ValueError:
            message_chiffre = "Erreur: La clé doit être un nombre entier."
    
    return render_template('chiffrer.html', message_chiffre=message_chiffre, message_input=message_input, cle_input=cle_input)


# Route 3b : Page de déchiffrement
@app.route('/dechiffrer', methods=['GET', 'POST'])
def page_dechiffrer():
    """Page pour déchiffrer un message."""
    message_dechiffre = None
    message_input = ''
    cle_input = ''
    
    if request.method == 'POST':
        message_input = request.form.get('message', '')
        cle_input = request.form.get('cle', '')
        try:
            cle = int(cle_input) if cle_input else 0
            if message_input:
                message_dechiffre = dechiffrer(message_input, cle)
        except ValueError:
            message_dechiffre = "Erreur: La clé doit être un nombre entier."
    
    return render_template('dechiffrer.html', message_dechiffre=message_dechiffre, message_input=message_input, cle_input=cle_input)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
