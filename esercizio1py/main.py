lista_spesa = []


def aggiungi():
    x = str(input("Aggiungi un elemento alla lista \n"))
    lista_spesa.append(x)

def visualizza():
    for i in range(len(lista_spesa)):
        print(f"{i + 1}. {lista_spesa[i]}")

def rimuovi():
    x = input("inserisci elemento da rimuovere\n")
    lista_spesa.remove(x)

def conta():
    x =  set(lista_spesa)
    for i  in x :
        if lista_spesa.count(i) > 1 :
            print(f"Il numero {i} appare {lista_spesa.count(i)} volte.")
        else :
            print(f"Il numero {i} appare {lista_spesa.count(i)} volta.")

def svuota_lista():
    lista_spesa.clear()


     

while True:
    print(" premi 0 per uscire,\n premi 1 per aggiungerre un elemento,\n premi 2 per visualizzare la lista,\n premi 3 per eliminare un elemento,\n premi 4 per contare gli elementi della lista,\n premi 5 per eliminare un elemento")
    x=int(input(""))
    if x == 0:
        break
    elif x == 1:
        aggiungi()
    elif x == 2:
        visualizza()
    elif x == 3:
        rimuovi()
    elif x == 4:
        conta()
    elif x == 5:
        svuota_lista()