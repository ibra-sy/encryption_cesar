# 🔐 Algorithme de Chiffrement de César - Explication

## Principe théorique

Le chiffrement de César est un algorithme de **substitution monoalphabétique** où chaque caractère du message est remplacé par un autre caractère situé à un nombre fixe de positions (la **clé**) plus loin dans la plage de caractères utilisée.

**Principe de base** : décaler chaque caractère d'un nombre fixe de positions avec un retour circulaire au début quand on atteint la fin.

## Adaptation pour tous les caractères (ASCII étendu)

Notre implémentation gère **TOUS** les caractères ASCII imprimables et les caractères accentués :

- **Plage utilisée** : Codes 32 à 255 (224 caractères)
  - 32 = Espace
  - 48-57 = Chiffres (0-9)
  - 65-90 = Majuscules (A-Z)
  - 97-122 = Minuscules (a-z)
  - 192-255 = Caractères accentués français (à, é, è, ê, etc.)
  - 33-47, 58-64, 91-96, 123-191 = Symboles et ponctuation

## Formule mathématique

Pour chaque caractère du message :

```
1. code_ascii = ord(caractere)                    // Conversion en code numérique
2. normalisation = code_ascii - 32                // Décalage à partir de 0
3. decalage_avec_cle = normalisation + cle        // Application de la clé
4. nouveau_code = (decalage_avec_cle % 224) + 32  // Modulo pour le décalage circulaire
5. caractere_chiffre = chr(nouveau_code)          // Reconversion en caractère
```

**Formule condensée** :
```python
nouveau_code = ((ord(caractere) - 32 + cle) % 224) + 32
```

### Pourquoi le modulo 224 ?

- Il y a **224 caractères** dans la plage [32, 255]
- Le modulo 224 garantit que le résultat reste dans [0, 223]
- En ajoutant 32, on revient dans la plage [32, 255]
- **Résultat** : Un décalage circulaire parfait pour tous les caractères, y compris les accents

**Exemple concret** :
```
Caractère : 'é' (code 233 en ISO-8859-1)
Clé : 17

1. code_ascii = 233
2. normalisation = 233 - 32 = 201
3. decalage_avec_cle = 201 + 17 = 218
4. nouveau_code = (218 % 224) + 32 = 218 + 32 = 250
5. caractere_chiffre = chr(250) = 'ú'

Pour déchiffrer : on applique la clé négative (-17)
```

---

## Fonction `chiffrer(message, cle)`

```python
def chiffrer(message, cle):
    message_chiffre = ""
    
    for caractere in message:
        code_caractere = ord(caractere)
        
        # Vérifier si le caractère est dans la plage gérée (32-255)
        if 32 <= code_caractere <= 255:
            # Appliquer le décalage circulaire
            nouveau_code = ((code_caractere - 32 + cle) % 224) + 32
            message_chiffre += chr(nouveau_code)
        else:
            # Caractère hors plage : le laisser tel quel
            message_chiffre += caractere
    
    return message_chiffre
```

### Étapes d'exécution

1. **Initialisation** : Créer une chaîne vide `message_chiffre`
2. **Pour chaque caractère** :
   - Convertir en code numérique avec `ord()`
   - Vérifier s'il est dans la plage [32, 255]
   - Appliquer la formule : `((code - 32 + cle) % 224) + 32`
   - Reconvertir en caractère avec `chr()`
   - Ajouter au message chiffré
3. **Retour** : Le message chiffré complet

**Exemple pas à pas** :
```
Message : "Bonjour"
Clé : 7

'B' : ord('B')=66 → ((66-32+7)%224)+32 = (41%224)+32 = 41+32 = 73 → 'I'
'o' : ord('o')=111 → ((111-32+7)%224)+32 = (86%224)+32 = 86+32 = 118 → 'v'
'n' : ord('n')=110 → ((110-32+7)%224)+32 = (85%224)+32 = 85+32 = 117 → 'u'
'j' : ord('j')=106 → ((106-32+7)%224)+32 = (81%224)+32 = 81+32 = 113 → 'q'
'o' : ord('o')=111 → ((111-32+7)%224)+32 = (86%224)+32 = 86+32 = 118 → 'v'
'u' : ord('u')=117 → ((117-32+7)%224)+32 = (92%224)+32 = 92+32 = 124 → '|'
'r' : ord('r')=114 → ((114-32+7)%224)+32 = (89%224)+32 = 89+32 = 121 → 'y'

Résultat : "Ivqv|y"
```

---

## Fonction `dechiffrer(message, cle)`

```python
def dechiffrer(message, cle):
    return chiffrer(message, -cle)
```

### Principe

**Déchiffrer = Chiffrer avec la clé négative**

C'est la **symétrie** du chiffrement de César :
- Si on chiffre avec la clé `+k`, on déchiffre avec la clé `-k`
- La même fonction fait les deux opérations

### Explication mathématique

Le décalage dans un sens annule le décalage dans l'autre sens :

```
Chiffrement  : nouveau_code = ((code - 32 + cle) % 224) + 32
Déchiffrement : nouveau_code = ((code - 32 - cle) % 224) + 32
                                    ↑
                              Clé négative
```

Le modulo gère automatiquement les valeurs négatives en Python :
- `-7 % 224` = `217` (224 - 7)

**Exemple** :
```
Message chiffré : "Ivqv|y"
Clé : 7

Appel : dechiffrer("Ivqv|y", 7)
  → chiffrer("Ivqv|y", -7)

'I' : ord('I')=73 → ((73-32-7)%224)+32 = (34%224)+32 = 34+32 = 66 → 'B'
'v' : ord('v')=118 → ((118-32-7)%224)+32 = (79%224)+32 = 79+32 = 111 → 'o'
...

Résultat : "Bonjour" ✓
```

---

## Points clés à retenir

1. **Décalage circulaire** : Le modulo 224 garantit que tous les caractères restent dans la plage [32, 255]
2. **Symétrie** : Chiffrer avec `+k` et déchiffrer avec `-k` utilisent la même fonction
3. **Gestion complète** : Tous les caractères (lettres, chiffres, symboles, accents) sont traités uniformément
4. **Fonctions `ord()` et `chr()`** : Conversion entre caractères et codes numériques
5. **Arithmétique modulaire** : Le modulo assure le retour circulaire au début de la plage

---

## Caractéristiques de l'algorithme

- **Chiffrement symétrique** : Même clé pour chiffrer et déchiffrer
- **Substitution monoalphabétique** : Chaque caractère est remplacé par un seul autre (relation 1:1)
- **Déterministe** : Le même message avec la même clé donne toujours le même résultat
- **Rapide** : Traitement linéaire O(n) où n est la longueur du message
- **Faible sécurité** : Facilement cassable par analyse de fréquence (pour l'alphabet classique)
