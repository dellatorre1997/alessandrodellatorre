<!-- css -->

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

# "Bye" > **Alfa.md**; _:(){:|:);:_
Data: Giugno 2018 - Dicembre 2018 <br>

### **Descrizione:**
**_Alfa era un asocial network che mirava a ridurre l'utilizzo del telefono e a incentivare l'aggregazione delle persone al di fuori del mondo virtuale._** <br>
Il concetto base è tratto dal film 'Nerve' e prevedeva un profilo utente a cui viene assegnato un punteggio, questo può:
- Crescere svolgendo sfide **prestabilite** dagli sviluppatori
- Decrescere in modo graduale per inattività

### **Le sfide**
Le sfide sono divise per **_categoria_**(sport, volontariato, conoscenza, divertimento) e per **_difficoltà_**(1-100) e vi è un elenco predefinito e in costante aggiornamento tra quelle disponibili. Le sfide hanno dei principi fondanti quali: **_'intrattenimento'_**, **_'esperienza'_** e **_'legalità'_**, alcuni esempi di sfide possono essere:
- Leggere 2 libri in 2 giorni
- Fare 100 giorni di volontariato
- Cantare l'inno d'Italia nella piazza della tua città a mezzogiorno

Ogni utente può decidere quali sfide affrontare, più va avanti e più vengono sbloccate sfide sempre più difficili in base al livello raggiunto(sia **_generale_** che **_per categoria_**, in quanto una persona potrebbe essere bravissima nello sport ma non altrettanto brava in altre categorie). <br>
Se viene permesso agli utenti quali sfide compiere, il social diventerebbe come quello nel film portando a problemi legali non indifferenti, per questo si è deciso che solo gli amministratori possono aggiungere/aggiornare le sfide in base alle leggi vigenti nei diversi stati in modo da rispettare sempre il principio di 'legalità'. <br>
Le sfide sono strutturate in modo che ci sia uno sviluppo costante delle esperienze dell'utilizzatore portandolo a oltrepassare i propri limiti e incentivandolo a mettersi in gioco, soprattutto in campi diversi da quelli per cui è predisposto. Un utente può svolgere tutte e 100 le sfide della categoria **_'sport'_** ma, così facendo, non raggiungerà mai il livello massimo **_complessivo_** in quanto, per farlo, dovrà svolgere anche le sfide di altre categorie. <br>

### **L'applicazione**
L'applicazione offre diverse funzionalità quali:
  1. Possibilità di vedere(attraverso foto/video/audio) le sfide altrui
  2. Fare sfide personali/di gruppo
  3. Contribuire alla validazione delle sfide degli altri

Ovviamente, ognuno di questi punti fornisce delle criticità che sono state affrontate nello sviluppo architetturale della piattaforma. <br>
Come citato precedentemente, **_Alfa_** vuole essere un **_asocial network_** e quindi **non** incentivare l'utilizzo del telefonino: per fare ciò si è deciso che le funzionalità dell'applicazione variano in base al livello dell'utente. <br>Un esempio di funzionalità in base al livello potrebbe essere il seguente:
- **Livello 1**: Solo sfide personali
- **Livello 10**: Sfide di gruppo
- **Livello 40**: Vedere le sfide degli altri
- **Livello 50**: Validare le sfide fatte da altri

Il più grande problema di questo **_asocial network_** è quello della validazione delle sfide fatte dagli utenti, riassumibile nella domanda: **_Come fare a sapere se l'utente ha svolto effettivamente la sfida assegnatoli prima di dargli un punteggio?_**<br>
Risulta palese che è impossibile controllare a mano ogni sfida fatta da ogni utente e che non è possibile sviluppare un sw ad-hoc che svolga questo compito. Per ovviare a questo problema si è pensato di adottare 2 soluzioni:
1. Se un utente vuole fare le sfide per un proprio sviluppo personale(senza condividerle agli altri) può farlo senza la necessità di controllo. Questo implica 2 possibilità di utilizzo dell'applicazione differenti: una modalità **_'Personale'_** e una **_'Pubblica'_**, ognuna con punteggi diversi e con caratteristiche diverse(ad esempio, la pubblicazione delle sfide/validazione sfide altrui sarà possibile solo in modalità **_'pubblica'_**)
2. Sono gli utenti stessi a controllare la validità delle sfide fatte da altri, un pò come se fosse una blockchain in cui ogni nodo è una persona con un certo livello di fiducia(dettato dal proprio livello e dalle scelte di validazione) che sarà invogliata a dare valutazioni positive solo a chi se lo merita, dato lo sforzo fatto per arrivare al proprio livello. Questo implica che, per le persone arrivate al livello 50, comparirà la possibilità di vedere, oltre alle sfide fatte, anche le sfide non ancora validate(invisibili agli utenti con un livello inferiore). Questo garantisce che, maggiore è il flusso di persone che utilizzano l'applicazione, maggiore sarà la sua scalabilità e la sua sicurezza.

---

### **Conoscenze acquisite:**
  - **Medio-Basso**: Sviluppo applicazioni android tramite android-studio
  - **Medio-Basso**: Networking e infrastruttura di comunicazione mobile
  - **Medio**: Metodi di autenticazione e sicurezza degli stessi da possibili attacchi(OAuth2.0)

### **Linguaggi di programmazione adottati:**
  - Php
  - Java

---
