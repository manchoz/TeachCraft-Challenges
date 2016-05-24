# Lezione 2

#### Obiettivi
Lascia una traccia di fiori dietro di te mentre cammini. (Puoi sostituire i fiori con qualsiasi tipo di blocco come, ad esempio, con la lava).

#### Nuovi Concetti

```python
print("Hi!")
my_variable = 5
print(my_variable)
```

- La funzione `print` stampa un testo sul terminale.
- È utile per fare il _debugging_ (trovare gli errori in un programma che non funziona), sia per vedere quando una certa porzione di codice viene eseguita, sia per visualizzare il contenuto di una variabile.

-----------------

E adesso introduciamo un nuovo costrutto, un ciclo (_loop_) infinito.

Un ciclo infinito `while` viene usato per eseguire una porzione di codice ripetutamente e in continuazione, fino a quando l'utente non decida di fermarla.

Un ciclo infinto `while` ha la seguente struttura:

```python
while <espressione booleana>:
    <esegui la porzione di codice indentata>
    <torna indietro all'inizio dell'istruzione while>
```

Ad esempio, il codice seguente, stamperà per sempre la sequenza "1 2 3 1 2 3 1 2 3 1 2 3..."

```python
while True:
    print("1")
    print("2")
    print("3")
```

Riassumendo, un ciclo infinito `while` eseguirà in continuazione lo stesso gruppo di istruzioni fino a quando non verrà fermato dall'utente con la combinazione di tasti `CTRL+C`

#### Codice
Apri il file `script.py` nell'editor di codice. Cancella tutto, iniziamo da capo!

```python
import mcpi.minecraft as minecraft
 
indirizzo_server = "192.168.85.1"
nome_giocatore = "mancho"
mc = minecraft.Minecraft.create(address=indirizzo_server, name=nome_giocatore)
```
Le prime quattro righe sono le stesse della prima lezione.
Ricorda di sostituire il nome "mancho" con il tuo nome!

-----------------

```python
import time
```
Questa istruzione importa una libreria Python chiamata `time` che ci permetterà di mettere lo script in pausa per tutto il tempo di cui abbiamo bisogno. 

-----------------

```python
print("Prima del while.")
```
Questa istruzione stampa semplicemente il testo nel terminale. La useramo per fare debugging, in modo da vedere quando le istruzioni successive stanno per essere eseguite.

-----------------

```python
while True:
```
Poi iniziamo un ciclo `while`. Nota che la _condizione_ del ciclo è semplicemente `True` (valore booleano 'vero'). In questo caso, il ciclo loop verrà eseguito per sempre fino alla pressione della combinazione `CTRL+C` oppure alla chiusura della finestra del terminale.

-----------------

```python
    # Recupera le coordinate x/y/z della posizione del giocatore
    pos = mc.player.getPos()
```
Per prima cosa, all'intero del ciclo loop recuperiamo la posizione del giocatore. La funzione `getPos` è molto simile alla funzione `setPos` della prima lezione, con la differenza che serve per recuperare invece che per impostare le coordinate del giocatore. 

**NOTA IMPORTATE** - Osserva con attenzione che questa istruzione e quella delle righe seguenti è _indentata_ (è distanziata dal margine sinistro con quattro spazi)! Questo è la sintassi che permette di dire a Python quali sono le righe di codice che appartengono allo stesso ciclo `while` e che devono essere esguite dentro questo ciclo. In Python l'indentazione è **importante**!


-----------------

```python
    # Memorizza le coordinate della posizione del giocatore nelle rispettive variabili x/y/z
    x = pos.x
    y = pos.y
    z = pos.z
```
Continuando nel ciclo `while`, memorizziamo la posizione del giocatore nelle variabili `x`, `y` e `z`, perché ci serviranno più avanti.

-----------------

```python
    # Questo è il Block ID di Minecraft che identifica i fiori.
    block = 38
```
Sempre nel ciclo `while` memorizziamo il Block ID di Minecraft per il blocco di tipo fiori in una variabile chiamata `block`. Puoi sceglier un blocco di qualsiasi tipo e memorizzare il suo ID nella stessa variabile. La lista dei Block ID di Minecraft è disponibile alla seguente [pagina web] (http://minecraft-ids.grahamedgecombe.com/).

-----------------

```python
    # Imposta il tipo del blocco su cui è posizionato il giocatore con il Block ID che abbiamo scelto precedentemente.
    mc.setBlock(x, y, z, block)
```
Ancora nel ciclo `while`, usiamo la nostra connessione `mc` al server Minecraft per impostare il tipo di blocco alle coordinate x/y/x che abbiamo memorizzato prima.

Dato che le variabili `x`/`y`/`x` contengono le coordinate della nostra posizione e dato che la variabile `block` contiene il tipo di blocco 'fiori', quello che stiamo facendo è mettere dei fiori nel punto in cui siamo!

Inoltre, dato che la istruzioni vengono eseguite dentro al ciclo `while`, camminando possiamo creare una scia di fiori! Aggiungiamo le ultime istruzione e siamo pronti per provare il programma.

-----------------

```python
    # Aspetta per due decimi di secondo e torna indietro all'inizio del ciclo
    print("Nel while. Mi fermo per due decimi di secondo")
    time.sleep(0.2)
```
Sempre nel ciclo `while` stampiamo un messaggio che ci permette di sapere dove siamo e poi mettiamo in pausa il programma per due decimi di secondo. Questo è importante perché i computer sono velocissimi e se non mettessimo il programma in pausa almeno per un po' il computer imposterebbe il nuovo tipo di blocco per migliaia e migliaia di volte e, probabilmetente, alla fine farebbe _crashare_ il server Minecraft.

-----------------

```python
print("Fuori dal while.")
```
Per finire, l'ultima istruzione che è **fuori** dal ciclo `while`. Sappiamo che è fuori perché non è indentata. Questa è la sintassi che dice al Python che il ciclo `while` è finito.

#### Terminale

Esegui lo script come al solito:
```shell
python script.py
```

Fai attenzione perché lo script verrà eseguito per sempre (`while True:`). Per fermarlo, digita la combinazione di tasti `CTRL-C` oppure chiudi la finestra del terminale.


# SFIDE

- Modifica lo script per creare una scia di lava ([Block ID Explorer](http://minecraft-ids.grahamedgecombe.com/))
- Invece di creare la lava sotto al giocatore potresti crearla dietro, oppure di lato!
- Fai esperimenti con altri Block ID! Qualche idea:
    - Potresti creare una strada gialla, fatta di blocchi d'oro.
    - Potresti posare dei binari sotto di te per creare delle montagne russe molto velocemente!
    
    
