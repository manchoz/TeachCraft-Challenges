# Lezione 5

#### Obiettivo
Utilizzando i concetti imparati nella lezione 4, scrivi un programma per costruire una piramide.
```
   _
  ___
 _____
_______
```

Suggerimento: Invece di pensare alla piramide come ad un'unica costruzione, pensa ad ogni livello della piramide come una contruzione separata alta solo un blocco.

#### Nuovi Concetti

- Copiare ed Incollare è uno degli strumenti più importanti per uno sviluppatore!
- Se stai scrivendo ripetutamente del codice simile, considera l'idea di copiarlo e incollarlo, quindi di editare il codice risultante.
- Il tasto rapido per copiare è cmd+C sul mac o control+C su una macchina windows.
- Il tasto rapido per incollare è cmd+V sul mac o control+V su una macchina windows.

#### Codice
Apri il file script.py in un editor di codice. Cancella tutto il contenuto, stiamo ricominciando da capo!

```python
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create(address="199.96.85.3", name="mancho")
```
Le prime due righe sono le stesse della lezione precedente. Assicurati di sostituire "mancho" con il tuo nome!

```python
block_id = 24
```
Questo è il codice del blocco di arenaria, che va bene per una piramide. Sostituiscilo con un codice differente se preferisci da [qui](http://minecraft-ids.grahamedgecombe.com/).

```python
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
```
Ottiene la posizione corrente del giocatore in modo da costruire li la piramide.


```python
x2 = x + 8 #Make it 8 blocks wide.
y2 = y #Make it only one block high, so don't add anything here.
z2 = z + 8 #Make it 8 blocks long.

mc.setBlocks(x, y, z, x2, y2, z2, block_id)
```

Costruisci il livello inferiore della piramide. Questo è il blocco di codice che dovrai copiare e incollare per creare i livelli aggiuntivi. Crea altri 3 livelli dopo questo per completare la piramide da te.


#### Terminale

Esegui lo script così:
```shell
python script.py
```

# SFIDE

- Completa i 3 livelli rimanenti della piramide (manca dal codice qua sopra)
