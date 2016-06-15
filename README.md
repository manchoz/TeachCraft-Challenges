## TeachCraft 

Una serie di lezioni per insegnare a bambini e ragazzi i fondamenti della programmazione!

Usando Python, ogni lezione insegnerà ai ragazzi nuovi concetti, passando dai cicli while, le condizioni if, i cicli for, algoritmi, chiamare le funzioni e così via.

L'intero processo è collaborativo - gli studenti possono vedere i progressi degli altri dato che sono insieme nello stesso server multyplayer. Infatti, una delle ultime lezioni aiuterà i ragazzi a costruire un sistema magico che potranno usare per combattere con gli altri, lanciare magie che avranno preparato nel codice.

Tutto ciò che serve per partire è scaricare questo il codice in questo repository e installare java sul tuo sistema (tutte le istruzioni le trovi nella [guida di setup](https://github.com/teachthenet/TeachCraft-Challenges/blob/master/setup.md))

Io ho un server attivo e funzionante con le api per python - tutte le lezioni puntano di default all'IP del mio server. Se preferisci la privacy o il mio server fosse non funzionante () potresti voler [creare il tuo](https://github.com/teachthenet/TeachCraft-Server). Se dovessi trovare il mio server non funzionante sentiti libero di aprire una issue qui per informarmi e io lo rimetterò su.

Il mio server Minecraft si trova
```
199.96.85.3:25570
```

### Lezioni & Setup

[Setup iniziale](https://github.com/teachthenet/TeachCraft-Challenges/blob/master/setup.md): Far funzionare minecraft, connettersi al  server.

[Lezione 1](https://github.com/teachthenet/TeachCraft-Challenges/blob/master/lesson_1.md): Teleporta il tuo personaggio in un punto dello spazio che decidi e definisci nel codice.

[Lezione 2](https://github.com/teachthenet/TeachCraft-Challenges/blob/master/lesson_2.md): Lascia una traccia di fiori dietro di te mentre cammini. (Puoi sostituire i fiori con qualsiasi tipo di blocco come, ad esempio, con la lava).

[Lezione 3](https://github.com/teachthenet/TeachCraft-Challenges/blob/master/lesson_3.md): Dai l'abilità al tuo personaggio di camminare sull'acqua (trasformando l'acqua sotto il tuo personaggion in ghiaccio).

[Lezione 4](https://github.com/teachthenet/TeachCraft-Challenges/blob/master/lesson_4.md): Creare una costruzione programmaticamente.

[Lezione 5](https://github.com/teachthenet/TeachCraft-Challenges/blob/master/lesson_5.md): Creare una piramide programmaticamente.

[Lezione 6](https://github.com/teachthenet/TeachCraft-Challenges/blob/master/lesson_6.md): Usare un algoritmo per costruire la piramide analizzando il pattern che hai scoperto nella lezione 5!

[Lezione 7](https://github.com/teachthenet/TeachCraft-Challenges/blob/master/lesson_7.md): Creare un sistema magico che ascolta la chat di Minecraft e lancia le magie che hai creato precedentemente.

[(Avanzato) Lezione 8](https://github.com/teachthenet/TeachCraft-Challenges/blob/master/lesson8/lesson8.py): Impara come importare un immagine in minecraft pixel art usando la Python Imaging Library.

### Vuoi hostare un tuo server / far girare un server in locale?
- Trovi tutto su [questo repository](https://github.com/teachthenet/TeachCraft-Server)

### Documentazione Minecraft
- [la versione pi](http://www.stuffaboutcode.com/p/minecraft-api-reference.html) Contiene la maggior parte delle api di base per python
- [la nostra versione](https://github.com/zhuowei/RaspberryJuice) Contiene, oltre alle api di base, il supporto alle nostre.
- [Minecraft block ids](http://minecraft-ids.grahamedgecombe.com/)

### Note
- La posizione dalle api python non combacia con la posizione ottenuta dal server.
    Questo perché raspberryjuice la calcola partendo dal punto di spawn, mentre il server la calcola dalle coordinate 0,0,0.
    Per fixarlo, lancia come amministratore:
    `setworldspawn 0 0 0`
