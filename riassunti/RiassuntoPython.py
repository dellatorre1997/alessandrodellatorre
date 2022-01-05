#Guida Python v4
# coding=utf-8
__author__  = 'Alessandro Della Torre'
__version__ = '4.0' #Aggiornato: 09.01.2020
#La guida ufficiale è ricavabile qui: https://docs.python.org/3/contents.html
#-----------------------------------
#Importare i moduli --> import <nomeDelModulo> è possibile importare anche programmi/librerie
import sys
import os
import random

#Main --> Funzione principale dove vengono eseguite le parti principali del nostro codice
def main(argv):

    #Commenti in Python
        #Il carattere '#' commenta l'intera linea, esempio:
        #print('Questo print non verrà eseguito)
        '''
        Tutto il codice presente tra i 3 apici non verrà eseguito
        print('Questo print non verrà eseguito')
        '''
        #COMMENTARE IL CODICE È IMPORTANTISSIMO E VA FATTO SEMPRE

    #Dichiarazione delle variabili/strutture dati
        #I nomi delle variabili non devono contenere numeri e lettere (es: 1997FugaNY --> no)
        #Non dare nomi come le Keyword di Python (es: def, if, for ecc...)
        #Non staccare le parole, piuttosto gobbaDiCammello
        numeroIntero = 1821
        carattere = 'B'
        stringa = "qui giace napoleone"
        vettore = [0,1024,2048]
        vettoreStringhe = ['primo' , 'secondo' , 'terzo']
        matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        lista = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
        dizionario = {'ajejie': 1, 'brazorf': 2, 'ispettore':3, 'carica':101, 'trentini':33 }
        #oggetto =
        #Se vuoi vedere un esempio di come vengono viste queste variabili setta a "true" la variabile 'showMe'
        showMeVar = 'false'
        if showMeVar == 'true':
            showMeVariabili(numeroIntero,carattere,stringa,vettore,matrice,lista,dizionario)

    #casting di una variabile
        stringaDaNumero = str(numeroIntero)
        #print(numeroIntero)
        #print(stringaDaNumero)

    #concatenazione di stringhe
        stringaSupp = 'Non tutto.. ma bonaParte!'
        #print(stringa + stringaSupp)
        stringaConcatenata = stringa + stringaSupp
        #print(stringaConcatenata)

    #Utilizzo confronto --> if
        #if <condiizone> || <condizione> && <condizione> :
        #    <corpoIf>
        #elif <condiizone> :
        #   <corpoElif>
        #else:
        #   <corpoElse>
        #Cambia il valore a 'x' e vedi cosa cambia!
        x = 1
        if x < 0:
            x = 0
            print('Negative changed to zero')
        elif x == 0:
            print('Zero')
        elif x == 1:
            print('Single')
        else:
            print('More')

    #Cicli
        #Precondizonato --> while/for
        #-----for-----
        #ciclo a contatore
        #for <contatore> in <lista/range>:
        #   <istruioniRipetute>
        print('elementi nel vettore <vettoreStrighe>: ')
        for cont in vettoreStringhe:
            print(cont)

        #Utilizzo renge() che mi esegue il ciclo un numero intero (finito) di volte
        print('For con funzione range(10):')
        for cont in range(10):
            print(cont)

        print('For con funzione range(5,10):')
        for cont in range(5,10):
            print(cont)

        #Utilizzo len() che mi restituisce la lunghezza del vettore (ovvero il suo numero di elementi)
        print('For con funzione length --> len()')
        for cont in range(len(vettoreStringhe)):
            print(cont, vettoreStringhe[cont])
        """
        print('Inserisco n elementi in un vettore')
        n = 5
        vettEx = []
        for cont in range(n):
            print('Dammi un elemento! ')
            vettEx.append(input())
        print('Glio elementi che mi hai dato sono:', vettEx)
        """

        #Con 'break' bn locco l'esecuzione del ciclo, con 'continue' vado all'interazione successiva
        print('Utilizzo di break')
        for cont in range(1000000):
            if cont == 5:
                break
            else:
                print(cont)

        print('Utilizzo di pass')
        for cont in range(10):
            if cont < 5:
                pass
            else:
                print(cont)

    #Precondizonato --> while/for
        #-----for-----
        #ciclo a contatore
        #while <condizione>:
        #   <istruioniRipetute>
        print('Esempio di utilizzo del ciclo while')
        fib(2000)

    #Liste
        #è possibile utilizzare le liste come liste, come stack, come pile ecc...ecc....ecc....
        #Le principali funzioni sono:
        lista.append('ciaomondo')
        lista.remove(lista.index('banana'))#rimuove il primo elemento di tipo banana
        lista.index('banana') #Restituisce la posizione del primo elemento con nome 'banana'
        lista.count('apple') #Conta il numero di elementi di tipo 'apple'
        lista.sort() #Ordina gli elementi
        lista.pop() #Restituisce l'ultimo elemento della lista, utile per creare uno stack.
        lista.insert(3,'fruttosio') #Inserisce un elemento(secondo argomento) nella posizione indicata(primo argomento = index)

    #dizionari
        dizionario['numFilippo'] = 3346589899 #Inserimento nuovo elemento
        del dizionario['numFilippo'] #Eliminato il numero di filippo
        list(dizionario.keys()) #Elenco elementi
        sorted(dizionario.keys())
        'ajejie' in dizionario #Restituisce 'true' perchè l'elemento è preseente nel dizionario

    #Ricorsione
        #Esempio di una funzione che richiama se stessa
        for i in range(40):
            print( i, rec_fib(i))

    #Esempio errore di sintassi
        #Se vuoi testare l'errore togli il carattere '#' all'inizio della prossima riga
        #print(<-- Qui manca l'apice e ho un errore di sintassi')

    #Utilizzo modulo os
        #L'utilizzo pi semplice è la funzione cls/clear che ripulisce la console
        clear = lambda: os.system('clear')
        clear()

    #Utilizzo modulo random
        #Genero numero casuale con estremi [1,datoUtente]
        estremo = int(input())
        numcasuale = int(random.uniform(1,estremo))

    #Utilizzo del modulo socket

    #Utilizzo try-exeption
    try:
        thisisexeption = 1/0
        pass
    except Exception as e:
        print(str(e))
        raise
    else:
        print("1/0 Is not an exeption")
        pass
    finally:
        pass



