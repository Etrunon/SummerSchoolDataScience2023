# Per testare i vari esercizi vai in fondo e 
# scommenta la riga corrispondente.
# Per modificare un esercizio, modifica il suo codice "sotto il def"


# ################################################################################
# ################################################################################
# ################################################################################
# ################################################################################


def castelli():
  # the castle project

  tn, bw  = 3, 7       # 3 towers,  each large 7 (excluding walls '|')
  #tn, bw  = 3, 3      # ASSUME bw has only values 3 + 4x  with x >= 0
  #tn, bw  = 2, 11     # ASSUME tn is always >= 1
  #tn, bw  = 1, 15     
  #tn, bw  = 4, 7
  #tn, bw  = 4, 3
  
  
  # adds extra ***** lines for clarity during development
  # once your code is working, you can set it to False         
  dev_mode = False  
                              
  """
      
  Single lines:   ─ │ ┌ ┐ └ ┘ ┬ ┴ ├ ┼ ┤     
  
  Double lines:   ═ ║ ╔ ╗ ╚ ╝ ╦ ╩ ╠ ╬ ╣     
  
       Shading:   ░ ▒ ▓ █ ▄ ▀ ■             
  
  
  bw2 = project.bw // 2      #  '|' excluded!
  
         bw      bw
      |-------|-------|
  
   bw2 bw2 bw2 bw2 bw2 bw2    
  |---|---|---|---|---|---| 
  
     ┌─┐ ┌─┐ ┌─┐     ┌─┐ ┌─┐ ┌─┐     ┌─┐ ┌─┐ ┌─┐
     │ └─┘ └─┘ │     │ └─┘ └─┘ │     │ └─┘ └─┘ │
     │         │     │         │     │         │
     └┬───────┬┘     └┬───────┬┘     └┬───────┬┘
      │       │       │       │       │       │
      │  ┌─┐  │       │  ┌─┐  │       │  ┌─┐  │     
      │  └─┘  │       │  └─┘  │       │  └─┘  │
      │       │       │       │       │       │
      │       │       │       │       │       │
  ┌───┴───────┴───────┴───────┴───────┴───────┴───┐
  │                                               │
  │                                               │ 
  │                    ╔═════╗                    │
  │                   ╔╝     ╚╗                   │
  │                   ║       ║                   │
  │                   ║       ║                   │
  └───────────────────╩═══════╩───────────────────┘
  """
  sTorre = "     "
  infraTorreA = " " * (bw-3)
  merloSu = "┌─┐ "
  merloGiu = "└─┘ "
  tn = tn+2
  
  cimaTorre = sTorre + (merloSu * 3 + infraTorreA) * tn  + "\n"
  cimaTorre = cimaTorre + sTorre + ("| " + merloGiu * 2 + "| " + infraTorreA) * tn + "\n"
  corpoTorre = sTorre + ("|" + " " * (bw + 2) + "|" + " " * (bw -2)) * tn + "\n"
  fineTorre = sTorre + ("└┬" + " " * bw + "┬┘ " + infraTorreA) * tn


  castello = cimaTorre + corpoTorre * 3 + fineTorre
  print(castello)
  print("\n"*10)
  


  
  cima = """     ┌─┐ ┌─┐ ┌─┐     ┌─┐ ┌─┐ ┌─┐     ┌─┐ ┌─┐ ┌─┐
     │ └─┘ └─┘ │     │ └─┘ └─┘ │     │ └─┘ └─┘ │
"""
  altezzaTorre = """     │         │     │         │     │         │\n"""
  baseCima = """     └┬───────┬┘     └┬───────┬┘     └┬───────┬┘\n"""
  muro = """      │       │       │       │       │       │\n"""
  muroCastello = """  │                                               │\n"""
  finestra = """      │  ┌─┐  │       │  ┌─┐  │       │  ┌─┐  │\n      │  └─┘  │       │  └─┘  │       │  └─┘  │\n"""  
  base = """  ┌───┴───────┴───────┴───────┴───────┴───────┴───┐\n"""
  porta = """  │                    ╔═════╗                    │
  │                   ╔╝     ╚╗                   │
  │                   ║       ║                   │
  │                   ║       ║                   │
  └───────────────────╩═══════╩───────────────────┘"""
  
  castello = cima + altezzaTorre * 8 + baseCima + muro * 5 + finestra + muro * 3 + finestra + muro * 2 + base + muroCastello * 5 + porta

  print(castello)




# ################################################################################
# ################################################################################
# ################################################################################
# ################################################################################


def treCarte():
  # Input (NON MODIFICARE)

  carta1, carta2, carta3 = (3, "Fiori"), (5, "Quadri"), (10, "Picche")
  #           Prima mano: ((3, 'Fiori'), (5, 'Quadri'))
  #         Seconda mano: ((3, 'Fiori'), (5, 'Quadri'), (10, 'Picche'))
  
  
  #carta1, carta2, carta3 = (6, "Cuori"), (8, "Picche"), (3, "Quadri")
  #          Prima mano: ((6, 'Cuori'), (8, 'Picche'))
  #        Seconda mano: ((6, 'Cuori'), (8, 'Picche'), (3, 'Quadri'))
  
  # scrivi qui
  prima = (carta1, carta2)
  #seconda = (carta1, carta2, carta3)

  print(type(carta3))
  print(type(1))
  print(type([1]))
  print(type([carta3]))
  print(type(([(carta3)],)))
  
  print(      (carta3, )        )
  print(      (carta3, "qualcosaltro")        )
  
  seconda = prima + (carta3, )

  print(f"Prima: {prima}")
  print(f"Seconda: {seconda}")



