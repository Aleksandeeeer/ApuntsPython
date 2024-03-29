```diff
! Els gràfics no he pogut fer embed dins del github però cada gràfic en cas de clicar-hi et porta al gràfic publicat a Tableau.
```
# Analisis de dataset polític sobre candidats a l'alcaldia de Barcelona

Aquest estudi es centrarà en analitzar les relacions y tendències observades en tuits on es mencionen qualsevol dels candidats polítics a l'alcaldia de barcelona.

## Tableau

## 1.- Quin és el candidat més mencionat?

Aqui tenim un gràfic on visualment gràcies al tamany dels cercles podem observar quins son els candidats més mencionats. D'on podem observar que el candidat més nombrat és sense sorpreses l'actual alcaldessa: Ada Colau. Això era esperable pel fet de que al ser l'actual alcaldessa té molta més notorietat y actualitat. En segona i tercera posició estan Basha Changue i Daniel Sirera respectivament.

[![Grafic 1](https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;No&#47;Nombredemencionstotalspercandidats&#47;Dashboard1&#47;1_rss.png)](https://public.tableau.com/views/Nombredemencionstotalspercandidats/Dashboard1?:language=es-ES&:display_count=n&:origin=viz_share_link)

## 2.- Quins son els usuaris més actius?

Quan analitzem els usuaris més actius a l'hora de parlar i mencionar dels candidats tenim un particular en primera posició l'usuarI "Ander_the_table" amb una quantitat de 88 tuits sobre aquest tema. En canvi en segona posició tenim un mitjà de comunicació, "nació digital", així que és perfectament entendible els 72 tuits sobre els candidats. Tot i així no tornem a trobar un mitjà fins la posició 7, on trobem "elnacionalcat".

[![Grafic 2](https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Us&#47;Usuariosmsactivos_16830506749830&#47;Dashboard1&#47;1_rss.png)](https://public.tableau.com/views/Usuariosmsactivos_16830506749830/Dashboard1?:language=es-ES&publish=yes&:display_count=n&:origin=viz_share_link)

## Quina és l'activitat de cada candidat als seus comptes oficials?

En canvia l'hora d'analitzar els polítics més actius els resultats canvien dràsticament respecte el primer gràfic. Per exemple Ada Colau ni apareix al gràfic, indicant que no fa servir twitter de forma habitual, de fet el seu últim tuit és de març de 2021. El que si podem veure és com el candidat més actiu és Eva Parera amb molta diferència, seguida de Daniel Sirera i Basha Changue.

[![Grafic 3](https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ca&#47;Candidatsmsactius3&#47;Dashboard2&#47;1_rss.png)](https://public.tableau.com/views/Candidatsmsactius3/Dashboard2?:language=es-ES&publish=yes&:display_count=n&:origin=viz_share_link)

## Quins temes destaquen? 

En el moment que analitzem els temes més recurrents a través dels hashtags tenim un clar número 1 i un clar número 2. Sent el número 1 "URGENTE" i el número 2 "Barcelona". Habent de baixar fins a la cinquena posició per a trobar el nom d'un dels candidats, en aquest cas "Colau"


[![Grafic 4](https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Te&#47;Temasmscomentados&#47;Dashboard1&#47;1_rss.png)](https://public.tableau.com/views/Temasmscomentados/Dashboard1?:language=es-ES&publish=yes&:display_count=n&:origin=viz_share_link)

## Quins són els usuaris amb major número de seguidors?

En aquest gràfic és facilment observable un patró. Tots els usuaris amb major número de seguidors són mitjans de notícies. Aquest fet era esperable, pero a la vegada és extrany no trobar ningún influencer o polític amb molts seguidors en el gràfic

[![Grafic 5](https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Us&#47;Usuariosconmayorfollowers&#47;Dashboard1&#47;1_rss.png)](https://public.tableau.com/views/Usuariosconmayorfollowers/Dashboard1?:language=es-ES&publish=yes&:display_count=n&:origin=viz_share_link)

## Gephi

Ha arribat el moment d'emprar l'eina de Gephi per veure relacions y diferents mesures. En aquesta primera imatge, veiem les relacions de forma general. On podem veure els principals usuaris amb més mencions i com estan relacionats aquests entre ells i altres usuaris. Com hem pogut veure amb Tableau el principal anomenat és el compte de "WillyTolerdo" on tots els usuaris que básicament interactuen amb ell es troben en el mateix color blau. El segon més anomenat es "Froilannister".

![Gephi 1](https://user-images.githubusercontent.com/116373618/235784781-b18c827f-acc4-4cb2-9db1-afb56ca23a50.JPG)

Tot i així ens interessa trobar als candidats i les seves relacions, és per això que mitjançant un fitre de PageRank podem veure els més importants treient les intereferències.

![Gephi 2](https://user-images.githubusercontent.com/116373618/235785610-88fe49c1-e16e-4681-a5d7-12b23bbf9c96.JPG)

I si agafem aquest grapho i mirem de més aprop veiem a candidats com Ada Colau relacionada amb algun mitjà i un compte anomenat "OnvasBarcelona", a Eva Parera parcialment relacionada amb Daniel Sirera. I a Basha Changue relacionada amb la Cup.!

![Gephi 3](https://user-images.githubusercontent.com/116373618/235786737-4f0bffce-f57f-43e5-9948-792947bf1d43.JPG)
![Gephi 4](https://user-images.githubusercontent.com/116373618/235786772-54f2da45-b993-444a-83ad-628030430313.JPG)

