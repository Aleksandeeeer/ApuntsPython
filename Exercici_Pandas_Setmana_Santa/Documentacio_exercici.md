```diff
! Els gràfics no he pogut fer embed dins del github però cada gràfic en cas de clicar-hi et porta al gràfic publicat a Tableau.
```
# Febrer a Twitch
## Estudi realitzat mitjançant l'extracció de dades gràcies a python i el posterior tractament d'aquestes amb Tableau
Aquest estudi compte amb les dades en idioma español, fet que significa que aquest analisis està orientat tant als streamers com a l'audiencia de parla hispana. Ara bé, tant la comunitat llatinoamericana com l'espanyola tenen unes diferencies significatives, sobretot en temes d'horaris i dates, cosa que serà observable en aquest estudi.

### 1.- Quina ha estat l'evolució d'espectadors (captura a captura) durant el periode?
[![Grafic 1](https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ev&#47;EvolucinumerodespectadorsfebrerTwitch&#47;Dashboard1&#47;1_rss.png)](https://public.tableau.com/views/EvolucinumerodespectadorsfebrerTwitch/Dashboard1?:language=es-ES&publish=yes&:display_count=n&:origin=viz_share_link)

Com podem veure en aquest gràfic hi ha un patró que es repeteix dia rere dia. Es molt interessant veure com cada dia hi ha 3 punts claus que es repeteixen. Un punt mínim que sol ser cap a les 10:00 del matí i després dos punts máxims, un sobre les 23:00 i l'altre sobre les 04:00 del matí. Hi ha una explicació ben senzilla per aquest punts claus així com el cicle. Els punts màxims corresponen primer al pic màxim d'espectadors d'espanya sobre les 23:00 i al pic màxim d'espectadors llatinoamericans sobre les 04:00 am. Durant aquests dos pics l'audiencia es manté alta degut a l'afluencia descendent espanyola així com ascendent llatinoamericana, una transició d'espectadors bastant constant.

En el cas de el mínim és deu al fet de que a les 10 del matí els espanyols o estan a l'escola o treballant, en canvi els llatinoamericans acaben d'anar-se a dormir. Aquests dos fets fan que els espectadors estiguin en mínims.

### 2.- Quines son les categoríes més vistes?
[![Grafic 2](https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ju&#47;Juegosmsvistos&#47;Dashboard1&#47;1_rss.png)](https://public.tableau.com/views/Juegosmsvistos/Dashboard1?:language=es-ES&publish=yes&:display_count=n&:origin=viz_share_link)

La categoría més vista el més de febrer va ser "Just Chatting", qui estigui una mica familiratizat amb twitch sabrà que això es normal. El que no es tan normal es el fet de tenir en la posició 2 la categoria d'esports, ja que sol ser una categoria molt marginal. Aquesta posició tant elevada es deu a la kingsleague. Les categories que segueixen son clàssics de Twitch, com Minecraft i League of legends, seguit per un joc molt potent aquests últims anys, Valorant. També es vol remarcar Hogwarts Legacy ja que es un joc amb una dinàmica molt diferent, com observarem més endavant. Ja que es tracta d'un joc nou de llençament single player.

[![Grafic 3](https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ju&#47;Juegosmsstreameados&#47;Dashboard2&#47;1_rss.png)](https://public.tableau.com/views/Juegosmsstreameados/Dashboard2?:language=es-ES&:display_count=n&:origin=viz_share_link)

En quant al total d'hores streamejades de cada categoria veiem que la cosa està més empatada, amb Fortnite aconseguint la primera posició. 

### Com han evolucionat aquestes categories TOP al llarg del mes?
[![Grafic 4](https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ev&#47;Evolucionespectadoresjuegos&#47;Dashboard1&#47;1_rss.png)](https://public.tableau.com/views/Evolucionespectadoresjuegos/Hoja1?:language=es-ES&publish=yes&:display_count=n&:origin=viz_share_link)

Gràcies a la gràfica de l'evolució dels espectadors per a cada cas particular podem confirmar i observar una série de coses:

   * La categoria "Just Chatting" és la més constant, així com la més potent, però no té els majors pics d'audiencia.
   * La categoria de "League of Legends" és molt constant també, però amb números més baixos.
   * La categoria de "Sports" té el pic més alt de tot el periode, coincidint amb diumenge, dia de partit a la Kingsleague. Tot i així la resta dels dies es troba en       el mínim del gràfic. Podent afirmar que es una categoria integrada pràcticament al 100% per la Kingsleague
   * Valorant molt semblant a League of Legends pero amb menys espectadors
   * El cas de Minecraft també és interessant ja que té una mitjana bastant bona però té dos pics clarament marcats. Probablement degut a la realització d'algun event      de minecraft entre streamers (solen ser bastant comuns)
   * Hogwarts Legacy en compte és clarament diferent. Ja que comença en 0 viewers, primer tenim un pic (degut als streamers provant el joc en accés anticipat) i            finalment el pic més gran quan el joc surt a la venta. A partir d'aques pic és produeix una baixada paulatina que acaba desembocant a com havia començat, en            practicament 0.
     
[![Grafic 5](https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ev&#47;Evolucioncantidaddestreamsdelosjuegosmsvistos&#47;Dashboard2&#47;1_rss.png)](https://public.tableau.com/views/Evolucioncantidaddestreamsdelosjuegosmsvistos/Dashboard2?:language=es-ES&publish=yes&:display_count=n&:origin=viz_share_link)


[![Grafic 6](https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Di&#47;DistribuciondelosStreamers&#47;Hoja1&#47;1_rss.png)](https://public.tableau.com/views/DistribuciondelosStreamers/Hoja1?:language=es-ES&publish=yes&:display_count=n&:origin=viz_share_link)

[![Grafic 7](https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Di&#47;DistribuciondelosStreamerssegnintervalos2&#47;Hoja1&#47;1_rss.png)](https://public.tableau.com/views/DistribuciondelosStreamerssegnintervalos2/Hoja1?:language=es-ES&publish=yes&:display_count=n&:origin=viz_share_link)


[![Grafic 8](https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Di&#47;Distribucindelnumerodestreamerssegunlashoras&#47;Hoja1&#47;1_rss.png)](https://public.tableau.com/views/Distribucindelnumerodestreamerssegunlashoras/Hoja1?:language=es-ES&publish=yes&:display_count=n&:origin=viz_share_link)

[![Grafic 9](https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;St&#47;Stddelosespectadores&#47;Dashboard2&#47;1_rss.png)](https://public.tableau.com/views/Stddelosespectadores/Dashboard2?:language=es-ES&publish=yes&:display_count=n&:origin=viz_share_link)

[![Grafic 10](https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;St&#47;Stdsegunlahora&#47;Dashboard1&#47;1_rss.png)](https://public.tableau.com/views/Stdsegunlahora/Dashboard1?:language=es-ES&publish=yes&:display_count=n&:origin=viz_share_link)