#-----------------------------------
#Creazione di una funzione
# def <nomeFunzione>(parametri):
#   <Corpo della funzoine>
#   return<valoreDiRitorno>
#Solo utilizzo di variabili LOCALI, eliminate alla chiusura della funzione
#Passaggio di parametri soltanto per valore e non per indirizzo
def showMeVariabili(numeroIntero,carattere,stringa,vettore,matrice,lista,dizionario):
    print('------Stampa delle variabili------')
    print('numeroIntero --> ', numeroIntero)
    print('carattere --> ', carattere)
    print('stringa --> ',stringa)
    print('vettore --> ',vettore)
    print('matrice --> ',matrice)
    print('lista --> ',lista)
    print('matrice --> ',matrice)
    #print(lista)
    #print(oggetto)
    print('------Di che tipo sono?------')
    print('numeroIntero --> ',type(numeroIntero))
    print('carattere --> ',type(carattere))
    print('stringa --> ',type(stringa))
    print('vettore --> ',type(vettore))
    print('matrice --> ',type(matrice))
    #type(lista)
    #stype(oggetto)

def fib(n):    # write Fibonacci series up to n
        """Print a Fibonacci series up to n."""
        a, b = 0, 1
        while a < n:
            print(a, end=' ')
            a, b = b, a+b

def rec_fib(n):
    '''inefficient recursive function as defined, returns Fibonacci number'''
    if n > 1:
        return rec_fib(n-1) + rec_fib(n-2)
    return n

def piuArgomenti(stringa1, stringa2, *args):
    result = ""
    result = result + stringa1 + stringa2
    for element in args:
        result = result + element
    print(result)

def ModuloOs():
    os.system("comando <opzione> <parametro1> " + parametro2 )

#-----------------------------------
#Classi in python3
class Esempio:
    listaN = []
    def __init__(self,argomento1,argomento2):
        listaN.append(argomento1)
        listaN.append(argomento2)
    def printLista():
        for element in listaN:
            print(str(element))







































#Esecuzione del Main
if __name__ == "__main__":
    main(sys.argv)
