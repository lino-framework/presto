=================
Datenbankstruktur
=================

.. contents::
   :depth: 1
   :local:



Kontakte
========

Als **Partner** bezeichnet Lino eine physische oder juristische Person, mit der
wir potentiell kommunizieren können.  Physische Personen stehen unter
:menuselection:`Kontakte --> Personen` juristische Personen unter
:menuselection:`Kontakte --> Organisationen`.

Während du in der Praxis eure Partner nach **Partnerart** anschaust, kannst du
:menuselection:`Explorer --> Kontakte --> Partner` eine Liste aller Partner
sehen, die euer Lino kennt. Dort werden also alle Partner in einen Topf
geworfen.

Lino Presto kennt neben den beiden Grundarten "Personen" und "Organisationen"
die Partnerarten Klienten, Angestellte, Haushalte.

Jede *Person* kann potentiell **Kontaktperson** für eine oder mehrere
Organisationen sein.  Und umgekehrt kann jede Organisation eine oder mehrere
Kontaktpersonen haben. Wenn man eine Person als Kontaktperson einer
Organisation definiert, kann man ausserdem angeben, welche **Funktion** diese
Person in dieser Organisation ausübt.

Alle physischen Personen (Direktoren, Mitarbeiter, Klienten, deren Onkels und
Tanten...) stehen in einer Tabelle "Personen", von der man dann für manche
dieser Personen in die Ansicht "als Klient" springen kann, in der die gleichen
Angaben wie für Personen *sowie zusätzliche weitere Angaben* stehen.

Der Anspruchsnehmer eines Auftrags muss Klient sein, aber der
Rechnungsempfänger kann auch eine einfache Person oder gar eine Organisation
sein. Jeder Partner kann potentiell als *Rechnungsempfänger* eines oder
mehrerer Aufträge* fungieren.

Ein Haushalt ist


Familienbeziehungen:


Vermögensverwalter = administrateur des biens

Verwalter der Person = administrateur de la personne (beides hiess früher « administrateur provisoire)

Delegierter Kontakt = accompagnateur – contact délégué (Begleiter, Sozialarbeiter, Helfer, Ehrenamtlicher Helfer)

Mitbewohner = wohnt mit der regelmäßig Person zusammen (ein Freund, ein Bekannter, …) – sei es gesetzlich oder de facto (nicht zu vergleichen mit den Statuten beim ÖSHZ oder der Gemeinde – das interessiert uns nicht).

Wohngemeinschaft = eine von einer anderen Einrichtung kollektiv organisierte Wohnform, in der mehrere Personen, die sich vorher nicht kannten und auch nicht Verwandt sind, zusammen leben.




Kalender
========

Ein **Termin** ist, wenn zu einem bestimmten Zeitpunkt ein Treffen zwischen
einem Partner und einem oder mehreren Angestellten vereinbart wurde. Der
*Autor* eines Termins ist der Systembenutzer, der sich um die Erfassung in Lino
kümmert.  Die "Gäste" oder "Teilnehmer" sind die Personen, die tatsächlich an
dem Termin teilnehmen. Falls eine Dienstleistung, die nicht in Lino als Termin
erfasst war, fakturiert werden soll, wird sie im Nachhinein wie ein Termin
erfasst.

Jeder Termin wird als **Kalendereintrag** gespeichert, also ein Eintrag im
Kalender, also etwas, das potentiell in einem Kalender angezeigt werden kann.

Die **Kalendereintragsart** (also die Art eines Kalendereintrags) ist für Lino
wichtig um zu sehen, ob fakturiert werden soll oder nicht. Zum Beispiel gibt es
auch Kalendereintragsarten wie "Feiertage" oder "Versammlung" hinzu.

Pro Termin gibt es ein Feld *Beschreibung*. Das kann verwendet werden für
Informationen zur Terminplanung.


Aufträge
========

