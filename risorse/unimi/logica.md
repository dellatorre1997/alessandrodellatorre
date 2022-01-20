{% include header.html %}

---

# Riassunto Logica

## Indice
1. ### **Concetti base**
   - Paradossi
   - Abusi retorici
   - Enunciati: _Atomici/Composti_
   - Principi: _Bivalenza/Estensionalità_
   - Teoremi
   - Nome
   - Senso
   - Sostituzione
     - Denotazione invariante per sos.
     - Senso non invariante per sos.
   - Logica proposizionale: Sintassi, Semantica, Calcolo
2. ### **Tipi di logica**
   1. #### [**Proposizionale**](#logica-proposizionale)
      * Proposizione: Atomica/Composta
      * Connettivi: estensionali
      * **[Sintassi](#logica-proposizionale-sintassi)**
        - **Alfabeto**: Lettere; T/F; Connettivi; Sim. Ausiliari(,); nient'altro_
        - **Fbf**: _Lettere; T/F; Connettivi; nient'altro_
        - **Stfm(P)**:
          - Se P è T/F/lett _$\rightarrow Stfm(P)=\{P\}$_
          - Se P è _$(∼Q) \rightarrow Stfm(P)=\{P\} \cup Stfm(Q)$_
          - Idem con patate per gli altri
        - Alberi di Struttura
        - Induzione Strutturale
          - TH Induzione Strutturale
      * **[Semantica](#logica-proposizionale-semantica)**
        - Interpretazioni _$fbf \rightarrow \{0,1\}$_
        - _fbf_ soddisfacibili / insodd.(_$\nvDash P$_)
        - Modello _$v \vDash P$_
        - Tautologie _$\vDash P$_
        - [Insiemi](#logica-proposizionale-insiemi) _$Γ$_
        - [Conseguenza Semantica](#logica-proposizionale-conseguenza-semantica) _$Γ \vDash P$_
        - **TH. Deduzione semantica**
          - _$Γ \cup \{P\} \vDash Q sse Γ \vDash (P \Rightarrow Q)$_
          - Corollario: _$P \vDash Q sse \vDash (P \Rightarrow Q)$_
        - Conseg. e Insodd.
          - _$Γ \vDash P sse Γ \cup \{\sim P\}$_ insodd.
        - **TH: Compattezza**
        - [**Equivalenza Semantica**](#logica-proposizionale-equivalenza-semantica)_$P \equiv Q$_
        - **Forme Normali**
          - _Congiuntive_
          - _Disgiuntive_
          - _Complete_
      * [**Calcolo**](#sistemi-deduttivi)(Sistemi Deduttivi)
        - [Deduzione Naturale](#deduzione-naturale)
        - [Calcolo dei Sequenti](#calcolo-sequenti)
        - Risoluzione Logica Proposizionale
          - Refutazione
          - Clausole
            - _$P=(A \vee B) \wedge (\sim A \vee C)$_
            - _$P^C=\{\{A,B\},\{\sim A,B\}\}$_
          - **Risolvente**
          - Derivazione
          - Refutazione
          - Lemma di Risoluzione
          - Teorema di Risoluzione
          - Verifiche tramite risoluzione
            - _$S^c \cup (\sim P)^c \vdash_R \square$_
            - _$(\sim P)^c \vdash_R \square$_
   2. #### [**Primo Ordine/Logica Predicati**](#logica-primordine)
      * **Sintassi**
        * Alfabeto
          - _Costanti; Variabili; Funzioni; Predicati; Connettivi(+T,F); Quantificatori($\exists \forall$), Sim. Ausiliari(,)_
        * **TER**: _Costanti; Variabili; Funzioni; Nient'altro_
        * **fbf**: _F/T; Predicato di termini; Connettivi; Quantificatori; Nient'altro_
        * _Stfm(P)_
        * Induzione Strutturale TER
        * Induzione Strutturale
      * **Semantica**
        * Scope: var Libere/Legate
        * Formule: Chiuse/Aperte
        * Ridenominazione
        * Sostituzione
        * **Struttura**: _$S=(D,I)$_
          - _Costante($c^S=I(c)$),Funzione($f^S=I(f)$),Predicato($B^S=I(B)$)_
          - no FV
        * **Ambiente** per S è funz. _$\xi^S: VAR \rightarrow D$_
          - _$ENV_S = \{\xi^S \| \xi^S:VAR \rightarrow D\}$_
        * Semantica _$L = (S,\xi^S)$_
          - Valore TER _${[\space]}_{S,\xi}: TER \rightarrow D$_
          - Funzione Valutazione _$v^{(S,\xi)}:FBF \rightarrow \{0,1\}$_
        * Soddisfacibilità
          - Lemma di soddisfacibilità
        * Equivalenza Semantica
        * FN Prenessa
        * **Forma Skolem**
          - _$\exists x \forall y \forall z \exists t B(x,y,z,t) \rightarrow$_
          - _$\forall y \forall z \exists t B(c,y,z,t) \rightarrow$_
          - _$\forall y \forall z B(c,y,z,g(y,z))$_
        * TH Skolem
      * **Calcolo**
        - **TH Church**
        - **Semidecidibilità**
        - Deduzione Naturale
        - Calcolo Sequenti
        - Criterio Equalità
        - Ricerca Dimostrazioni
        - Ricerca Contromodelli
        - **TH Correttezza**
        - **TH Completezza**
        - Metodo Risoluzione Predicativo
          - Sostituzione
          - Composizione diSostituzioni
          - Unificatore
          - **Mgu**
          - Insieme Disaccordo
          - [Algoritmo di Unificazione](#algoritmo-unificazione)
          - **Risolvente**
          - Teorema di Risoluzione
          - Verifica di _$S \vDash P$_ con Risoluzione
       * **Programmazione Logica**
         - Programmazione Lineare
         - TH Completezza
         - Risoluzione di Input
         - Programmazione Logica
         - Clausole di Horn
         - Programmi Logici
         - Risoluzione SLD
         - Sostituzione di Risposta
   3. #### **Logica Fuzzy**
      * Fuzziness e Probabilità
      * **Insiemi fuzzy**
      * Funzioni di Appartenenza
      * Rappresentazioni di μ: continua/discreta
      * Variabili linguistiche
        - var.ling{ins.termini{ins.fuzzy=termine{Primario/Modificato}}}
      * Operazioni su insiemi
      * Sottoinsiemi fuzzy
      * **Modificatori**
      * Logica fuzzy
      * Neg. Cong. Disg. Impl.
4. ### **Diagrammi Binari di Decisione(BDD)**
   1. Diagrammi Binari di Decisione(BDT)
      1. Trasformazioni
   3. Grafi Diretti Aciclici(DAG)
   4. **BDD**
      1. Riduzioni
      2. BDD Ridotti
   5. BDD Ordinati
   6. **OBDD** ^cfdfb8
      1. Rappresentazione Canonica
      2. ALGO. Reduce(B)
      3. Restrizione _$f[0/x] \|\| f[1/x]$_
      4. Espansione di Shannon _$f \equiv \bar{x} * f[0/x] + x*f[1/x]$_
      5. ALGO. _$Apply(op,B_f, B_g)$_
         - _$f op g = \bar{x} * (f[0/x] op g[0/x]) + x*(f[1/x] op g[1/x])$_
      6. ALGO. Restrict
5. ### **Verifica Programmi**
   1. Stato _σ_
   2. Valori Espressioni _$Eσ$_
   3. _$σ \vDash P$_
   4. Triple di Hoare [P] C [Q]
      1. Correttezza Parziale: _$\vDash_{par}[P]C[Q]$_
      2. Correttezza Totale: _$\vDash_{tot}[P]C[Q]$_
   5. Variabili: Programma/Logiche
   6. Stato con Var: _$σ=(Var \vee FV(P) \vee FV(Q)) \rightarrow Z$_
   7. **Calcolo Corretezza Parziale**
      1. Weakest Precondition: _$[R]C[Q]: R \Rightarrow wp(C,Q)$_
      2. Comando vuoto: _$wp(skip, Q) = Q$_
      3. Assegnamento _$wp(x:= E,Q)= Q\{E/x\}$_
      4. Sequenza: _$wp(C_1; C_2,Q) = wp(C_1; wp(C_2,Q))$_
      5. Condizionale: _$wp(if \space B \space \{C\} \space else \space \{C'\},Q)=(B \Rightarrow wp(C,Q)) \cup (\sim B \Rightarrow wp(C',Q))$_
      6. While: _$wp(while \space B \space \{C\}, Q)= I$_
      7. Iterativo Parziale
         1. Invariante
   8. **Calcolo Correttezza Totale**
      1. Iterativo Totale: _$wp(while \space B \space {C}, Q) = I \space ∧ \space E≥0$_
6. ### **[CalcoloComplessità](#calcolo-complessità)**

<a name="concetti-base"></a>
# Concetti base
## Introduzione
Type of logic:
  - Linguistic logic
  - Fisolofy Logic
  - Math Logic

#### Linguistic Logic
**Possible trategy**: Reductio ad absurdum.
**Retorical Abuse**: Sentencies seems correct but it doesn't.
Exemple:
  - Congiunction
  - Disgiunction
  - Negation
  - Implicity
  - Quantificator

#### Filosofic
**Paradox** -> "contro opinione corrente"
When a sentences is equally **not true** and **not false**.

#### Math
Dimostration.
  - **Enunciati**: Simple statement
  - **Theorem**: statement that have a demostration

ps: **Dicotomia**: Suddivisione infinitesimale

#### Denotation
- **Name**: Linguistic expression that denote some entity
- **Name Sense**: How many true have the name
- **Substitution**: The _denotation_ is invariant for substitution
  - The _sense_ is not inviariant for substitution

<a name="enunciati"></a>
#### Enunciate
Type:
  - Interrogative
  - Imperatives
  - Declarative

In this course we use only _Declarative enunciate_.
**Atomic enunciate**: A sinple enunciate(or atomic) is when thet do not contains any other enunciate.<br>
**Compound enunciate**: A enunciate is composed into more enunciates.<br>

<a name="principi"></a>
#### Principi
  - **Bivalenza**: Ogni enunciato assume solo un valore di verità, che può essere _vero_ oppure _falso_
  - **Estensionalità**: Il valore degli enunciati composti dipende solo dal valore di verità degli enunciati che li compongono

<a name="logica-proposizionale"></a>
## Propositional Logic
### Components
#### Proposition
In this type of logic we call _enunciate -> proposition_.
A proposition is an enunciate that can is:
  - **Atomica**
  - **Composta** with connec: _$\sim , \vee , \wedge, \Rightarrow$_

#### Conectives:
They are **extensional**: It means that, the value of the subproposition connected by a connective, release the value about the main sentences.<br>
Connective **not extensional**: We will not consider this specific type of connective.

<a name="logica-proposizionale-sintassi"></a>
### Syntax
Atomic proposition: A, B, C<br>
Componed proposition: P, Q<br>
Logic connective: not, and, or....<br>
Alfabeto:
  - Simboli atomici/lettere enunciative: _$A,B,C...$_
  - Connettivi logici: _$\sim , \vee , \wedge, \Rightarrow$_
  - Simboli ausiliari: _$(,)$_

The **syntax** specify _how_ we can _combine_ this symbol.<br>

<a name="logica-proposizionale-fbf"></a>
**Formule ben formate(_fbf_)**: Sono le formule corrette del linguaggio; vengono definite in modo ricorsivo:
  - _Enunciates letter and $T,F$ are f.b.f_
  - _$P$ is f.b.f also $(\sim P)$ is f.b.f_
  - _if $P,Q$ are f.b.f, then $(P \wedge Q),(P \vee Q), (P \Rightarrow Q)$ are f.b.f_
  - _Anything else is a fbf_

**Precedence of connectives**: not, and, or , =>.<br>
**Subformulas(_Stfm( P)_)**:
  - if $P$ is enunciative letter about $F$ or $T$: $Stfm(P) = {P}$
  - if $P$ is $(\sim Q): Stfm(P)={P} \cup Stfm(Q)$
  - _if P are $(P_1 \wedge P_2),(P_1 \vee P_2), (P_1 \Rightarrow P_2)$ are f.b.f_

The Subformulas can be calculated by _three of structure_.
The **tree of structure** have:
  - with _root_, the _**last** connective_
  - with _leaves_ the _enunciative letter_
  - with _internal nodes_ there are the _connectives_

**E.q.**
_~(A ^ B) => (A => B v A)_.
![AlberoStruttura](./Immagini/AlberoStruttura.png)

<a name="induzione-strutturale"></a>
#### Induzione Strutturale
The f.b.f are defined in _recursive_ method.<br>
For demostrating the f.b.f propriety's we will use the _inductional structure_.<br>
**Theorem**: if $Z$ is a propriety and
  - _$Z$_ vale per tutte le lettere enunciative e per _$T,F$_
  - and if _$Z$_ holds for _$P$_ and _$Q$_, then it can be shown that _$Z$_ also holds for _$(P \wedge Q),(P \vee Q), (P \Rightarrow Q)$_
  - then _$Z$_ holds fot each fbf

**That allow them to not demostrate all the possible formulas**.<br>
We have 5 possible case: we have to demostrate that the proprety holds for _all possible base connectives_.

Information we have to know before demostrating theorems:
  1. The Hypothesis Injuction is what we also known
  2. The Thesis is what we are looking for

<a name="logica-proposizionale-semantica"></a>
### Semantics
**Truth value**:
  - 1 true
  - 0 false
**Semantic function**: _$fbf -> {0,1}$_<br>
The **semantic function** are called **interpretation**.
   - $v(T)=1 ; v(F)=0$
   - $v(A)=1 \| v(A)=0$ (A can be true o false)

#### Negation
_$v(~P) = 1 - v( P)$_

P | ~P |
--|----|
0 | 1 |
1 | 0 |

#### Conjunction
**P $\wedge$ Q is true iff P is true and Q is true**.<br>
_$v(P \wedge Q) = 1$ **<-->** $v( P)=1 and v(Q)=1$._<br>
_$v(P \wedge Q) = min(v( P), v(Q))$_<br>

P | Q | P $\wedge$ Q |
--|---|------------|
0 | 0 | 0 |
0 | 1 | 0 |
1 | 0 | 0 |
1 | 1 | 1 |

#### Disjunction
**P $\vee$ Q is true iff P is true or Q is true**.<br>
_$v(P \vee Q) = 1$ **<-->** $v( P)=1$ **or** $v(Q)=1$._<br>
_$v(P \vee Q) = max(v( P), v(Q))$_<br>

P | Q | P $\vee$ Q |
--|---|------------|
0 | 0 | 0 |
0 | 1 | 1 |
1 | 0 | 1 |
1 | 1 | 1 |

#### Implication
A false premise implies any preposition.<br>
_$v(p \Rightarrow Q) = 0$ **iff** $v( P) = 1$ **and** $v(Q) = 0$._<br>
_$v(P \Rightarrow Q) = 1$ **iff** $v( P) = 0$ **OR** $v(Q) = 1$._<br>
_**! $v( P=>Q) = 1$ <--> $v(~P \vee Q) = 1$**._<br>
_**! $v( P=>Q) = 1$ <--> $v( P) <= v(Q)$**._<br>

P | Q | P -> Q |
--|---|--------|
0 | 0 | 1 |
0 | 1 | 1 |
1 | 0 | 0 |
1 | 1 | 1 |

### Interpretation
Fix an **interpretation** _$v:fbf -> {0,1}$_ means:
  - To attribute $0 \rightarrow F$ and $1 \rightarrow T$
  - To attribute a truth value (0 or 1) at each enunciatives letter
  - Attribuire il valore di verità $A, \sim A, A \wedge B, A \vee B, A \Rightarrow B$ seguendo le regole delle loro tabole di verità.

The function **$v:fbf \rightarrow {0,1}$** is an interpretation if:
  - _$v(\sim P) = 1-v(P)$_
  - _$v(T) = 1 \wedge v(F)=0$_
  - _$v(P \wedge Q)=min(v(P), v(Q))$_
  - _$v(P \vee Q)=max(v(P), v(Q))$_
  - _$v(P \Rightarrow Q)=max(1-v(P), v(Q))$_

**The interpretation of a preposition depends exclusively on the interpretation of the atomic prepositions that compose it.**<br>

<a name="logica-proposizionale-soddisfacibilità"></a>
#### fbf. Soddisfacibile(satisfiable)
  - A fbf says '_soddisfacibile_' iff exist at least one interpretation $v$ such that _$v(P)=1$_
  - An interpretation $v$ that '_soddisfa_' $P$ it calls **Model of P** (_$v \vDash P$_)

<a name="logica-proposizionale-soddisfacibilità"></a>
#### Tautologies
An fbf for wich **every** interpretation is a Model it says **tautology** and you write it _$\vDash P$_.

<a name="logica-proposizionale-insoddisfacibilità"></a>
#### Unsatisfactory(insoddisfacibile)
An fbf for wich every interpretation is **NOT** a Model it says **unsatisfactory**.<br>

In general, the nunber of preposition is $2^n$.<br>
**unsatisfactory = ~tautoligies**

<a name="logica-proposizionale-insieme"></a>
#### Insieme(set)
**The concept**: _model, unsatisfactory, tautoligies_  can they **extend** in an _insieme_ $\ulcorner$.
  - A **model** for $\ulcorner$ is an **interpretation _v_** that is a model for **each fbf** about $\ulcorner$
  - **$\ulcorner$** is **satisfactory** if admit a model
  - **$\ulcorner$** is **unsatisfactory** if no interpretation is a model for $\ulcorner$

<a name="logica-proposizionale-conseguenza-semantica"></a>
#### ! Semantics Consequence
_A fbf $P$ is **semantic consequence** about a insieme $\ulcorner$ of fbf and you write it **$\ulcorner \vDash P$**, if every model of $\ulcorner$  is a model for $P$_.<br>
In particular **P** is **semantic conseguence** of **Q** if every model of **Q is a model for P**.

<a name="logica-proposizionale-deduzione-semantica"></a>
#### Semantic Deduction
**Theorem**:  _$\ulcorner \cup {P} \vDash Q$   **iff**   $\ulcorner \vDash (P \Rightarrow Q)$_.<br>
**Corollary**: _$P \vDash Q$  **iff**  $\vDash (P \Rightarrow Q)$_.
  - This corollary says that for demostrating **$P \vDash Q$** is just enough demostrating that **$(P \Rightarrow Q)$ is a tautology**!

<a name="logica-proposizionale-conseguenza-semantica-insoddisfacibilità"></a>
#### Semantic conseguence and unsatisfiable
**Theorem**: _$\ulcorner \vDash$P **iff** $\ulcorner \cup {\sim P}$ is unsatisfiable_.

<a name="logica-proposizionale-compattezza"></a>
#### Compactness
**Theorem**:  A set(insieme) $\ulcorner$ about fbf is satisfied iff each subset $\triangle$ finished is satisfiable.

<a name="logica-proposizionale-equivalenza-semantica"></a>
#### Semantic Equivalence
A formula P is **semantically equivalent** to Q(**P $\equiv$ Q**) if all and only P models are Q models.<br>
**In other words**: if _P is a semantically conseguence of Q_ and _Q is a semantically conseguence of P_.

<a name="logica-proposizionale-connettivi-derivabili"></a>
#### Conettivi derivabili
Un connettivo è semanticamente derivabile se è possibile definirlo in funzione di altri connettivi.

<a name="logica-proposizionale-compattezza-funzionale"></a>
#### Compattezza funzionale
Un insieme di connettivi logici si didce **funzionalmente completo** se per ogni funzione $f:{0,1}^n \rightarrow {0,1}$ esiste una funzione fbf P costituita mediante questi e tale che $f_P=f$.<br>
Ovvero un insieme di connettivi è competo se ogni altro connettivo può essere derivato da essi.

ps: Una formula si definisce **normale** se non è più possibile semplificarla sostutuendoci altre formule.

<a name="sistemi-deduttivi"></a>
## Sistemi Deduttivi
Proprietà dei sistemi deduttivi:
  - **Correttezza**: Il sistema deduttivo non inferisce proposizioni non valide
  - **Completezza**: Ogni formula valida è dimostrabile con il sistema deduttivo

<a name="deduzione-naturale"></a>
### Deduzione naturale
**Notazione**:  $\frac{Premesse}{Conclusioni}$ <br>
Due tipi di regole:
  - Regole elementari
  - Regole Condizionali

**Regole congiunzione**:

|$\wedge$ e.1| $\wedge$ e-2| $\wedge$ i|
|-|-|-|
|$\frac{P \wedge Q}{P}$ | $\frac{P \wedge Q}{Q}$ | $\frac{P \space \space Q}{P \wedge Q}$ |

**Regole disgiunzione**:

|$\vee$ i.1|$\vee$ 1.2| $\vee$ e|
|-|-|-|
|$\frac{P}{P \vee Q}$ | $\frac{Q}{P \vee Q}$ | $\frac{P \vee Q \space \frac{[P]}{R} \space \frac{[Q]}{R}}{R}$|

**Regole implication**:

|$\Rightarrow$e|$\Rightarrow$i|
|-|-|
|$\frac{P \space P \Rightarrow Q}{Q}$ | $\frac{\frac{[P]}{Q}}{P \Rightarrow Q}$ |

**Regole negazione**:

|$\sim$e|$\sim$i|Fe|
|-------|-------|--|
|$\frac{P \space \space \sim P}{F}$ | $\frac{\frac{[P]}{F}}{\sim P}$ | $\frac{F}{P}$ |

**Regole: RAA -> $\frac{\frac{[\sim P]}{F}}{P}$**

<a name="calcolo-sequenti"></a>
### Calcolo sequenti
**Γ ⊢ ∆** is a sequent.<br>
**Γ** and **∆** are sets of **f.b.f**.<br>
The formulas **Γ** must be thought of as joined by connective **$\wedge$**.<br>
**Forma regola di inferenza**:
  - **$\frac{Γ_1 ⊢ ∆_1}{Γ_2 ⊢ ∆_2}$**

  - **$\frac{Γ_1 ⊢ ∆_1 \space \space Γ_2 ⊢ ∆_2}{Γ_3 ⊢ ∆_3}$**

**Axiom**: A⊢A

<a name="calcolo-sequenti-regole-strutturali"></a>
#### Structural Rules
|perm-l|perm-r|
|-|-|
|$\frac{Γ, P, Q, Γ’ \space ⊢ \space ∆}{Γ, Q, P, Γ’ \space ⊢ \space ∆}$ | $\frac{Γ \space ⊢ \space ∆, P, Q, ∆’}{Γ \space ⊢ \space ∆, Q, P, ∆’}$ |

|**indeb-l**|**indeb-r**|
|$\frac{Γ ⊢ ∆}{Γ, P \space ⊢ \space ∆}$ | $\frac{Γ ⊢ ∆}{Γ \space ⊢ \space ∆,P}$ |

<a name="calcolo-sequenti-regole-logiche"></a>
#### Logic Rules
**AND**<br>

|$\wedge$-l|$\wedge$-r|
|-|-|
|$\frac{Γ, P, Q \space ⊢ ∆}{Γ, P ∧ Q\space  ⊢ ∆}$ | $\frac{Γ \space ⊢ P, ∆ \space \space \space \space Γ \space ⊢ \space Q, ∆}{Γ \space ⊢ P ∧ Q, ∆}$ |

**OR**<br>

|$\vee$-l|$\vee$-r|
|-|-|
|$\frac{Γ, P \space ⊢ \space ∆ \space \space \space \space Γ, Q \space ⊢ \space ∆}{Γ, P ∨ Q \space ⊢ \space ∆}$ | $\frac{Γ \space ⊢ P, Q, ∆}{Γ \space ⊢ P ∨ Q, ∆}$ |

**NOT**<br>

|$\sim$-l|$\sim$-r|
|-|-|
|$\frac{Γ \space ⊢ P, ∆}{Γ, ∼P \space ⊢ \space ∆}$ | $\frac{Γ, P \space ⊢ \space ∆}{Γ \space ⊢ \space ∼P, ∆}$ |

**IMPLICATION**<br>
Se ci si ricorda che l' $\Rightarrow$ non è nient'altro che $\sim P \vee Q$, fa formula vien da sola.
|$\Rightarrow$-l|$\Rightarrow$-r|
|-|-|
|$\frac{Γ \space ⊢ \space P , ∆ \space\space\space\space Γ, Q \space ⊢  \space ∆}{Γ, P \Rightarrow Q \space ⊢ \space ∆}$ | $\frac{Γ,  P \space ⊢ Q, ∆}{Γ \space ⊢ \space P \Rightarrow Q, ∆}$ |

<a name="calcolo-sequenti-ricerca-contromodelli"></a>
#### Ricerca contromodelli
Con questo calcolo possiamo anche dimostrare che una consegenza semantica è falsa, basta dimostrare che non esista un modello dell'insieme che non sia modello per P. <br> Tale interpretazinoe è detta **contromodello**

<a name="calcolo-sequenti-invertibilità"></a>
#### Invertibilità
Dimostrazione **automatica**; sistema di prova **costruttivo**; Se esiste una dimostrazione, questa si può trovare partendo da una qualsiasi scelta della formula principale su cui lavorare.

<a name="calcolo-sequenti-teorema-correttezza"></a>
#### Teorema correttezza
Se _$Γ ⊢_S ∆$_ allora _$Γ \vDash ∆$_ (se ∆ è derivabile da Γ allora ∆ è soddisfatto in Γ)

<a name="calcolo-sequenti-teorema-completezza"></a>
#### Teorema completezza
Se _$Γ \vDash ∆$_ allora _$Γ ⊢_S ∆$_ (se ∆ è soddisfatto in Γ allora ∆ è derivabile da Γ)

<a name="calcolo-sequenti-teorema-completezza-finita"></a>
#### Teorema completezza Finita
Sia Γ un insieme finito di fbf, se _$Γ \vDash ∆$_ allora _$Γ ⊢_S ∆$_

<a name="calcolo-sequenti-teorema-completezza-forte"></a>
#### Teorema completezza Forte
Se _$Γ \vDash ∆$_ allora _$Γ ⊢_S ∆$_

<a name="logica-proposizionale-risoluzione"></a>
### Risoluzione Logica Proposizionale(?)
**Refutazione**: Per dimostrare che $P$ è valida si dimostra che _la negazione di $P$_ è insoddisfacibile.<br>
**Clausola**
  - Clausola: Disgiunzione di 0 o + letterali
  - Clausola **vuota**: Non contiene leterali
  - Clausola **soddisfatta**: Se ha almeno un letterale vero
  - Clausola vuota($□$) = **$F$**
  - Clausola **tautologia**: letterale + suo negato
  - Clausola vuota **$\{\} = T$**

Le clausole sono rappresentate come **insiemi**.<br>
**Trasformazione** $P$ in $P^c$:
  1. $P$ trasformata in **FNC**
  2. Ogni fattore(clausola) rappr. come insieme
  3. **□=F** , **{}=T**

<a name="logica-proposizionale-risolvente"></a>
**Risolvente $R$**: Insieme degli elementi che compaiono normali in un insieme e negati nell'altro:
  * $l \in C_1$ **e** $\sim l \in C_2$ **allora** $R=(C_1 - \{l\}) \cup (C_2 - \{\sim l\})$

**Definizione tecnica Risolvente**: La clausola $R$ è risolvente delle clausole _$C_1,C_2$_ sse sono verificate le seguenti condizioni:
  * Siano $s_1,s_2$ due sostituzioni che, se applicate a $C_1,C_2$, ne ridenominano le variabili in modo che $C_1s_1,C_2s_2$ non abbiano variabili in comune
  * Dati due insiemi di letterali _$\{l_1,...,l_n\} \in C_1$ e $\{l'_1,...,l'_m\} \in C_2$_ con _$n,m>0$_ t.c. l'insieme _$L=\{\sim l_1,..., \sim l_m, l'_1,...,l'_m\}$_ sia unificabile tramite l'unificatore _$\sigma$_
  * $R$ ha così la forma: _$R=(C_1-\{l_1,...,l_n\} \cup C_2-\{l'_1,...,l'_m\})\sigma$_

<a name="logica-proposizionale-derivazione"></a>
**Derivazione**: Sia S un insieme di clausole, una derivazione per risoluzione di $S_1$ da $S$ è una sequenza $C_1,...,C_m$ di clausole tali che:
  * $C_m = S$
  * $C_i, \forall i \in \{1,2,...,m\}$, è o:
    - Una clausola in $S$
    - Un risolvente di due clausole $C_j$ e $C_k$ con $j,k < i$

<a name="logica-proposizionale-refutazione"></a>
**Refutazione**: Derivazione di □ a partire da S.<br>
<a name="logica-proposizionale-lemma-risoluzione"></a>
**Lemma di Risoluzione**: Siano $C_1$ e $C_2$ clausole e R un loro **risolvente**, allora R è **conseguenza semantica** di $C_1$ e $C_2$<br>
**Teorema Risolzione**: Un insieme id clausole $S$ è insoddisfacibile sse _$S ⊢_R □$_<br>
> **Corollario**: $S \vDash P$ **sse** $S \cup \{\sim P\} ⊢_R □$

**Algoritmo risoluzione**:
  1. Scriviamo $S$ e $\sim P$ in FNC
  2. Trasformiamo le FNC negli insiemi di clausole $S^c$ e $(\sim P)^c$
  3. Troviamo una refutazione di _$S^c \cup (\sim P)^c$_

---

<a name="calcolo-complessità"></a>
# Calcolo Complessità
Calcolabilità:
  - **Problemi decidibili**: Risolvibili per via algoritmica
  - **Problemi non decidibili**: Non risolvibili per via algoritmica

Il problema della fermata non è decidibile.<br>
I problemi decidibili a loro volta possono essere classificati come:
  - **Problemi trattabili**: Hanno una soluzione algoritmica efficiente
  - **Problemi non trattabili**: Non hanno una soluzione algoritmica efficiente

### Classi di complessità
Problemi decisionali: Insieme di problemi che hanno come soluzione o _"si"_ o _"no"_<br>
  * **P** : Classe di problemi decisionali che possono essere risolti con un algoritmo **polinomiale**
  * **NP**: Classe di problemi decisionali che possono essere risolti con un algoritmo _non deterministico_ in tempo **polinomiale**
    - **Algo Deterministico**: In un passo può fare un'unica azione
    - **Algo Non Deterministico**: In un passo si possono fare più azioni contemporaneamente
    In modo equivalente, NP è la classe dei problemi decisionali che possono avere un tempo di risoluzione maggiore di quello polinomiale(utilizzando algo deterministico) ma il risultato può comunque essere valutato in tempo polinomiale.<br>
  * **NP-Completi**(per gli amici, ER FECCIA): Sono i problemi più difficili della classe NP

---
<a name="logica-primordine"></a>
# Logica Primordine / Logica Predicati
Tramite il calcolo preposizionale non è possibile esprimere la nozione di _Generalità_<br>
**Quantificatori**: Esistenziale + Universale<br>
**Insieme TER**:
  - Ogni costante appartiene a TER
  - Ogni variabile appartiene a TER
  - Se **$t_1,t_2,...,t_n \in TER$** e **f** è un simbolo di funzione n-ario, allora: **$f(t_1,t_2,...,t_n) \in TER$**
  - Nient'altro appartiene a TER

**FBF**:
  - F e T sono fbf
  - Se **$t_1,t_2,...,t_n \in TER$** e **A** è un simbolo di predicato n-ario, allora: **$A(t_1,t_2,...,t_n) \in FBF$**
  - Se P è una fbf, anche (~P) è fbf
  - Stessa cosa con not and, or, implica
  - Se P è fbf allora anche **$(\forall x)P$** e **$(\exists x)P$** sono fbf
  - Nient'altro è una fbf


**Scope**: Il campo di azione di un quantificatore è la fbf immediatamente alla sua destra, ovvero è l'espressione su cui il quantificatore ha effetto <br>
  - Una variabile che  è nel campo di azione di un quantificatore è detta **legata**, atrimenti **libera**.

**Variabili libere in TER**:
  - Sia $t \in TER$: L'insieme $FV(t)$ delle variabili libere in $t$ è così definito:
    - $FV(x)={x}, x$ variabile
    - $FV(a)={}$, costante
    - $FV(f(t_1,...,t_n)) = FV(t_1) \cup ... \cup FV(t_n)$ con funzione f n-aria
  - Per ogni fbf $P$ l'insieme delle variabili libere di $P$ è così definito:
    - $FV(F)=FV(T)={}$
    - $FV(a(t_1,...,t_n)) = FV(t_1) \cup ... \cup FV(t_n)$
    - $FV(~P)=FV(P )$
    - $FV(P_1 ∧ P_2) = FV(P_1 \vee P_2) = FV(P_1 ⇒ P_2) = FV(P_1) \cup FV(P_2)$
    - $FV(\forall x P) = FV(\exists x P) = FV(P)-\{x\}$
  - E' importante posizionare correttamente i quantificatori nella formula

**Ridenominazione**:
  * I nomi di variabili quantificate ($\forall x, \exists x$) hanno il ruolo di parametri formali
  * In $\forall x P$ e $\exists x P$ possiamo cambiare x in y senza modificarne il significato
  * Il nuovo nome y non deve comparire nella formula P

> La sostituzione si applica solo alle variabili libere.<br>

**Struttura**: Una struttura è una coppia _$S=(D,I)$_ dove _$D$_ è un insieme non vuoto detto dominio e _$I$_ è un assegnamento che associa:
  * Ad ogni costante un elemento _$I(c) \in D$_
  * Ad ogni funzione f di arità k>0 una funzione: _$I(f): D^k \rightarrow D$_
  * Ad ogni predicato A di arità k>0 una funzione: _$l(A): D^k \rightarrow \{0,1\}$_
  * Notazione
    - $c^S = I(c)$
    - $f^S = I(f)$
    - $B^S = I(B)$
  * Osservazione
    - Non si può interpretare una fbf contenente variabili libere
    - Si assegnano ad esse degli elementi di D
    - Il valore di verità di una fbf dipende dall'assegnazione delle variabili libere

**Ambiente**:
  * Un ambiente per S è la funzione _$\xi^S: VAR \rightarrow D$_
  * L'insieme di tutti i possibili ambienti è _$ENV_S = \{\xi^S \| \xi^S:VAR \rightarrow D\}$_
  * Siano $d \in D$ e $x \in VAR, \xi^S[d/x]$ è l'ambiente così definito:
    - se _$y \neq x$ allora  $\xi^S[d/x](y) = \xi^S(y)$_
    - se _$y=x$ allora $\xi^S[d/x](y) = d$_

**Semantica**: <br>
Un'interpretazione di un linguaggio proposizionale _L_ è una coppia $(S,\xi^S)$ con S struttura e $\xi^S$ ambiente per S<br>
L'interpretazione ci consente di dare significato alle fbf <br>

**Interpretazione valore TER**<br>
Sia P una fbf e $(S,\xi)$ un'interpretazione. Per ogni termine t in P il suo valore $(S,\xi^S)$ è denotato dalla funzione ${[]}_{S,\xi}: TER \rightarrow D$
  - se t è una variabile x allora $[t]_{S,\xi} = \xi(x)$
  - se t costante c allora $[t]_{S,\xi} = c^S$
  - se t funzione $f(t_1,...,t_n)$ allora $[t]_{S,\xi} = f^S([t_1]_{S,\xi},...,[t_n]_{S,\xi})$

**Funzione di valutazione**<br>
Sia P una fbf e $(S,\xi)$ un'interpretazione. La funzione di valutazione $v^{(S,\xi)}:FBF \rightarrow \{0,1\}$
  - $v^{(S,\xi)}(F) = 0$ e $v^{(S,\xi)}(T) = 1$
  - $v^{(S,\xi)}(A(t_1,...,t_n)) = A^S([t_1]_{S,\xi},...,[t_n]_{S,\xi})$
  - $v^{(S,\xi)}(~P) = 1- v^{(S, \xi)}(P)$
  - I restanti sono i soliti
  - $v^{(S,\xi)}(\forall x P_1) = min\{v^{(S,\xi[a/x])}(P_1) \| a \in D \}$
  - $v^{(S,\xi)}(\exists x P_1) = max\{v^{(S,\xi[a/x])}(P_1) \| a \in D \}$

Conseguenza Semantica
Dati un insieme di fbf Γ e una fbf P, diremo che P è una conseguenza semantica di Γ(Γ ⊨ P) se per ogni struttura S e ogni ambiente $\xi^S$ tali che
  - Per ogni $Q \in Γ$ si ha che $(S,\xi^S) ⊨ Q$
  - Si ha anche che $(S,\xi^S) ⊨ Q$

Proprietà:
  - P è valida sse ~P è insoddisfacibile
  - P è soddisfacibile sse ~P non è valida
  - Γ⊨P sse Γ∪{∼P} è insoddisfacibile
  - P non è valida
    - è Equivalente a dire ~P soddisfacibile
    - NON è equivalente a dire che P è insoddisfacibile ovvero che ~P è valida

**Equivalenza semantica**
Due fbf P e Q sono semanticamente quivalenti $(P \equiv Q)$ se per tutte le interpretazioni $(S,\xi^S)$ di P e Q si ha: $v^{(S,\xi)}(P) = v^{(S,\xi)}(Q)$<br>
Due fbf P e Q sono quivalenti sse: $\models P \Leftrightarrow Q$

<a name="calcolo-predicativo"></a>
## Calcolo predicativo
<a name="calcolo-predicativo-deduzione-naturale"></a>
### Deduzione Naturale
**Quantificatore Universale** <br>

| $\forall$ i | $\forall$ e |
|-|-|
|$\frac{P[y/x]}{\forall x P}$ | $\frac{\forall x P}{P[t/x]}$ |
| _$y$_ non compare libera nelle foglie derivate da _$P[y/x]$_ | _$t$_ termine qualsiasi |

**Quantificatore Esistenziale**
|$\exists$ i| $\exists$ e|
|-|-|
|$\frac{P[t/x]}{\exists x P}$ | **$\frac{\exists x P \space \frac{[P[y/x]]}{Q}}{Q}$** |
| _$t$_ termine qualsiasi | _$y$_ non compare libera nelel foglie derivate da _$P[y/x]$_ |

<a name="calcolo-predicativo-calcolo-sequenti"></a>
### Calcolo Sequenti
**Quantificatore Universale**

|_$\forall$-l_|**$\forall$-r**|
|-|-|
|$\frac{Γ,\forall x P, P[t/x] \space ⊢ ∆}{Γ, \forall x P \space ⊢ ∆}$ | $\frac{Γ \space ⊢ P[y/x], ∆}{Γ \space ⊢ \forall x P, ∆}$ |

**Quantificatore Esistenziale**

|**$\exists$-l**|_$\exists$-r_|
|-|-|
|$\frac{Γ, P[y/x] \space ⊢ ∆}{Γ, \exists x P \space ⊢ ∆}$ | $\frac{Γ \space ⊢ P[t/x], \exists x P, ∆}{Γ \space ⊢ \exists x P, ∆}$ |

**IMPORTANTISSIMO**:
  - Nelle regole **$\exists -l$ e $\forall -r$**: La variabile _$y$_ deve essere **_NUOVA_**(non esistente nella formula)
  - Nelle regole _$\exists -r$ e $\forall -l$_: Il temine _$t$_ deve essere scelto tra quelli **_VECCHI_** se ce ne sono, altrimenti ne prendiamo uno nuovo(ad esempio una variabile nuova)
    - Non si scelgono variabili legate
    - Si scelgono solo variabili libere e gli altri termini
  - Nelle regole _$\exists -r$ e $\forall -l$_: C'è la _ricopiatura della formula quantificata_, questo rende i sequenti reversibili ma il calcolo può rivelarsi infinito!

#### Sostituzione
Sia **$\sigma=\{t_1/x_1,...,t_n/x_n\}$** una sostituzione ed **$E$** un'espressione. **$E \sigma$** è l'applicazione di **$\sigma$** a **$E$** ottenuta cambiando ogni occorrenza della variabile **$x_i$** con il termine **$t_i$**

#### Unificatore
Una sostituzione _$\sigma$_ si dice unificatore di un insieme _$E=\{E_1,...,E_n\}$_ di espressioni se _$E_1 \sigma = E_2 \sigma = E_n \sigma$_<br>
Se esiste una unificazione _$\sigma$_ di _$E, E$_ si dice **unificabile**

#### MGU
Un unificatore _$\sigma$_ per un insieme _$E=\{E_1,...,E_n\}$_ di espressioni è detto **unificatore più generale(mgu)** sse per ogni altro unificatore _$\vartheta$_ dello stesso insieme esiste una sostituzione _$p$_ t.c. **$\vartheta = \sigma \circ \rho$**

#### Algoritmo di unificazione
$k=0; σ_k = ε;$<br>
**repeat**<br>
**if** _$(\|E_{σ_k} \| == 1)$_<br>
  - **then**: output $σ_k$; stop;<br>
  - **else**: trova $D(E_{σ_k})$<br>

**if** _$(\exists x,t \in D(E_{σ_k}) \| x=var \notin T)$_<br>
  - **then**: $σ_{k+1}= σ_k \circ \{t/x\}$; k++;<br>
  - **else**: output "E non è unificabile"; stop;<br>

**until()**;

## Programmazione logica
#### Risoluzione lineare
Una prova per risoluzione lineare di _$C$_ da un insieme di clausole _$S$_ è una sequenza di _$C_1,...,C_n$_ tale che:
  - $C_1 \in S$
  - $C_n = C$
  - $\forall i=2,...,n$ risulta:
    - $C_i$ è la risolvente di $B_{i-1} \in S$ o $B_{i-1} = C_j$ con $j<i$

#### TH Completezza
Se un insieme di clausole S è insoddisfacibile, allora la clausola vuota è derivabile per risoluzione lineare

#### Risoluzione d input
Una prova per risoluzione lineare da input di _$C$_ da un insieme di clausole _$S$_, è una sequenza _$C_1,...,C_n$_ tale che _$C_n = C$_ e, ad ogni passo, una delle due clausole risolventi è una istanza di un elemento di _$S$_.

La refutazione lineare da input è:
  - Particolarmente efficiente
  - Ma non _completa per refutazione_

MA se ci restringiamo alle clausole di horn la risoluzione da input diventa completa per refutazione

#### Clausole di Horn
Una clausola di Horn è una clausola che contiene al più una formula atomica **positiva**.
  * **Clausola Horn definita**: _$\{A_0, \sim A_1,...,\sim A_n\}$_
    - $A_0:- A_1,..., A_n$
  * **Clausola Goal**: _$\{\sim A_0, \sim A_1,...,\sim A_n\}$_
    - $?:- A_1,..., A_n$

**Programma logico**: è un isnieme finito di clausole definite<br>
Una **prova per risoluzione SLD** è una derivazione per risoluzione lineare di input che:
  - Ogni risolvente laterale è una clausola di Horn definita
  - Ogni altro risolvente è una clausola goal

La **risoluzione SLD** è completa per clausole di Horn<br>
Una **refutazione SLD** è una prova per risoluzione SLD nella quale l'ultimo risolvente è la clausola vuota<br>

#### Sostituzione di Risposta
Siano un prograsmma logico $P$ e un goal $G$. La sostituzione di risposta per **$P \cup \{G\}$** è la composizione:
  - _$\theta=\theta_0 \circ ... \circ \theta_n$_ delle sostituzioni _mgu_ della risoluzoine LSD di _$P \cup \{G\}$_
  - **Ristretta alle sole variabili di $G$**

#### Alberi SLD
Fissata una regola di selezione(_leftmost/rightmost_), sia _$P$_ un programma logico e _$G$_ una clausola goal. **L'albero SLD** di _$P \cup \{G\}$_ è un albero tale che:
  - La radice contiene $G$
  - Ogni altro nodo contiene una clausola $C_i$ che è la risolvente di $C_j$ con una clausola $P$. Dove $C_j$ è la clausola contenuta dal nodo padre $C_i$

## Esercizi esempi paradossi
**Esercizio 1**. (Esame del 10 Aprile 2008)
  1. Definire il concetto di paradosso.
  2. Descrivere in dettaglio un esempio di paradosso.
  3. Determinare se la seguente frase è vera, falsa oppure è un paradosso.

Giusti-ficare la risposta: _“Io dico sempre il falso.”_ <br>
**Soluzione** (proposta da Andrea Nardelli):
  1. Paradosso indica qualcosa “che va contro il senso comune”; una dimostrazione
che giunge a conclusioni che risultano contraddittorie.
Più semplicemente è un’affermazione che non è né vera né falsa.
  2. _“La frase seguente è falsa. La frase precedente è vera.”_<br>
  - Assumo che la frase sia vera
    - Se fosse vero che _“la frase seguente è falsa”_ vuol dire che _“la frase precedente”_ non è vera, e questo porterebbe ad un ciclo senza soluzione ossia assurdo.
  - Assumo che la frase sia falsa
    - Il discorso è analogo al precedente se fosse falsa risulterebbe _“la frase seguente è vera, la frase precedente è falsa”_ e anche qui ci troveremmo in un ciclo senza soluzione.
  - Questo quindi è un esempio di paradosso.
  3. _“Io dico sempre il falso.”_
  - Assumo che la frase sia vera
    - Se è vero che dico sempre il falso ora sto mentendo(dicendo questa frase), quindi la frase non può essere vera altrimenti ora direi la verità.
    - Assurdo la frase non può essere vera.
  - Assumo che la frase sia falsa
    - Se non è vero che dico sempre il falso, vuol dire che _“io qualche volta non dico il falso”_ ovvero qualche volta dico la verità, quindi ora potrei dire il vero.
    - La frase quindi è falsa.
  - Questo non è un paradosso

**Esercizio 2** (Esame del 15/06/2009)
  1. Descrivere in dettaglio un esempio di paradosso.
  2. Descrivere in dettaglio un esempio di frase che non sia un paradosso.
  3. Determinare se la seguente frase è vera, falsa oppure è un paradosso.

Giustificare la risposta: _“Questa frase è falsa”_<br>

**Soluzione** (proposta da Stefano Biancardi e Guido Lena Cota)
  1. Il paradosso di Philip Jourdain è una rielaborazione di quello del mentitore formulata da Epimenide nel VI sec. a.C.<br>
  Il paradosso è formato da due frasi collegate tra loro:
    1. (a)_“La frase seguente è falsa”_
    2. (b)_“La frase precedente è vera”_
  - Supponiamo ora che la frase (a) sia vera, avremo quindi che:
    1. (a) _“La frase seguente è falsa”_
    2. (b) _“La frase precedente è falsa”_
  - Dato che _“La frase precedente”_ cui fa riferimento (b) è la (a) che abbiamo supposto vera, avremo che (a) è sia vera che falsa.<br>
  Se invece supponiamo che la frase (a) sia falsa, le due frasi diventeranno:
    1. (a) _“La frase seguente è vera”_
    2. (b) _“La frase precedente è vera”_
  - Dato che _“La frase precedente”_ cui fa riferimento (b) è la (a) che abbiamo supposto falsa, avremo ancora che (a) è sia vera che falsa.
  2. Il terzo dei paradossi di Zenone è il cosiddetto _“paradosso della freccia”_, il quale afferma che una freccia che appare in movimento in realtà è immobile.
  Ciò è spiegato con il fatto che in ognuno degli infiniti istanti che ne compongono lo spostamento, la freccia appare immobile. <br>
  Dunque la conclusione è che una somma di immobilità non può dare luogo a movimento.<br>
  Questo paradosso presuppone però un concetto di indivisibilità del tempo che in realtà non è pensabile, dal momento che è un non senso immaginare un istante non ulteriormente scomponibile in più istanti, se pur infinitamente piccoli. <br>
  Quando Zenone dice che in ogni istante la freccia appare immobile, egli trascura tutti quei sottoinsiemi che in realtà andrebbero considerati in una grandezza continua come il tempo.
  3. La frase _“Questa frase è falsa”_ è un paradosso perché:
     - supponendo che la frase sia vera, allora sosteniamo che la frase è falsa;
     - supponendo che la frase sia falsa, allora stiamo sostenendo la negazione della frase, ovvero che _“Questa frase è vera”_
  - In entrambi i casi si arriva ad una conclusione assurda, in cui la frase ècontemporaneamente vera e falsa, da cui il paradosso.

**Esercizio 3** (Esame del 21/01/2009)
  1. Definire il concetto di paradosso.
  2. Descrivere in dettaglio un esempio di paradosso.
  3. Determinare se la seguente frase è vera, falsa oppure è un paradosso.

Giustificare la risposta: _“Tutte le frasi che dico sono false”_

**Soluzione** (proposta da Marco Casazza):
  1. _Il termine paradosso, dal greco para (contro) e doxa (opinione), in- dica un’affermazione che si scontra contro l’opinione generale, la cui dimostrazione porta a conclusioni contraddittorie. Non è possibile stabilire se un paradosso sia vero o falso, perché semplicemente non è ne l’uno ne l’altro._
  2. Come esempio di paradosso si può prendere la frase _“Questa frase è falsa”_:
  - Se fosse vera: se la frase fosse vera allora starei dicendo una frase falsa.
    - Ma è assurdo che una frase sia allo stesso tempo sia vera che falsa. Possiamo quindi affermare che la frase non è vera.
  - Se fosse falsa: se fosse falsa allora la frase pronunciata dovrebbe essere vera, quindi non falsa.
    - Ma per ipotesi ho assunto fosse falsa, quindi ho falsificato le ipotesi. La frase non può essere falsa.
  - La frase _“Questa frase è falsa”_ è un paradosso.
  3. Per stabilire se la frase è vera, falsa oppure un paradosso è necessario procedere in questo modo:
  - Assumere che sia vera:
    - Se l’affermazione fosse vera io starei pronunciando una frase vera, quindi non falsa. Allora è vero che non tutte le frasi che dico sono false, cioè a volte dico frasi vere.
    - Questo però falsifica l’affermazione, che non può quindi essere vera.
  - Assumere che sia falsa:
    - Se l’affermazione fosse falsa allora è vero che io dico almeno una frase vera.
    - La frase appena pronunciata è falsa, ma ciò non vuol dire che in passato io non abbia mai pronunciato frasi vere o che non ne dica in futuro.
  - La frase _“Tutte le frasi che dico sono false”_ è falsa, quindi non è un paradosso.

## Esercizi esempi traduzioni
Cose da ricordare:
1. $\forall$ generalmente abbinato ad implicazione($\Rightarrow$)
2. $\exists$ generalmente applicato ad una congiunzione

Esempio 1. :
  - _'Tutti gli uomini sono mortali'_
  - $U(x)$ : Uomo
  - $M(x)$ : Mortale
  - $\forall x (U(x) \Rightarrow M(x))$

Esempio 2. :
  - _'Ci sono barbieri che radono se stessi'_
  - $B(x)$ : Barbiere
  - $R(x,y)$ : x rade y
  - $\exists x (B(x) \wedge R(x,x))$

Esercizio 1. :
  - _'C'è un libro non utilizzato da nessuno studente'_
  - $L(x)$ : Libro
  - $S(y)$ : Studente
  - $U(y,x)$ : Studente y utilizza libro x
  - $\exists x (L(x) \wedge \forall y(S(y) \Rightarrow \sim U(y,x)))$

Esercizio 2. :
  - _'Se Ada è più colta di Sara allora almeno un libro di Sara è stato sfogliato da tutti gli amici di Ada'_
  - $C(x,y)$ : Piu colto x di y
  - $A(y,x)$ : Amico x di y
  - $L(x)$ : Libro
  - $P(y,x)$ : Persona y possiede libro x
  - $S(y,x)$ : Persona y sfoglia libro x
  - $\exists ada \exists sara (C(ada,sara) \Rightarrow \exists libro(P(sara, libro) \wedge \forall amico (A(amico, ada) \Rightarrow S(amico,libro)) ))$
