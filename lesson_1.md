# Lezione 1

#### Obiettivo
Teleporta il tuo personaggio in un punto dello spazio che decidi e definisci nel codice.

#### Nuovi Concetti

Le **variabili** sono delle _etichette_ utilizzate come riferimento a qualcosa. Una variabile viene _assegnata_ utilizzando il segno **uguale** (`=`).

```python
x = 5
```

Ad esempio, puoi assegnare dei numeri a delle variabili in modo da memorizzarli per poterli usarli successivamente.

```python
player_position = mc.player.getPos()
```

Puoi anche usare le variabili per memorizzare delle informazioni importanti, come la posizione del giocatore.

#### Codice sorgente (o 'codice' o 'sorgente')
Apri il file `script.py` nel editor di codice. Per iniziare, analizzeremo il file una riga alla volta. 

```python
import mcpi.minecraft as minecraft
```
La prima linea _importa_ la _libreria_ `mcpi.minecraft` e la rende disponibile con il nome `minecraft`.


-----------------

```python
# NOTA - sostituisci "mancho" qui sotto con il tuo nome
indirizzo_server = "192.168.85.1"
nome_giocatore = "mancho"
mc = minecraft.Minecraft.create(address=indirizzo_server, name=nome_giocatore)
```

- Qualsiasi riga che inizia con il simbolo `#` ('cancelletto') è un _commento_ per il lettore e viene ignorato dal computer.
- Con queste istruzioni creiamo una connessione al nostro server minecraft e la memorizziamo nella variabile `mc`
- Il server a cui ci stiamo connettendo si trova all'indirizzo IP `192.168.85.1` e ci stiamo connettendo come utente `mancho`.
- Come scritto nel commento prima delle istruzioni, puoi cambiare `mancho` con il nome utente che preferisci.

-----------------

```python
x = 10
y = 110
z = 12
```

- Qui creiamo 3 nuove variabili da usare più tardi.
- Nella variabile che chiamiamo `x` memorizziamo il numero `10`.
- In quella `y`, il numero `110`.
- In quella `z`, il numero `12`.

-----------------

```python
mc.player.setPos(x, y, z)
```

- Usando la connessione al server minecraft che abbiamo creato e memorizzato precedentemente nella variabile `mc`...
- ... usiamo l'entità (nel gergo della programmazione si chiama '_oggetto_') che rappresenta il nostro giocatore all'interno del server minecraft...
- ... e, infine, impostiamo la nostra posizione minecraft alle coordinate x/y/z memorizzate nelle variabili assegnate poco prima.

Quello che succede è che le variabili vengono sostituite automaticamente con il valore che gli è stato assegnato.
Di fatto, l'istruzione di sopra è equivalmente a:

```python
mc.player.setPos(10, 110, 12)
```

#### Terminale a riga di comando (o 'Terminale' o 'Riga di comando')

Per poter _eseguire_ lo script, usando la riga di comando in un terminale, ci spostiamo nella _directory_ in cui è salvato il file `script.py` 
```shell
cd ~/TeachCraft-Challenges
```

Poi eseguiamo lo script con il seguente comando:
```shell
python script.py
```

Ogni volta che facciamo una modifica al codice sorgente, dobbiamo eseguire nuovamente lo script utilizzando questo comando.

----------------------

# Esercizi

- Modifica lo script per andare in una diversa posizione x/y/z.
- Facendo delle prove, cerca di capire qualche delle tree coordinate x, y o z è quella che ti fa spostare verso l'altro.
