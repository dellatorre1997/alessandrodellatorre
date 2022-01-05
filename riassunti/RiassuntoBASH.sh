#!/bin/bash
#Programma di riassunto dei comandi bash e stutture degli script bash
#For execute a random cmd, write it in the script, for example:
ls
#Caratteristiche della shell:
  #1 - Redirezione
    #Salva l'output di ls in list.txt
    ls > list.txt
    #Aggiunge il contenuto di ls nel file list.txt
    ls >> list.txt
    #spedisce il contenuto di list.txt a indirizzo@mail.it
    mail indirizzo@mail.it < list.txt
    #Reindirizza stdout e stderr del comando ls al file /dev/null, quindi non vengono visualizzati
    ls file.txt >& /dev/null

  #2 - Pipes
    #Shell permette di utilizzare lo standard output di un processo come stdin di un'altro processo
    ls -al | grep "tuammamma" | sort

  #3 Wildcars
    #Utilizzati per specificare file pattern; La stringa contenente wildcards viene sostituita con l'elenco dei file che
    #soddisfano la condizione.
    #Elenco caratteri speciali:
      # * all string
      # ? qualsiasi carattere singolo (equivalente del  '_' in python)
      # [...] maching di qualsiasi cartatere inserito nelle parentesi
    #esempi:
      ls -al | grep "*.c" "prova00?.c" "prova[0-9][0-9].txt"

  #4 Sobstitution
    #Gli apici rovesciati `` (altgr + apici) vengono autilizzatri per fare command sobstitution
    #Il comando racchiuso tra apiuci viene eseguito, e il suo standard output viene sostituito al posto del comando
    echo "Data odierna: `date`"

  #5 Sequenze (condizionali e non)
    #Sequnze non condizionali
    #Il metacarattere ; viene utliizzato per eseguire due comandi in sequenza
    date ; pwd ; ls
    #sequanze non condizionali
    # ||  (or); &&  (and)

  #6 Raggruppamento di comandi
    #é possibile raggruppare comandi mettendoli dentro le parentesi
    #vengono eseguiti in una subshell
    #condividono gli stessi stdin,stdout e stderr
    #esempio:
      (date ; ls ; pwd) > out.txt

  #7 Esecuzione in background
    #Se un comando è seguito dal metacarattere & :
    #Viene creata una subshell e ilcomando vienen eseguito in background parallelamente alla shell corrente
    #Non prende il controllo della ttastiera, utile per eseguire attività lunghe che non richiedono l'uso della tastiera
    find / -name passwd -print &

  #8 Quoting
    #Esiste la possibilità di disabilitare wildcard / command sobstitution / variable substitution
    #utilizzando l'apice '
    #Mentre le double quotes (apici) inibiscono wildcard e basta
    echo 3 * 4 = 12
    echo '3*4=12'
    echo "my name is $name - date is 'date'"
    echo 'my name is $name - date is `date`'

  #9 Subshell
    #Quando aprite il terminale viene eseguita una shell
    #Viene creata una subshell nel caso di :
      #Comandi raggruppati
      #Eseguito uno script
      #Quando viene eseguito un processo in background
    #Caratteristiche :
      #Hano la propria directory corrente
      #Due distinte aree di variabili vengono gestite differentemente

  #10 Variabili
    #Ogni shell supporta dfue tipo di variabili :
      #Variabili locali: Non ereditate dalla shell alla subshell
      #Variabili ereditate
    #Entrambe le variabili contengtono dati di tipo stringa
    #Ogni shell utilizza dell evariabili d'ambiente inizializzate da file di startup o dalla shell stessa
    #Per visualizzarle chiamare il comando 'env'
    #Accedere al contenuto di una variabile: Utilizzare il metacarattere $ prima del nome
    nome = 'stocazzo'
    echo $nome
    #Per trasformare una variabile locale in una d'ambiente bisogna digitare:
    export nome

    #Per usare una forma minima di tipizzazione delle variabili è possibile utilizzare i costrutti:
      #Declare
      declare -r var #lettura
      declare -i var #intera
      declare -a var #array

    #Let
    #Let esegue operazioni aritmetiche sulle variabili; in molti casi può essere usata al posto di expr

    #Unset
    #Cancella il contenuto di una variabile

  #Alias/Unalias
    #Un alias bash non è altro che una scorciatoia per abbreviare lunghe sequenze di comandi 
    alias dir="ls -l"
    alias rd="rm -r"
    unalias dir
    alias h="history -r 10"


  #Cat
  #Concatenazione, di solito seguito da ridirezione, serve per concatenare i file
  cat file.1 file.2 > file.12

  #Find
  #Analizza ricordivamente i path contenuti in pathlist e applica expression ad ogni file
  #Struttura: find pathlist expression
  #Sintassi expression:
    # -name pattern
    # -perm permission
    # -print --> stampa ilpathname e ritorna true
    # -ls --> tsmpa attribiti del file e ritorna true
    # -user username | -uid userId --> Ritorna true se il possessore del file è uno o l'altro
    # !!!! -atime | -mtime | -ctime -count --> True se il file è stato acceduto modificato o ppure cambiati gli attributi negli ultimi n giorni

  #xargs command
    #Legge una lista di argomenti dallo standard input, delimitati da blank oppure da newline
    #Esegue command passandogtli la suddetta lista di argomenti
    #Esempio, concatena tutti i file in c
      find -name "*.c" -print | xargs cta > prova
    #Utilizza emacs per visualizzare tutti i file nella directory corrente e nelle sottodirectory che hanno estensione java e contengono la parola "Alfa"
    emacs $(find . –name “*.java” | xargs grep –l \ “Alfa”)






















# ------------------------ Scripting -------------------------
#Utilizzo variabili built-in per lo scripting
  # $$ Identificatore di processo della shell
  # $0 Il nome dello script
  # $1-$9 Argomenti della linea di comando
  # ${n} Nesimo argomento della riha di comando
  # * Lista di tutti gli argomenti della linea di comando
  # $# Numero di argtomenti della command line
  # $? Valore di uscita dell'ultimo comando eseguito

#Le espressioni nello scripting vanno effettuate utilizzando il comando expr
  # Tutti i metacaratteri vanno preceduti da backslash '/'
    # • Aritmetici: + -* / %
    # • Confronto: = != > < >= <=
    # • Logici: &, |, !
    # • Parentesi: ( )
    # • Nota: devono essere prefissate dallo backslash
  #esempi:
    x = 1
    x = 'expr $x +1'
    echo $x #Il risultato è 2 ovviamente

#Exit status
  #Quando un processo termina viene ritornato un codice di exit, per convenzione IN UNIX:
  # 0 Secsess
  # nz failure

#IF
if [[ -n "$1" ]]
then
  lines=$1
elif [[ -n "$2" ]]
then
  lines=$2
else
  lines=$3
fi

#CASE IN ESAC
case "$1" in
  "") lines=50
  ;;
  *[!0-9]*) echo "Usage: `basename $0` usersnum";
  exit 1
  ;;
  *) lines=$1
  ;;
esac
du –s /home/* | sort –gr | head -$lines

#WHILE
while list1
do
  list2
done

#UNTIL
#E' una specie di while con precondizione
until list1
do
  list2
done

#FOR
for name [in words]
do
  list
done
  #Esempio:
  for file in $(ls *~)
  do
    echo –n “Sei sicuro di voler rimuovere $file ?”
    read reply
    if [ $reply = “Y” –o $reply = “y” ]; then
      rm –f $file
        echo File $file removed
    fi
  done
