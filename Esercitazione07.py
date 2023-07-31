import random
import string

# ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  
# #####   #####   #####   #####   #####   #####   #####   #####   #####   
# ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  

# FUNZIONE GIA' COMPLETA, NON TOCCARE !
def raggi_cosmici(flusso_dati):
    for x in range(random.randint(1,min(3,len(flusso_dati)))):
        i = random.randint(0,len(flusso_dati)-1)
        #print('i',i)
        lista = list(flusso_dati[i])
        for c in range(random.randint(1,3)):
            #print('lista',lista)
            lista[random.randint(0,len(lista)-1)] = random.choice('0123456789$/()')
            #print('flusso_dati[i]=',flusso_dati[i])
            #print('modifico',flusso_dati[i])
            flusso_dati[i] = ''.join(lista)

# IMPORTANTE: dopo un primo round di testing, SCOMMENTA queste istruzioni random.seed
#             per cambiare gli errori casuali introdotti  e verificare
#             che il tuo programma gestisca anche quelle
# NOTA: Il numero del parametro non influisce sul numero o tipo di errori,
# determina solo  quale sequenza di errori viene generata.
# Se non imposti il seed otterrai errori completamente casuali diversi
# ad ogni esecuzione del programma!

def controllo(data):
  try:
    print("Parsing di: ", data)
    
    if data.count("/") != 2 or data[2] != "/" or data[5] != "/":
      raise ValueError("Formato non valido!")
    
    giorno = data[:2]
    iGiorno = int(giorno)
    if iGiorno > 31:
      raise ValueError("Giorno non valido!")

    mese = data[3:5]
    iMese = int(mese)
    if not (iMese >= 1 and iMese <= 12):
      raise ValueError("Mese non valido!")

    anno = data[6:]
    iAnno = int(anno)
    if not iAnno in range(2020, 2023+1):
      raise ValueError("Anno non valido!")

    print("Conversione OK")
    return iGiorno, iMese, iAnno
      
  except ValueError as mioBellissimoErrore:
    print("ERRORE: ", mioBellissimoErrore)



def baseRaggi():
  #random.seed(7)
  random.seed(6)   # scommenta
  #random.seed(9)   # scommenta
  
  
  calendario = [
      '07/11/2020',
      '30/04/2020',
      '02/10/2022',
      '08/11/2023',
      '25/01/2021',
      '29/05/2023',
  ]
  
  raggi_cosmici(calendario)  # modifica calendario con errori casuali !
  
  # scrivi qui
  for data in calendario:
    print(controllo(data))

# ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  
# #####   #####   #####   #####   #####   #####   #####   #####   #####   
# ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  

# Test che mette a confronto il comportamento di pass e continue
def passEContinue():
  lista = [1, "ciao", [("Asso", 3), ("Quadri", "K")]]

  for i in range(len(lista)):
    print(lista[i])

  for calimero in lista:
    print(calimero)

  print("#" * 30)
  
  for i in range(10):
    print(i)
    pass
    print("ciao")

  for i in range(10, 20):
    print(i)
    continue
    print("ciao")

# ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  
# #####   #####   #####   #####   #####   #####   #####   #####   #####   
# ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  

def murabasso():
  lavori = [
    ["Straordinari in fonderia", 175.13, "non pagato"],
    ["Part time gelateria",      450, "non pagato"],
    ["Rendita investimenti",     1000, "pagato"],
    ["Pettinatura pitoni",       1000, "pagato"],
    ["Installazione artistica",  600, "non pagato"],
    ["Noleggio scarpe eleganti", 100, "non pagato"]
  ]

  # scrivi qui
  valorePagato = 0
  valoreNonPagato = 0
  '''
  for i in range(len(lavori)):
    if lavoro[i][2] == "non pagato":
      valoreNonPagato += lavoro[1]
    elif lavoro[i][2] == "pagato":
      valorePagato += lavoro[1]
  '''
  for lavoro in lavori:
    if lavoro[2] == "non pagato":
      valoreNonPagato += lavoro[1]
    elif lavoro[2] == "pagato":
      valorePagato += lavoro[1]

  print(f"Pagato: {valorePagato}")
  print(f"Non Pagato: {valoreNonPagato}")

  print("########################################################")

  # Ora trovo il lavoro più pagato
  #record = ""
  maxPagato = -1
  for lavoro in lavori:
    if lavoro[2] == "pagato":
      if lavoro[1] > maxPagato:
        maxPagato = lavoro[1]
        #record = lavoro[0]
  
  if maxPagato > 0:
    for lavoro in lavori:
        if lavoro[1] == maxPagato and lavoro[2] == "pagato":
          print(f"Il lavoro più pagato è {lavoro[0]}")
  else:
    print("Ma vai a lavorare pigrone")


#baseRaggi()
#passEContinue()
murabasso()