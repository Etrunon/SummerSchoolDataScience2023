import math
import re

# Per testare i vari esercizi vai in fondo e 
# scommenta la riga corrispondente.
# Per modificare un esercizio, modifica il suo codice "sotto il def"

def aereoporto():
  
  sic1,sic2,sic3,ga1,ga2,bo1,bo2 = 4,5,8,5,2,7,6   # 24 minuti e 30 secondi
  #sic1,sic2,sic3,ga1,ga2,bo1,bo2 = 9,7,1,3,5,2,9  # 10 minuti e 50 secondi
  
  # scrivi qui
  
  secPrimaFila = (min(sic1, sic2, sic3) + 1) * 4 * 60
  secSecondaFila = (min(ga1, ga2) + 1) * 20
  secTerzaFila = (min(bo1, bo2) + 1) * 30
  
  tot = secPrimaFila + secSecondaFila + secTerzaFila
  
  print(tot)
  
  #minuti = tot // 60
  minuti = 7
  print(minuti)
  
  secondi = tot % 60
  
  print(secondi)
  
  print(minuti, " minuti e ", secondi, " secondi")
  
  print("modulo: ", 600 % 60)


# ################################################################################
# ################################################################################
# ################################################################################
# ################################################################################


def boccino():
  h = 30
  w = 20
  r = 5
  
  
  #x=17; y=25   # a   fascia: False   cerchio: False
  #x=19; y=36  # b   fascia: True    cerchio: False
  x=8;  y=36  # c   fascia: True    cerchio: True
  #x=16; y=32  # d   fascia: True    cerchio: False
  #x=7;  y=41  # e   fascia: False   cerchio: False
  #x=12;y=33   # f   fascia: True    cerchio: True
  
  # scrivi qui
  print("Calcolo per la boccia in: ", x, ",", y)
  print(f"Calcolo per la boccia in: {x}, {y}")

  fascia = y < (h + 2*r) and y > h
  print("E' nella fascia? ", fascia)


  boc_x = w / 2
  boc_y = h + r
  distanza = math.sqrt((boc_x - x)**2 + (boc_y -y)**2)
  cerchio = distanza < r
  print("E' nel cerchio? ", cerchio)


# ################################################################################
# ################################################################################
# ################################################################################
# ################################################################################


def psycho():
  lunghezza_etichetta = 48
  #num_canzone = 3    #  Into the Void _________________________________
  num_canzone = 9   #  Journey of 1,000 Years ________________________
  
  kiss_album = """Psycho Circus _________________________________
Within ________________________________________
I Pledge Allegiance to the State of Rock & Roll
Into the Void _________________________________
We Are One ____________________________________
You Wanted the Best ___________________________
Raise Your Glasses ____________________________
I Finally Found My Way_________________________
Dreamin _______________________________________
Journey of 1,000 Years ________________________"""

  i = num_canzone * lunghezza_etichetta
  canzone = kiss_album[i:i+lunghezza_etichetta -1]
  print(canzone)

  canzone = kiss_album[num_canzone*lunghezza_etichetta: 47+num_canzone*lunghezza_etichetta]
  print(canzone)

  print(len("Psycho Circus _________________________________"))


# ################################################################################
# ################################################################################
# ################################################################################
# ################################################################################


def tiramisu():
  testo = """Ed è proprio da questa portentosa crema che nasce la crema al mascarpone
base del tiramisù, prima classificata al premio Crema dell'Anno insieme
alla nutella. Il dolce italiano per eccellenza, quello più famoso e amato,
ma soprattutto che ha dato vita a tantissime altre versioni, anche tiramisù senza uova!
Poi il Tiramisù alle fragole o quello alla Nutella, giusto per citarne un paio!
Senza contare le rivisitazioni più raffinate come la crostata morbida o la torta al tiramisù.
"""

  parola_malefica1 = "Tiramisù"
  parola_malefica2 = "nutella"
  
  censura = "******"
  
  testo_censurato = ''
  
  # scrivi qui
  testo_censurato = testo.replace(parola_malefica1, censura)
  testo_censurato = testo_censurato.replace(parola_malefica1.lower(), censura)

  testo_censurato = testo_censurato.replace(parola_malefica2, censura)
  testo_censurato = testo_censurato.replace(parola_malefica2.capitalize(), censura)
  
  #######################################################
  
  testo_censurato = testo.replace(parola_malefica1, censura)\
  .replace(parola_malefica1.lower(), censura)\
  .replace(parola_malefica2, censura)\
  .replace(parola_malefica2.capitalize(), censura)
  

  print(testo_censurato)

  occorrenze = testo_censurato.count(censura)
  
  print(f"Cesurate {occorrenze} parole")


# ################################################################################
# ################################################################################
# ################################################################################
# ################################################################################


def cocomero():
  testo = """Ed è cocomero proprio da questa portentosa crema che nasce la crema al mascarpone
base del tiramisù,  cocomero prima classificata al premio Crema dell'Anno insieme
alla nutella. Il dolce italiano per eccellenza, quello più famoso cocomero e amato,
ma soprattutto che ha dato vita a tantissime altre versioni, anche tiramisù senza uova!
Poi il Tiramisù alle fragole o quello alla Nutella, giusto cocomero per citarne un paio!
Senza contare le rivisitazioni più raffinate come la crostata morbida o la torta al tiramisù.
"""

  parola_malefica1 = "cocomero"
  censura = "******"

  taglio = testo.find(parola_malefica1) + len(parola_malefica1) + 1
  prima = testo[:taglio]
  seconda = testo[taglio:].replace(parola_malefica1, censura)

  print(prima + seconda)




# ################################################################################
# ################################################################################
# ################################################################################
# ################################################################################

#aereoporto()
#boccino()
#psycho()
#tiramisu()
#cocomero()