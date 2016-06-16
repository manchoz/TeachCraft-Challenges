# Lezione 3

#### Obiettivi
Concedi al tuo personaggio l'abilità di camminare sull'acqua... trasformando i blocchi d'acqua sotto sotto al personaggio in blocchi di ghiaccio.

#### Nuovi Concetti

```python
if <condizione>:
    <esegui questo codice>
```

- Abbiamo un altro construtto chiamato *if*.
- Un *if* controlla una condizione.
- Se la condizione passa (è vera), esegue il codice indentato che ha sotto di sé **una volta**.
- Se la condizione fallisce (non è vera), salta il codice indentato che ha sotto di sé.
- Quindi una *if* esegue il suo codice una volta, mentre il ciclo *while* lo esegue in ripetizione!

```python
x = 4
if x == 3:
    print("x uguale a 3")
```

Questo esegue l'istruzione *print* se x è uguale a 3. Nota il segno di doppio uguale nell'istruzione *if*! E` super importante. Il doppio uguale controlla che qualcosa sia equivalente, a differenza del singolo segno di guguale che assegna qualcosa ad una variabile.

```python
if y > 10:
    if x > 10:
        print("y e` almeno alto 10 blocchi e x e` almeno distante 10 blocchi")
```

Nota che puoi annidare più *if* uno dentro l'altro, finchè continui ad aumentare l'indentazione.

```python
if y >= 10 and y <= 20:
    print("y e' alto tra i 10 e i 20 blocchi")
```

Puoi anche combinare gli *if* usando gli operatori *and* ed *or*.


#### Codice
Apri *script.py* nel tuo editor. Cancella tutto quello che c'è dentro, cominceremo da zero!

```python
import time
import mcpi.minecraft as minecraft
nome_giocatore = "mancho"
mc = minecraft.Minecraft.create(address="199.96.85.3", name=nome_giocatore)
```
Le prime quattro righe sono uguali a come erano nella lezione precedente. Ricordati di sostituire *mancho* con il tuo nome!

```python
water_block = 9
ice_block = 79
```

Quindi salviamo gli *id* dei blocchi di acqua e di ghiaccio in variabili che andremo ad usare successivamente.

```python
while True:
```

Dopo vogliamo un loop infinito che eseguirà il nostro prossimo pezzo di codice finchè non gli diremo di fermarsi.

```python
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z
```
Dentro il ciclo *while*, vogliamo ricevere la posizione corrente del giocatore, e salvarla in variabili che andremo ad usare successivamente.

```python
    block_below_player = mc.getBlock(x, y - 1, z)
```
Dentro il ciclo *while*, vogliamo ottenere il blocco che sta sotto al giocare. Per fare questo, eseguigiamo la funzione *getBlock*, passandole le coordinate x/y/z appena sotto al giocatore! Fai attenzione all'*y-1*. Dal momento che la posizione del giocatore è composta da x/y/z, sottraendo 1 da *y* ottieniamo il blocck immediatamente sotto al giocatore.

```python
    # Se il blocco sotto al giocare e` acqua, trasformalo in ghiaccio.
    if block_below_player == water_block:
        mc.setBlock(x, y - 1, z, ice_block)
```
Dentro il ciclo *while*, controlla se il blocco sotto al giocatore è acqua. Se è così, trasformale in ghiaccio!

```python
    time.sleep(0.2)
```
Dentro il ciclo *while*, riposiamoci per 0.2 secondi


#### Terminale

Esegui lo script in questo modo:
```shell
python script.py
```

Fai attenzione che questo script girerà all'infinito. Per terminarlo devi premere *control+C*, o semplicemente chiudi il terminale.


# SFIDE

Puoi aver notato che lo script per camminare sull'acqua non è perfetto; c'è una piccolo ritardo prima che lo script si accorga che tu sia sopra all'acqua, e ci cadrai dentro.

Per sistemare questo inconveniente, al posto di controllare solo il block al di sotto del giocatore, modifica lo script per controllare anche di fronte, dietro ed ai lati del giocatore.

In questo modo, possiamo trasformare i blocchi in ghiaccio prima che il giocatore ci camminerà sopra!

