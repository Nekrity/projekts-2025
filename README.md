# Programmēšana 1, projekts 2025

Projekts tiek īstenots patstāvīgi. Projekta tiek aizstavēts ar prezentāciju un demo.
Kods tiek analizēts pēc aizstavēšanas.

## Analīze, projektēšana, plānošana (0.5pt) (prezentācija)
- Analīze - Problēmas apraksts, kāpēc tā ir aktuāla
- Analīze - Mērķauditorija, kura lietos programmu
- Analīze - eksistējošo risinājumu analīze, ekrānšāviņi, plusi un mīnusi
- Projektēšana - specifikācija, vismaz 5 funkcionālas un 5 nefunkcionālas prasības
- Plānošana - darba uzdevumu saraksts, vismaz 5
- Risinājuma prezentācija - demo vai ekrānšāviņi

## Izstrāde (0.5pt)
- Kods atbilst izvirzītam prasībam
- Ir ievaddatu validācija (pārbaude ka tika ierakstīti korrekti dati)
- Mainīgie rakstīti snake_case, bez saisinājumiem
- Ir komentāri pirms if, for, while kosntrukcijam
- Kods nemet kļūdas darbības laikā
- Izmaiņas saglabātas Github repozitorijā
- Izmaiņas saglabātas vairākas iterācijās (vairāki commit)
- Izmantoti saraksti vai vārdnīcas vai klases
- Izmantota jebkura bibliotēka (modulis uzinstalēts ar PIP un izmantots kodā) 
- Izmantoti JSON faili vai SQLite datubāze datu glabāšanai

## Testēšana (0.5pt)
- Testēšana - 2 veiksmes scenāriji
1)knowing that asgore will deal 5 damage per hit by default, when player is hit by a fireball(1 hit) without asgore stats lowered, player will receive 5 damage
2)knowing that player can attack asgore, when player attacks asgore, asgore takes damage

- Testēšana - 4 lietošanas scenāriji
1)knowing that asgore can kill player only when player's health is at 1 health and his attacks deal 5 damage per hit, when player is hit by a fireball(1 hit) and player's current health is 4, player health after attack will be 1 health
2)knowing that butterscotch pie heals 99 heath and max health is 20, when player eats butterscotch pie when his health is 1 health, player's health will be 20 health
3)knowing that talking to asgore 3 times will lower his attack and defence, when player talks to ASGORE 3 times, his attack and defence will go down.
4)knowing that blue attacks won't hit player when he doesn't  moves and orange attacks when he moves, when player moved on blue attack during asgore trident attack, player will receive damage

- Testēšana - 2 robež-scenāriji
1)knowing that to hit enemy player must complete minigame(hit on timing), when player won't attack during minigame, asgore will receive no damage and "miss" will be displayed
2)knowing that presing x button on the window closes game, when player preses x button on window, game closes
- Testēšana - 4 automatizēti testi (pytest bilbiotēka)
