.. include:: /../docs/shared/include/defs.rst

.. _presto.de.tour:

=======================
Erste Besichtigungstour
=======================

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

Beispiel : Erfassung eines einfachen einmaligen Einsatzes ausgehend von der
händisch ausgefüllten Rechnung:

- Klient erstellen

  - :menuselection:`Kontakte --> Klienten`
  - |insert|
  - Dubletten vermeiden: vorher suchen, ob er nicht schon existiert.

  - NB Das Layout des Detail-Fensters (welche Reiter, und welche Elemente wo
    angezeigt werden) ist ein schnell hingeworfener Vorschlag, weil das leicht
    anpassbar ist und der AG dabei mitreden sollte, und weil das am
    einfachsten direkt auf den Daten im Prototypen geht.

- Auftrag erstellen:

  - vom Klienten aus:

     - Doppelklick auf überletzter Zeile im Panel "Aufträge" im Reiter "Fakturierung",
     - Team auswählen, Erfassungsdatum bestätigen, :kbd:`Ctrl-S`

  - vom Hauptmenü aus:

     - :menuselection:`Aufträge --> Aufträge`
     - |insert|
     - Klient auswählen, Team auswählen, Erfassungsdatum, :kbd:`Ctrl-S`

- Auftrag detaillieren:

  - ggf. Rechnungsempfänger angeben
  - Arbeiter erfassen
  - Fahrtkosten eintragen in "Kosten pro Einsatz"
  - Beschreibung der Arbeiten

- Auftrag ausdrucken

- Termin(e) erfassen:

  - einzelne Termine mit |insert| im Panel "Termine" im Reiter "Kalender"
  - `Terminvorschläge generieren`_

  - Workflow : jeder Termin steht zunächst im Status "Vorschlag" bzw.
    "Geplant", und man muss auf :guilabel:`☑` klicken, damit er in den Zustand
    "Stattgefunden" wechselt. Ansonsten erstellt Lino keine Rechnung.

- Auf "Fakturieren" klicken.


Terminvorschläge generieren
===========================

- Gehe auf den Auftrag und aktiviere den Reiter Kalender
- Fülle die Felder aus
- Klicke auf |flash|
