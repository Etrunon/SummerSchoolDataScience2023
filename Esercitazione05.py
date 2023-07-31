# Per testare i vari esercizi vai in fondo e 
# scommenta la riga corrispondente.
# Per modificare un esercizio, modifica il suo codice "sotto il def"



# Correzione Esame

def esercizio1():
  intervallo,  parola = (3,8) , "passeggiare"   # pasSEGGIare
  #intervallo, parola = (2,5) , "calamaro"      # caLAMaro
  #intervallo, parola = (0,5) , "barca"         # BARCA

  p1 = parola[:3]
  p2 = parola[3:8].upper()
  p3 = parola[8:]
  
  nuovaParola = p1 + p2 +p3
  print(nuovaParola)


def esercizio2():
  messaggio,la="METTIb-POS3-VOLTE4", ['c','h','e','g','a','r','b','a']  # ['c', 'h', 'e', 'bbbb', 'a', 'r', 'b', 'a']
  #messaggio,la="METTIe-POS4-VOLTE2", ['p','a','s','t','a']             # ['p', 'a', 's','t','e', 'e']

  lettera = messaggio[5]
  print(lettera)
  splittato = messaggio.split("-")
  posizione = int(splittato[1][-1])
  volte = int(splittato[2][-1])

  #la = list("nuovaStringa") # QUESTO NO
  la[posizione] = lettera * volte # QUESTO SI

  print(la)


def esercizio3():
  coppia1 = ['pomodoro','zucca']
  coppia2 = 'grano-mais'  # => ("grano", "mais")

  ricettario = {('zucca', 'grano'):'torta di zucca',
         ('grano', 'grano'):'polenta',
         ('pomodoro', 'zucca'):'cavatelli sugo pomodoro e zucca',
         ('grano', 'mais'):'pane injera',
         ('zucca', 'pomodoro'):'parmigiana di zucca e pomodoro',
      }

  print(f"1 {ricettario[tuple(coppia1)]}")

  tmp = coppia2.split("-")   # => ["grano", "mais"]
  print(f"2 {ricettario[tuple(tmp)]}")

def esercizio4():
  deco = ['a','b','c','d','e','f','g','h','i','m','n','o']
  #deco = ['J','I','A','V','M','H']


  limite1 = len(deco) // 3
  terzo1 = deco[:limite1]
  terzo2 = deco[limite1: limite1*2]
  terzo3 = deco[limite1*2:]

  print(terzo1)
  print(terzo2)
  print(terzo3)

  for lettera in terzo1:
    print(lettera)
  print("----")
  for lettera in terzo2:
    print(lettera*2)
  print("----")
  for lettera in terzo3:
    print(lettera*3)
  

# ################################################################################
# ################################################################################
# ################################################################################
# ################################################################################

def codeGolf():
  s = str(111111111**2) 
  for i in map(int,s):
    print(f"{s[:i-1]}{s[-i:]}")

# ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  
# #####   #####   #####   #####   #####   #####   #####   #####   #####   
# ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  

def numnum(num):
  # sostituisci pass (che non fa niente) con il codice della funzione
  pass
  
def pacmanNumeri():
  # NON TOCCARE, queste linee devono funzionare
  x = numnum(3)       # Deve RITORNARE 9
  print(x)
  
  y = numnum(10)      # Deve RITORNARE 100
  print(y)
  
  z = numnum(33)      # Deve RITORNARE 33
  print(z)
  
# ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  
# #####   #####   #####   #####   #####   #####   #####   #####   #####   
# ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  

def miaPrint(parametro):
  parolaMia = "zebra"
  print(parolaMia + parametro)


#miaPrint()
parola = "ciao"
miaPrint("parametroBLABLABLA")
print(parola)

# ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  
# #####   #####   #####   #####   #####   #####   #####   #####   #####   
# ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  

def nobulli(stringaDaPulire):
  risultato = ""
  #caratteriBuoni = ["w", "a", "k", " "]
  caratteriBuoni = "wak "
  for carattere in stringaDaPulire:
    if carattere in caratteriBuoni: # carattereè buono
      risultato += carattere

  return risultato

# ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  
# #####   #####   #####   #####   #####   #####   #####   #####   #####   
# ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  

def bulli():
  bullo1 = "waekai waekai waekai waekai"
  bullo2 = "bwaka rwaka swaka twaka zwaka mmmmmmmmmmmmmmmmmmmmmmmmmmwatka"
  bullo3 = "eweaekea zwxarkma qwoagkpa"
  bullo4 = "    "
  bullo5 = "zzzz"
  
  res1 = nobulli(bullo1)   # Deve RITORNARE il verso pulito "waka waka waka waka"
  print(res1)
  res2 = nobulli(bullo2)   # Deve RITORNARE il verso pulito "waka waka waka waka waka waka"
  print(res2)
  res3 = nobulli(bullo3)   # Deve RITORNARE il verso pulito "waka waka waka"
  print(res3)

# ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  
# #####   #####   #####   #####   #####   #####   #####   #####   #####   
# ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  

#codeGolf()
#esercizio1()
#esercizio2()
#esercizio3()
#esercizio4()
#bulli()