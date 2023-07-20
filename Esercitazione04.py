# Per testare i vari esercizi vai in fondo e 
# scommenta la riga corrispondente.
# Per modificare un esercizio, modifica il suo codice "sotto il def"


# ################################################################################
# ################################################################################
# ################################################################################
# ################################################################################


def artu():
  ginevra = False; merlino = False; morgana = False
  #ginevra = False; merlino = False; morgana = True
  #ginevra = False; merlino = True; morgana = False
  #ginevra = False; merlino = True; morgana = True
  #ginevra = True; merlino = False; morgana = False
  #ginevra = True; merlino = False; morgana = True
  #ginevra = True; merlino = True; morgana = False
  #ginevra = True; merlino = True; morgana = True
  
  # scrivi qui
  if ginevra and merlino and morgana:
    print("Sono tutti veri cavalieri")
  elif ginevra or merlino or morgana:
    print("C'è almeno un vero cavaliere")
  else:
    print("Non c'è nessun vero cavaliere")


# ###########################################################################
# ###########################################################################
# ###########################################################################


def ascensore2():
  piano_utente = 'terra'; piano_ascensore = 'rialzato'     # rialzato, terra, DING!
  #piano_utente = 'rialzato'; piano_ascensore = 'terra'    # terra, rialzato, DING!
  #piano_utente = 'terra'; piano_ascensore = 'terra'       # DING!
  #piano_utente = 'rialzato'; piano_ascensore = 'rialzato' # DING!
  
  # scrivi qui
  if piano_ascensore != piano_utente: 
    print(piano_ascensore)
    print(piano_utente)
  print("DING!")

  
# ###########################################################################
# ###########################################################################
# ###########################################################################


def ascensore10():
  piano_utente = 3; piano_ascensore = 7
    
  if piano_ascensore != piano_utente:  
    if piano_ascensore < piano_utente:
      #L'ascensore sale
      for i in range(piano_ascensore, piano_utente+1):
        print(i)
    else:
      #L'ascensore scende
      for i in range(piano_ascensore, piano_utente-1, -1):
          print(i)
  print("DING!")


# ###########################################################################
# ###########################################################################
# ###########################################################################


def ascensore10SuperPro():
  piano_utente = 3; piano_ascensore = 7
  verso = 0
  if piano_ascensore < piano_utente:
    verso = 1
  elif piano_ascensore > piano_utente:
    verso = -1
  
  if piano_ascensore != piano_utente:  
    for i in range(piano_ascensore, piano_utente, verso):
      print(i)
    print(piano_utente)
  
  print("DING!")


# ###########################################################################
# ###########################################################################
# ###########################################################################


def spiegazione10Piani():
  print("Quanti tipi di range esistono?")
  for i in range(10):
    print(f"Semplice: {i}")
  for i in range(4, 10):
    print(f"Da-a: {i}")
  for i in range(4, 10, 2):
    print(f"Da-a-passo: {i}")
  for i in range(10, 0, -1):
    print(f"Da-a-passoNegativo: {i}")
  for i in range(10, -1):
    print(f"Da-passoNegativo?: {i}")
  
  print("\n" *20)
  ###########################################
  print("che significa mettere un if dentro un for o viceversa?")
  gelatoCioccolato = True
  indiceGoloso = 3
  
    # "se ti piace il gel cioccolato te ne mangi 10"
  if gelatoCioccolato:
    for i in range(indiceGoloso):
      print("gnam")
    print("x"*5)
  # "per tante volte tante quanti gelati ti mangeresti ti chiedo se ti 
  # piace il cioccolato e se si te ne do uno"
  for i in range(indiceGoloso):
    if gelatoCioccolato:
      print("gnam")
  

# ###########################################################################
# ###########################################################################
# ###########################################################################

  
def palazzo():
  parola = 'palazzo'

  contatore = 0

  print("Soluzione ok")
  for lettera in parola:
    print(f"{contatore}\t{lettera}\t{lettera.upper()}")
    contatore += 1
  print("#"*10)
  print("Soluzione brulla")
  contatore = 0
  for lettera in parola:
    print(f"{contatore}\t{parola[contatore]}\t{parola[contatore].upper()}")
    contatore += 1
  print("#"*10)
  print("Soluzione ok")
  for i in range(len(parola)):
    print(f"{i}\t{parola[i]}\t{parola[i].upper()}")

  
# ###########################################################################
# ###########################################################################
# ###########################################################################

  
def doveIncremento():

  print("Quante dita ha una persona?")
  contatore = 1
  for i in range(5):
    print(contatore)
    contatore += 1

  print("Quante dita ha un alieno?")
  contatore = 0
  for i in range(5):
    contatore += 1
    print(contatore)
  

# ###########################################################################
# ###########################################################################
# ###########################################################################


def bestemmia():
  ricetta = "\t\t   riso\n, \t\t\tpatate\n, cozze\n\t\n"
  print(ricetta)
  ricetta = ricetta.split(",")
  print(ricetta)


  for ingrediente in ricetta:
    ingrediente = ingrediente.strip()
    print(ingrediente)
  
  print(ricetta)
  

# ###########################################################################
# ###########################################################################
# ###########################################################################


def menoBestemmia():
  ricetta = "\t\t   riso\n, \t\t\tpatate\n, cozze\n\t\n"
  print(ricetta)
  ricetta = ricetta.split(",")
  print(ricetta)

  ricettaPulita = []

  for ingrediente in ricetta:
    ricettaPulita.append(ingrediente.strip())
    # Oppure
    # ricettaPulita + ingrediente.strip()
  
  print(ricetta)
  print(ricettaPulita)
  

# ###########################################################################
# ###########################################################################
# ###########################################################################


def esempioBorderline():
  l = [1, 2, 3]

  print(l)
  for i in range(len(l)):
    l.append(i)

  print(l)
  

# ###########################################################################
# ###########################################################################
# ###########################################################################


#artu()
#ascensore2()
#ascensore10SuperPro()
#spiegazione10Piani()
#palazzo()
#doveIncremento()
#bestemmia()
#menoBestemmia()
esempioBorderline()
