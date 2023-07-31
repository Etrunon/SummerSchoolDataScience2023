import csv

def leggiERiscriviFile():
  # Apertura file CSV con libreria
  with open("esempio-1.csv", encoding='utf-8', newline='') as fileOrigine:
      lettore = csv.reader(fileOrigine, delimiter=',')
  
      with open("file_destinazione.csv", "w", encoding='utf-8', newline='') as fileDestinazione:
        scrittore = csv.writer(fileDestinazione, delimiter=',')

        scrittore.writerow(["ciao", "mamma"])
        for riga in lettore:
          scrittore.writerow(riga)

# ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  
# #####   #####   #####   #####   #####   #####   #####   #####   #####   
# ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  

def leggiMaterializzaEScrivi():
  deposito = []
  with open("esempio-1.csv", encoding='utf-8', newline='') as fileOrigine:
    lettore = csv.reader(fileOrigine, delimiter=',')

    for riga in lettore:
      deposito.append(riga)
      
  with open("file_destinazione.csv", "w", encoding='utf-8', newline='') as fileDestinazione:
    scrittore = csv.writer(fileDestinazione, delimiter=',')
  
    for riga in deposito:
      scrittore.writerow(riga)

# ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  
# #####   #####   #####   #####   #####   #####   #####   #####   #####   
# ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  

def leggiInvertiERiscrivi():
    # Apertura file CSV con libreria
  with open("esempio-1.csv", encoding='utf-8', newline='') as fileOrigine:
      lettore = csv.reader(fileOrigine, delimiter=',')
  
      with open("file_destinazione.csv", "w", encoding='utf-8', newline='') as fileDestinazione:
        scrittore = csv.writer(fileDestinazione, delimiter=',')
  
        for riga in lettore:
          scrittore.writerow([riga[1], riga[0]])

# ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  
# #####   #####   #####   #####   #####   #####   #####   #####   #####   
# ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  

def cheSuccede():
    # Apertura file CSV con libreria
  with open("esempio-1.csv", encoding='utf-8', newline='') as fileOrigine:
    lettore = csv.reader(fileOrigine, delimiter=',')



    with open("file_destinazione_cheSuccede.csv", "w", encoding='utf-8', newline='') as fileDestinazione:
      scrittore = csv.writer(fileDestinazione, delimiter=',')
          
      scrittore.writerow(["ciao", "mamma"])
      for riga in lettore:
        print(riga)
        scrittore.writerow(riga)

# ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  
# #####   #####   #####   #####   #####   #####   #####   #####   #####   
# ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  

def selezioneRiga():
    with open("esempio-1.csv", encoding='utf-8', newline='') as fileOrigine:
      lettore = csv.reader(fileOrigine, delimiter=',')

      contatore = 0
      for riga in lettore:
        # Sampiamo solo la riga contenente "pellicano"
        if "pellicano" in riga:
          print(riga)
        if "pellicano" == riga[0]:
          print(riga)
        if contatore == 3:
          print(riga)
        contatore += 1

# ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  
# #####   #####   #####   #####   #####   #####   #####   #####   #####   
# ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  

def comeSaltarePrimaRiga():
  # Stampiamo tutti dati senza la prima riga
  with open("esempio-1.csv", encoding='utf-8', newline='') as fileOrigine:
    lettore = csv.reader(fileOrigine, delimiter=',')
    next(lettore)   # <--------------------
    for riga in lettore:
      print(riga)
  
# ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  
# #####   #####   #####   #####   #####   #####   #####   #####   #####   
# ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  

def cureTermali():
  costoUnitario = 100
  risultato = {}
  
  with open("centro-benessere1.csv", encoding='utf-8', newline='') as fileOrigine:
    lettore = csv.reader(fileOrigine, delimiter=',')
    next(lettore)   # <--------------------
  
    for riga in lettore:
      serviziUsufruiti = riga[1:]
      prezzo = serviziUsufruiti.count("1") * costoUnitario
      risultato[riga[0]] = prezzo

  print(risultato)

# ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  
# #####   #####   #####   #####   #####   #####   #####   #####   #####   
# ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  

def cureTermaliMaterializzate():
  costoUnitario = 100
  risultato = {}

  deposito = []
  with open("centro-benessere1.csv", encoding='utf-8', newline='') as fileOrigine:
    lettore = csv.reader(fileOrigine, delimiter=',')
    next(lettore)   # <--------------------
    for riga in lettore:
      deposito.append(riga)

  print(deposito)
  
  for riga in deposito:
    serviziUsufruiti = riga[1:]
    prezzo = serviziUsufruiti.count("1") * costoUnitario
    risultato[riga[0]] = prezzo

  print(risultato)

# ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  
# #####   #####   #####   #####   #####   #####   #####   #####   #####   
# ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  ###  

#leggiERiscriviFile()
#leggiMaterializzaEScrivi()
#cheSuccede()
#leggiInvertiERiscrivi()
#selezioneRiga()
#comeSaltarePrimaRiga()

#cureTermali()
cureTermaliMaterializzate()