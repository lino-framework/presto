.. include:: /../docs/shared/include/defs.rst

.. _presto.de.tour:

=================
Besichtigungstour
=================

Kontakte
========

Als **Partner** bezeichnen wir allgemein jede Einzelperson oder Gruppe, die als
**Rechnungsempfänger** oder sonstiger Gesprächspartner fungieren kann.
Jeder Partner kann unterschiedliche Rollen oder gar parallele Rollen je
nach Auftragstyp oder Finalität einer Dienstleistung haben.

Lino unterscheidet fünf Partnerarten: **Personen**, **Klienten**, **Arbeiter**,
**Haushalte** und **Organisationen**. Klienten und Arbeiter sind Personen, über
die wir mehr wissen als über eine normale Person.  Ein Klient oder Arbeiter ist
immer auch eine Person.

Damit die Suche und die familiäre Einschätzung einfacher ersichtlich wird,
können für jede Person auch deren Familienzusammensetzungen (generell
Mitgliedschaft in Haushalten) und familiäere Beziehungen erfasst werden.

Pro Partner können mehrere Adressen hinterlegt werden. Mögliche Adressenarten
können definiert werden (z.B. "Referenzadresse" oder "Wohnsitz")

Pro Klient kann ein oder mehrerere Grund der Anfrage (mehrfach Auswahl)

Aufträge
========

Ein **Auftrag** ist, wenn man für einen bestimmten Klienten eine Serie von
Terminen plant, bei denen ein bestimmter Arbeiter arbeitet.  Die Serie von
Terminen kann sich auf einen einzigen Einsatz beschränken. Aufträge sind in
*Journale** gruppiert. Der Auftrag gilt als Grundlage für die Fakturierung.
Ohne Auftrag keine Rechnung.  Im Auftrag können neben den vorgesehenen
Arbeitern auch Fahrtkosten und sonstige planbare Nebenkosten erfasst werden,
die pro Einsatz fakturiert werden.

Ein Auftrag muss immer einem Klienten zugewiesen sein und kann optional einen
anderen Partner als Rechnungsempänger haben.

Kalender
========

Ein **Termin** ist, wenn an einem bestimmten Tag und Uhrzeit ein bestimmter
Arbeiter (oder mehrere) zu einem bestimmten Klienten gehen. Ein Termin muss
einem Auftrag zugewiesen sein, um **fakturierbar** zu sein. Man kann in Lino
auch **unfakturierbare Termine** verwalten (z.B. interne Besprechungen,
Urlaubstage, sonstige Termine der Mitarbeiter, ...)

Teams
=====

Für die verschiedenen Tätigkeitsbereiche eines Betriebs zu differenzieren, kann
der Systemverwalter **Teams** konfigurieren.
Jeder Auftrag muss einem Team zugewiesen sein.
Pro Auftragsjournal kann man definieren, welches Team für Aufträge in diesem Journal zuständig ist.
Eventuell können mehrere Auftragsjournale pro Team angelegt werden.


Beispiel 1
==========

Erfassung eines einfachen einmaligen Einsatzes ausgehend von der händisch
ausgefüllten Rechnung:

- Klient erstellen

  - :menuselection:`Kontakte --> Klienten` und dort auf |insert| klicken.

  - Dubletten vermeiden: vorher suchen, ob er nicht schon existiert.

  - NB Das Layout des Detail-Fensters (welche Reite, und welche Elemente wo
    angezeigt werden) ist ein Vorschlag, der leicht
    anpassbar ist und bei dem der Kunde mitreden sollte (was am
    einfachsten direkt auf den Daten im Prototypen geht).

- Auftrag erstellen:

  - vom Klienten aus:

     - Reiter "Fakturierung", Panel "Aufträge", Doppelklick auf überletzter Zeile
     - Journal auswählen, Erfassungsdatum bestätigen, :kbd:`Ctrl-S`

  - vom Hauptmenü aus:

     - :menuselection:`Aufträge --> (Auftragsjournal)` und dort |insert|
     - Klient auswählen, Erfassungsdatum, :kbd:`Ctrl-S`

- Auftrag detaillieren:

  - ggf. Rechnungsempfänger angeben
  - Arbeiter erfassen

  - Fahrtkosten eintragen in "Kosten pro Einsatz". Hier können ausser
    Fahrtkosten auch z.B. Verbrauchsprodukte angegeben werden.  Die hier
    angegebenen Kosten werden für jeden stattgefundenen Termin zusätzlich zur
    Arbeitszeit fakturiert.

  - ggf. Beschreibung der Arbeiten

- Auftrag ausdrucken (noch nicht programmiert)

- Termin(e) erfassen:

  - einzelne Termine mit |insert| im Panel "Termine" im Reiter "Kalender"
  - `Terminvorschläge generieren`_

  - Workflow : jeder Termin steht zunächst im Status "Vorschlag" bzw.
    "Geplant", und man muss auf :guilabel:`☑` klicken, damit er in den Zustand
    "Stattgefunden" wechselt. Ansonsten erstellt Lino keine Rechnung.

- :kbd:`Escape` um auf den Auftrag zurück zu springen.

- Auf "Fakturieren" klicken.

  NB: Lino fakturiert immer alle Termine eines Auftrags.

- Im Fakturierungsplan auf


Terminvorschläge generieren
===========================

- Gehe auf den Auftrag und aktiviere den Reiter Kalender
- Fülle die Felder aus
- Klicke auf |flash|
