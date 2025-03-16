#Décodeur Cipher

#Sert à retirer les accents
import unicodedata

#Détecte un nombre dans le Cipher
def Numberin(Kryptos):
    return(any(char.isdigit() for char in Kryptos))

#Détecte si il y a deux même lettres dans le Cipher
def TwoLin(Kryptos):
    TwoOcc = False
    for i in range(len(Kryptos)):
        if Kryptos.count(Kryptos[i]) > 1:
            TwoOcc = True
        else:
            if not TwoOcc:
                TwoOcc = False
    return(TwoOcc)

#Fonction qui remplace les accents et points
def Repoints(Sentence):
    Sentence = ''.join(c for c in unicodedata.normalize('NFD', Sentence) if not unicodedata.combining(c))
    Sentence = Sentence.replace("'","")
    Sentence = Sentence.replace("-","")
    Sentence = Sentence.replace(".","")
    Sentence = Sentence.replace("!","")
    Sentence = Sentence.replace(":","")
    Sentence = Sentence.replace("?","")
    Sentence = Sentence.replace(",","")
    return(Sentence)

#Définit la première ligne de la table de Cipher
def AlpKryptation(Startkey):
    AlpKrypted = Startkey
    for i in range(26):
        if not Alphabet[i] in Startkey:
            AlpKrypted += Alphabet[i]
    print(AlpKrypted)
    return(AlpKrypted)

#Demande un début d'alphabet
Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Startkey = str(input("Quel est le début de la table ? (Par défaut ABC...) : ")).upper()
while Numberin(Startkey) or TwoLin(Startkey):
    print("Ne mettez pas de nombres ni deux mêmes charactères.")
    Startkey = str(input("Quel est le début de la table ? (Par défaut ABC...) : ")).upper()
Startkey = Repoints(Startkey)
AlpKrypted = Alphabet
if not Startkey == "":
    AlpKrypted = AlpKryptation(Startkey)

#Fait une liste pour chaque ligne de la table
listAlp = []
for i in range(26):
    listAlp.append(AlpKrypted)
    Letter = AlpKrypted[0]
    Intermed = AlpKrypted[1:]
    AlpKrypted = Intermed + Letter

#Définit une liste pour décoder un message
def Decode():
    CODE = str(input("Quel est le code à décoder ? ")).upper()
    Keycode = Repoints(str(input("Quelle est la clé ? ")).upper())
    while len(Keycode) > len(CODE):
        print("La clé est plus longue que le code, veuillez rentrer une clé plus courte.")
        Keycode = Repoints(str(input("Quelle est la clé ? ")).upper())
    Keycodeind=0
    Solution = ""
    for i in range(len(CODE)):
        Letter = Keycode[Keycodeind]
        Indice = listAlp[0].index(Letter)
        Line = 0
        actuaLine = listAlp[Line]
        while actuaLine[Indice] != CODE[i]:
            Line += 1
            actuaLine = listAlp[Line]
        Solution += actuaLine[0]
        Keycodeind += 1
        if Keycodeind > (len(Keycode)-1):
            Keycodeind = 0
    print("")
    print("Votre message décodé est : " + Solution)

#Définit une liste pour encoder un message
def Encode():
    CODE = Repoints(str(input("Quel est le message à encoder ? ")).upper().replace(" ",""))
    Keycode = Repoints(str(input("Quelle est la clé ? ")).upper())
    while len(Keycode) > len(CODE):
        print("La clé est plus longue que le code, veuillez rentrer une clé plus courte.")
        Keycode = Repoints(str(input("Quelle est la clé ? ")).upper())
    Keycodeind = 0
    Coded = ""
    for i in range(len(CODE)):
        Letter = Keycode[Keycodeind]
        Indice = listAlp[0].index(Letter)
        Line = 0
        actuaLine = listAlp[Line]
        while actuaLine[0] != CODE[i]:
            Line += 1
            actuaLine = listAlp[Line]
        Coded += actuaLine[Indice]
        Keycodeind += 1
        if Keycodeind > (len(Keycode)-1):
            Keycodeind = 0
    print("")
    print("Votre message codé est : " + Coded)

#Demande quelle action éxécuter entre décoder ou encoder
def Question():
    print("")
    print("Voulez-vous :")
    print("(1) Décoder")
    print("    ou    ")
    print("(2) Encoder ?")
    Option = input("1 ou 2 : ")
    if Option == "1" or Option == "2":
        Option = int(Option)
    return(Option)

#Execute Decode() ou Encode() en fonction de la réponse
Answer = Question()
while type(Answer) != int:
    print("")
    print("Veuillez rentrer 1 ou 2")
    Answer = Question()
print("")
if Answer == 1:
    Decode()
else:
    Encode()