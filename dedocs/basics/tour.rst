go noereth
.. include:: /../docs/shared/include/defs.rst

.. _presto.de.tour:

=================
Besichtigungstour
=================

Wortschatz
==========

Lino unterscheidet zwischen Personen und Organisationen. Beides sind Partner.

Ein Klient ist eine Person, über die wir mehr wissen als über eine normale
Person.

Ein Auftrag ist, wenn man für einen bestimmten Kunden eine Serie von Terminen
plant, bei denen ein bestimmter Arbeiter arbeitet.  Die Serie von Terminen kann
sich auf einen einzigen Einsatz beschränken.  Der Auftrag gilt als Grundlage
für die Fakturierung.  Ohne Auftrag keine Rechnung.  Im Auftrag kann auch

Ein **Termin** ist, wenn an einem bestimmten Tag und Uhrzeit ein bestimmter
Arbeiter (oder mehrere) zu einem bestimmten Klienten gehen.

Ein Termin muss einem Auftrag zugewiesen sein, um **fakturierbar** zu sein.

Man kann in Lino auch **unfakturierbare Termine** verwalten (z.B. interne
Besprechungen, Urlaubstage, sonstige Termine der Mitarbeiter, ...)

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
