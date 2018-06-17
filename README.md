# Autors
Antonio Ciordia.

Nil Bardou. 

# PASSES A SEGUIR PEL FUNCIONAMENT DEL PROGRAMA SEQÜENCIAL
- pas 1: Ens situem el directori on es troba la prctica amb tots els arxius.
- pas 2: Coloquem al fitxer (file1.txt) l'arxiu qe volem tractar.
- pas 3: Escrivim la comanda para iniciar el proces de l'arxiu seqüencial 
(Comanda: python secuencial.py)
- pas 4: Observem el temps que ha tardat tant el WordCount com el CountWord. 

# PASSES A SEGUIR PEL FUNCIONAMENT DEL PROGRAMA AMB MAPPERS
- pas 1: Ens situem el directori on es troba la prctica amb tots els arxius.
- pas 2: Activem el SimpleHTTPServer ((Comanda: python -m SimpleHTTPServer)
- pas 3: Enjeguem el server.py (Comanda: python server.py)
- pas 4: Enjeguem el registry.py (Comanda: python registry.py)
- pas 5: Enjeguem el reducer.py (Comanda: python reducer.py)
- pas 6: Enjeguem els 4 host.py (Comanda: python hostX.py)
- pas 7: En el terminal on tenim obertel server.py decidim quina opció volem dur a terme (wordcount o countword) i quin arxiu volem tractar.
- pas 8: Observem en el terminal de del word.py el resultat de l'opció escollida. 

# IPLEMENTACIÓ
- Hosts: primer creem el host, després agafem la referència del Registry per a poder executar la seva funció bind la qual li passarem un nom (mapperX) i el host, i ens quedem escoltant. 
- Reducer: primer creem el host, després agafem la referència del Registry per a poder executar la seva funció bind la qual li passarem un nom (reducer) i el host, i ens quedem escoltant.  
- Registry: creem el seu host i accedim a la classe Registry on tenim les funcions bind i lookup. La funció bind el que fa es ficar guardar una referència amb un nom per a que després amb la funció lookup passant un nom puguem obtenir una referència.   
- Server:  conté el codi per a separar el text en parts iguals i el codi per a que els mappers analitzin el text. Primer obtenim el text i eliminem del text tots els caràcters que no siguin lletres, números o espais, desprès dividim el text en parts iguals, li demanem al registry totes les referències dels hosts i del reducer, un cop obtingudes per cada host crearem un mapper el qual li passarem una part del text i aquest executarà la funció CountWord o WordCount.  
- Word:  conté el codi per a que els mappers puguin fer el WordCount o el CountWord i el codi per a que el reducer junti totes les respostes dels mappers. En el CountWord dels mappers el que fem es augmentar en una unitat un contador amb valor inicial 0, cada cop que trobem una paraula en el text que haguem passat i quan haguem acabat de mirar tot el text cridem al reducer per a que executi el seu CountWord el qual suma en un contador general les paraules contades pel  mapper i quan tots els mappers hagin passat la seva resposta al reducer imprimirem la resposta per pantalla i quan temps s’ha tardat. En el WordCount el que fem es que a partir d’un diccionari on la clau serà la paraula i el valor serà el numero de vegades que apareix aquesta paraula, si la paraula no esta al diccionari s’afegirà de nou i el seu valor valdrà 1 i si ja existeix sumarem 1 al valor, quan s’acabi d’analitzar tot el text cridarem al reducer per a que executi WordCount el qual tindrà un diccionari general amb el mateix format que el del mapper on anirem introduint totes les claus i valors que han generat els mappers i quan tots els mappers hagin passat les seves respostes al reducer imprimirem la resposta per pantalla i quan temps s’ha tardat. 
