<style>
.link-menu {
    float: left;
    margin-right: 5em;
}
ul{
overflow: hidden;
}
img{
    width: 200;
    height: 200;
}
strong{
  color: #b5e853
}
</style>
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    TeX: {
      equationNumbers: {
        autoNumber: "AMS"
      }
    },
    tex2jax: {
      inlineMath: [ ['$','$'], ['\\(', '\\)'] ],
      displayMath: [ ['$$','$$'] ],
      processEscapes: true,
    }
  });
</script>
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<ul>
  <li class="link-menu">
    <a href="/">Home</a>
  </li>
  <li class="link-menu">
    <a href="/aboutme">AboutMe</a>
  </li>
  <li class="link-menu">
    <a href="/competenze">Competenze</a>
  </li>
  <li class="link-menu">
    <a href="/progetti">Progetti</a>
  </li>
  <li class="link-menu">
    <a href="/contatti">Contatti</a>
  </li>
</ul>

---

# Modellazione e Analisi dei Sistemi
#### Tool
[ASMETA](asmeta.github.io)

# Indice Pratica
0. [**ASM-template**](#asm-template)
1. [**Scenario-template**](#scenario-template)


# Indice Teoria
0. **Introduzione**
   1. Specifiche Linguaggio Naturale
   2. Specifiche Formali
      - Limiti metodi formali
   3. Formalismi
      - _Operazionali_(operazioni)
      - _Dichiarativi_(proprietà)
   4. Analisi
      - _Validazione_
      - _Verifica_
1. **Automi**
   1. FSM
   2. Mealy-Moore _$(s,i,o,s')$_
   3. FSM Estese _$(s,i,o,g,a,s')$_
   4. FSM Comunicazione
      - _$c,p$_ | _$(s,null,s'), (s,c?i,s'), (s,c!o,s')$_
   5. FSM Temporizzate _$(s,g,a|I/O,S',[t_1,t_2])$_
   6. FSM Harel(_uml-SM_)
2. [**ASM-AbstractStateMachine**](#asm) **$(\sum, A, R)$**
   1. _ASM_=(header,body,mainRule,initialization)
   2. Funzioni
      * _FunzioneCaratteristica_
      * _Variabile_($0$-arie)/_Funzione_($n$-arie)
      * Statiche(_arietà=0_)=cost| Statiche(_arietà>0_)=operaz | Dinamiche(_arietà=0_)=var | Derivate(_arietà=0_)
      * Base{_statiche, dinamiche_} | Dinamiche{_in, out, controlled, shared_} | Derivate
      * Locazione: **$loc=(f,(a_1,...,a_n))$**
      8. _Classificazione di Funzioni_
   3. Vocabolario **$\sum$**
   4. Stato
      * **$s=(Dom, F(Dom))$**
      * struttureAlgebriche **$\rightarrow$** Algebre
      * StatiControllo {_Dati, Operazioni, Algebra_}
   5. Domini
      * Superuniverso **$\supseteq$**(funzioneCaratteristica) Universi **$\Rightarrow$** DominiEterogenei
   6. Termini
      * **$(var, c, f(t_1,t_2,...,t_n)) \in Ter$**
   7. Transizioni
      * **$S_1 \rightarrow S_2$**
      * CostrutturiRegole
   8. Aggiornamenti e Locazioni
      - _UpdateSet_
      - Aggiornamento: **$(loc,b)=((f,(a_1,...,a_n)),b)$**
      * AssegnamentoAggiornamento: **$f(v_1,...,v_n):= b$**
   9. Aggiornamenti Consistenti
      * **$((f,(a_1,...,a_n)),b) \in U$** | **$((f,(a_1,...,a_n)),c) \in U$** $\Rightarrow$ **$b=c$**
   10. Regole Transizione ASM
       - regoleTransizione
       - Programma ASM
       - CostruttoriRegole
         1. _Update_ Rule
         2. _Conditional_ Rule
         3. _Skip_ Rule
         4. _Let_  Rule
         5. _Block_ Rule
         6. _Call_ Rule
         7. _Seq_ Rule
         8. _Forall_ Rule
         9. _Choose_ Rule
         10. _Extended_ Rule
   11. Automi Kripke
3. [**Prime Tecniche di Analisi**](#prime-tecniche-analisi)
   *  Analisi di un Modello
   *  Prime forme di Analisi
      1. **`Invarianti`**
         - Uso degli Invarianti
         - Dichiarazione degli Invarianti
      2. **`Validazione tramite Scenari`**
         - Tecniche di validazione
         - Validazione tramite Scenari in ASM
         - ASM Observer
         - Doppio uso degli Scenari
         - Scenario ASM
         - Primitive di Avalla
4. [**ASMETA**](#asmeta)
   1. asmeta
   2. [_ASMETAL_](#asmetal): linguaggio
      * Linguaggio _Strutturale_
      * Linguaggio _Definizioni_
      * Linguaggio _Termini_
      * Linguaggio _Regole_
   3. [_ASMETAS_](#asmetas): simulatore
   4. [_ASMETAVis_](#asmetavis): visualizzatore
5. [**Composizione di Modelli**](#composizione-modelli): _ASM multi-agenti_
   1. ASM Multi-agenti
   2. Agenti ASM
      * CreatiDinamicamente| _$View(a,M) \rightarrow f(self,x)$_
   3. _$Sync/Async$_ ASM **$(a,ASM(a))$**
      * ASM sincrone: computazione
        - _quasi-sequential-run_
      * ASM asincrone: computazione
        - _run-parzialmente-ordinata_
        1. _Storia Finita_
        2. _Sequenzialità agenti_
        3. _Coerenza_
6. [**Metodologia di Specifica**](#metodologia-specifica): _Ground Model & Raffinamento di Modelli_
   * Metodo ASM
     1. **ASMs**
     2. **Ground Model**
        * Definizione
        * Caratteristiche
        * Livello di astrazione opportuno
        * Creazione GM
        * Prove di Correttezza
     3. **Raffinamento di Modelli**
        1. Principio di Sostituzione
        2. Schema per il raffinamento
        3. Prova di correttezza di raffinamento
        4. Minimalità Sequenze
     4. [**Stuttering Refinement**](#shittering-rafinament)
        1. Schema per il raffinamento
        2. Tipi di raffinamento
           - _Orizzontale_
           - _Verticale_
        3. Combinare tipi di Raffinamento
           - _Raffinamento della segnatura_
           - _Raffinamento procedurale_
7. [**Model Checking**](#model-checking)
   * **Logiche Temporali**
   * **CTL - ComputationalTreeLogic**
     - _Semantica Connettivi_
     - _Equivalenze Importanti_
     - _Descrizione Formule CTL_
     - _Possibili esercizi_
       - Verifica formula Ben-formata
       - Verifica Automa di Kripke
       - Dimostrazione Equivalenza formule CTL
     - _Algoritmo Model Checking_
     - _Algoritmo Labelling_
       - Pseudocodice **$SAT$**
       - Funzione **$SAT_{AF}(\phi)$**
       - Funzione **$SAT_{EU}(\phi, \varphi)$**
       - Funzione **$SAT_{EX}(\phi)$**
   * **Strutture Dati Efficienti**
   * [**Verifica Proprietà Temporali**](#verifica-proprietà-temporali)
     1. **`Reachability Property | Proprietà di raggiungibilità`** **$EF \phi$**
        * Raggiungibilità Condizionale **$EU$**
        * Raggiungibilità applicata a stati raggiungibili **$EF(AG) \ AG(EF)$**
          * Grafo ri Raggiungibilità
            - _Algoritmi Forward Chaining_
            - _Algoritmi Backword Chaining_
            - _Esplorazione on-the-fly_
     2. **`Safety Property | Proprietà di Sicurezza`** **$AG \phi$**
        - Safety Condizionale **$AU$**
        - Safety **$\neq$** Rechability **$\neg EF$**
        - Safety senza passato **$AU$**
        - Safety con explicit past **$AG$**
          * _Eliminazione operatori del passato_
          * _History Variables_
     3. **`Liviness Property | Proprietà di Vivacità`** **$AG + AF \ AG + EF$**
     4. **`Assenza di Deadlock`** **$AG(EX true)$**
     5. **`Fairness Property | Proprietà di Equità`** **$nope$**
  * [**NuSMV**](#nusmv)

# Introduzione
#### Metodi Formali
Le specifiche in **linguaggio naturale** sono:
  1. _Inconsistenti_
  2. _Ambigue_
  3. _Difficili da seguire_

Le specifiche **formali**
  1. _Forzano a pensare più a fondo sul significato della specifica scritta_
  2. _Possono essere usate per provare la correttezza del programma_
  3. _Possono essere usate per generare dei dati di test_

**Limiti metodi formali**:
  - Scrivere una specifica formale è come scrivere un programma $\Rightarrow$ Inserimento errori
  - Fare prove di correttezza è un processo lungo e difficile $\Rightarrow$ Errori, correttezza?

#### Formalismi
- **Operazionali**: Forniscono una descrizione del comportamento del sistema in termini di _operazioni_ di una macchina astratta
  - Facilitano la _Validazione_
- **Dichiarativi**: Definiscono il sistema in termini di _proprietà_ che devono essere soddisfatte
  - Facilitano la _Verifica_

#### Analisi
- **Validazione**: Il processo di valutare un _sistema_ o una _componente_ durante o alla fine del processo di sviluppo per determinare se esso _soddisfa i requisiti specificati_
  - Necessaria per controllare che il sistema soddisfa i requisiti richiesti
- **Verifica**: Il processo di valutare un _sistema_ o una _componente_ per determinare se i prodotti _di una data fase di sviluppo_ soddisfano le condizioni(_proprietà_) _imposte allo stato_ di tale fase
  - Necessaria per garantire proprietà

Queste cose verranno approfonditte nella sezione [`Prime techiche di Analisi`](#prime-tecniche-analisi)

<a name="asm"></a>
# Abstract State Machine
### ASM
>Le _ASM_ rappresentano la forma matematica delle _Macchine Virtuali_ che estendono la nozione di _Finite State Machine_

**ASM**=_(header,body,mainRule,initialization)_<br>
Può essere rappresentata come una FSM<br>
Differenze ASM-FSM:
  - _Concezione degli stati_
    - Nelle FSM esiste un solo stato di controllo, nelle ASM può essere piu complesso perchè è espresso in termini di algebra
  - _Condizioni di input e le azioni di output_
    - Nelle FSM alfabeto finito, nelle ASM qualsiasi input che sia una espressione o azioni generiche

**ASMETAL**: _Linguaggio per la creazione di modelli_<br>
  - Le ASM hanno una notazione matematica in termini di algebra
  - AsmetaL come notazione concreta per l'editing di modelli ASM

<a name="funzioni"></a>
### Funzioni
> Le funzioni vengono espresse in forma di dominio e codominio all'interno del contesto della logica, non devono essere pensate come funzioni e metodi dell'informatica

_Ci sono diversi tipi di funzione che vengono menzionate all'interno del testo, la prima da sapere è la funzione carattreristica perchè ci servirà per capire il concetto di stato._

<a name="funzione-caratteristica"></a>
**Funzione caratteristica**: Una funzione caratteristica per un sottoinsieme _$S$_ di un insieme _$X$_, _$(S ⊆ X)$_, è la funzione _$ƒ_S: X → {0, 1}$_ tale che, per ogni _$x ∈ X$_, il suo valore è _$1$_ se _$x$_ appartiene a _$S$_, è _$0$_ altrimenti

_Poi bisogna fare distinzioni tra le funzioni che non hanno argomenti e quelle che hanno più di un argomento, queste sono:_
  - **Variabili**(_0-arie_): Quindi funzioni che non hanno nessun argomento(le chiamiamo variabili per far campire la distinzione con le funzioni a più argomenti, in realtà queste verranno specificate meglio dopo)
  - **Funzioni**(_n-arie_): Funzioni con _$0-n$_ argomenti

_La principale distinzione viene fatta guardando se il valore di queste funzioni cambia da uno stato all'altro(contando anche i loro argomenti), per questo le dividiamo in:_
  - **statiche**(_arietà=0_):
    - Funzioni statiche di arietà 0 sono dette **costanti**
    - Se il valore dell'interpretazione della funzione non cambia da uno stato all'altro
  - **statiche**(_arietà>0_):
    - Vengono definite tramite una legge fissa; un loro esempio sono le operazioni **$+,-,or,not$**...
    - La loro legge non cambia da stato a stato, la loro semantica o funzione non cambia(un + è una funzione che fa la somma sia in uno stato sia nell'altro) MA hanno una arietà maggiore di zero perchè gli passo degli argomenti(come i 2 numeri per fare la somma)
  - **dinamiche**(_arietà=0_): Se il valore dell'interpretazione della funzione cambia da uno stato all'altro(in programmazione sono le **variabili**)

**Classificazione di Funzioni**<br>
Sia _$M$_ una ASM e _$env$_ l'ambiente di _$M$_
  * **Base**: Contenute all'interno del vocabolario
    - **Statiche**: Valore/Significato non cambia tra le diverse algebre
    - **Dinamiche**: La cui interpretazione può cambiare da algebra a algebra(quindi da stato a stato); I valori dipendono dagli stati di _$M$_
      - **in**(monitored): Lette(non aggiornate) da _$M$_, scritte da _$env$_
      - **out**: scritte(ma non lette) da _$M$_, lette da env
      - **controlled**: Lette e scritte da _$M$_
      - **shared**: Lette e scrittte da _$M$_ e da _$env$_
  * **Derived**: Valori computati da funzioni monitorate e funzioni statiche per mezzo di una "legge" o "schema" fissata a priori

Le funzioni vengono salvate in memoria in delle locazioni.<br>
**Locazione**: _$(f,(v_1,...,v_n))$_ con
  * _$f$_ nome di funzione
  * _$(v_1,...,v_n)$_ i suoi argomenti

In uno stato _$S$_, una _locazione_ ha un _valore_: interpretazione della funzione nello stato.<br>
Questi verranno spiegati e contestualizzati meglio dopo quando si avrà già affrontato il concetto di stato e di transizione di stato [**QUI**](#aggiornamenti-locazioni)

<a name="vocabolario"></a>
### Vocabolario
>Un vocabolario _$\sum$_ è una collezione finita di nomi di funzioni<br>

_In pratica il vocabolario contiene al suo interno solo i nomi delle funzioni(come se fosse un insieme di simboli), queste funzioni non hanno ancora una interpretazione(quindi non hanno ancora un significato)_<br>

**Definizione vocabolario**:
  1. Definizione insieme di simboli
  2. Scegliere dominio, detto superuniverso, per dare significato ai simboli
  3. Automaticamente abbiamo algebra ASM

**RIASSUMENDO**: Abbiamo le funzioni matematiche che sono divise in base al numero di loro argomenti e se cambiano da uno stato all'altro, queste funzioni stanno in un vocabolario senza una semantica o interpretazione.

<a name="stato"></a>
### Stato
_Ci sono diverse definizioni di uno stato a seconda di come questo viene visto, le prime vengono date nelle slide iniziali e servono per contestualizzarlo e per far capire di cosa si sta parlando mentre dopo viene data la definizione formale(ma notare che sono tutte corrette)_<br>

>Lo stato è rappresentato in termini di _domini reali_ e da un _insieme di funzioni_ su questi domini che, insieme, rappresentano lo _stato_.

>Gli stati di una ASM sono delle _strutture algebriche_, dette _algebre_
  * Le _algebre_ sono un insieme di simboli di funzione con una loro interpretazione

> Gli stati sono delle funzioni definite su dei domini con una loro interpretazione(quindi un loro Valore)

_Fin qui abbiamo detto la stessa cosa in 3 modi diversi, adesso viene data la definizione formale prendendo in causa anche il vocabolario:_<br>

**Definizione formale di stato in una ASM**<br>
>Fissato un vocabolario _$\sum$_, uno **stato** _$A$_ del vocabolario $\sum$ è un insieme non vuoto _$X$_, detto _superuniverso di A_, con le interpretazioni dei nomi delle funzioni di $\sum$
  * Se _$f$_ è un nome di funzione n-aria di $\sum$, allora la sua _interpretazione $f^A$_ è una funzione _$f^A: X^n \rightarrow X$_
  * Se _$c$_ è in nome di costante di $\sum$, allora la sua interpretazione _$c^A$_ è un elemento di _$X$_

**Stati di controllo**, non strutturati, sostituiti da **stati strutturati** che modellano:
  - **Dati**: Dati complessi arbitrari(con domini di base e funzioni per la struttura)
  - **Operazioni**: Operazioni per la manipolazione dei dati
  - **Algebra**: Insiemi su cui vengono definite _operazioni_ che hanno significato su questi _domini_, possono essere definite delle _variabili_, delle interpretazioni delle funzioni sulle variabili che hanno senso nei loro domini

Nelle _ASM_ gli stati sono associati a un insieme di valori di qualsiasi tipo, memorizzate in apposite locazioni
  * Ogni stato ha associato un numero di _locazioni_.

<a name="domini"></a>
### Domini ASM
>Il Superuniverso è un _'Dominio'_ in cui tutto prende significato; il superuniverso di uno stato ASM è 'suddiviso' in _universi_, rappresentati dalle loro funzioni caratteristiche<br>

_Nella teoria dell'algebra il dominio non c'è ma esiste solo la [funzione caratteristica](#funzione-caratteristica) dei valori nei diversi universi_<br>
In linea più generale, ogni universo rappresenta un dominio.<br>
Se _$X$_ è il superuniverso dello stato _$A$_, l'universo _$G$_ di _$A$_ è rappresentato dalla funzione _$G:X \rightarrow Bool$_ tale che:
  * _$G(t)=true$_ per tutti gli elementi _$t$_ del superuniverso _$X$_ di _$A$_ che formano la partizione _$G$_
  * _$G(t)=false$_ altrimenti

In pratica abbiamo questa funzione _$G$_ che ci permette di specificare cosa _vale_(quindi lo definiamo _true_) all'interno di un _universo_(dominio). <br>
In base a questa rappresentazione degli insiemi in termini di funzioni caratteristiche, uno stato di una ASM consente di modellare **domini eterogenei**

**RIASSUMENDO**: Abbiamo le _funzioni_ all'interno di un _vocabolario_, a queste viene data una interpretazione dando un valore alla _locazione_ della funzione all'interno dello _stato_, il valore che gli assegnamo sta inizialmente in un _superuniverso_(ovvero il dominio dei domini dove tutto prende significato) e grazie ad una _funzione caratteristica_ diciamo quali valori stanno all'interno dei vari _universi_(chiamati informalmente domini).

<a name="termini"></a>
### Termini ASM
I termini di $\sum$ sono espressioni sintattiche definite per costruzione dalle seguenti regole:
  1. Variabili _$v_0, v_1,...,v_n$_ sono termini
  2. Costanti _$c$_ in _$\sum$_ sono termini
  3. Se _$f$_ è nome di funzione n-aria di $\sum$ e _$t_1,t_2,...,t_n$_ sono termini, allora _$f(t_1,t_2,...,t_n)$_ è un termine

_Un termine che non contiene variabili è detto **chiuso**_<br>

Questi non hanno significato se non vegono interpretati attraverso l'algebra.<br>
**I termini sono oggetti sintattici, assumono significato(semantica) nello stato.** <br>
Il valore dei termini è l'interpretazione del termine in _$A$_(algebra), quindi termini diversi hanno significato diverso in base, ad esempio, se vengono interpretati nell'algebra di boole o nell'algebra dei reali.<br>

<a name="transizioni"></a>
### Transizioni
>Sono _regole_ che descrivono il cambiamento di funzioni da uno stato al successivo

Vengono create tramite _costruttori di regole_.<br>
**Aggiornamenti**: Le transizioni di stato delle FSM corrispondono alle transazioni di stato delle ASM con _aggiornamenti_ dei valori contenuti nelle locazioni
  * Se _$loc$_ è _$(f,(v_1,...,v_n))$_ con valore _$a$_, l'assegnamento ha forma: _$f(v_1,...,v_n):=newVal$_

Allo stato sostituiremo un'algebra e al posto di freccie sostituiremo dei costruttori di regola finiti.

<a name="aggiornamenti-locazioni"></a>
### Aggiornamenti e Locazioni
Data la funzione _$f(a_1,...,a_n)$_ in uno stato _$S$_ della macchina:
  * La coppia _$loc=(f,(a_1,...,a_n))$_ è detta locazione e rappresenta matematicamente il valore di una funzione _$f(a_1,...,a_n)$_ in memoria dove:
    - _$f$_ nome di funzione
    - _$(v_1,...,v_n)$_ i suoi argomenti
  * Un aggiornamento(o update) è la coppia _$(loc,b)=((f,(a_1,...,a_n)),b)$_
    - L'interpretazione della funzione _$f$_ in _$S$_ viene modificata per gli argomenti _$a_1,...,a_n$_ con il valore _$b$_
  * Un _update set_ è un insieme di aggiornamenti
  * In uno stato _$S$_, una _locazione_ ha un _valore_: interpretazione della funzione nello stato.

### Aggiornamenti Consistenti
Un _update set_ _$U$_ è consistente, se vale la condizione:<br>
se _$((f,(a_1,...,a_n)),b) \in U$_ ed _$((f,(a_1,...,a_n)),c) \in U$_ allora _$b=c$_
  * Se l'update set _$U$_ è consistente, allora i suoi aggiornamenti possono essere effettivamente eseguiti
  * Il risultato è un nuovo stato(di arrivo) dove le interpretazioni dei nomi delle funzioni dinamiche sono cambiati secondo _$U$_
  * Le interpretazioni dei nomi delle funzioni statiche sono le stesse dello stato precedente(di partenza)
  * Le interpretazioni dei nomi delle funzioni monitorate sono date dall'ambiente esterno e possono dunque cambaire in maniera arbitraria

<a name="regole-transizione"></a>
#### Regole Transizione ASM
> Aggiornare gli stati astratti(_abstract state_) significa cambiare l'interpretazione delle(o solo alcune) funzioni della segnatura della macchina

**Regole di transizione**: Il modo in cui una macchina ASM aggiorna il proprio stato è descritto dalle regole di transizione(_transition rules_) di una certa macchina<br>
**Programma ASM**: L'insieme delle regole di transizione di una ASM definiscono la sintassi di un programma ASM<br>
**Costrutturi di regole**: Sia _$\sum$_ un vocabolario, le regole di transizione di una ASM sono espressioni sintattiche su _$\sum$_ generate come segue attraverso l'uso di costruttori di regole<br>
  1. **Update Rule**: _$f(t_1,...,t_n) := s$_ dove:
     - _$f$_ nome di funzione dinamica n-aria di _$\sum$_
     - _$t_1,...,t_n$_ e _$s$_ sono termini di _$\sum$_
     - Nello stato successivo, il valore di _$f$_ per gli argomenti _$t_1,...,t_n$_ è aggiornato ad _$s$_. Se _$f$_ è 0-aria, cioè una variabile, l'aggiornamento ha forma **$x:=s$**
     - Il ":" ha il significato di _aggiornamento_, quindi è importante ricordarselo e distinguerlo dal semplice assegnamento "="
  2. **Conditional Rule**: **if** _$\varphi$_ **then** _$R$_ **else** _$S$_
     - Se _$\varphi$_ è vera, allora esegui _$R$_, altrimenti esegui _$S$_
  3. **Skip Rule**: _skip_
     - Non fare niente
  4. **Let Rule**: **let** _$x=t$_ **in** _$R$_
     - Se R ha parametri, realizza il passaggio di valore
     - Assegna il valore di _$t$_ a _$x$_ ed esegui _$R$_
  5. **Block Rule**(composizione parallela): <br>
     * _$par$_
       - _$R$_
       - _$S$_
     * _$endpar$_
     - _$R$_ e _$S$_ sono eseguite in parallelo
  6. **Call Rule**(Macro): _$r[t_1,...,t_n]$_
     - Chiama _$r$_(regola con parametri) con argomenti _$t_1,...,t_n$_
     - Una definizione di regola per un nome di regola _$r$_ di arietà _$n$_ è un'espressione<br>
       _$r(x_1,...,x_n)=R$_<br>
       Dove _$R$_ regola di transizione
  7. **Seq Rule**(composizione sequenziale):
     * _$seq$_
       - _$R$_
       - _$S$_
     * _$endseq$_
     - _$R$_ e _$S$_ sono eseguite in sequenza(gli update causati in _$R$_ sono già visibili in _$S$_; lo stato tra _$R$_ e _$S$_ non è mai visibile)
  8. **Forall Rule**: **forall** _$x$_ **with** _$\varphi$_ **do** _$R$_
     - Esegui _$R$_ in parallelo per ogni _$x$_ che soddisfa _$\varphi$_
     - **`!!!!!!Implementa il concetto di parallelismo sincrono(bounded)!!!!!!`**
  9. **Choose Rule**: **choose** _$x$_ **with** _$\varphi$_ **do** _$R$_
     - Esegui _$R$_ in parallelo per un _$x$_ che soddisfa _$\varphi$_
     - **`!!!!!Implementa il concetto di non-determinismo!!!!!!`**
  10. **Extended Rule**: **import** _$x$_ **do** _$R$_
      - Per estendere un sub-universo dal superuniverso con nuovi elementi
      - Scegli un elemento _$x$_ da Reserve, cancellalo da Reserve, aggiungi _$x$_ al superuniverso e esegui _$R$_

![costrutturiRegole](./Immagini/costrutturiRegole.png)

**RIASSUMENDO**:<br>
![riassuntoASM](./Immagini/riassuntoASM.png)

<a name="automi-kripke"></a>
### Automi Kripke
Un'interpretazione di $CTL$ è una struttura di Kripke $M$ con relazione di serialità definita mediante la quadrupla:

$$M=(S, \Delta, I, L)$$

Dove:
  - **$S$**: Insieme degli stati
  - **$\Delta$**(o **$\rightarrow$**): Funzione di transizione t.c. **$\forall s \in S \exists s' \in S$** con **$s \rightarrow s'$**
  - **$I$**: Insieme degli stati detti iniziali
  - **$L$**: Funzione di etichettatura t.c. **$L: S \rightarrow 2^{PA}$**

Rappresentazione automa Kripke **$\Rightarrow$** GrafiDiretti:
  * **Stati**: Cerchi rappresentanti dei nodi(ovvero gli stati) con al loro interno gli atomi proposizionali(o lettere proposizionali come le chiama lei) che sono vere in quello stato
  * **Transizioni**: Archi orientati tra i nodi del grafo

Questo verrà affrontato meglio durante la sezione riguardante il [Model Checking](#model-checking)

---
<a name="prime-tecniche-analisi"></a>
# Prime Tecniche di Analisi
### Analisi di un Modello
Ci sono due approcci:
  1. **Validazione**: Necessaria per controllare che il sistema soddisfi i requisiti richiesti
  2. **Verifica**: Necessaria per garantire _proprietà_(safety, leaveness, assenza di deadlock, reachability...)

La Validazione è meno _human-intensive_ della verifica<br>
La Validazione dovrebbe _precedere_ la verifica
  - Individuare errori il prima possibile
  - Evita di provare prorpietà corrette su specifiche incorrette

### Prime forme di Analisi
Sono possibili due prime forme di analisi sul ground model
  1. _Garanzia degli invarianti_
  2. _Validazione tramite scenari_

### _Invarianti_:
#### Uso degli Invarianti
In un modello ASM gli invarianti sono usati per esprimere _vincoli_ su funzioni e/o regole che devono essere garantite _in ogni stato_<br>
In programmi AsmetaL usare gli invarianti è utile per scoprire _errori di modellazione_
  - In generale, l'assenza di violazione di invarianti _non_ può essere considerata una prova della correttezza del modello
  - Mentre la violazione degli assiomi _è prova_ della incorrettezza del modello

#### Dichiarazione degli invarianti
Gli _invarianti_ vanno dichiarati subito prima della `main rule`<br>
Ogni invariante è dichiarato mediante la keyword `invariat` che precede il nome attribuito all'assioma<br>
Le funzioni e regole su cui è espresso il vincolo vanno listate dopo la keyword `over`<br>
Un esempio di invariante è il seguente: <br>
> _$invariant$ $over$_ id_function,...,id_rule: _$term$_

### _Validazione tramite Scenari_
#### Tecniche di validazione
  - **Tecniche**: Generazione di scenari, sviluppo di prototipi, animazione, simulazione, testing
  - **Scenario**: Descrizione di un possibile comportamento del sistema
    - Itegrazione osservabile tra il sistema ed il suo ambiente in specifiche sitiazioni

#### Validazione tramite Scenari in ASM
Scenari costruiti attraverso una nozione testuale(linguaggio _Avalla_)<br>
Semantica chiara(definita in _termini_ di ASM)<br>
Capacità di descrivere anche dettagli interni
  - Non solo blackbox come pe _UML use cases_ ma anche informazioni sullo stato

Per validare i modelli ASM scritti in _AsmetaL_
  - Integrato nell'_ASMETA framework_

#### ASM Observer
  1. _Checks_ stato interno della macchina e gli invarianti
  2. Richiede _execution_ di regola arbitrarie
  3. Gray box view

#### Doppio uso degli scenari
Due tipi di attori esterni:
  - **User**: Ha una _black-box-view_ del sistema
  - **Observer**: Ha una _grey-box-view_ del sistema

Gli scenari hanno _$2$_ obbiettivi:
  - **Validazione classica**: Azione dell'utente e reazioni della macchina
  - **Attività di testing**: Ispezione dell'observer dello stato interno della macchina

#### Scenario ASM
Sequenza di iterazione consistente delle azioni:
  - Da parte di **user/observer**
    1. _set_ the enviroment; **NON** è possibile utilizzare questo statement per sistemi _chiusi_
    2. _check_ for the machine outputs
    3. _check_ the machine state and invariants
    4. _ask_ for the execution of given transition rules
  - Da parte della **macchina**:
    1. _makes_ one step as reaction of the actor actions

Lo scenario è scritto nel linguaggio Avalla

#### Primitive di Avalla:
  1. _Set_
  2. _Check_
  3. _Step_
  4. _StepUntil_
  5. _Invariant_
  6. _Exec_

---

<a name="asmeta"></a>
# **ASMETA**

![ASMETA-basedDesignProcess](./Immagini/ASMETA-basedDesignProcess1.png)
![ASMETA-basedDesignProcess](./Immagini/ASMETA-basedDesignProcess.png)

Un modello ASM può essere letto come pseudocodice su strutture dati astratte<br>
>ASM=(name, header, body, main_rule, initialization)

Sintassi astratta => metamodello<br>

![ASMETA-architecture](./Immagini/ASMETA_toolset.png)
Il toolset ASMETA è stato sviluppato partendo dalla definizione di AsmM, unmetamodello per le ASMs. AsmM è stato definito utilizzando L'eclipse Modeling Framework. <br>
**AsmetaToolset**:
  - **Generated**: Tool ottenuti in modo (semi-)automatico applicando le trasformazioni MOF verso gli spazi Javaware, XMLware e grammarware
    1. GraphicalEditor
    2. [_AsmetaL_](#asmetal): Sintassi concreta che permette di scrivere modelli ASMs in formato testuale
       - _AsmetaLc_(asmetaLCompiler): Compilatore text-to-model che permette di effettuare il parsing di modelli AsmetaL e controllare che rispettino i vincoli imposti da AsmM(espressi come vincoli OCL); permette, inoltre, di processare specifiche AsmetaL e controllare la consistenza rispetto ai vincoli OCL del metamodello.<br>
       Permette anche di generare la rappresentazione XMI corrispondente
       - _ATGT_: Tool per la generazione di casi di test basato sul model chacker SPIN
    3. OCL Checker
    4. AsmM JMI
    5. AsmM XMI
  - **Based**: Tool sviluppati nativamente nell'ambiente ASMETA
    1. [AsmetaV](#asmetav)
       - _Avalla_: Linguaggio per la scrittura di scenari, interpretati ed eseguiti da AsmetaV
    2. _AsmetaSMV_: Model Checker basato su NuSMV di modelli asmetaL
    3. _ASMEE_: Front-end grafico per la scrittura di modelli di AsmetaL
    4. [_AsmetaS_](#asmetas): Simulatore per eseguire modelli ASMs
    5. StandardLibrary
  - **Integrated**: Tool esterni collegati all'ambiente ASMETA
    1. AsmM to SAL
    2. AsmM to CoreAsm
    3. ATGT


<a name="asmetal"></a>
#### AsmetaL: _Linguaggio_
Lista dei linguaggi:
  - **Linguaggio Strutturale**
    - **Nome**: asm ASM_name
    - **Modulo**: Un modulo ASM  è come una ASM senza main rule e senza inizializzazione. Nel definire un modulo ASM si usa la parola chiave _module_ anzichè _asm_
    - **Header**: Contiene le _importazioni_(quindi solo standard library) e le _signature_
    - **Signature**: Contiene _dichiarazioni_ di domini e funzioni e non _definizioni_
    - **Body**: Contiene le _definizioni_ con al suo interno(appunto) la definizione dei domini, delle regole(rule) e delle funzioni statiche e derivate e degli inviarianti, in particolare:
      - Solo _domini concreti statici_ possono essere definiti
      - Solo _funzioni statiche_ e _derivate_ possono essere definite
      - MA ATTENZIONE che, per una regola, richiarazione e definizione sono la stessa cosa
    - **Main Rule**: La main rule è sempre una (macro-)regola _chiusa_, cioè senza parametri
    - **Initialization**: Sequenza di stati iniziali tali che:
      - Uno stato iniziale deve essere denotato come _default_
      - Solo _domini concreti dinamici_ possono essere inizializzati
      - Solo _funzioni dinamiche_, non monitorate, possono essere inizializzate
  - **Linguaggio Definizioni**
    - Funzioni
    - Domini: La caratterizzazione dei domini li divide in:
      - **`type-domain`**: Caratterizzano il superuniverso e possono essere basic
         _basic type-domain_: Domini degli altri linguaggi di programmazione definiti nella StandardLibrary+Natural+Undef(=null)
       - _structured_: Utilizzati per definire insiemi finiti, sequenze, bag...
       - _enum_: Enumerazioni
       - _abstract_: Elementi di natura "astratta", non definiti se non attraverso funzioni definite su tale dominio (Agent e Reserve definiti nella standard library!)
      - **`concrete domain`**: Definiti dall'utente e sottoinsieme dei type-domain
    - Regole
    - Invarianti
  - **Linguaggio Termini**
    - Termini di base: Come nella logica del primo ordine(costati, variabili, termini funzionali $f(t_1,t_2,...,t_n)$)
    - Termini speciali: Come tuple, collezioni(quelli che prima vengono definiti come STRUCTURED CRISTO ovvero insiemi, sequenze, bag, mappe...),etc..
  - **Linguaggio Regole**
    - Regole di base: Come skip, update, parallel, block...
    - Turbo regole: Non le faremo

<a name="asmetas"></a>
#### AsmetaS: Caratteristiche
  - **Axiom Checker**: Se un assioma viene violato, AsmetaS lancia eccezione InvalidAxiomExeption
  - **Consistent Update Checking**: In caso di update inconsistenti, AsmetaS lancia l'eccezione UpdateClashExeption che tiene traccia della coppia di locazioni oggetto dell'incostistenza
  - **Random Simulation**: Per mezzo di un ambiente random per le funzioni monitorate

<a name="asmetavis"></a>
#### AsmetaVis: Caratteristiche
Visualizza un modello in termini di una foresta navigabile di _tree structures_<br>
Applica dei:
  * **Structural Patterns**: Utile per visualizzare la struttura del modello in modo compatto
  * **Semantic Patterns**: Utile quando altre informazioni sul workflow della ASM possono essere inferiti dal modello

---

<a name="composizione-modelli"></a>
# Composizione di modelli: _ASM multi-agenti_
Grazie alle regole per la strutturazione, è possibile definire un sistema distribuito come una composizione di ASM dove:
  - Ogni componente del sistema distribuito viene modellato mediante una opportuna ASM
  - Risulta un sistema di _ASM Distribuite_, dette anche _ASM multi-agenti_

Esse descrivono un _modello distribuito_ della computazione, modellata mediante un insieme di _Agenti_ che operano in modo concorrente
  - _Movimenti concorrenti_ sincroni/asincroni
  - _Stati globali_ condivisi tra _Agenti_

#### Agenti ASM
_$(StatiGlobali) \leftarrow [Condivisi | Visione parziale] \rightarrow (Agenti)-[eseguono] \rightarrow (Programma)$_
  1. Possono essere creati _dinamicamente_
  2. Hanno una visione parziale dello stato globale
     - _$View(a,M)$_: Indica la vista dell'agente _$a$_ sullo stato globale di una ASM _$M$_
     - Ogni Agente può avviare una _visione privata_, non condivisa con altri agenti
     - Dati i due stati globali _$A,B$_ e data una funzione globale _$f:A \rightarrow B$_, la dichiarazione di _$f$_ diventa _$f: Agent \space X \space A \rightarrow B$_
     - _$f(self,x)$_ denota la versione privata di _$f(x)$_ dell'agente corrente _self_, in questo caso voglio dire che posso definire delle funzioni il cui primo parametro è chi può vedere la funzione(in questo caso _$self$_) e, come secondo parametro, il parametro vero e proprio della funzione(in questo caso _$x$_)
     - _self_ viene interpretata da _$a$_(agente) come se stesso
  3. Hanno il proprio _programma_ da eseguire
    - Ognuno dotato di un proprio programma(regole ASM)
  4. Gli stati globali sono _condivisi_ tra gli Agenti


Sono classificati in:
  - **Sincrone**: Gli agenti eseguono il loro programma in parallelo, sincronizzati su un implicito _clock globale_ del sistema
  - **Asincrone**: Gli agenti eseguono il loro programma in parallelo, ma in modo indipendente tra loro
    - Ciascuna ha il _proprio clock_ che regola la durata su una mosssa
    - Ciascuno opera nel proprio _stato locale_

**Definizione**:
> Una _sync/async ASM_ è un insieme di coppie **$(a, ASM(a))$** di _agenti_ $a \in Agent$(dominio agenti) e _programmi_ $ASM(a)$ che sono ASM di base

#### ASM _sincrone_: Computazione
Tutte le ASM lavorano in parallelo
  - L'insieme delle ASM opera negli _stati globali_, ottenuti dall'unione di tutti gli stati che compongono le ASM
  - La sequenza di eventi che determina un'esecuzione è la sequenza degli stati che rappresentano l'esecuzione della _sync_ASM_(ergo, l'esecuzione è determinata dalla sequenza degli stati che rappresentano la _sync_ASM_)

Una _multi-agent ASM_ con agenti sincroni ha una _quasi-sequential run_
  - Una sequenza di **stati** _$S_0,S_1,...,S_n$_ dove ciascuno stato _$S_i$_ (con _$i \in 1,2,...,n$_)è ottenuto dal precedente _$S_{i-1}$_ eseguendo in parallelo le regole di tutti gli agenti

#### ASM _asincrone_: Computazione
Nelle _async_ASM_ gli agenti possono essere eseguiti con clock differenti con step di durate diverse tra loro
  - Non esiste il concetto di _controllo globale_ del sistema
  - Difficoltà di gestione della _consistenza_

Una _multi-agent ASM_ con agenti asincroni ha una _run parzialmente ordinata_, ossia un insieme parzialmente ordinato _$(M,<)$_ di mosse _$m$_ dei suoi agenti che soddisfano le condizioni:
  1. **Storia finita**: Dato un insieme di stati _$S$_ sulla _ASM $A$_, essa ha una storia finita se partendo dallo stato _$S_0$_ arriva ad uno stato _$S_t$_(con _$t$_ istante di tempo finito) attraverso un _numero finito_ di _"mosse"_ o _"iterazioni"_, dove anche ciascuna _mossa_ ha un numero finito di predecessori
  2. **Sequenzialità degli agenti**: Ogni agente opera in modo sequenziale(l'insieme delle mosse di ogni agente è linearmente ordinato)
     - Dato un insieme di mosse _$M$_ parzialmente ordinato _$(M,<)$_, con _$A$_ insieme degli agenti, l'insieme delle mosse t.c. _$a$_ esegue _$m$_ (con _$a \in Agent, m \in M$_) è linearmente ordinato per _$<$_
     - **Prof**: L'insieme di mosse _${m|m \in M, a \space exec \space m}$_ di ogni agent _$a \in Agent$_ è linearmente ordinato per _$<$_
  3. **Coerenza**
     - Sia _$X$_ un segmento iniziale finito(sottoinsimee chiuso a sx) di _$(M,<)$_
     - Sia _$\phi(X)$_ lo stato associato ad _$X$_ t.c. _$\phi(X)$_ è il risultato di tutte le mosse _$m$_ in _$X$_
     - Per ogni segmento iniziale finito _$X \in (M,<)$_ esso ha uno stato associato _$\phi(X)$_, nient'altro che il risultato dell'applicazione della mossa _$m$_ nello stato _$\phi(X-\{m\})$_, per ogni elemento massimale _$m \in X$_

---

<a name="metodologia-specifica"></a>
# Metodologia di Specifica: _Ground Model & Raffinamento di Modelli_
Definire un _framework concettuale_ semplice e preciso per supportare e integrare
  - le principali attività di sviluppo sw
  - le principali tecniche di modellazione e analisi

Occorrono:
  - Un metodo di specifica
  - Un processo di sviluppo

#### Metodo ASM
Il metodo basato sulle ASM permette la specifica:
  - rigorosa e formale
  - di sistemi sw ad elaborazione:
    - _sequenziale_
    - _parallela_
    - _non deterministica_
    - _distribuita_

Il metodo si basa su 3 concetti:
  1. _ASMs_
  2. _Ground Model_
     - Primo modello corretto ma non necessariamente completo di requisiti
  3. _Raffinamento di Modelli_
     - Metodo di progettazione che permette di formalizzare i requisiti tramite _sviluppo incrementale_ della progettazione:
       - _Raffinamento Orizzontale_: Sviluppo per composizione
       - _Raffinamento Verticale_: Dal ground-model modelli sempre più dettagliati fino al livello di codice

![processoDiSviluppo](./Immagini/processoDiSviluppo.png)

#### Metodologia di Sviluppo
Supporta tutte le attività di progettazione dai requisiti del codice:
  - _Specifica dei requisiti_: Costruzione del Ground Model(GM)
  - _Architettura_ e progetto delle componenti
  - _Validazione_ dei modelli, mediante simulazione
  - _Verifica_ delle proprietà del modello
  - _Documentazione_

## **Ground Model**
> GM è il contratto tra cliente e sviluppatore

Descrive i requisiti del sistema in modo: _evolutivo, consistente e non ambiguo, semplice e conciso, astratto anche se non completo_(rispetto ai requisiti)<br>
Il GM deve risultare comprensibile e verificabile sia per gli specialisti del _dominio applicativo_ che del _dominio tecnologico_<br>
  - Le ASMs permettono di calibrare il livello di complessità
  - Deve essere verificabile la correttezza e la consistenza del modello rispetto ai requisiti

#### Caratteristiche
Permette di rendere noto all'inizio dello sviluppo ciò che il sistema deve fare in forma di _definizione matematica_<br>
Tutti gli _elementi del GM_(predicati, funzioni, trasformazioni) corrispondono a _entità del mondo reale_(proprietà, relazioni, processi)<br>
Il GM deve essere _preciso_ rispetto al livello di astrazione prescelto e _flessibile_, in modo da poter essere facilmente modificato ed esteso
  * Riusabilità
  * Adattabile a diversi domini applicativi

Deve essere _semplice_ e _conciso_ per soddisfare la comprensibilità sia da parte dei progettisti che dei conoscitori del dominio applicativo<br>
Deve essere sufficientemente _astratto_ ma:
  - _Corretto_ rispetto ai requisiti
  - _Completo_ in base al livello di dettaglio desiderato

Deve essere _validabile_.

#### Livello di astrazione opportuno
>La _scelta del livello di astrazione_ è il problema principale della definizione del GM.<br>

Il metodo ASM affronta il problema riducendolo a un problema di scelta del _linguaggio opportuno_ per la comunicazione tra dominio applicativo e tecnologico

#### Creazione GM
Domande da porsi:
  1. _Quali sono gli agenti del sistema e quali relazioni intercorrono tra essi?_
     - In particolare, quale relazione sussiste tra il sistema e il suo ambiente?
  2. _Quali sono gli stati del sistema?_
     - Quali sono i domini degli oggetti e quali sono le funzioni, predicati e relazioni definiti su di essi?
     - Quali sono le parti statiche e quali quelle dinamiche degil stati?
  3. _Quali sono gli stati del sistema coinvolti dalle transazioni?_
     - Sotto quali condizioni per gli agenti si verificano le transizioni?
     - Quali effetti sugli agenti hanno le transazioni?
     - Che cosa si suppone accada quando le condizioni non sono soddisfatte?
     - Quali forme di uso erroneo devono essere previste e quali meccanismi di gfestione delle eccezioni devono essere implementati?
     - Quali sono le caratteristiche di robustezza desiderate?
     - Come sono collegate le azioni interne agli agenti alle azioni esterne?
  4. _Chi analizza il sistema e in cosa consiste l'inizializzazione?_
     - Che relazione esiste tra l'inizializzazione e l'imput?
  5. _Esistono condizioni di terminazione?_
     - Se si, come sono determinate?
     - Che relazione esiste tra terminazione e output?
  6. _La descrizione del sistema è completa e consistente?_
  7. _Quali sono le assunzioni relativamente al sistema e quali sono le proprietà desiderate?_

#### Prove di Correttezza
Ad ogni livello di dettaglio sono verificate le proprietà di _correttezza_
  - A livello di _GM_ ci si riferisce alla correttezza _rispetto ai requisiti_
  - A livelli _successivi_ è la corretteza _rispetto al livello più astratto_

Grazie alla verifica di queste proprietà, il modello è _consistente_.

## **Raffinamento**
E' il secondo _blocco concettuale_ usato nell'applicazione del metodo<br>
Consiste nell'ottenere a partire da una macchina più astratta una sua forma più raffinata(_concreta_)<br>
E' applicato iterativamente sino al punto di raffinamento considerato << _sufficiente_ >> dallo sviluppatore

#### Principio di Sostituzione
**Definizione**: _E' accettabile sostituire un programma con un'altro a patto che sia impossibile per un utente rendersi conto della sostituzione_.

> Il metodo di raffinamento per le ASM non è basato su alcun principio di sostituzione ma bensì sulle _commutazioni algebriche_


#### Schema per il raffinamento
Per raffinare una ASM **$A$** in una ASM **$R$** si devono definire:
  1. Una nozione di _stato raffinato_(a livello **$R$**)
  2. Una nozione di _stati di interesse_ e di _corrispondenze_ tra gli stati d'interesse **$S$** di **$A$** e quelli **$S'$** di **$R$**
     * Coppie di stati delle run che uno vuole relazionare, inclusa corrispondenza stati iniziali/finali
  3. Una nozione di _segmenti di computazione astratta_ **$T_1,T_2,...,T_m \in A$** e i corrispondenti _segmenti di computazione raffinata_ **$\sigma_1,\sigma_2,...,\sigma_n \in R$**
  4. Una nozione di _locazioni di interesse_(in **$A$**) e di _locazioni corrispondenti_(in **$R$**); per le quali si vuole stabilire la corrispondenza nel raffinare
  5. La relazione di _equivalenza_(**$\equiv$**) _dei dati_ tra le locazioni di interesse(a livello **$A$** ed **$R$**)

![schemaRaffinamento](./Immagini/schemaRaffinamento.png)

#### Prova di correttezza di raffinamento
Una volta stabilita la corrispondenza degli stati e la loro quivalenza, è possibile asserire che **$M*$** _è un corretto raffinamento di_ **$M$** sse:
  - Ogni run raffinata(finita o infinita) simula una run astratta(finita o infinita) tra stati corrispondenti equivalenti

**Formalmente**:<br>
Fissata la nozione di equivalenza _$\equiv$_ tra gli stati di interesse, fissati gli stati iniziali e finali, una ASM _$R$_ è detta corretto raffinamento di _$A$_ _$sse$_:<br>
_$\forall$_ _$R$_-run _$S'_0, S'_1,...,$_ esiste una _$A$_-run _$S_0,S_1,...$_ e sequenze _$i_0 < i_1 < ... <$_ e _$j_0 < j_1 < ...$_ tali che _$i_0 = j_0 = 0$_ e _$S_{i_k} \equiv S'_{j_k}$_ per ogni _$k$_<br>
E si verifica una delle due condizioni:
  1. Entrambe le run terminano e gli stati finali sono l'ultima coppia di stati quivalenti; oppure
  2. Entrambe le run sono infinite

#### Minimalità delle sequenze
Le sequenze di stati corrispondenti devono essere scelte in modo tale che siano _minimali_, ossia che all'interno di sequenze corrispondenti non ci siano stati equivalenti<br>
i.e. non esistano _$i,j$_ t.c. _$i_k < i < i_{k+1}, j_k < j < k_{k+1}$_ con _$S_i \equiv S'_j$_

![minimalita-sequenze](./Immagini/minimalita-sequenze.png)


**SPIEGAZIONE**: <br>
_Date due macchine, una astratta $A$ e una raffinata $R$ che rappresentano la stessa realtà, queste avranno_:
  - `Per $R$-run e $A$-run si intende la simulazione dei diversi modelli`
  1. _Degli stati di interesse corrispondenti: ad esempio, la sala cinesca aperta e quella chiusa e quando raffino cambio il comportamento del sistema in mezzo a questi due stati(di interesse corrispondenti) magari aggiungendone altri(stati) infatti, come possiamo vedere in figura, il numero di passi tra la versione astratta e quella raffinata NON è identico perchè(magari) quella raffinata avrà meno passi poichè non coglie a pieno il comportamento del sistema come quella raffinata MA ci saranno sicuramente degli stati equivalenti che catturano la stessa realtà dei fatti tra le 2 macchine._
  2. _Quando parlo di segmenti di computazione astratti e segmenti di computazione raffinati mi riferisco ad un insieme di passi che intercorrono tra uno stato all'altro_
  3. _Quindi definiamo gli stati di interesse e quelli dovranno essere equivalenti quando eseguiremo una simulazione di entrambi i modelli, tra cui ci sono gli stati iniziali e finali di entrambe le macchine, definita la funzione d'equivalenza, decidiamo che gli stati di interesse in $A$ avranno le loro locazioni di interesse(e locazioni corrispondenti in $R$) tali che i dati in esse contenuti siano equivalenti._
  4. **Formalmente**: _Per ogni run raffinata ne esiste una astratta t.c. esistono sequenze di stati successivi in entrambi i modelli che partiranno dallo stato iniziale(che sarà equivalente per le 2 macchine) e, per ognuna di questi indici delle sequenze, gli stati alla fine corrisponderanno + termineranno / andranno infinite_
  5. **Minimali**: _All'interno di queste sequenze non devono esserci degli stati rappresentati dagli indici $ij$ che corrispondono. Quindi se prendo 2 run, una astratta e una raffinata, e le divido in pezzetti dove gli stati di partenza e di arrivo corrispondono, però in mezzo a questi frammenti non ci devono essere degli stati che che si quivalgono tra loro_

<a name="shittering-rafinament"></a>
## **Stuttering Refinement**
Versione più semplice di raffinamento che permette il _controllo automatico della correttezza_ di raffinamento tra _$R$_ raffinata e _$A$_ astratta

#### Schema per il raffinamento
Per raffinare una ASM _$A$_ in una ASM _$R$_ si devono definire:
  1. Una nozione di _stato raffinato_(a livello _$R$_)
  2. Una nozione di _stati di interesse_ e di _corrispondenze_ tra gli stati d'interesse _$S$_ di _$A$_ e quelli _$S'$_ di _$R$_
  3. Una nozione di _locazioni di interesse_(in _$A$_) e di _locazioni corrispondenti_(in _$R$_); per quali si vuole definire una corrispondenza nel raffinare
  4. La relazione di _equivalenza_(_$\equiv$_) _dei dati_ tra le locazioni di interesse(a livello _$A$_ ed _$R$_)

**Formalmente**: <br>
Fissata la nozione di equivalenza _$\equiv$_ tra gli stati di interesse, fissati gli stati iniziali e finali, una ASM _$R$_ è detta _corretto raffinamento stuttering_ di _$A$_ _$sse$_: <br>
Ogni _$R$_-run _$S'_0,S'_1,..,$_ può essere ripartita in sotto-run _$\rho'_0, \rho'_1,...$_ ed esiste una _$A$_-run _$S_0,S_1,...$_ t.c. per ogni _$\rho'_i$_ vale che _$\forall S' \in \rho'_i: S' \equiv S_i$_ <br>
<br>

![stuttering](./Immagini/stuttering.png)

**SPIEGAZIONE**: <br>
_Ogni run del modello raffinato è composta da un insieme di stati $S'$,questi li posso ripartire in sotto run $\rho'_0, \rho'_1,...$(dove una sotto-run può contenere anche solo un singolo stato) t.c. esiste una $A$-run sopra(ovvero una run astratta) che corrisponda alla $R$-run sotto(ovvero gli stati della run raffinata $S'_0,S'_1,...$ appartenenti alla sotto-run corrispondente)_

#### Tipi di Raffinamento
  - **Orizzontale**:<br>
    Raffinamento _incrementale_ usato per introdurre nuovi _comportamenti_ o _adattamenti_ a condizioni dell'ambiente<br>
    Supporta il principio di _design for change_
  - **Verticale**:<br>
    Permette di introdurre via via sempre più dettagli sugli _elementi di un modello_(domini, funzioni, regole)<br>
    Supporta il principio del _design for use_

#### Combinare i tipi di raffinamento
  - **Raffinamento della segnatura** <br>
    Raffinamento su domini e funzioni stabilendo:
      1. _La notazione di stato raffinato_
      2. _La relazione tra stati di interesse e tra locazioni_
      3. _La relazione di equivalenza_
  - **Raffinamento procedurale** <br>
    Raffinamento di regole(raffinamento di _sottomacchine_):<br>
    Consiste nel sostituire una macchina(=complesso di regole) con una più complessa<br>
    Stabilendo la corrispondenza tra segmenti di computazione in modo tale che l'effetto di un'operazione concreta sui dati sia equivalente all'effetto di operazioni astratte su dati astratti.

---

<a name="model-checking"></a>
# **Model Checking**
Le tecniche di verifica formale sono generalmente viste come la somma di 3 componenti:
  1. Framework con cui modellare il sistema che vogliamo analizzare
  2. Linguaggio di specifica delle proprietà da verificare
  3. Metodo per verificare che il sistema soddisfi le proprietà specificate

Queste diventano:
  1. Modello _$M$_ che descrive il comportamento del sistema **$\Rightarrow$** Automa di Kripke _$M=(S, \Delta, I, L)$_
  2. Codifica della proprietà da verificare in una logica temporale  **$\Rightarrow$** _$BTL$_ (Branch-time-logic) **$\Rightarrow$** Discreta **$\Rightarrow$** _$CTL$_ (Computational-tree-logic)
  3. Algoritmo di model Checking **$\Rightarrow$** Algoritmo di Labelling

### _Automi Kripke_
Argomento trattato durante la spiegazione delle ASM [QUI](#automi-kripke)

### _Logiche temporali_
  * _$LTL$ - Linear-time-logic_: Considera il tempo come un insieme di cammini, dove il _cammino_ è una sequenza di istanti di tempo
  * _$BTL$ - Branching-time-logics_: Rappresenta il tempo come un albero, con radice l'istante corrente

Un'altra classificazione divide tra tempo _continuo_ e _discreto_.<br>
**$\Rightarrow$** Noi studieremo la logica _BTL discreta_, ovvero la _$CTL$ - Computational-tree-logic_
  * _$CTL$_: I suoi modelli sono rappresentabili mediante una struttura ad albero in cui il futuro non è deterministico e in cui ogni stato futuro include quello passato.

<a name="ctl"></a>
#### $CTL$ - Computational-tree-logic
Logica costruita da formule atomiche che rappresentano delle descrizioni atomiche del sistema.<br>
Vengono definite in modo induttivo come: <br>
$$\phi := \bot | \top | p | (\neg \phi) | (\phi \wedge \phi) | (\phi \vee \phi) |
(\phi \rightarrow \phi) \\ | AX \phi | EX \phi | AF  \phi | EF \phi | AG \phi | EG\phi | A[ \phi U \phi] | E [\phi U \phi]$$

Dove:
  * **$\top, \bot, \neg, \wedge, \vee, \rightarrow$**: sono connettivi logici _classici_
  * **$AX, EX, AG, EG, AU, EU, AF, EF$**: Sono connettivi _temporali_

In prarticolare:
  - **$A$**: Sta per "along-all-paths" (inevitabile/inevitabilmente/inevitably)
  - **$E$**: Sta per "along-at-least-one-path" (possibile/possibly)
  - **$X,F,G,U$**: Operatori della logica temporale dove:
    - **$X$**: Si riferisce allo stato successivo($AX$ per tutti gli stati successivi)
    - **$F$**: Per qualche stato futuro($AF$ questa regola varrà per forza in qualche stato futuro per ogni cammino)
    - **$G$**: Per tutti gli stati futuri ($AG$ regola che deve valere per tutti gli stati di tutti i cammini)


##### Semantica connettivi CTL:
![Semantica connettivi CTL](./Immagini/SemanticaConnettiviCTL1.png)<br>
![Semantica connettivi CTL](./Immagini/SemanticaConnettiviCTL2.png)
<br>
**PS**: _Quando parliamo di stati futuri includiamo anche il presente_

##### Equivalenze Importanti:
  * $\neg AF \phi = EG \neg \phi$
  * $\neg EF \phi = AG \neg \phi$
  * $\neg AX \phi = EX \neg \phi$
  * $AF \phi = A[T U \phi]$
  * $EF \phi = E[T U \phi]$

_Per ricordarsi le equivalenze si può pensare alla loro forma negata, per poi negarla a sua volta._ <br>
Ad esempio, af _$AF \phi$_ significa che _$\phi$_ varrà prima o poi in tutti i cammini/path, quando questa cosa non è vera? quando esisterà un cammino/path dove non varrà mai _$\phi$_(quindi dove varrà sempre _$\neg \phi$_), quindi _$EG \neg \phi$_ <br>
<br>
Queste formule saranno importanti quando si parlerà dell'algoritmo di model checking dove da queste formule dovremo ricavarne un loro sottoinsieme di base.<br>

#### Descrizione formule CTL
  1. $\top = \neg \bot$
  2. $\phi_1 \vee \phi_2 = \neg(\neg \phi_1 \wedge \neg \phi_2)$
  3. $\phi_1 \rightarrow \phi_2 = (\neg \phi_1 \vee \phi_2)$
  4. $AX(\phi_1) = (\neg EX \neg \phi_1)$
  5. $EF(\phi_1) = E(T U \phi_1)$
  6. $EG(\phi_1) = (\neg AF \neg \phi_1)$
  7. $AG(\phi_1) = (\neg EF \neg \phi_1)$
  8. $A(\phi_1 U \phi_2) = \neg(E[\neg \phi_2 U (\neg \phi_1 \wedge \neg \phi_2)] \vee \neg AF \phi_2)$

Due formule molto importanti(verranno utilizzate veramente sempre durante l'algoritmo di SAT spiegato successivamente) ma non menzionate nel testo sono:
  1. **$Pre_{\exists}(Y)$** = $\{s \in S | \exists s', s \rightarrow s' \wedge s' \in Y\}$
  2. **$Pre_{\forall}(Y)$** = $\{s \in S | \forall s', s \rightarrow s' \wedge s' \in Y\}$

### Possibili Esercizi
#### Verifica formula Ben-formata
Per _verificare_ che una formula è ben formata rispetto alla logica CTL, e quindi alla semantica dei suoi connettivi, dobbiamo costruire l'_Albero di Parsing_.<br>
Bisogna scorrere la formula da SX verso DX etichettando i nodi degli alberi in base agli operatori all'interno della formula. <br>
Se i nodi sono unari(_$AG$_ etc..) avranno solo 1 figlio, se binari(_$AU$_, _$EU$_ etc..) avranno 2 figli, nelle foglie ci saranno solo le preposizioni atomiche.
  * Se riesco a costruire l'albero di parsing senza avere incertezze su quali siano i nodi successivi fino ad arrivare alle proposizioni atomiche, allora si può dire che la formula di partenza è ben formata
  * Se mi trovo in una situazione dove non capisco la precedenza o non c'è una formulazione corretta dei diversi connettivi(vedi _$A \neg G \neg P$_ dove non riesco a capire se per _$A$_ si intende _$AG, AF, AX, AU$_ e qundi non c'è una formulazione corretta di questo connettivo) la formula non è ben formata.

#### Verifica Automa di Kripke
Per capire se un automa è anche un automa di Kripke dobbiamo verificare che ci sia sempre uno stato successivo: quindi non è vero che, arrivati ad un certo punto della computazione, arriviamo in uno stato da cui non riusciamo ad uscire.
  * _$(p,q) \rightarrow (r) \rightarrow (t) \rightarrow (p,q)$_: Automa di Kripke
  * _$(p,q) \rightarrow (r) \leftarrow (t)$_: Automa Non di Kripke

#### Dimostrazione Equivalenza formule CTL
Per dimostrare una formula CTL facciamo come abbiamo fatto in Logica:
  1. _$\Rightarrow$_
  2. _$\Leftarrow$_

Quindi dimostriamo l'equivalenza sia in un senso sia nell'altro prendendo la formula a SX come ipotesi(in cui assumiamo valgano le proposizioni al suo interno) e prendiamo la formula a DX come tesi che dobbiamo verificare. <br>
Quando dobbiamo dimostrare una proprietà negata(come ad esempio da **$EX \neg \phi$** a **$\neg AX \phi$**) procediamo per assurdo in modo tale che:
  1. Ci permette di togliere la negazione
     * Quindi, se prendiamo l'esempio di prima, dimostrare che **$\forall s, \forall M \space \Rightarrow \space s,m \models AX \phi$**
  2. Cerchiamo di trovare una contraddizione con le ipotesi(ricordandosi di segnare con un numero la contraddizione trovata, ad esempio _$(n)$_)
     * **$\forall s$ t.c. $s \rightarrow s' \space \Rightarrow \space M,s' \models \phi$ $(n)$**
  3. Diamo che la formula _[numero della formula]_ contraddice le ipotesi [_qui dobbiamo dire quali ipotesi contraddice_]
     * **$(n)$** contraddice l'ipotesi che **$M,s \models EX \neg \phi$**
  4. L'assurdo si rimuove e quindi [_formula originale che si voleva dimostrare_]
     * L'assurdo si rimuove e quindi **$s,m \models \neg AX \phi$**

### _Algoritmo Model Checking_
Dati _$M,s \in S$_ e _$\phi$_, verifica se _$M,s \models \phi$_.<br>
Possiamo considerare due tipi di problema:
  * Considerare uno stato _$s_0 \in I$_ in cui verificare che _$M,s_0 \models \phi$_
  * Considerare uno stato _$s \in S$_ qualsiasi, cioè estrarre l'insieme _$X \subseteq S$_ di stati in cui _$M,s \models \phi$_

In questo ultimo caso possiamo anche veriicare che _$M, s_0 \models \phi$_, verificando che _$s_0$_ sia contenuto nell'insieme degli stati che soffisfano _$\phi$_, ottenuto come detto predentemente.

### _Algoritmo Labelling_
  * **INPUT**: Un modello _$M$_ e una formula _$\phi$_
  * **OUTPUT**: Un insieme _$X \subseteq S$_ di stati in cui _$\phi$_ è soddisfatta

Possiamo restringere l'insieme degli operatori CTL all'insieme adeguato composto solo da _$\top, \bot, \wedge, AF, EU, EX$_<br>
L'algoritmo etichetta ciascuno stato _$s \in S$_ con l'insieme delle formule vere in _$s$_ stesso; quindi ogni stato è etichettato da un insieme di formule. <br>
<br>
Sia _$\psi$_ una sottoformula di _$\phi$_ e tutte le sottoformule immediate di _$\psi$_ siano state già aggiunte alle etichette degli stati che le soffisfano.<br>
L'algoritmo etichetta fli stati valutando la struttura di _$\psi$_.<br>
Se **$\psi$** è:
  * **$\bot$**: Nessuno stato deve essere etichettato con _$\bot$_
  * **$p$**: Etichetta uno stato con _$s$_ con _$p$_ se _$p \in L(s)$_
  * **$\psi_1 \wedge \psi_2$**: Etichetta uno stato _$s$_ con _$\psi_1 \wedge \psi_2$_ se _$s$_ è già stato etichettato con _$\psi_1$_ e _$\psi_2$_
  * **$\neg \psi$**: Etichetta uno stato _$s$_ con _$\neg \psi$_ se _$s$_ non è già etichettato con _$\psi_1$_
  * **$AF \psi_1$**:
    1. Se uno stato _$s$_ è etichettato con _$\psi_1$_ allora _$s$_ viene etichettato con _$AF \psi_1$_
    2. Se uno stato è etichettato con _$AF \psi_1$_ se tutti gli stati successori sono etichettati con _$AF \psi_1$_, fin quando è possibile
  * **$E[\psi_1 \cup \psi_2]$**:
    1. Se uno stato _$s$_ è etichettato con _$\psi_2$_ allora viene etichettato con _$E[\psi_1 \cup \psi_2]$_
    2. Uno stato è etichettato con _$E[\psi_1 \cup \psi_2]$_ se è etichettato con _$\psi_1$_ e almeno uno dei suoi successori è etichettato con _$E[\psi_1 \cup \psi_2]$_ , fin quando è possibile.
  * **$EX \psi_1$**: Etichetta uno stato _$s$_ con _$EX \psi_1$_ se uno dei suoi successori è etichettato con _$\psi_1$_


<a name="pseudocodice-sat"></a>
#### Pseudocodice $SAT$
![SAT](./Immagini/SAT.png)

_Tramite l'algoritmo di SAT voglio verificare in quali stati vale la formula argomento, questo algoritmo è un pseudo codice dell'algoritmo di model chacking che quindi utilizza l'algoritmo di labelling._

#### Funzione **$SAT_{AF}(\phi)$**
![SAT](./Immagini/SAT_AF.png)

  * _local var $X,Y$_: 2 variabili che sono 2 insiemi
  * _$X := S$_: Nella variabile(insieme) _$X$_ ci metto tutti gli stati della macchina
  * _$Y := SAT(\phi)$_: Nella variabile _$Y$_ ci metto gli stati che soddisfano la formula argomento
  * _repeat until $X=Y$_: Il ciclo continua(e anche la funzione) funchè i due insiemi non sono uguali, ovvero ripeto i passi dell'algoritmo di _$AF \phi$_ finchè non trovo il sottoinsieme degli stati in cui vale _$\phi$_.
  * _$X := Y$_: Metto il valore di _$Y$_ dentro _$X$_ in modo da poter rieseguire un'altro passo di _$AF \phi$_ senza perdere le computazioni precedenti
  * _$Y := Y \cup \{s| \forall s', s \rightarrow s' \wedge s' \in Y\}$_ =
    - = _$Y := Y \cup pre_{\forall}\{Y\}$_ dove:
      1. _$Y$_: Copre il primo punto dell'algoritmo di labelling in cui diceva che ogni stato in cui vale _$\phi$_ vale anche _$AF \phi$_, ricordando il fatto che il futuro comprende il persente
      2. _$pre_{\forall}\{Y\}$_: Copre il secondo punto dell'algoritmo di labelling in cui controlla tutti gli stati _$s$_ tali che tutti i loro successori sono _$s' \in Y$_
  * _return $T$_: Alla fine ritorno tutti gli stati della macchina che soddisfano _$AF \phi$_

![SAT](./Immagini/SAT_AF_1.png)

#### Funzione **$SAT_{EU}(\phi, \varphi)$**
![SAT](./Immagini/SAT_EU.png)<br>
![SAT](./Immagini/SAT_EU_1.png)

#### Funzione **$SAT_{EX}(\phi)$**
![SAT](./Immagini/SAT_EX.png)<br>
![SAT](./Immagini/SAT_EX_1.png)


### Strutture Dati Efficienti
![ROBDD](./Immagini/ROBDD.png)

<a name="verifica-proprietà-temporali"></a>
### _Verifica delle Proprietà Temporali_
1. **Reachability Property | Proprietà di raggiungibilità** _$EF \phi$_
   * "Determinate situazioni particolari possono essere raggiunte"
   1. **Raggiungibilità Condizionale** _$EU$_
      * "Quando una condizione restringe la forma dei cammini che raggiungono lo stato desiderato"
   2. **Raggiungibilità applicata a stati raggiungibili** _$EF(AG) | AG(EF)$_
   - **Model Checker e Raggiungibilità**
     - Le proprietà di raggiungibilità sono le più facili da verificare
     - Se un tool è in grado di costruire il grafo di raggiungibilità, la verifica di questo tipo di proprietà comporta solo l'analisi dei cammini del grafo
     - Grafo ri Raggiungibilità
       - Esistono 2 classi di algoritmi che trattano il problema della raggiungibilità e che servno per costruire l'insieme degli stati raggiungibili all'interno del grafo:
       1. _Algoritmi Forward Chaining_
          1. Si parte dagli stati iniziali
          2. Si aggiungono i successori
          3. Si procede fino a saturazione
       2. _Algoritmi Backword Chaining_
          1. Si parte dagli stati finali
          2. Si aggiungono i successori
          3. Si procede fino a saturazione
          4. Si testa se qualche stato iniziale appartiene all'insieme di saturazione
       3. _Esplorazione on-the-fly_
          1. Esplora il grafo di raggiungibilità senza di fatto costruirlo:<br>
             Costruisce solo parzialmente il grafo, via via che l'esplorazione procede e senza memorizzare ciò che è già stato visitato
          2. L'esplorazione può avvenire in modo forward e/o backward
          3. E' efficiente solo quando l'insieme degli stati finali è effettivamente raggiungibile
2. **Safety Property | Proprietà di Sicurezza** _$AG \neg \phi$_
   * "Sotto certe condizioni, un evento non può mai accadere"
   * **Safety Condizionale** _$AU$_
     - `Safety` _$\neq$_ `Rechability` _$\neg EF$_
       * Nella maggior parte dei casi una proprietà di safety si esprime come come la negazione di una prorprietà di raggiungibilità
     - `Safety senza passato` _$AU$_
       * Spesso una proprietà di safety non si riferisce al passato ma al futuro
     - `Safety con explicit past` _$AG$_
       * Proprietà di safety che fa riferimento al passato
       - I tool di model checking non hanno operatori del passato; esistono 2 modi per gestire la proprietà di safety con riferimento al passato:
         1. _Eliminazione operatori del passato_: <br>
            Consiste nel tradurre una formula _$AG \phi^-$_ in una proprietà di raggiungibilità che fa uso di variabili history <br>
            Una _variabile history_ memorizza l'occorrenza di qualche evento(passato) senza modificare il comportamento(futuro) del sistema<br>
            Per ogni formula _$\phi^-$_, introduciamo una variabile booleana _$h_{\phi^-}$_ che è vera sse _$\phi^-$_ è vera <br>
            La variabile _$h_{\phi^-}$_ viene aggiornata ad ogni transazione
         2. _History Variables_
3. **Liviness Property | Proprietà di Vivacità** _$AG(AF \phi) | AG(EF \phi)$_
   * "Sotto certe condizioni, un evento accadrà"
4. **Assenza di Deadlock** _$AG(EX true)$_
   * "Il sistema non si troverà mai in una condizione in cui non è possibile alcun progresso"
   * Qualunque sia lo stato raggiunto (_$AX$_), esiste uno stato immediatamente successore(_$EX true$_)
   * `Deadlock + Safety`
     - Spesso si pensa ad una proprietà di deadlock come ad una proprietà di safety; si descrivono esplicitamente gli stati di deadlock e si prova che non possono essere raggiunti
     - In verità le cose non sonon sempre così
5. **Fairness Property | Proprietà di Equità** _$nope$_
   * "Sotto certe condizioni, un evento accadrà infinite volte"
   * Le proprietà di fairness non possono essere espresse in pura CTL perchè manca l'operatore _$F^{\inf}$_ che descrive _"un numero infinito di volte"_ o _"infinitamente spesso"_
   * In _$SMV$_ le ipotesi di fairness vanno specificate come parte del modello piuttosto che ricorrere alla logica CTL + fairness


<a name="nusmv"></a>
# **NuSMV**
**SMV**: "Symbolic Model Verifier"<br>
**NuSMV**: Reimplementazione SMV <br>

Strutture di _Kripke_ descritte in un linguaggio che permette la specifica di _formule CTL_ in aggiunta della proprietà di _Fairness_("sotto certe condizioni, un evento accadrà infinitamente spesso")<br>
La rappresentazione al suo interno è fatta tramite _ROBDDs_(reduced ordered binary decision diagrams)<br>
Permette la _verifica automatica delle specifiche_, in caso contrario produce un _controesempio_.<br>

#### Esempio programma SMV
**MODULE** _main_<br>
**VAR**<br>
&nbsp;&nbsp;&nbsp;&nbsp;request: _boolean_;<br>
&nbsp;&nbsp;&nbsp;&nbsp;state: {ready, busy};<br>
**ASSIGN**<br>
&nbsp;&nbsp;&nbsp;&nbsp;_init_(state) := ready;<br>
&nbsp;&nbsp;&nbsp;&nbsp;_next_(state) :=<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_case_<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;state=ready & request: busy;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;state=busy & request: busy;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;state=ready & not request: ready;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TRUE: {ready, busy};<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_esac_;<br>

**SPEC** _AG_(request -> _AF_ (state = busy))

#### Kripke $\rightarrow$ NuSMV

![kripke](./Immagini/Kripke-NuSMV.png)

---

---

# **Pratica**
<a name="asm-template"></a>
### ASM Template
**Header**:<br>
_asm_ nomeASM <br>
_import_ ../LIB/StandardLibrary <br>

_signature_: <br>
&nbsp;&nbsp;&nbsp;&nbsp;// Domini Astratti<br>
&nbsp;&nbsp;&nbsp;&nbsp;_abstract domain_ Person<br>
&nbsp;&nbsp;&nbsp;&nbsp;// Domini concreti<br>
&nbsp;&nbsp;&nbsp;&nbsp;_domain_ minuti _subsetof_ Integer <br>
&nbsp;&nbsp;&nbsp;&nbsp;// Enumerabili<br>
&nbsp;&nbsp;&nbsp;&nbsp;_enum domain_ RISULTATO = {passato, bocciato}<br>
&nbsp;&nbsp;&nbsp;&nbsp;// Funzioni che vengono modellate interamente dalla macchina<br>
&nbsp;&nbsp;&nbsp;&nbsp;_dynamic controlled_ A: Integer <br>
&nbsp;&nbsp;&nbsp;&nbsp;// Funzion date dall'ambiente esterno o rilasciate ad esso<br>
&nbsp;&nbsp;&nbsp;&nbsp;_dynamic monitored_  B: boolean <br>
&nbsp;&nbsp;&nbsp;&nbsp;// Funzioni definite su tutti i domini la cui interpretazione non cambia<br>
&nbsp;&nbsp;&nbsp;&nbsp;_static_ minutiInOre: Integer <br>
&nbsp;&nbsp;&nbsp;&nbsp;// Funzioni i cui valori sono computati da funzioni statiche <br>
&nbsp;&nbsp;&nbsp;&nbsp;// o monitorate mediante legge fissa<br>
&nbsp;&nbsp;&nbsp;&nbsp;_derived_ changeResult: RISULTATO -> RISULTATO  <br>
&nbsp;&nbsp;&nbsp;&nbsp;_static_ somma: Prod(Integer, Integers) -> Integers <br>
&nbsp;&nbsp;&nbsp;&nbsp;// Agenti relativi alle ASM_multiagenti<br>
&nbsp;&nbsp;&nbsp;&nbsp;_domain_ Producer _subsetof_ Agent<br>
&nbsp;&nbsp;&nbsp;&nbsp;_domain_ Consumer _subsetof_ Agent<br>
&nbsp;&nbsp;&nbsp;&nbsp;_static_ producer: Producer

**Body**<br>
_definitions_:<br>
_domain_ minuti = {0:59}<br>
_function_ minutiInOre=60<br>
_function_ changeResult($s in RISULTATO) = <br>
&nbsp;&nbsp;&nbsp;&nbsp;_if_($s = bocciato) <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_then_ passato <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_else_ bocciato <br>
&nbsp;&nbsp;&nbsp;&nbsp;_endif_ <br>

_rule_ macroConRule($a in RISULTATO) = <br>
&nbsp;&nbsp;&nbsp;&nbsp;_skip_ <br>
&nbsp;&nbsp;&nbsp;&nbsp;// Importantissimo: se voglio utilizzare una macro rule 2 all'interno della macro rule 1 <br>
&nbsp;&nbsp;&nbsp;&nbsp;//  la macro rule 2 DEVE essere dichiarata PRIMA della macro rule 1 <br>

_rule_ r_produce = <br>
&nbsp;&nbsp;&nbsp;&nbsp;_skip_ <br>

_rule_ r_consumer = <br>
&nbsp;&nbsp;&nbsp;&nbsp;// Con una certa probabilità estendo un nuovo agente <br>
&nbsp;&nbsp;&nbsp;&nbsp;choose $probabilita in {1:100} with true do: <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if($probabilita > 90) then // Quindi ho il 10% che accada <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;extend Consumer with $consumern do <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_skip_

// Invarianti <br>
_invariants over_ A,B: A implies B <br>

// ProprietàCTL <br>
_CTLSPEC_(ag(ef(noBrainLeft)))<br>


**Main Rule**<br>
_main rule_ r_Main = <br>
&nbsp;&nbsp;&nbsp;&nbsp;_par_<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_program_(producer)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_program_(consumer)<br>
&nbsp;&nbsp;&nbsp;&nbsp;_endpar_<br>

**Initialization**<br>
_default init_ s0:<br>
&nbsp;&nbsp;&nbsp;&nbsp; _function_ changeResult($s in RISULTATO) = bocciato<br>
&nbsp;&nbsp;&nbsp;&nbsp;_agent_ Producer:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;r_produce[]<br>

&nbsp;&nbsp;&nbsp;&nbsp;_agent_ Consumer:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;r_consume[]<br>


---

<a name="scenario-template"></a>
### Scenario Template
_scenario_ nomeScenario <br>
_load_ ../ASMETA/nomeASM.asm <br>

// Impostiamo l'invariante per verificare che A sia minore di Orwell <br>
_invariant_ inv_1: A < 1984 <br>

// Controllo lo stato iniziale <br>
// check statements-of-terms <br>
_check_ A=0 <br>

// Se va tutto bene faccio un passo della macchina andando allo stato successivo<br>
_step_ <br>

// Controllo stato successivo <br>
_check_ A=1 <br>
// Faccio andare avanti la macchina fino ad una determinata condizione <br>
_step until_ A=10 <br>

_check_ A=11 <br>

// "Impostare una par rule che, con 2 update rule, modifica lo stato della macchina"<br>
_exec_ <br>
&nbsp;&nbsp;&nbsp;&nbsp;_par_ <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A:=111 <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; B:=111 <br>
&nbsp;&nbsp;&nbsp;&nbsp;_endpar_ <br>
// Possibile utilizzare il costrutto _set_ per istanziare le variabili(monitorate) libere<br>
// come, ad esempio, la variabile `carry` in Ferryman<br>










































<style>
a, b, strong { color: #0033cc}
em, code {color:#0066cc}
</style>
