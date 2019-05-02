.. include:: /../docs/shared/include/defs.rst

.. _presto.de.tour:

=================
Besichtigungstour
=================

.. contents::
  :local:


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
Arbeiter (oder mehrere) zu einem bestimmten Klienten gehen.

Fakturierbare Termine sind mit einem Auftrag **verknüpft**. Man kann in Lino
auch **unfakturierte Termine** verwalten (z.B. interne Besprechungen,
Urlaubstage, sonstige Termine der Mitarbeiter, ...).

Die Termine eines bestimmten Auftrags kann man im Detail des Auftrags (Reiter
"Kalender") sehen.

Alle Termine eines bestimmten Klienten (für alle Aufträge dieses Klienten,
sowie unfakturierte Termine) kann man im Detail des Klienten (Reiter
"Kalendereinträge") sehen.

Die Termine eines bestimmten Arbeiters kann man im Detail des Arbeiters
(Reiter "Anwesenheiten") sehen.

Über :menuselection:`Kalender --> Kalenderansicht` kann man alle Kalendereinträge
global einsehen (pro Tag, Woche oder Monat).

Im Menü :menuselection:`Kalender` gibt es diverse Tabellen von Terminlisten
(manche davon können vielleicht raus, und manche fehlen vielleicht).  Zum
Beispiel "Überfällig Termine" sind Termine, die älter als eine Woche sind und
bei denen man noch nicht bestätigt hat, ob sie stattgefunden haben oder nicht.

Der **Autor** eines Kalendereintrags ist der administrative Mitarbeiter, der
den Termin erstellt hat (manuell oder automatisch).

Die **Arbeiter** eines Kalendereintrags stehen im Panel "Anwesenheiten".

Ob ein fakturierbarer Termin bereits fakturiert ist, kann man im Detail dieses
Termins (Reiter "Mehr") sehen. Dort stehen sowohl Dienstleistungen als auch
Nebenkosten,


Teams
=====

Um die verschiedenen Tätigkeitsbereiche eines Betriebs zu differenzieren, kann
der Systemverwalter **Teams** und entsprechende **Auftragsjournale** konfigurieren.
Pro Auftragsjournal kann man definieren, welches Team für Aufträge in diesem Journal zuständig ist.
Eventuell können mehrere Auftragsjournale pro Team angelegt werden.

Fakturierungsbereiche
=====================

Jedes Team unterliegt einem **Fakturierungsbereich**.
à priori gibt es deren zwei:

- handwerkliche Arbeiten
- regelmässige Dienstleistungen


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

  - Bachte das Feld **Workflow** : jeder Termin steht zunächst im Status "Vorschlag" bzw.
    "Geplant", und man muss auf :guilabel:`☑` klicken, damit er in den Zustand
    "Stattgefunden" wechselt. Ansonsten erstellt Lino keine Rechnung.

- :kbd:`Escape` um auf den Auftrag zurück zu springen.

- Auf |basket| klicken um einen **Fakturierungsplan** für diesen Auftrag zu
  starten.
  Ein Fakturierungsplan ist, wenn ein Benutzer plant, eine Serie von Rechnungen erstellen zu lassen.
  Lino zeigt hier normalerweise einen Vorschlag an.

- Vergleiche den von Lino vorgeschlagenen Betrag der Rechnung mit der händisch
  erstellten Rechnung.  Falls ein Unterschied ist: entweder :kbd:`Escape` und den
  Auftrag überprüfen oder Rechnung trotzdem erstellen lassen und dann manuell
  bearbeiten.

- Im Fakturierungsplan auf |money| klicken, um die vorgeschlagenen
  Rechnungen zu generieren.

- Wenn eine Rechnung generiert wurde, steht im betreffenden Vorschlag nicht
  mehr ein |money|, sondern die anklickbare Nummer der erstellten Rechnung.  Auf
  diese Nummer kann man klicken, um die Rechnung im Detail anzuzeigen.

Rechnung manuell bearbeiten
===========================

Man kann eine erstellte Rechnung jederzeit manuell bearbeiten:

- Die Rechnung im Detail anzeigen (z.B. über den Fakturierungsplan, oder über
  :menuselection:`Verkauf --> (Journal)` und dann Doppelklick auf der
  gewünschten Rechnung).

- Im Feld :guilabel:`Workflow` auf "Entwurf" klicken falls die Rechnung auf
  "Registriert" steht.

- Inhalt bearbeiten

- Im Feld :guilabel:`Workflow` auf "Registriert" klicken, um sie wieder zu
  registrieren.

Automatikfakturierung
=====================

Lino fakturiert immer alle stattgefundenen Termine eines Auftrags (die noch
nicht fakturiert sind).

Falls ein Termin nicht fakturiert werden soll:

- Den Termin löschen
- Status auf "Abgesagt" (⚕) oder "Verpasst" (☉) setzen

Falls nötig könnten wir einen globalen Parameter definieren "Termine vor diesem
Datum nicht fakturieren"


Terminvorschläge generieren
===========================

- Gehe auf den Auftrag und aktiviere den Reiter Kalender
- Fülle die Felder aus
- Klicke auf |flash|