# ################################################################################
# ################################################################################
# ################################################################################
# ################################################################################


def cannocchiale():
  s = "cannocchiale"

  cannolist = list(s)

  print(cannolist)
  cannolist.sort()
  print(cannolist)
  cannotupl = tuple(cannolist)

  print(cannotupl)

  res = sorted(tuple(s))
  print(f"res: {res}")
  print(f"cose: {res[2]*6}!!! :D")




# ################################################################################
# ################################################################################
# ################################################################################
# ################################################################################


def festoneLaurea():
  # Input (NON modificare)

  invitati_miei =   ["VittorioG", "LucaB", "DavidL", "GiorgioC", "MichelaF", "GiuliaA", "VittorioG", ]
  invitati_gianni = ["SamanthaV", "LucaB", "GiorgioC", "MichelaF", "MartaB", "EmmaK"]
  invitati_giulia = ["DavidL", "GiorgioC", "MichelaF", "MassimilianoL", "VittorioG", "RobertoU", "EmmaK"]
  
  # scrivi qui
  #1 Trova il numero di invitati effettivi (le persone che verranno alla festa)
  #2 Stampa la lista di nomi SENZA duplicati
  #3 Trova il numero delle persone che hanno ricevuto almeno 2 inviti
  #4 Trova l’elenco delle persone che hanno ricevuto almeno 2 inviti

  invitatiUnici = set(invitati_miei+invitati_gianni + invitati_giulia)

  print(f"Numero invitati unici: {len(invitatiUnici)}") # punto 1
  print(f"ListaInvitatiUnici: {sorted(list(invitatiUnici))}\n\n") # punto 2

  invMiei = set(invitati_miei)
  invGiulia = set(invitati_giulia)
  invGianni = set(invitati_gianni)

  #amiciComune = (invMiei & invGiulia | invMiei & invGianni | invGianni & invGiulia)
  # ERRORE amiciComune = invMiei | invGiulia | invGianni
  # tre volte
  amiciComune = invMiei & invGianni & invGiulia

  print(f"Amici in comune: {sorted(list(amiciComune))}")
  print(f"Amici in comune: {len(amiciComune)}")
  



# ################################################################################
# ################################################################################
# ################################################################################
# ################################################################################


def matrimoni():
  matrimoni = ["Amilcare-Maria Eusonia", "Oronzo Pio-Genoveffa", "Venceslao-Elvira"]
  #matrimoni = ["Liutprando-Brunilde", "Clodoveo-Elvira Pancrazia Ludmilla", "Gian Evaristo-Ubalda"]

  # scrivi qui
  dt1 = matrimoni[0].find("-")
  dt2 = matrimoni[1].find("-")
  dt3 = matrimoni[2].find("-")

  diz = {
    matrimoni[0][:dt1] : matrimoni[0][dt1+1:],
    matrimoni[1][:dt2] : matrimoni[1][dt2+1:],
    matrimoni[2][:dt3] : matrimoni[2][dt3+1:],
  }

  print(diz)

  # Soluzione Pro
  sm1 = matrimoni[0].split("-")
  sm2 = matrimoni[1].split("-")
  sm3 = matrimoni[2].split("-")

  print(sm1)

  diz = {
    sm1[0] : sm1[1],
    sm2[0] : sm2[1],
    sm3[0] : sm3[1]
  }

  print(diz)




# ################################################################################
# ################################################################################
# ################################################################################
# ################################################################################


def pescatori():
  ristorante, pesci = "Il Galeone", "carpe"            # True
  ristorante, pesci = "Il Galeone", "aringhe"         # False
  #ristorante, pesci = "Al Molo",    "trote"           # True
  #ristorante, pesci = "Al Molo",    "orate"           # False
  #ristorante, pesci = "La Cambusa", "merluzzi"        # False
  ristorante, pesci = "Da Zio Beppe", "aringhe"        # ??
  ristorante, pesci = "Da Zio Beppe", "tostapane"        # ??
  


  registro = {
    "L'Ancora"  : ['aringhe', 'carpe'],
    "Il Galeone": ['merluzzi', 'carpe', 'trote'],
    "Al Molo"   : ['trote'],
    "La Cambusa": ['aringhe', 'carpe'],
  }

  # scrivi qui

  res = ristorante in registro and pesci in registro[ristorante]

  # alternativa equivalente  print(ristorante in registro.keys())
  
  print(res)




# ################################################################################
# ################################################################################
# ################################################################################
# ################################################################################


#castelli()
#treCarte()
#cannocchiale()
#festoneLaurea()
#matrimoni()
#pescatori()